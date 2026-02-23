#!/usr/bin/env python3
"""
Cliente robusto para API Pier Cloud com retry, renovacao automatica e CLI.
"""

import requests
import os
import time
import logging
import argparse
import json
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PierCloudClient:
    """Cliente robusto para API Pier Cloud"""
    
    def __init__(self):
        load_dotenv()
        self.api_base = "https://api.piercloud.io"
        self.client_id = os.getenv("PIERCLOUD_CLIENT_ID")
        self.client_secret = os.getenv("PIERCLOUD_CLIENT_SECRET")
        self.tenancy_id = os.getenv("PIERCLOUD_TENANCY_ID", os.getenv("PIERCLOUD_BUSINESS_ID"))
        
        self.token = None
        self.token_expires = None
        
        self._validate_config()
    
    def _validate_config(self):
        """Validar configuracao necessaria"""
        required = ["client_id", "client_secret", "tenancy_id"]
        missing = [k for k in required if not getattr(self, k)]
        
        if missing:
            raise ValueError(f"Configuracao faltando: {missing}")
    
    def authenticate(self):
        """Autenticar e obter token"""
        logger.info("Autenticando...")
        
        response = requests.post(
            f"{self.api_base}/auth",
            json={"client_id": self.client_id, "client_secret": self.client_secret},
            timeout=30
        )
        
        if response.status_code == 201:
            data = response.json()['data']
            self.token = data['access_token']
            # Renovar 5 minutos antes de expirar
            self.token_expires = time.time() + data['expires_in'] - 300
            logger.info("OK Autenticado com sucesso")
            return True
        else:
            logger.error(f"X Falha na autenticacao: {response.text}")
            return False
    
    def ensure_authenticated(self):
        """Garantir token valido"""
        if not self.token or time.time() >= self.token_expires:
            return self.authenticate()
        return True
    
    def make_request(self, method, endpoint, **kwargs):
        """Fazer requisicao com retry e renovacao automatica"""
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                if not self.ensure_authenticated():
                    raise Exception("Falha na autenticacao")
                
                headers = kwargs.get('headers', {})
                headers['Authorization'] = f"Bearer {self.token}"
                kwargs['headers'] = headers
                kwargs.setdefault('timeout', 30)
                
                response = requests.request(method, f"{self.api_base}{endpoint}", **kwargs)
                
                if response.status_code == 401:
                    logger.warning("Token expirado, renovando...")
                    self.authenticate()
                    continue
                
                if response.status_code == 429:
                    wait_time = 2 ** attempt
                    logger.warning(f"Rate limit. Aguardando {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                
                response.raise_for_status()
                return response.json()
                
            except requests.exceptions.RequestException as e:
                logger.error(f"Erro na tentativa {attempt + 1}: {e}")
                
                if attempt == max_retries - 1:
                    raise
                
                time.sleep(2 ** attempt)
        
        return None
    
    def list_contexts(self):
        """Listar contextos"""
        endpoint = f"/lighthouse/tenancies/{self.tenancy_id}/contexts"
        return self.make_request('GET', endpoint)
    
    def list_workspaces(self, page=1, page_size=10):
        """Listar workspaces"""
        endpoint = f"/lighthouse/tenancies/{self.tenancy_id}/workspaces"
        params = {"page": page, "page_size": page_size}
        return self.make_request('GET', endpoint, params=params)
    
    def get_workspace(self, workspace_id):
        """Obter workspace especifico"""
        endpoint = f"/lighthouse/tenancies/{self.tenancy_id}/workspaces/{workspace_id}"
        return self.make_request('GET', endpoint)
    
    def get_all_workspaces(self):
        """Obter todos os workspaces com paginacao automatica"""
        all_workspaces = []
        page = 1
        page_size = 100
        
        while True:
            result = self.list_workspaces(page=page, page_size=page_size)
            workspaces = result['data']['workspaces']
            meta = result['meta']
            
            all_workspaces.extend(workspaces)
            logger.info(f"Pagina {page}: {len(workspaces)} workspaces")
            
            if page * page_size >= meta['total']:
                break
            
            page += 1
        
        return all_workspaces

def main():
    parser = argparse.ArgumentParser(description="Cliente CLI para API Pier Cloud")
    parser.add_argument("--action", required=True, 
                       choices=["list-contexts", "list-workspaces", "get-workspace", "get-all-workspaces"],
                       help="Acao a executar")
    parser.add_argument("--workspace-id", type=int, help="ID do workspace (para get-workspace)")
    parser.add_argument("--page", type=int, default=1, help="Numero da pagina")
    parser.add_argument("--page-size", type=int, default=10, help="Itens por pagina")
    parser.add_argument("--output", help="Arquivo de saida JSON")
    
    args = parser.parse_args()
    
    try:
        client = PierCloudClient()
        
        if args.action == "list-contexts":
            result = client.list_contexts()
            contexts = result['data']['contexts']
            print(f"\nContextos: {len(contexts)}")
            for ctx in contexts:
                print(f"  - {ctx['name']} ({ctx['provider']})")
        
        elif args.action == "list-workspaces":
            result = client.list_workspaces(page=args.page, page_size=args.page_size)
            workspaces = result['data']['workspaces']
            meta = result['meta']
            print(f"\nWorkspaces: {len(workspaces)} de {meta['total']}")
            for ws in workspaces:
                print(f"  - [{ws['id']}] {ws['name']}")
        
        elif args.action == "get-workspace":
            if not args.workspace_id:
                print("X Erro: --workspace-id e obrigatorio")
                exit(1)
            result = client.get_workspace(args.workspace_id)
            ws = result['data']
            print(f"\nWorkspace: {ws['name']}")
            print(f"ID: {ws['id']}")
            print(f"Visualizacoes: {len(ws.get('views', []))}")
        
        elif args.action == "get-all-workspaces":
            workspaces = client.get_all_workspaces()
            print(f"\nTotal: {len(workspaces)} workspaces")
            
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    json.dump(workspaces, f, indent=2, ensure_ascii=False)
                print(f"OK Salvo em {args.output}")
        
    except Exception as e:
        logger.error(f"X Erro: {e}")
        exit(1)

if __name__ == "__main__":
    main()
