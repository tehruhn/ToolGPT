import sqlite3
from typing import List, Any, Tuple

def get_max_sale(database: str = 'sales_data.db') -> Tuple[str, str, int, float]:
    """
    Function to get the row with maximum sales quantity.

    Parameters
    ----------
    database : string
        The name of the SQLite database.

    Returns
    -------
    max_sale : Tuple[str, str, int, float]
        The row with maximum sales quantity.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(database)

    # Create a cursor object
    c = conn.cursor()

    # Execute the query
    c.execute('SELECT * FROM sales ORDER BY quantity DESC LIMIT 1')

    # Fetch the result
    max_sale = c.fetchone()

    # Close the connection
    conn.close()

    return max_sale


def get_top_rows(column: str, database: str = 'sales_data.db', limit: int = 5) -> List[Tuple[str, str, int, float]]:
    """
    Function to get the top rows sorted by a particular column.

    Parameters
    ----------
    column : string
        The column to sort by.
    database : string
        The name of the SQLite database.
    limit : integer
        The number of rows to return.

    Returns
    -------
    top_rows : List[Tuple[str, str, int, float]]
        The top rows sorted by the given column.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(database)

    # Create a cursor object
    c = conn.cursor()

    # Execute the query
    c.execute(f'SELECT * FROM sales ORDER BY {column} DESC LIMIT ?', (limit,))

    # Fetch the result
    top_rows = c.fetchall()

    # Close the connection
    conn.close()

    return top_rows


def setup_database(database: str = 'sales_data.db') -> None:
    """
    Function to setup the SQLite database and populate it with sample sales data.

    Parameters
    ----------
    database : string
        The name of the SQLite database.
    """

    # Connect to the SQLite database
    conn = sqlite3.connect(database)

    # Create a cursor object
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE sales
                 (name text, product text, quantity integer, price real)''')

    # Insert a row of data
    sales_data = [
        ('John', 'Apples', 10, 1.25),
        ('Sarah', 'Bananas', 20, 0.75),
        ('Dave', 'Oranges', 30, 0.80),
        ('Lisa', 'Pears', 15, 1.50),
        ('Mike', 'Grapes', 40, 2.00),
        ('Mary', 'Cherries', 50, 3.00),
        ('Anne', 'Pineapples', 60, 1.75),
        ('Paul', 'Mangoes', 70, 2.25),
        ('Olivia', 'Peaches', 80, 1.00),
        ('Nick', 'Pomegranates', 90, 2.50)
    ]

    c.executemany('INSERT INTO sales VALUES (?,?,?,?)', sales_data)

    # Save (commit) the changes
    conn.commit()

    # Close the connection
    conn.close()

