import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as err:
        print(err)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    """
    try:
        conn = conn.cursor()
        conn.execute(create_table_sql)
    except Error as err:
        print(err)


def main():
    """ main a table from the create_table_sql statement
    """
    database = r"pdf_extraction.db"

    sql_create_pdf_table = """CREATE TABLE IF NOT EXISTS pdf (
                                    id integer PRIMARY KEY,
                                    date_creation VARCHAR,
                                    author VARCHAR,
                                    creator VARCHAR,
                                    producer VARCHAR,
                                    subject VARCHAR,
                                    title VARCHAR,
                                    modification_date VARCHAR,
                                    number_of_page VARCHAR,
                                    content VARCHAR
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create pdf table
        create_table(conn, sql_create_pdf_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
