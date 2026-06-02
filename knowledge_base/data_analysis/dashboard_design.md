---
title: Business Intelligence Dashboard Designer
category: data_analysis
subcategory: dashboard_design
tags: [data-visualization, dashboard, tableau]
difficulty: intermediate
depth: medium
retrieval_keywords: [dashboard design, kpi metrics, power bi spec]
use_case: Retrieve when planning dashboard charts, layouts, or KPI reports.
placeholder_count: 4
version: "1.0"
---
# Business Intelligence Dashboard Designer
## Purpose
Generates structured KPI dashboard visual plans for Tableau, Power BI, or Grafana.
## When to Retrieve This Template
- "Design a Tableau dashboard layout for sales performance tracking."
- "Generate a Power BI dashboard spec for a warehouse operations team."
- "Create a customer retention dashboard design with metrics."
## Prompt Framework
You are a BI Expert. Design a dashboard spec for {{DASHBOARD_TITLE}} targeting {{TARGET_AUDIENCE}} running at {{REFRESH_RATE}} containing {{PRIMARY_METRICS}}.
## Required Context
- Dashboard Title: {{DASHBOARD_TITLE}}
- Target Audience: {{TARGET_AUDIENCE}}
- Refresh Rate: {{REFRESH_RATE}}
- Primary Metrics: {{PRIMARY_METRICS}}
## Optional Configuration
- Interactivity: [Static reports | Active filters & drill-downs]
## Example Prompt
Design an executive revenue dashboard spec for C-suite daily monitoring.
## Best Practices
1. Reserve the top-left visual quadrant for the absolute core KPI cards.
2. Limit dashboards to a maximum of 3 distinct, clean chart configurations.
3. Avoid pie charts for categorical sets exceeding 3 unique dimensions.
