#!/usr/bin/env python3
"""
Script para listar workspaces da API Pier Cloud com paginação.
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
    """Obter token de autenticação"""
    url = f"{API_BASE}/auth"
    payload = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
    response = requests.post(url, json=payload, timeout=30)
    
    if response.status_code == 201:
        return response.json()['data']['access_token']
    else:
        raise Exception(f"Erro na autenticação: {response.text}")

def list_workspaces(token, page=1, page_size=10, sort_field="name", sort_order="ASC"):
    """Listar workspaces com paginação"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/workspaces"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "page": page,
        "page_size": page_size,
        "sort_field": sort_field,
        "sort_order": sort_order
    }
    
    response = requests.get(url, headers=headers, params=params, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        workspaces = data['data']['workspaces']
        meta = data['meta']
        
        total_pages = (meta['total'] - 1) // meta['pageSize'] + 1
        
        print(f"\n=== Workspaces (Página {meta['page']}/{total_pages}) ===")
        print(f"Total: {meta['total']} workspaces")
        print(f"Ordenação: {meta['sortBy']['field']} {meta['sortBy']['order']}\n")
        
        for ws in workspaces:
            print(f"ID: {ws['id']}")
            print(f"Nome: {ws['name']}")
            print(f"Descrição: {ws.get('description', 'N/A')}")
            print(f"Visualizações: {ws['count_views']}")
            print(f"Acesso: {ws['access_scope']}")
            print(f"Criado em: {ws['created_at']}")
            print("-" * 60)
        
        return workspaces, meta
    else:
        raise Exception(f"Erro ao listar workspaces: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Listar workspaces da API Pier Cloud")
    parser.add_argument("--page", type=int, default=1, help="Número da página (padrão: 1)")
    parser.add_argument("--page-size", "--page_size", dest="page_size", type=int, default=10, help="Itens por página (padrão: 10, máximo: 100)")
    parser.add_argument("--sort-field", "--sort_field", dest="sort_field", choices=["name", "created_at"], default="name", help="Campo para ordenação")
    parser.add_argument("--sort-order", "--sort_order", dest="sort_order", choices=["ASC", "DESC"], default="ASC", help="Ordem de ordenação")
    
    args = parser.parse_args()
    
    # Validar variáveis
    if not TENANCY_ID:
        print("X Erro: PIERCLOUD_TENANCY_ID (ou PIERCLOUD_BUSINESS_ID) deve estar definido no .env")
        exit(1)
    required = ["CLIENT_ID", "CLIENT_SECRET"]
    missing = [v for v in required if not os.getenv(f"PIERCLOUD_{v}")]
    
    if missing:
        print(f"✗ Erro: Variáveis faltando no .env: {missing}")
        exit(1)
    
    try:
        print("Autenticando...")
        token = authenticate()
        print("✓ Autenticado")
        
        workspaces, meta = list_workspaces(
            token,
            page=args.page,
            page_size=args.page_size,
            sort_field=args.sort_field,
            sort_order=args.sort_order
        )
        
        print(f"\n✓ Exibidos {len(workspaces)} workspaces de {meta['total']} total")
        
    except Exception as e:
        print(f"\n✗ Erro: {e}")
        exit(1)
