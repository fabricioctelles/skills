#!/usr/bin/env python3
"""
Script para obter todos os workspaces da API Pier Cloud com paginacao automatica.
"""

import requests
import os
import argparse
import json
import csv
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

def get_all_workspaces(token):
    """Obter todos os workspaces com paginacao automatica"""
    all_workspaces = []
    page = 1
    page_size = 100  # Maximo permitido
    
    while True:
        url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/workspaces"
        headers = {"Authorization": f"Bearer {token}"}
        params = {"page": page, "page_size": page_size}
        
        response = requests.get(url, headers=headers, params=params, timeout=30)
        
        if response.status_code != 200:
            raise Exception(f"Erro na pagina {page}: {response.text}")
        
        data = response.json()
        workspaces = data['data']['workspaces']
        meta = data['meta']
        
        all_workspaces.extend(workspaces)
        
        print(f"OK Pagina {page}: {len(workspaces)} workspaces obtidos")
        
        # Verificar se ha mais paginas
        if page * page_size >= meta['total']:
            break
        
        page += 1
    
    return all_workspaces

def save_json(workspaces, filename):
    """Salvar workspaces em arquivo JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(workspaces, f, indent=2, ensure_ascii=False)
    print(f"OK Salvo em {filename}")

def save_csv(workspaces, filename):
    """Salvar workspaces em arquivo CSV"""
    if not workspaces:
        print("Nenhum workspace para salvar")
        return
    
    keys = ['id', 'name', 'description', 'access_scope', 'count_views', 'created_at']
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        
        for ws in workspaces:
            row = {k: ws.get(k, '') for k in keys}
            writer.writerow(row)
    
    print(f"OK Salvo em {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obter todos os workspaces da API Pier Cloud")
    parser.add_argument("--output", help="Arquivo de saida (JSON ou CSV)")
    parser.add_argument("--format", choices=["json", "csv"], default="json", help="Formato de saida")
    
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
        print("OK Autenticado\n")
        
        print("Obtendo todos os workspaces...")
        workspaces = get_all_workspaces(token)
        
        print(f"\nOK Total: {len(workspaces)} workspaces obtidos")
        
        # Salvar em arquivo se especificado
        if args.output:
            if args.format == "json":
                save_json(workspaces, args.output)
            else:
                save_csv(workspaces, args.output)
        
    except Exception as e:
        print(f"\nX Erro: {e}")
        exit(1)
