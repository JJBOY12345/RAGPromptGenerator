---
title: Exploratory Data Analysis (EDA) Blueprint
category: data_analysis
subcategory: eda_framework
tags:
  - data-science
  - eda
  - statistical-analysis
  - python-pandas
  - data-visualization
difficulty: advanced
depth: deep
retrieval_keywords:
  - exploratory data analysis
  - eda python script
  - statistical distribution check
  - correlation analysis matrix
  - outlier detection method
  - data visualization guide
use_case: >
  Retrieve when the user is starting a data analysis task, writing EDA python scripts
  (pandas/numpy/seaborn), checking statistics, or summarizing datasets.
placeholder_count: 6
version: "1.0"
---

# Exploratory Data Analysis (EDA) Blueprint

## Purpose
This template provides a rigorous analytical framework for performing Exploratory Data Analysis (EDA). It guides the user in writing systematic Python scripts to handle missing values, map statistical distributions, run correlations, isolate outliers, design visualizations, and formulate actionable, data-backed business hypotheses.

## When to Retrieve This Template
- "How do I perform a thorough EDA on a new marketing dataset?"
- "Generate a Python script to analyze user churn data distributions."
- "Write an analytical plan to locate correlation anomalies in sales columns."
- "Create a data analysis structure for customer transaction logs."
- "What visualizations and outlier checks should I run on medical survey data?"

## Prompt Framework
```markdown
You are a Principal Data Scientist and Business Intelligence Analyst specializing in statistical modeling and advanced exploratory data analysis.

### 1. DATASET PROFILE & DIMENSIONS
- **Dataset Description:** {{DATASET_DESCRIPTION}}
- **Business Domain:** {{BUSINESS_DOMAIN}}
- **Dataset Shape:** {{ROW_COUNT}} rows, {{COLUMN_COUNT}} columns.
- **Key Columns & Types:** {{KEY_FIELDS}} (e.g., `user_id (str)`, `revenue (float)`)
- **Statistical Depth:** [Choose: Descriptive Statistics Only | Inferential Testing | Predictive Modeling Baseline]

### 2. ANALYTICAL STEPS & SCRIPT SPECIFICATION
- **Data Quality Check:** Code to scan missing values, identify duplicate keys, and handle null inputs.
- **Distribution Analysis:** Plotting univariate distributions using density curves and histograms.
- **Correlation Mapping:** Bivariate correlations (Pearson, Spearman) visualized via annotated heatmaps.
- **Outlier Quarantine:** Isolating numeric anomalies using the Interquartile Range (IQR) method or Z-Score metrics.

### 3. VISUALIZATION DIRECTIVES
- Build clean, publication-ready charts (e.g., Seaborn, Matplotlib, Plotly) with high data-to-ink ratios, labeled axes, and consistent color palettes.

### 4. DELIVERABLES EXPECTED
1. **Clean Python Code (Pandas/Seaborn):** Copy-pasteable script blocks to clean, describe, and plot the dataset.
2. **EDA Executive Report Structure:** Section templates for findings, data limitations, isolated anomalies, and a structured list of 3-5 business hypotheses to test.
```

## Required Context
- Dataset Description: `{{DATASET_DESCRIPTION}}`
- Business Domain: `{{BUSINESS_DOMAIN}}`
- Row Count: `{{ROW_COUNT}}`
- Column Count: `{{COLUMN_COUNT}}`
- Key Fields: `{{KEY_FIELDS}}`
- Analysis Objective: `{{ANALYSIS_OBJECTIVE}}`

---

## Optional Configuration
- Plotting Library: `[Choose: Seaborn | Plotly Express | Matplotlib]`
- Outlier Cutoff: `[Choose: 1.5 * IQR | 3 * Z-score]`
- Show Code Comments: `[Yes / No]`

---

## Full Example Prompt
```markdown
You are a Principal Data Scientist and Business Intelligence Analyst specializing in statistical modeling and advanced exploratory data analysis.

### 1. DATASET PROFILE & DIMENSIONS
- **Dataset Description:** Monthly active customer app usage logs and purchases.
- **Business Domain:** Mobile E-Commerce SaaS
- **Dataset Shape:** 150,000 rows, 12 columns.
- **Key Columns & Types:** `customer_id (str)`, `session_duration (int)`, `monthly_spent (float)`
- **Statistical Depth:** Descriptive Statistics and Inferential Testing
```

## Best Practices
1. **Clean Missing Data First:** Document the strategy for missing values (e.g., median imputation vs. deletion) before executing any charts.
2. **Label Visualizations Clearly:** Every chart must include an descriptive title, labeled X/Y axes with units, and a clear legend.
3. **Handle Skewed Data:** Apply logarithmic transformations (e.g., `np.log1p`) to highly right-skewed variables (like revenue or transaction volumes) before plotting.
4. **Isolate Testable Hypotheses:** Translate statistical observations into clear business ideas (e.g., "High session durations correlate positively with invoice size").
5. **Always Set Random Seeds:** When sampling or bootstrapping datasets, declare a static seed (`random_state=42`) to guarantee reproducible numbers.

## Common Mistakes to Avoid
- **Skipping Data Quality Checks:** Plotting graphs before handling data types or missing fields, leading to runtime script crashes.
- **Overcrowded Heatmaps:** Plotting correlation matrix charts with more than 15 columns, making text and labels illegible.
- **Correlation vs. Causation:** Claiming strong causal relationships solely because of high correlation coefficient numbers.
- **Ignoring Multi-Collinearity:** Suggesting regression features that are highly collinear without addressing structural variance inflation.
