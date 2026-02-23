#!/usr/bin/env python3
"""
Script para obter informacoes de uma visualizacao especifica da API Pier Cloud.
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

def get_view(token, view_id):
    """Obter informacoes de uma visualizacao especifica"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/views/{view_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        view = data['data']
        
        print(f"\n=== Visualizacao: {view['name']} ===\n")
        print(f"ID: {view['id']}")
        print(f"Nome: {view['name']}")
        print(f"Descricao: {view.get('description', 'N/A')}")
        
        if 'workspace' in view:
            print(f"\nWorkspace:")
            print(f"  ID: {view['workspace']['id']}")
            print(f"  Nome: {view['workspace']['name']}")
        
        return view
    else:
        raise Exception(f"Erro ao obter visualizacao: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obter informacoes de visualizacao da API Pier Cloud")
    parser.add_argument("--view-id", "--view_id", dest="view_id", type=int, required=True, help="ID da visualizacao")
    
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
        
        view = get_view(token, args.view_id)
        
        print(f"\nOK Visualizacao obtida com sucesso")
        
    except Exception as e:
        print(f"\nX Erro: {e}")
        exit(1)
