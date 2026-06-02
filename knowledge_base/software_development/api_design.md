---
title: RESTful & OpenAPI API Design Specifier
category: software_development
subcategory: api_design
tags:
  - api-design
  - openapi
  - rest
  - graphql
  - system-integration
difficulty: advanced
depth: deep
retrieval_keywords:
  - api design spec
  - openapi specification
  - rest api developer
  - graphql schema designer
  - endpoint documentation
  - web service contract
use_case: >
  Retrieve when the user is designing APIs, endpoints, webhooks,
  or writing OpenAPI/Swagger technical documentation.
placeholder_count: 3
version: "1.0"
---

# RESTful & OpenAPI API Design Specifier

## Purpose
This template generates professional, industry-standard API designs and OpenAPI 3.1 specifications. It enforces RESTful naming conventions, uniform resource mapping, pagination, error schemas, security strategies, and robust webhook patterns.

## When to Retrieve This Template
- "Design the REST API for a subscription billing platform."
- "Write an OpenAPI 3.1 schema for our user account microservice."
- "Create an API interface spec between our payment processor and backend."
- "How do I structure error payloads and responses for public APIs?"

## Prompt Framework
```markdown
You are a Principal API Architect and REST/GraphQL Integration Specialist. Your goal is to design a secure, production-grade, and self-documenting API.

### 1. API PROFILE & SECURITY
- **Service Name:** {{API_NAME}}
- **Core Purpose:** {{API_PURPOSE}}
- **Resource Model:** {{PRIMARY_RESOURCES}} (comma-separated list)
- **Auth Strategy:** [Choose: JWT Bearer Tokens | OAuth2 Client Credentials | API Keys | Session-based]
- **API Versioning:** [Choose: URI versioning (e.g., /v1/...) | Header-based versioning]

### 2. ARCHITECTURAL PROTOCOLS
- **Resource Naming:** Nouns only, lowercase, plural (e.g., `/users`, `/billing-accounts`).
- **Idempotency & Safety:** Strict enforcement of GET/PUT/DELETE idempotency and POST non-idempotency.
- **Pagination Strategy:** Cursor-based pagination for high-frequency resource streams, offset for static tables.
- **Rate Limiting:** HTTP header definitions (`X-RateLimit-Limit`, `X-RateLimit-Remaining`).

### 3. OUTPUT SPECIFICATION CONTRACTS
1. **OpenAPI 3.1.0 Yaml/JSON Schema:** Full spec including paths, request bodies, components, and securitySchemes.
2. **Detailed Endpoint Profiles:** Request verbs, parameters, exact JSON request/response bodies, and description.
3. **Robust Error Payload Contract:** A strict RFC-7807 problem details JSON schema for all error codes.
```

## Required Context
- API Name: {{API_NAME}}
- API Purpose: {{API_PURPOSE}}
- Primary Resources: {{PRIMARY_RESOURCES}}

---

## Optional Configuration
- Versioning Style: [Optional: Header Versioning | URL Path /v1/]
- Format: [Choose: YAML | JSON]
- Include Webhooks: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Principal API Architect and REST/GraphQL Integration Specialist. Your goal is to design a secure, production-grade, and self-documenting API.

### 1. API PROFILE & SECURITY
- **Service Name:** InvoiceHub API
- **Core Purpose:** Managing client invoicing, invoice lifecycles, and automatic PDF receipt issuance.
- **Resource Model:** clients, invoices, payments
- **Auth Strategy:** JWT Bearer Tokens
- **API Versioning:** URI versioning (e.g., `/v1/...`)

### 2. ARCHITECTURAL PROTOCOLS
- **Resource Naming:** Nouns only, lowercase, plural.
- **Idempotency & Safety:** Strict enforcement of API structures.
- **Pagination Strategy:** Cursor-based pagination using `starting_after` and `limit`.

### 3. OUTPUT SPECIFICATION CONTRACTS
1. **OpenAPI 3.1.0 Yaml/JSON Schema:** Full spec including paths, schemas, and security.
2. **Detailed Endpoint Profiles:** Exact JSON structures for creating, retrieving, and paying invoices.
3. **Robust Error Payload Contract:** Standard JSON error envelopes with code, message, and target details.
```

## Best Practices
1. **Use HTTP Status Semantics:** Return correct codes (`201 Created` for creations, `422 Unprocessable Entity` for validation errors).
2. **CamelCase/snake_case Consistency:** Maintain snake_case keys in all JSON payloads and query parameters across all endpoints.
3. **Secure Headers:** Include security headers (`Content-Type: application/json`, `X-Content-Type-Options: nosniff`) in responses.
4. **Define Schemas in Components:** Keep OpenAPI files clean by defining models inside the `#/components/schemas` section.
5. **Rate Limiting Enforcements:** Return `429 Too Many Requests` when limits are breached with a `Retry-After` header.

## Common Mistakes to Avoid
- **Verb Endpoints:** Creating endpoints like `/getInvoices` or `/createClient` instead of using HTTP methods on nouns.
- **Returning naked arrays:** Returning `[]` as the top level of responses. Always wrap datasets inside an object envelope (`{ "data": [...] }`).
- **Leaking Server Stack traces:** Returning verbose server framework error messages in `500` responses, exposing internals to users.
- **Silent Validation Failures:** Returning `200 OK` for requests that failed semantic validation, forcing client-side parsing.
