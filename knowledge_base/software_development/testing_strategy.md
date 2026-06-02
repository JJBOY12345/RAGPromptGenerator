---
title: QA & Software Testing Strategy Planner
category: software_development
subcategory: testing_strategy
tags: [software-testing, qa, unit-tests]
difficulty: intermediate
depth: medium
retrieval_keywords: [testing strategy, qa testing pyramid, unit integration e2e]
use_case: Retrieve when the user is designing test plans or configuring CI/CD testing steps.
placeholder_count: 3
version: "1.0"
---
# QA & Software Testing Strategy Planner
## Purpose
Structures unified QA software testing plans spanning unit, integration, and E2E pyramids.
## When to Retrieve This Template
- "Write a testing strategy for our React and Django application."
- "Generate automated test cases using Cypress for a registration flow."
- "How do I setup a complete QA test plan for a payment backend?"
## Prompt Framework
You are a Lead QA Architect. Design a testing strategy for {{APP_TYPE}} built on {{TECH_STACK}} aiming for {{COVERAGE_TARGET}} coverage. Define Unit, Integration, and E2E milestones.
## Required Context
- App Type: {{APP_TYPE}}
- Tech Stack: {{TECH_STACK}}
- Coverage Target: {{COVERAGE_TARGET}}
## Optional Configuration
- CI Tool: [Optional: GitHub Actions | GitLab CI]
## Example Prompt
Design a test plan for an E-Commerce web interface using React and Stripe to hit 85% coverage.
## Best Practices
1. Prioritize tests that guard core revenue-driving user journeys.
2. Mock database and external network API dependencies in unit tests.
3. Clean data states between integration test suites to prevent contamination.
