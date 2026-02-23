#!/usr/bin/env python3
"""
Script para listar contextos da API Pier Cloud.
"""

import requests
import os
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

def list_contexts(token):
    """Listar todos os contextos"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/contexts"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        contexts = data['data']['contexts']
        
        print(f"\n=== Contextos ({len(contexts)} encontrados) ===\n")
        
        for ctx in contexts:
            print(f"ID: {ctx['id']}")
            print(f"Nome: {ctx['name']}")
            print(f"Provider: {ctx['provider']}")
            print(f"Moeda: {ctx['currency']}")
            print(f"Padrão: {'Sim' if ctx['is_default'] else 'Não'}")
            print("-" * 60)
        
        return contexts
    else:
        raise Exception(f"Erro ao listar contextos: {response.text}")

if __name__ == "__main__":
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
        
        contexts = list_contexts(token)
        print(f"\n✓ Total: {len(contexts)} contextos")
        
    except Exception as e:
        print(f"\n✗ Erro: {e}")
        exit(1)
