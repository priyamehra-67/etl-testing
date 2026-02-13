# ETL Testing Project – Sales Data Validation

## Overview
This project demonstrates an **ETL Testing workflow** where sales data is extracted from a CSV file,
transformed for data quality, and loaded into a SQLite database.
The primary focus of this project is **ETL data validation** using **SQL and Python automation**.

---

## ETL Flow
1. **Extract**
   - Source data is read from a CSV file

2. **Transform**
   - Removed duplicate records
   - Handled null values
   - Standardized column names
   - Applied business rules to categorize sales amounts

3. **Load**
   - Cleaned data is loaded into a SQLite database

---

## ETL Testing Scope
The following ETL testing validations are performed:

- Source to target **record count validation**
- **Duplicate data detection**
- **Null value checks**
- **Transformation rule validation**
- **Data type and date validation**

---

## Automated ETL Testing
ETL validations are automated using Python by executing SQL queries against the target database.
This ensures repeatable and reliable data quality checks after each ETL run.

---

## Technologies Used
- Python
- Pandas
- SQLite
- SQL

---

## Project Structure
ETL_Testing_Project
├── data/
│ └── sales_data.csv
├── etl/
│ └── etl_process.py
├── tests/
│ ├── etl_validation.sql
│ └── run_etl_tests.py
├── README.md


---

## How to Run the Project

### Step 1: Run ETL Process
From the project root directory:
```bash
python etl/etl_process.py
This will create the target database and load transformed data.

Step 2: Run ETL Tests (Automated)
python tests/run_etl_tests.py
All ETL validation results will be displayed in the terminal.

Key Learnings
Practical understanding of ETL testing concepts

Writing SQL queries for data validation

Automating ETL tests using Python

Handling real-world data quality issues
