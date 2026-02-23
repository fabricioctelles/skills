#!/usr/bin/env python3
"""
Script para autenticar na API Pier Cloud e obter token JWT.
"""

import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

API_BASE = "https://api.piercloud.io"
CLIENT_ID = os.getenv("PIERCLOUD_CLIENT_ID")
CLIENT_SECRET = os.getenv("PIERCLOUD_CLIENT_SECRET")

def authenticate():
    """Obter token de autenticação"""
    print("Autenticando na API Pier Cloud...")
    
    url = f"{API_BASE}/auth"
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 201:
            data = response.json()
            token = data['data']['access_token']
            expires_in = data['data']['expires_in']
            
            print(f"\n✓ Token obtido com sucesso!")
            print(f"Token: {token[:50]}...")
            print(f"Expira em: {expires_in} segundos ({expires_in//60} minutos)")
            print(f"Tipo: {data['data']['token_type']}")
            
            return token
        else:
            print(f"\n✗ Erro na autenticação (Status {response.status_code})")
            print(f"Resposta: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\n✗ Erro de conexão: {e}")
        return None

if __name__ == "__main__":
    # Validar variáveis de ambiente
    if not CLIENT_ID or not CLIENT_SECRET:
        print("✗ Erro: PIERCLOUD_CLIENT_ID e PIERCLOUD_CLIENT_SECRET devem estar definidos no .env")
        exit(1)
    
    token = authenticate()
    
    if token:
        print("\n✓ Autenticação concluída com sucesso!")
    else:
        print("\n✗ Falha na autenticação")
        exit(1)
