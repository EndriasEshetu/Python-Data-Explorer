# Python Data Explorer

A practical data analysis project using Python and Pandas to explore
retail sales transactions, investigate data quality, identify sales
trends, and communicate business insights through visualizations.

> **Project status:** In progress\
> **Project type:** Exploratory Data Analysis (EDA)\
> **Focus:** Data cleaning, sales analysis, visualization, and business
> reporting

## 1. Project Overview

The goal of this project is to analyze retail sales data and answer
common business questions about revenue, product performance, category
performance, and sales trends.

The project follows a typical data analyst workflow:

1.  Obtain and inspect a dataset.
2.  Identify data-quality issues.
3.  Clean and validate the data.
4.  Create useful analytical features.
5.  Calculate business metrics.
6.  Visualize results.
7.  Summarize findings and recommendations.

## 2. Business Questions

This project aims to answer the following questions:

- What is the total revenue in the dataset?
- What is the average order value (AOV)?
- Which products sell the most units?
- Which products generate the most revenue?
- Which categories contribute the most revenue?
- How does revenue change over time?
- Which countries or regions contribute the most sales, where the
  available data supports that comparison?

## 3. Dataset

The initial dataset is **Online Retail** from the UCI Machine Learning
Repository.

- **Source:** [UCI Online Retail
  dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Format:** Excel (`.xlsx`)
- **Original size:** Approximately 541,909 transaction records
- **Period:** December 2010 to December 2011
- **License:** CC BY 4.0

The original dataset includes invoice number, stock code, product
description, quantity, invoice date, unit price, customer ID, and
country.

For the initial exploration, a smaller sample may be used. The dataset
does **not** contain a product category or sales region column. Any
derived categories or geographic groupings will be documented, and
country will not be presented as a sales region without an explicit
definition.

### Data dictionary

---

Field Description

---

`order_id` Invoice or transaction identifier

`order_date` Date and time of the invoice

`product` Product description

`quantity` Number of units in the transaction

`unit_price` Price per unit in the dataset's
currency

`country` Customer's country, as supplied by
the source

`category` To be added only if a documented
categorization is created

`region` To be added only if a documented
geographic mapping is created

---

## 4. Tools and Technologies

- **Python** --- analysis programming language
- **Pandas** --- data loading, cleaning, transformation, and
  aggregation
- **NumPy** --- numerical operations
- **Matplotlib** --- data visualization
- **Seaborn** --- statistical visualization (optional)
- **Jupyter Notebook** --- interactive analysis
- **Git and GitHub** --- version control and project publishing

## 5. Repository Structure

```text
python-data-explorer/
├── data/
│   ├── Online Retail.xlsx
│   ├── raw_sales.csv
│   └── cleaned_sales.csv
├── notebooks/
│   └── sales_analysis.ipynb
├── charts/
│   ├── product_sales.png
│   ├── monthly_revenue.png
│   ├── category_revenue.png
│   └── regional_revenue.png
├── reports/
│   └── analysis_report.md
├── src/
│   └── data_cleaning.py
├── requirements.txt
├── .gitignore
└── README.md
```

Files will be added as the project progresses. Do not commit duplicate
or generated files unless they are useful for reproducing the analysis.

## 6. Project Workflow

### Step 1: Data acquisition

Download the dataset from the UCI link above and place it in the `data/`
directory.

### Step 2: Data inspection

Use Pandas to examine:

- The first 10 rows
- Number of rows and columns
- Column names and data types
- Summary statistics
- Missing values and duplicate records

### Step 3: Data cleaning

Investigate and document:

- Missing product descriptions
- Duplicate records
- Invalid or unparseable dates
- Negative or zero quantities
- Negative or zero unit prices
- Cancelled invoices and possible returns

Cleaning decisions should be based on the meaning of the data. For
example, negative quantities may represent returns rather than erroneous
records. Record the number of affected rows and explain whether each
issue is corrected, excluded, or retained.

### Step 4: Feature engineering

Calculate transaction revenue:

`revenue = quantity × unit_price`

Create a month field from the invoice date for monthly analysis.
Interpret revenue carefully because returns and cancellations can affect
totals.

### Step 5: Exploratory data analysis

Calculate and investigate:

- Total revenue
- Average order value, using a clearly defined order identifier
- Units sold
- Product sales and revenue
- Monthly revenue
- Country-level sales, if relevant

### Step 6: Visualization

Planned charts:

1.  **Product sales:** compare products by units sold.
2.  **Monthly revenue:** examine revenue over time.
3.  **Category revenue:** include only after a category mapping is
    defined.
4.  **Geographic sales:** compare countries or documented regions.

### Step 7: Reporting

Write a Markdown report containing key metrics, at least five
evidence-based findings, business implications, recommendations, and
project limitations.

## 7. Installation and Usage

### Prerequisites

- Python 3.10 or later
- Git
- Jupyter Notebook or VS Code with Jupyter support

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-data-explorer.git
cd python-data-explorer
```

Replace `YOUR_USERNAME` with your GitHub username.

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

If you are reading the original Excel dataset, make sure `openpyxl` is
included in `requirements.txt`.

### Launch the notebook

```bash
jupyter notebook
```

Open `notebooks/sales_analysis.ipynb` and run the cells in order.

## 8. Key Findings

> Update this section after completing the analysis. Do not publish
> example values as actual results.

1.  **Overall sales:** \[Insert the calculated total revenue and the
    period covered.\]
2.  **Product performance:** \[Identify products with the highest unit
    sales and revenue.\]
3.  **Order value:** \[Report the calculated average order value and
    explain its definition.\]
4.  **Sales trend:** \[Describe the observed monthly revenue pattern.\]
5.  **Geographic performance:** \[Summarize country or region results,
    where supported by the data.\]

## 9. Business Recommendations

Recommendations will be based on the observed results. Potential areas
to investigate include:

- Reviewing inventory for products with consistently high unit sales.
- Investigating products with high revenue but low unit volume.
- Examining months with unusual changes in revenue.
- Comparing geographic markets using consistent definitions.
- Separating returns and cancellations from completed sales when
  reporting performance.

Only retain recommendations that are supported by the analysis.

## 10. Limitations

- The source data covers a limited historical period and may not
  represent current retail behavior.
- The dataset does not provide product cost, so revenue should not be
  described as profit.
- Customer-level information is incomplete for some transactions.
- Negative quantities may represent returns and require careful
  treatment.
- The source does not include product categories or predefined sales
  regions.
- A small sample may not represent the full dataset.

## 11. Future Improvements

- Add SQL analysis using a relational database.
- Build an interactive dashboard with Power BI or Streamlit.
- Add automated data-quality checks.
- Compare sales across longer periods if more data becomes available.
- Explore customer purchasing patterns where the data supports them.

## 12. Author

**Endrias Eshetu**\
GitHub: [EndriasEshetu](https://github.com/EndriasEshetu)

---

_This project is for learning and portfolio development. All conclusions
should be reproducible from the included data and analysis._
