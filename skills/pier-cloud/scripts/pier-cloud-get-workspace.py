#!/usr/bin/env python3
"""
Script para obter detalhes de um workspace especifico da API Pier Cloud.
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

def get_workspace(token, workspace_id):
    """Obter detalhes de um workspace especifico"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/workspaces/{workspace_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        ws = data['data']
        
        print(f"\n=== Workspace: {ws['name']} ===\n")
        print(f"ID: {ws['id']}")
        print(f"Descricao: {ws.get('description', 'N/A')}")
        print(f"Acesso: {ws['access_scope']}")
        print(f"Grupo: {ws['workspace_group_id']}")
        
        if 'views' in ws and ws['views']:
            print(f"\n--- Visualizacoes ({len(ws['views'])}) ---")
            for view in ws['views']:
                print(f"\n  ID: {view['id']}")
                print(f"  Nome: {view['name']}")
                print(f"  Descricao: {view.get('description', 'N/A')}")
                print(f"  Criado em: {view['created_at']}")
        else:
            print("\nNenhuma visualizacao encontrada.")
        
        return ws
    else:
        raise Exception(f"Erro ao obter workspace: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obter detalhes de workspace da API Pier Cloud")
    parser.add_argument("--workspace-id", "--workspace_id", dest="workspace_id", type=int, required=True, help="ID do workspace")
    
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
        
        workspace = get_workspace(token, args.workspace_id)
        
        print(f"\nOK Workspace obtido com sucesso")
        
    except Exception as e:
        print(f"\nX Erro: {e}")
        exit(1)
