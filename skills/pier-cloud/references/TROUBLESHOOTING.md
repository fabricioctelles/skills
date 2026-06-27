## Troubleshooting

### Error 401 - Invalid Credentials

**Problem**: Authentication fails with error 401

**Symptoms**:
```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Common Causes**:
- Incorrect `client_id` or `client_secret`
- Credentials not registered on the Pier Cloud platform
- Environment variables not loaded correctly

**Solutions**:
1. Check credentials in the `.env` file
2. Confirm that variables are being loaded
3. Validate credentials with the Pier Cloud team
4. Verify that the HTTP client is registered on the platform

### Error 403 - Access Denied

**Problem**: Valid token but no permission to access resource

**Symptoms**:
```json
{
  "code": "authorization/forbidden",
  "message": "Access denied"
}
```

**Causes**:
- Account without adequate permissions
- Incorrect `tenancy_id`
- Resource does not belong to the specified tenant

**Solutions**:
1. Check account permissions on the Pier Cloud platform
2. Confirm correct `tenancy_id`
3. Contact administrator to request permissions

### Error 404 - Resource Not Found

**Problem**: Endpoint or resource does not exist

**Symptoms**:
```json
{
  "code": "workspace/not-found",
  "message": "Workspace not found"
}
```

**Causes**:
- Incorrect or non-existent `workspace_id`
- Invalid `tenancy_id`
- Incorrect endpoint URL

**Solutions**:
1. List all workspaces first to verify available IDs
2. Confirm endpoint URL is correct
3. Validate tenancy_id

### Expired Token

**Problem**: JWT token expired after ~1 hour

**Symptoms**:
- Requests that were working start returning 401
- Error "invalid or expired token"

**Solution**:

Use the robust client that implements automatic renewal:

```bash
python scripts/pier_cloud_client.py --action list-contexts
```

The `pier_cloud_client.py` client automatically renews the token before it expires.

### Connection Timeout

**Problem**: Request takes too long or does not respond

**Symptoms**:
- Timeout after 30+ seconds
- Connection not established
- Network error

**Solutions**:
1. Check internet connectivity
2. Test API availability: `curl -I https://api.piercloud.io/auth`
3. Check if there is a proxy or firewall blocking
4. Try again after a few minutes

### Rate Limiting (Too Many Requests)

**Problem**: API returns error 429 (Too Many Requests)

**Symptoms**:
- Error 429 after several rapid requests
- Message about rate limit

**Solutions**:
1. Use the robust client that implements automatic retry
2. Reduce request frequency
3. Implement delays between requests
4. Use pagination with smaller `page_size` if needed
