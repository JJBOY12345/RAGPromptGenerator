---
title: Relational & NoSQL Database Schema Architect
category: software_development
subcategory: database_design
tags:
  - database-design
  - schema-architecture
  - sql
  - postgresql
  - normalization
difficulty: advanced
depth: deep
retrieval_keywords:
  - database design spec
  - sql schema architect
  - erd relationship diagram
  - database normalization guide
  - query performance indexing
  - postgresql ddl generator
use_case: >
  Retrieve when the user is planning database schema architectures, SQL scripts,
  normalizing data models, or designing indexes for performance.
placeholder_count: 2
version: "1.0"
---

# Relational & NoSQL Database Schema Architect

## Purpose
This template generates highly optimized relational database schemas (focused primarily on PostgreSQL and MySQL) or NoSQL data models. It models strict relationships, normalizes models to 3NF/BCNF, creates robust indexes, and ensures referential integrity via foreign key cascades.

## When to Retrieve This Template
- "Design a PostgreSQL schema for an e-commerce platform with products, orders, and clients."
- "Create an optimized MySQL database for a medical clinic booking system."
- "Write the SQL DDL commands for a school management app database."
- "How do I model a many-to-many relationship with junction tables in SQL?"

## Prompt Framework
```markdown
You are a Principal Database Architect specializing in writing performant, secure, and highly normalized database schemas.

### 1. TARGET DOMAIN & TECH STACK
- **System Domain:** {{SYSTEM_DOMAIN}}
- **Database Engine:** [Choose: PostgreSQL | MySQL | SQLite | MongoDB | mixed hybrid]
- **Key Schema Entities:** {{PRIMARY_ENTITIES}} (comma-separated list)
- **Target Normalization Level:** [Choose: 3NF | BCNF | 2NF (for analytical data warehouses)]

### 2. DATA MODELING STRATEGIES
- **Key Constraints:** Mandatory Primary Keys (UUIDs or BIGSERIAL), non-nullable audit fields (`created_at`, `updated_at`).
- **Referential Integrity:** Enforce explicit FOREIGN KEY constraints with cascading deletions or nullifications where necessary.
- **Indexing Rules:** B-Tree indexes on highly joined foreign keys, unique indices on alternate keys, partial indices for conditional flags.

### 3. EXPECTED DELIVERABLES
1. **Entity-Relationship Diagram (ERD):** Documented textual mapping of tables, columns, constraints, and cardinalities (1:1, 1:N, N:M).
2. **Standard-Compliant SQL DDL Script:** Executable CREATE TABLE scripts, schema scopes, primary/foreign key definitions, and checks.
3. **Indexing Script:** Optimized CREATE INDEX commands matching query workloads.
4. **Normalization & Denormalization Notes:** Brief discussion of BCNF mapping and any intentional performance trade-offs.
```

## Required Context
- System Domain: {{SYSTEM_DOMAIN}}
- Primary Entities: {{PRIMARY_ENTITIES}}

---

## Optional Configuration
- DB Engine: [Choose one: PostgreSQL | MySQL | MongoDB]
- ID Strategy: [Choose: Auto-incrementing BigInt | UUIDv4]
- Add Seed Data: [Yes / No]

---

## Full Example Prompt
```markdown
You are a Principal Database Architect specializing in writing performant, secure, and highly normalized database schemas.

### 1. TARGET DOMAIN & TECH STACK
- **System Domain:** Subscription-based Video Streaming Platform
- **Database Engine:** PostgreSQL
- **Key Schema Entities:** users, subscriptions, plans, viewing_logs
- **Target Normalization Level:** 3NF / BCNF

### 2. DATA MODELING STRATEGIES
- **Key Constraints:** UUIDv4 for ID fields, audit fields on all main tables.
- **Referential Integrity:** Set cascading deletions on log relations, restrict deletes on payment records.

### 3. EXPECTED DELIVERABLES
1. **Entity-Relationship Diagram (ERD):** Map tables and connections in clear text markup.
2. **Standard-Compliant SQL DDL Script:** Executable DDL schema for PostgreSQL.
3. **Indexing Script:** Custom CREATE INDEX commands for fast viewing log fetches.
```

## Best Practices
1. **Prefer UUIDs over Serial IDs:** Use UUIDs for public-facing IDs to prevent enumeration attacks and simplify distributed database merges.
2. **Auditing Fields:** Include `created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP` and an automated trigger for `updated_at` on every table.
3. **Prevent Junction Table Bloat:** Junction tables for N:M relationships must declare a composite primary key (`(table_a_id, table_b_id)`).
4. **Lowercase Naming:** Use `snake_case` with lowercase characters for tables, fields, and index names to prevent uppercase syntax mapping bugs.
5. **Add CHECK Constraints:** Enforce data validation at the database layer using SQL `CHECK` blocks (e.g., `price >= 0`).

## Common Mistakes to Avoid
- **Missing Foreign Key Indexes:** Forgetting indexes on foreign key columns, causing nested-loop sequential scans during large JOIN operations.
- **Using Naked text Datatype:** Using elastic types without sizing constraints for bounded attributes.
- **Hard Deleting Audited Data:** Deleting records permanently when regulatory frameworks require soft-deletion flags.
- **Storing Raw Passwords:** Storing raw authentication strings instead of requiring hashed, salted keys.
