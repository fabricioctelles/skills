#!/usr/bin/env python3
"""
Script para obter dados de uma visualizacao da API Pier Cloud com filtros.
"""

import requests
import os
import argparse
import json
from datetime import datetime, timedelta
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

def get_view_data(token, view_id, start_date=None, end_date=None, date_type="date", filters=None):
    """Obter dados de uma visualizacao"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/views/{view_id}/data"
    headers = {"Authorization": f"Bearer {token}"}
    
    # Parametros de query
    params = {}
    
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date
    if date_type:
        params['date_type'] = date_type
    if filters:
        params['filters'] = json.dumps(filters)
    
    response = requests.get(url, headers=headers, params=params, timeout=60)
    
    if response.status_code == 200:
        data = response.json()
        results = data['data']
        
        print(f"\n=== Dados da Visualizacao {view_id} ===")
        print(f"Periodo: {start_date or 'inicio do mes'} ate {end_date or 'fim do mes'}")
        print(f"Tipo de data: {date_type}")
        print(f"Total de registros: {len(results)}\n")
        
        if results:
            # Mostrar primeiros registros
            print("Primeiros registros:")
            for i, record in enumerate(results[:5]):
                print(f"\nRegistro {i+1}:")
                for key, value in record.items():
                    print(f"  {key}: {value}")
            
            if len(results) > 5:
                print(f"\n... e mais {len(results) - 5} registros")
        
        return results
    else:
        raise Exception(f"Erro ao obter dados: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Obter dados de visualizacao da API Pier Cloud")
    parser.add_argument("--view-id", "--view_id", dest="view_id", type=int, required=True, help="ID da visualizacao")
    parser.add_argument("--start-date", "--start_date", dest="start_date", help="Data inicial (YYYY-MM-DD)")
    parser.add_argument("--end-date", "--end_date", dest="end_date", help="Data final (YYYY-MM-DD)")
    parser.add_argument("--date-type", "--date_type", dest="date_type", choices=["date", "month"], default="date", 
                       help="Tipo de filtro de data (date ou month)")
    parser.add_argument("--filters", help="Filtros em formato JSON")
    parser.add_argument("--output", help="Arquivo de saida JSON")
    
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
    
    # Parse filters se fornecido
    filters = None
    if args.filters:
        try:
            filters = json.loads(args.filters)
        except json.JSONDecodeError as e:
            print(f"X Erro ao parsear filtros JSON: {e}")
            exit(1)
    
    try:
        print("Autenticando...")
        token = authenticate()
        print("OK Autenticado")
        
        results = get_view_data(
            token, 
            args.view_id,
            start_date=args.start_date,
            end_date=args.end_date,
            date_type=args.date_type,
            filters=filters
        )
        
        # Salvar em arquivo se especificado
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"\nOK Salvo em {args.output}")
        
        print(f"\nOK Total: {len(results)} registros obtidos")
        
    except Exception as e:
        print(f"\nX Erro: {e}")
        exit(1)
