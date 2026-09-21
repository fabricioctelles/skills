# Pier Cloud API Reference (Lighthouse)

Synced from official public routes docs (EN) on 2026-09-21.

- **Base URL:** `https://api.piercloud.io`
- **Docs:** https://docs.piercloud.com/api-docs-pier-cloud
- **Auth:** JWT Bearer from `POST /auth`

All Lighthouse routes are under `/lighthouse/tenancies/{tenancy_id}/...`.

> **Workspace groups path:** the official segment is `workspaces-groups` (plural *workspaces*), not `workspace-groups`.

## Endpoint map

| Method | Path | Notes |
|--------|------|-------|
| POST | `/auth` | client_id + client_secret → JWT |
| GET | `/lighthouse/tenancies/{tenancy_id}/contexts` | list contexts |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces` | list workspaces (paginated) |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces/{id}` | workspace detail |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces-groups` | list workspace groups |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces-groups/{id}` | group detail |
| GET | `/lighthouse/tenancies/{tenancy_id}/workspaces/{workspace_id}/views` | list views |
| GET | `/lighthouse/tenancies/{tenancy_id}/views/{id}` | view detail |
| GET | `/lighthouse/tenancies/{tenancy_id}/views/{id}/data` | view data + filters |

## Workflows (agent cheat sheet)

### 1 — Authenticate
```bash
curl -X POST https://api.piercloud.io/auth \
  -H 'Content-Type: application/json' \
  -d '{"client_id":"...","client_secret":"..."}'
# → data.access_token, data.expires_in (typically 3600)
```

### 2 — List contexts
```bash
curl -H "Authorization: Bearer $TOKEN" \
  https://api.piercloud.io/lighthouse/tenancies/$TENANCY_ID/contexts
```

### 3 — List / get workspaces
```bash
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.piercloud.io/lighthouse/tenancies/$TENANCY_ID/workspaces?page=1&page_size=20"
curl -H "Authorization: Bearer $TOKEN" \
  https://api.piercloud.io/lighthouse/tenancies/$TENANCY_ID/workspaces/{id}
```

### 4 — List / get workspace groups
```bash
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.piercloud.io/lighthouse/tenancies/$TENANCY_ID/workspaces-groups?context_id=<uuid>"
curl -H "Authorization: Bearer $TOKEN" \
  https://api.piercloud.io/lighthouse/tenancies/$TENANCY_ID/workspaces-groups/{id}
```

### 5 — Views + data
```bash
curl -H "Authorization: Bearer $TOKEN" \
  https://api.piercloud.io/lighthouse/tenancies/$TENANCY_ID/workspaces/{workspace_id}/views
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.piercloud.io/lighthouse/tenancies/$TENANCY_ID/views/{id}/data?start_date=2026-01-01&end_date=2026-01-31"
```

---

## Upstream excerpts (EN)


### Authentication

# Public Routes (EN-US)

Lighthouse API Public Routes Usage Description

***

## API Documentation

### Base URL

```
https://api.piercloud.io
```

### HTTP Client Authentication

