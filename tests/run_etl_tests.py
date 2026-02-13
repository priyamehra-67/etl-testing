import sqlite3

DB_PATH = "sales.db"

def run_query(query, description):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()

    print("\n" + description)
    print("Result:", rows)

# 1. Record count check
run_query(
    "SELECT COUNT(*) FROM sales_target;",
    "1. Record Count Check"
)

# 2. Duplicate check
run_query(
    """
    SELECT order_id, COUNT(*)
    FROM sales_target
    GROUP BY order_id
    HAVING COUNT(*) > 1;
    """,
    "2. Duplicate Check"
)

# 3. Null check
run_query(
    "SELECT * FROM sales_target WHERE amount IS NULL;",
    "3. Null Check"
)

# 4. Transformation check
run_query(
    "SELECT order_id, amount, amount_category FROM sales_target;",
    "4. Transformation Check"
)

# 5. Date validation
run_query(
    "SELECT * FROM sales_target WHERE order_date IS NULL;",
    "5. Date Validation"
)
