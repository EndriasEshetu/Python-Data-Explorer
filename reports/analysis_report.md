# Online Retail Sales Analysis

## 1. Executive Summary

This project analyzes the UCI Online Retail dataset to understand sales performance, product performance, monthly revenue patterns, geographic distribution, and negative-quantity transactions.

The analysis was performed using Python, Pandas, Matplotlib, Seaborn, and Jupyter Notebook.

The dataset initially contained 541,909 transaction records. After removing 528 exact duplicate rows, 541,381 records remained in the cleaned transaction dataset.

The analysis of positive sales transactions produced the following results:

| Metric                                           |        Result |
| ------------------------------------------------ | ------------: |
| Positive sales revenue                           | 10,642,110.80 |
| Total orders                                     |        19,960 |
| Total units sold                                 |     5,572,420 |
| Average order value                              |        533.17 |
| Negative-quantity records                        |        10,587 |
| Recorded value of negative-quantity transactions |   -893,979.73 |

The analysis found that PAPER CRAFT, LITTLE BIRDIE had the highest sales quantity, while DOTCOM POSTAGE generated the highest revenue. The United Kingdom led in both revenue and order count. November 2011 had the highest monthly revenue, while February 2011 had the lowest.

## 2. Project Objectives

The main objectives of this project were to:

- Investigate and clean the retail transaction dataset.
- Calculate revenue and create useful analytical features.
- Measure overall sales performance.
- Identify top-performing products.
- Analyze monthly revenue trends.
- Compare sales across countries.
- Examine negative-quantity transactions.
- Present findings through visualizations and a written report.

## 3. Dataset Overview

The project uses the UCI Online Retail dataset, which contains transactions from a UK-based online retailer.

The dataset includes the following fields:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

Each row represents a transaction line rather than necessarily an entire customer order.

## 4. Data Preparation

The original dataset was inspected for missing values, duplicate rows, unusual quantities, invalid prices, and cancellation indicators.

The cleaning process included:

- Removing exact duplicate records.
- Preserving transaction records with missing customer identifiers.
- Retaining negative quantities in the cleaned transaction dataset for further investigation.
- Separating positive sales transactions for sales performance analysis.
- Excluding records that did not meet the defined positive sales analysis criteria.

After removing exact duplicates, 541,381 records remained in the cleaned transaction dataset.

The positive sales dataset was used for the main sales analysis. Negative-quantity records were analyzed separately.

## 5. Methodology

The project followed these stages:

1. Data loading and initial inspection using Pandas.
2. Data quality investigation.
3. Data cleaning and validation.
4. Feature engineering, including revenue and date features.
5. Exploratory Data Analysis.
6. Data visualization.
7. Interpretation and reporting of findings.

Revenue was calculated by multiplying quantity by unit price for each transaction line.

Monthly revenue was calculated by grouping positive sales by year and month. Product and country performance were examined using aggregated revenue, quantity, and order counts.

## 6. Key Findings

### 6.1 Overall Sales Performance

The positive sales dataset recorded 10,642,110.80 in revenue across 19,960 orders, with 5,572,420 units sold.

The average order value was 533.17.

These figures describe the positive sales records under the project's cleaning criteria.

### 6.2 Product Performance

PAPER CRAFT, LITTLE BIRDIE was the product with the highest quantity sold, while DOTCOM POSTAGE generated the highest revenue.

This difference demonstrates that the product with the greatest sales volume is not necessarily the product with the highest revenue.

### 6.3 Monthly Sales Trends

November 2011 recorded the highest monthly revenue, while February 2011 recorded the lowest.

The results demonstrate variation in revenue during the observed period. Further investigation would be needed to determine the factors behind these differences.

### 6.4 Country Performance

The United Kingdom recorded the highest revenue and the largest number of orders.

This indicates that the UK was the main market in the analyzed dataset. A more detailed comparison of other countries can help quantify the concentration of sales.

### 6.5 Negative-Quantity Transactions

The dataset contained 10,587 negative-quantity records with a combined recorded value of -893,979.73.

These records reduce net recorded revenue when their signed values are included. Negative quantities may represent returns or other transaction adjustments, so they should not automatically be interpreted as confirmed customer returns.

## 7. Visualizations

The project produced the following visualizations:

1. Top 10 products by quantity sold.
2. Top 10 products by revenue.
3. Monthly revenue trend.
4. Top 10 countries by revenue.
5. Products with the largest negative recorded values.

The visualizations provide a graphical view of product performance, monthly revenue, geographic distribution, and negative transaction values.

## 8. Business Insights

The analysis suggests several areas for further business investigation:

- **Product performance:** Compare high-volume products with high-revenue products to understand differences in their contribution to sales.
- **Monthly sales:** Investigate the factors associated with high and low revenue months.
- **Geographic concentration:** Examine the dependence of recorded sales on the UK market and compare performance in other countries.
- **Negative transactions:** Investigate negative-quantity records to understand their causes and potential impact on sales reporting.

These are areas for investigation rather than proven explanations of customer behavior or business performance.

## 9. Limitations

- The dataset covers a limited historical period, so the findings should not be assumed to represent current retail behavior.
- Missing customer identifiers limit customer-level analysis.
- Negative quantities may represent returns or other adjustments; their exact meaning cannot always be established from the available columns.
- The dataset does not include predefined product categories, so category-level analysis was not performed.
- The analysis is descriptive and does not establish the causes of sales trends.
- Positive sales revenue is not equivalent to profit because product costs and operating expenses are not included.
- The results depend on the project's data-cleaning rules and should not be treated as audited financial statements.

## 10. Conclusion

This project demonstrates a complete introductory data analysis workflow, from data inspection and cleaning to feature engineering, exploratory analysis, visualization, and reporting.

The analysis identified differences between product sales volume and revenue, variations in monthly revenue, the importance of the UK market in the dataset, and the presence of substantial negative-quantity transactions.

The results provide a foundation for more advanced analysis, including customer segmentation, product-level profitability analysis when cost data becomes available, and forecasting with additional data.

## 11. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git and GitHub

## 12. Project Structure

```text
python-data-explorer/
├── data/
│   ├── Online Retail.xlsx
│   ├── cleaned_transactions.csv
│   ├── cleaned_sales.csv
│   └── engineered_sales.csv
├── notebooks/
│   └── sales_analysis.ipynb
├── charts/
│   ├── top_products_quantity.png
│   ├── top_products_revenue.png
│   ├── monthly_revenue.png
│   ├── top_countries_revenue.png
│   └── negative_value_products.png
├── reports/
│   └── analysis_report.md
├── .gitignore
└── README.md
```
