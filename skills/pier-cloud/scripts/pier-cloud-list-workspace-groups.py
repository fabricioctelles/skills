#!/usr/bin/env python3
"""
Script para listar grupos de workspaces da API Pier Cloud.
"""

import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv()

API_BASE = "https://api.piercloud.io"
CLIENT_ID = os.getenv("PIERCLOUD_CLIENT_ID")
CLIENT_SECRET = os.getenv("PIERCLOUD_CLIENT_SECRET")
TENANCY_ID = os.getenv("PIERCLOUD_TENANCY_ID", os.getenv("PIERCLOUD_BUSINESS_ID"))

def authenticate():
    """Obter token de autenticacao"""
    url = f"{API_BASE}/auth"
    payload = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
    response = requests.post(url, json=payload, timeout=30)
    
    if response.status_code == 201:
        return response.json()['data']['access_token']
    else:
        raise Exception(f"Erro na autenticacao: {response.text}")

def list_workspace_groups(token, page=1, page_size=10):
    """Listar grupos de workspaces"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/workspace-groups"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"page": page, "page_size": page_size}
    
    response = requests.get(url, headers=headers, params=params, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        groups = data['data']
        meta = data['meta']
        
        print(f"\n=== Grupos de Workspaces (Pagina {meta['page']}) ===")
        print(f"Total: {meta['total']} grupos\n")
        
        for i, group in enumerate(groups, 1):
            print(f"\n{'='*60}")
            print(f"GRUPO {i}")
            print(f"{'='*60}")
            print(f"ID COMPLETO: {group['id']}")
            print(f"Nome: {group['name']}")
            print(f"Descricao: {group.get('description', 'N/A')}")
            print(f"Acesso: {group['access_scope']}")
            print(f"Context ID: {group.get('context_id', 'N/A')}")
            print(f"Business ID: {group.get('business_id', 'N/A')}")
            print(f"Criado em: {group['created_at']}")
            print(f"Atualizado em: {group.get('updated_at', 'N/A')}")
            print(f"Workspaces: {len(group.get('workspaces', []))}")
            
            if group.get('workspaces'):
                print("\n  Workspaces incluidos:")
                for ws in group['workspaces']:
                    print(f"    - [{ws['id']}] {ws['name']}")
            
            print(f"\n  Comando para obter detalhes:")
            print(f"  python scripts/pier-cloud-get-workspace-group.py --group-id {group['id']}")
            print(f"{'='*60}")
        
        return groups, meta
    else:
        raise Exception(f"Erro ao listar grupos: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Listar grupos de workspaces da API Pier Cloud")
    parser.add_argument("--page", type=int, default=1, help="Numero da pagina (padrao: 1)")
    parser.add_argument("--page-size", "--page_size", dest="page_size", type=int, default=10, help="Itens por pagina (padrao: 10)")
    
    args = parser.parse_args()
    
    # Validar variaveis
    if not TENANCY_ID:
        print("X Erro: PIERCLOUD_TENANCY_ID (ou PIERCLOUD_BUSINESS_ID) deve estar definido no .env")
        exit(1)
    required = ["CLIENT_ID", "CLIENT_SECRET"]
    missing = [v for v in required if not os.getenv(f"PIERCLOUD_{v}")]
    
    if missing:
        print(f"X Erro: Variaveis faltando no .env: {missing}")
        exit(1)
    
    try:
        print("Autenticando...")
        token = authenticate()
        print("OK Autenticado")
        
        groups, meta = list_workspace_groups(token, page=args.page, page_size=args.page_size)
        
        print(f"\nOK Exibidos {len(groups)} grupos de {meta['total']} total")
        
    except Exception as e:
        print(f"\nX Erro: {e}")
        exit(1)
