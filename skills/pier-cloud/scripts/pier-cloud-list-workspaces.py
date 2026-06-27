#!/usr/bin/env python3
"""
Script to list workspaces from the Pier Cloud API with pagination.
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
    """Obtain authentication token"""
    url = f"{API_BASE}/auth"
    payload = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET}
    response = requests.post(url, json=payload, timeout=30)
    
    if response.status_code == 201:
        return response.json()['data']['access_token']
    else:
        raise Exception(f"Authentication error: {response.text}")

def list_workspaces(token, page=1, page_size=10, sort_field="name", sort_order="ASC"):
    """List workspaces with pagination"""
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
        
        print(f"\n=== Workspaces (Page {meta['page']}/{total_pages}) ===")
        print(f"Total: {meta['total']} workspaces")
        print(f"Sort: {meta['sortBy']['field']} {meta['sortBy']['order']}\n")
        
        for ws in workspaces:
            print(f"ID: {ws['id']}")
            print(f"Name: {ws['name']}")
            print(f"Description: {ws.get('description', 'N/A')}")
            print(f"Views: {ws['count_views']}")
            print(f"Access: {ws['access_scope']}")
            print(f"Created at: {ws['created_at']}")
            print("-" * 60)
        
        return workspaces, meta
    else:
        raise Exception(f"Error listing workspaces: {response.text}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List workspaces from the Pier Cloud API")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--page-size", "--page_size", dest="page_size", type=int, default=10, help="Items per page (default: 10, max: 100)")
    parser.add_argument("--sort-field", "--sort_field", dest="sort_field", choices=["name", "created_at"], default="name", help="Sort field")
    parser.add_argument("--sort-order", "--sort_order", dest="sort_order", choices=["ASC", "DESC"], default="ASC", help="Sort order")
    
    args = parser.parse_args()
    
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
        
        workspaces, meta = list_workspaces(
            token,
            page=args.page,
            page_size=args.page_size,
            sort_field=args.sort_field,
            sort_order=args.sort_order
        )
        
        print(f"\n✓ Displayed {len(workspaces)} workspaces of {meta['total']} total")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        exit(1)
