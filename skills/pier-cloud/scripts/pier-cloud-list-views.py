#!/usr/bin/env python3
"""
Script para listar visualizacoes de um workspace da API Pier Cloud.
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

def list_views(token, workspace_id):
    """Listar visualizacoes de um workspace"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/workspaces/{workspace_id}/views"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        views = data['data']['views']
        total = data['data']['total']
        
        print(f"\n=== Visualizacoes do Workspace {workspace_id} ===")
        print(f"Total: {total} visualizacoes\n")
        
        for view in views:
            print(f"ID: {view['id']}")
            print(f"Nome: {view['name']}")
            print(f"Descricao: {view.get('description', 'N/A')}")
            print(f"Criado em: {view['created_at']}")
            print("-" * 60)
        
        return views
    else:
        raise Exception(f"Erro ao listar visualizacoes: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Listar visualizacoes de workspace da API Pier Cloud")
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
        
        views = list_views(token, args.workspace_id)
        
        print(f"\nOK Total: {len(views)} visualizacoes")
        
    except Exception as e:
        print(f"\nX Erro: {e}")
        exit(1)
