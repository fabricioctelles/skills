#!/usr/bin/env python3
"""
Script para obter detalhes de um grupo de workspace especifico da API Pier Cloud.
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

def get_workspace_group(token, group_id):
    """Obter detalhes de um grupo de workspace especifico"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/workspace-groups/{group_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        group = data['data']
        
        print(f"\n=== Grupo de Workspace: {group['name']} ===\n")
        print(f"ID: {group['id']}")
        print(f"Nome: {group['name']}")
        print(f"Descricao: {group.get('description', 'N/A')}")
        print(f"Acesso: {group['access_scope']}")
        print(f"Context ID: {group['context_id']}")
        print(f"Business ID: {group['business_id']}")
        print(f"Criado em: {group['created_at']}")
        print(f"Atualizado em: {group['updated_at']}")
        
        if 'workspaces' in group and group['workspaces']:
            print(f"\n--- Workspaces ({len(group['workspaces'])}) ---")
            for ws in group['workspaces']:
                print(f"\n  ID: {ws['id']}")
                print(f"  Nome: {ws['name']}")
                print(f"  Descricao: {ws.get('description', 'N/A')}")
                print(f"  Acesso: {ws['access_scope']}")
                print(f"  Criado em: {ws['created_at']}")
        else:
            print("\nNenhum workspace neste grupo.")
        
        return group
    else:
        raise Exception(f"Erro ao obter grupo: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obter detalhes de grupo de workspace da API Pier Cloud")
    parser.add_argument("--group-id", "--group_id", dest="group_id", required=True, help="ID do grupo de workspace (numerico ou UUID)")
    
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
        
        group = get_workspace_group(token, args.group_id)
        
        print(f"\nOK Grupo obtido com sucesso")
        
    except Exception as e:
        print(f"\nX Erro: {e}")
        exit(1)
