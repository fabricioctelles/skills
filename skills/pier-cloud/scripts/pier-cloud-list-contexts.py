#!/usr/bin/env python3
"""
Script to list contexts from the Pier Cloud API.
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
    """Obtain authentication token"""
    url = f"{API_BASE}/auth"
    payload = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
    
    response = requests.post(url, json=payload, timeout=30)
    
    if response.status_code == 201:
        return response.json()['data']['access_token']
    else:
        raise Exception(f"Authentication error: {response.text}")

def list_contexts(token):
    """List all contexts"""
    url = f"{API_BASE}/lighthouse/tenancies/{TENANCY_ID}/contexts"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers, timeout=30)
    
    if response.status_code == 200:
        data = response.json()
        contexts = data['data']['contexts']
        
        print(f"\n=== Contexts ({len(contexts)} found) ===\n")
        
        for ctx in contexts:
            print(f"ID: {ctx['id']}")
            print(f"Name: {ctx['name']}")
            print(f"Provider: {ctx['provider']}")
            print(f"Currency: {ctx['currency']}")
            print(f"Default: {'Yes' if ctx['is_default'] else 'No'}")
            print("-" * 60)
        
        return contexts
    else:
        raise Exception(f"Error listing contexts: {response.text}")

if __name__ == "__main__":
    # Validate variables
    if not TENANCY_ID:
        print("X Error: PIERCLOUD_TENANCY_ID (or PIERCLOUD_BUSINESS_ID) must be defined in .env")
        exit(1)
    required = ["CLIENT_ID", "CLIENT_SECRET"]
    missing = [v for v in required if not os.getenv(f"PIERCLOUD_{v}")]
    
    if missing:
        print(f"✗ Error: Missing variables in .env: {missing}")
        exit(1)
    
    try:
        print("Authenticating...")
        token = authenticate()
        print("✓ Authenticated")
        
        contexts = list_contexts(token)
        print(f"\n✓ Total: {len(contexts)} contexts")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
