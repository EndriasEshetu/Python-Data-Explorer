# Database Schema

## Database

`retail_analysis.db`

The database stores retail transaction data in a relational structure to support SQL-based analysis.

## Tables

### countries

Stores the countries represented in the dataset.

| Column       | Type    | Key | Description               |
| ------------ | ------- | --- | ------------------------- |
| country_id   | INTEGER | PK  | Unique country identifier |
| country_name | TEXT    |     | Country name              |

### customers

Stores customer information.

| Column      | Type    | Key | Description                       |
| ----------- | ------- | --- | --------------------------------- |
| customer_id | INTEGER | PK  | Unique customer identifier        |
| country_id  | INTEGER | FK  | References `countries.country_id` |

### products

Stores product information.

| Column      | Type    | Key | Description               |
| ----------- | ------- | --- | ------------------------- |
| product_id  | INTEGER | PK  | Unique product identifier |
| stock_code  | TEXT    |     | Original product code     |
| description | TEXT    |     | Product description       |

### transactions

Stores individual transaction lines.

| Column            | Type    | Key | Description                        |
| ----------------- | ------- | --- | ---------------------------------- |
| transaction_id    | INTEGER | PK  | Unique transaction-line identifier |
| invoice_no        | TEXT    |     | Invoice/order identifier           |
| product_id        | INTEGER | FK  | References `products.product_id`   |
| customer_id       | INTEGER | FK  | References `customers.customer_id` |
| invoice_date      | TEXT    |     | Transaction date and time          |
| quantity          | INTEGER |     | Quantity purchased                 |
| unit_price        | REAL    |     | Price per unit                     |
| is_zero_quantity  | INTEGER |     | Zero-quantity flag                 |
| is_return         | INTEGER |     | Return flag                        |
| is_zero_price     | INTEGER |     | Zero-price flag                    |
| is_negative_price | INTEGER |     | Negative-price flag                |
| is_cancelled      | INTEGER |     | Cancellation flag                  |

## Relationships

- One country can have many customers.
- One customer can have many transactions.
- One product can appear in many transactions.

## Entity Relationship

```text
countries
    1
    |
    |----< customers
              |
              |----< transactions >---- products
```
