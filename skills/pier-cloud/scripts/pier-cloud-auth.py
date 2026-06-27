#!/usr/bin/env python3
"""
Script to authenticate with the Pier Cloud API and obtain a JWT token.
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_BASE = "https://api.piercloud.io"
CLIENT_ID = os.getenv("PIERCLOUD_CLIENT_ID")
CLIENT_SECRET = os.getenv("PIERCLOUD_CLIENT_SECRET")

def authenticate():
    """Obtain authentication token"""
    print("Authenticating with Pier Cloud API...")
    
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
            
            print(f"\n✓ Token obtained successfully!")
            print(f"Token: {token[:50]}...")
            print(f"Expires in: {expires_in} seconds ({expires_in//60} minutes)")
            print(f"Type: {data['data']['token_type']}")
            
            return token
        else:
            print(f"\n✗ Authentication error (Status {response.status_code})")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\n✗ Connection error: {e}")
        return None

if __name__ == "__main__":
    # Validate environment variables
    if not CLIENT_ID or not CLIENT_SECRET:
        print("✗ Error: PIERCLOUD_CLIENT_ID and PIERCLOUD_CLIENT_SECRET must be defined in .env")
        exit(1)
    
    token = authenticate()
    
    if token:
        print("\n✓ Authentication completed successfully!")
    else:
        print("\n✗ Authentication failed")
        exit(1)
