---
title: Work Breakdown Structure (WBS) & Task Planner
category: productivity
subcategory: task_management
tags: [task-breakdown, wbs, gtd]
difficulty: intermediate
depth: medium
retrieval_keywords: [work breakdown structure, gtd task list, project roadmap]
use_case: Retrieve to decompose projects into prioritized, hourly-estimated tasks.
placeholder_count: 3
version: "1.0"
---
# Work Breakdown Structure (WBS) & Task Planner
## Purpose
Generates prioritized Work Breakdown Structures using GTD and Eisenhower frameworks.
## When to Retrieve This Template
- "Break down the launch of a new marketing website into tasks."
- "Generate a WBS for a database migration project."
- "Create a GTD-prioritized checklist to write a research paper."
## Prompt Framework
You are a Project Manager. Build a WBS for {{PROJECT_GOAL}} due by {{DEADLINE}} to be executed by {{TEAM_SIZE}}. Map priorities P1/P2/P3 with hour estimates.
## Required Context
- Project Goal: {{PROJECT_GOAL}}
- Deadline: {{DEADLINE}}
- Team Size: {{TEAM_SIZE}}
## Optional Configuration
- Granularity: [High-level milestones | Detailed action items]
## Example Prompt
Decompose a 2-week mobile app CD pipeline migration setup for a solo dev.
## Best Practices
1. Ensure the sum of child tasks equals 100% of the parent epic scope.
2. Initiate all low-level action items with strong, measurable action verbs.
3. Limit individual action items to a maximum execution cap of 8 hours.