All HTTP clients need to be registered on the Pier Cloud platform to obtain access credentials. For more information, [visit the link](https://docs.piercloud.com/plataforma-de-finops/finops-platform-english/platform-configuration/setup-features/api-keys).

***

### Authentication

#### 1. Generate Access Token

Generate an access token for the HTTP client.

* **URL:** `/auth`
* **Method:** `POST`
* **Description:** Returns the access token and other information based on the provided credentials.

**Headers**

| Name           | Type   | Required | Description                |
| -------------- | ------ | -------- | -------------------------- |
| `Content-Type` | string | Yes      | Must be `application/json` |

**Body**

```json
{
  "client_id": "string",
  "client_secret": "string"
}
```

**Example Request**

```bash
curl -X POST https://api.piercloud.io/auth \
     -H "Content-Type: application/json" \
     -d '{
           "client_id": "client_id",
           "client_secret": "client_secret",
         }'
```

**Successful Response (201 Created)**

```json
{
  "code": "success",
  "data": {
    "access_token": "JWT Token",
    "expires_in": "Expiration time in seconds",
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "session_state": "",
    "scope": "List of access permissions for the HTTP client"
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

***


### Contexts

# Contexts

#### 1. List Contexts

Returns a list of all data contexts.

* **URL:** `/lighthouse/tenancies/{tenancy_id}/contexts`
* **Method:** `GET`
* **Description:** Retrieves a paginated list of contexts.

**Query Params**

| Name        | Type    | Required | Description                                        |
| ----------- | ------- | -------- | -------------------------------------------------- |
| `page`      | integer | No       | Page number (default: 1)                           |
| `page_size` | integer | No       | Number of results per page (default: 10, max: 100) |
| `search`    | string  | No       | Key used as search filter                          |

**Notes on Parameters**

* **page\_size:** If the value provided is greater than 100, it will automatically be converted to the limit value.

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/contexts  \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
  "code": "success",
  "data": {
    "contexts": [
      {
        "id": "uuid",
        "name": "Amazon Web Services",
        "provider": "aws",
        "currency": "USD",
        "is_default": true,
        "business_id": "uuid"
      }
    ],
    "total": 1
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```


### Workspaces

# Workspaces

#### 1. List Workspaces

Returns a list of all workspaces.

* **URL:** `/lighthouse/tenancies/{tenancy_id}/workspaces`
* **Method:** `GET`
* **Description:** Retrieves a paginated list of workspaces.

**Query Params**

| Name                 | Type    | Required | Description                                                |
| -------------------- | ------- | -------- | ---------------------------------------------------------- |
| `page`               | integer | No       | Page number (default: 1)                                   |
| `page_size`          | integer | No       | Number of results per page (default: 10, max: 100)         |
| `search`             | string  | No       | Key used as search filter                                  |
| `context_id`         | uuid    | No       | ID of the context to which the workspace belongs           |
| `workspace_group_id` | uuid    | No       | ID of the group where the workspace belongs                |
| `sort_field`         | string  | No       | Field used to sort the results (default: created\_at)      |
| `sort_order`         | string  | No       | Determines the sorting order of the results (default: ASC) |

**Notes on Parameters**

* **page\_size:** If the value provided is greater than 100, it will automatically be converted to this value (100).
* **sort\_field:** `name` or `created_at`
* **sort\_order:** `ASC` or `DESC`

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/workspaces \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
  "code": "success",
  "data": {
    "workspaces": [
      {
        "id": 1,
        "name": "Workspace name",
        "description": null,
        "access_scope": "public",
        "created_at": "2022-01-01T00:01:45.941Z",
        "workspace_group_id": "uuid",
        "count_views": 1
      }
    ]
  },
  "meta": {
    "total": 1,
    "page": 1,
    "pageSize": 10,
    "sortBy": {
      "field": "created_at",
      "order": "ASC"
    }
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```

***

#### 2. Access Workspace Information

Returns information about a specific workspace.

* **URL:** `/lighthouse/tenancies/{tenancy_id}/workspaces/{id}`
* **Method:** `GET`
* **Description:** Returns information about a single workspace.

**Query Params**

| Name | Type | Required | Description |
| ---- | ---- | -------- | ----------- |
|      |      |          |             |

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/workspaces/1234 \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
  "code": "success",
  "data": {
    "id": 1234,
    "name": "Workspace name",
    "description": "Workspace description",
    "access_scope": "public",
    "workspace_group_id": "uuid",
    "views": [
      {
        "id": 123,
        "name": "View name",
        "description": "Description",
        "created_at": "2025-01-01T00:00:00.911Z",
        "workspace_id": 1234
      }
    ]
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```

**Error Response (404 Not Found)**

```json
{
  "code": "workspace/not-found",
  "message": "Workspace not found"
}
```


### Workspace Groups

# Workspace Groups

#### 1. List Workspace Groups

Returns a list of all workspace groups.

* **URL:** `/lighthouse/tenancies/{tenancy_id}/workspaces-groups`
* **Method:** `GET`
* **Description:** Retrieves a paginated list of workspaces.

**Query Params**

| Name         | Type    | Required | Description                                                |
| ------------ | ------- | -------- | ---------------------------------------------------------- |
| `page`       | integer | No       | Page number (default: 1)                                   |
| `page_size`  | integer | No       | Number of results per page (default: 10)                   |
| `search`     | string  | No       | Key used as search filter                                  |
| `context_id` | uuid    | No       | ID of the context to which the group belongs               |
| `sort_field` | string  | No       | Field used to sort the results (default: created\_at)      |
| `sort_order` | string  | No       | Determines the sorting order of the results (default: ASC) |

**Notes on Parameters**

* **page\_size:** If the value provided is greater than 100, it will automatically be converted to this value (100).
* **sort\_field:** `name` or `created_at`
* **sort\_order:** `ASC` or `DESC`

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/workspaces-groups?context_id=uuid \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
  "code": "success",
  "data": [
    {
      "id": "uuid",
      "name": "Group name",
      "description": "Description",
      "created_by_id": "uuid",
      "updated_by_id": "uuid",
      "created_at": "2025-01-01T00:00:00.911Z",
      "updated_at": "2025-01-01T00:00:00.911Z",
      "business_id": "uuid",
      "context_id": "uuid",
      "workspaces": [
        {
          "id": 1234,
          "name": "Workspace name",
          "description": "Description",
          "context_id": "uuid",
          "access_scope": "private",
          "created_at": "2025-01-01T00:00:00.911Z",
          "business_id": "uuid",
          "workspace_group_id": "uuid"
        }
      ],
      "access_scope": "public"
    }
  ],
  "meta": {
    "page": 1,
    "page_size": 10,
    "total": 1
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```

***

#### 2. Access Workspace Group Information

Returns information about a specific group.

* **URL:** `/lighthouse/tenancies/{tenancy_id}/workspaces-groups/{id}`
* **Method:** `GET`
* **Description:** Returns information about a single group.

**Query Params**

| Name | Type | Required | Description |
| ---- | ---- | -------- | ----------- |
|      |      |          |             |

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/workspaces-groups/{id} \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
  "code": "success",
  "data": {
    "id": "uuid",
    "name": "Group name",
    "description": "Description",
    "created_at": "2025-01-01T00:00:00.911Z",
    "updated_at": "2025-01-01T00:00:00.911Z",
    "business_id": "uuid",
    "context_id": "uuid",
    "workspaces": [
      {
        "id": 1234,
        "name": "Workspace name",
        "description": "Description",
        "context_id": "uuid",
        "access_scope": "private",
        "created_at": "2025-01-01T00:00:00.911Z",
        "business_id": "uuid",
        "workspace_group_id": "uuid"
      }
    ],
    "access_scope": "public"
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```

**Error Response (404 Not Found)**

```json
{
  "code": "workspace-group/not-found",
  "message": "Workspace group not found"
}
```


### Views

# Views

#### 1. List Views

Returns a list of all views.

* **URL:** `/lighthouse/tenancies/{tenancy_id}/workspaces/{workspace_id}/views`
* **Method:** `GET`
* **Description:** Retrieves a non-paginated list of views.

**Query Params**

| Name | Type | Required | Description |
| ---- | ---- | -------- | ----------- |
|      |      |          |             |

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/workspaces/{workspace_id}/views \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
  "code": "success",
  "data": {
    "views": [
      {
        "id": 1,
        "name": "View name",
        "description": null,
        "created_at": "2025-01-01T00:00:00.911Z"
      }
    ],
    "total": 1
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```

***

#### 2. Access View Information

Returns information about a specific view.

* **URL:** `/lighthouse/tenancies/{tenancy_id}/views/{id}`
* **Method:** `GET`
* **Description:** Returns information about a single view.

**Query Params**

| Name | Type | Required | Description |
| ---- | ---- | -------- | ----------- |
|      |      |          |             |

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/views/{id} \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
  "code": "success",
  "data": {
    "id": 123,
    "name": "View name",
    "description": null,
    "workspace": {
      "id": 1234,
      "name": "Workspace name"
    }
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```

**Error Response (404 Not Found)**

```json
{
  "code": "view/not-found",
  "message": "View not found"
}
```

***

#### 3. Get View Data

* **URL:** `/lighthouse/tenancies/{tenancy_id}/views/{id}/data`
* **Method:** `GET`
* **Description:** Returns the access token and other information based on the provided credentials.

**Query Params**

| Name        | Type   | Required | Description                                                                                                            |
| ----------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| start\_date | date   | No       | Start date of the period (YYYY-MM-DD). Default: Beginning of the current month                                         |
| end\_date   | date   | No       | End date of the period (YYYY-MM-DD). Default: End of the current month                                                 |
| date\_type  | string | No       | Enter "month" if you want to filter by competence (monthly basis), or "date" if you want to filter by a specific date. |
| filters     | JSON   | No       | Enter the filters you want to add to the view, following the JSON format according to the example below.               |

**Example of JSON filters**

<pre><code>[
    {
        "name": "lineitem/usageaccountid",
        "data_type": "string",
        "role": "filter",
        "filters": [
            {
                "expression": "IS",
                "value": ["12345678901"],
                "negative_expression": false
            }
        ]
    }
<strong>]
</strong></code></pre>

| Column                       | Type           | Required | Description                                                             |
| ---------------------------- | -------------- | -------- | ----------------------------------------------------------------------- |
| name                         | string         | Yes      | Name of the column you want to filter                                   |
| data\_type                   | string         | Yes      | Enter the column type. Possible values: "string", "number", and "date". |
| role                         | string         | Yes      | Enter the rule type. Possible value: "filter".                          |
| filters.expression           | string         | Yes      | Enter the filter expression. Possible values: "IS", "CONTAINS".         |
| filters.value                | Array\<string> | Yes      | Enter the values you want to filter by.                                 |
| filters.negative\_expression | Boolean        | No       | Specify if you want to apply a negation expression.                     |

**Example Request**

```bash
curl -X GET https://api.piercloud.io/lighthouse/tenancies/{tenancy_id}/views/{id}/data \
     -H "Authorization: Bearer  "
```

**Successful Response (200 OK)**

```json
{
    "code": "success",
    "data": [
        {
            "key_1": "value_1",
            "key_2": "value_2",
            "key_3": "value_3"
            ...
        }
    ]
}
```

**Error Response (400 Bad Request)**

```json
{
  "code": "bad-request/invalid-parameters",
  "message": "error message"
}
```

**Error Response (401 Unauthorized)**

```json
{
  "code": "failed",
  "message": "invalid or expired token"
}
```

**Error Response (403 Forbidden)**

```json
{
  "code": "authorization/forbidden",
  "message": "Unable to give access to the user"
}
```

**Error Response (404 Not Found)**

```json
{
  "code": "view/not-found",
  "message": "View not found"
}
```

