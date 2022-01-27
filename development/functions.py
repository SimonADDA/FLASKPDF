"""Use of PDFminer to extract content and metadata"""

from development.extract import create_connection


def allowed_file(filename: str):
    """return only pdf files"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {'pdf'}


def get_text_id(conn, id_text):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("""SELECT content 
                FROM pdf 
                WHERE id=?""", (id_text,))
    rows = cur.fetchall()
    return rows


def get_meta_id(conn, id_meta):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("""SELECT date_creation, author, creator, producer, subject, title, modification_date, number_of_page 
                FROM pdf
                WHERE id=?""", (id_meta,))
    rows = cur.fetchall()
    return rows


def dict_factory(cursor, row):
    """Convert to dictionnary"""
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    return dict


def show_text_id(id_txt):
    """Display text content of the pdf  from the database"""
    database = r"development/database/pdf_extraction.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        conn.row_factory = dict_factory
        return get_text_id(conn, id_txt)


def show_metadata_id(id_meta):
    """Display metadata  of the pdf  from the database"""
    database = r"development/database/pdf_extraction.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        conn.row_factory = dict_factory
        return get_meta_id(conn, id_meta)[0]




