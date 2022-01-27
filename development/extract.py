"""Extraction of and connection to DataBase"""

from io import StringIO
import sqlite3
from sqlite3 import Error
from PyPDF2 import PdfFileReader
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, resolve1
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_pdf(conn, project):
    """
    Create a new pdf into the projects table
    """
    sql = '''
    INSERT INTO pdf(date_creation,author,creator,producer,subject,title,modification_date,number_of_page,content)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def insert_row(keywords=None, author=None, creator=None, title=None, creationDate=None, producer=None, moddate=None, value=None, nb_page=None):
    """Insert the rows extract in Database"""
    database = r"development/database/pdf_extraction.db"
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new pdf
        pdf_info = (creationDate, author, creator, producer, keywords, title, moddate, nb_page, value)
        return create_pdf(conn, pdf_info)


def store_in_database(filename):
    """Insert the elements extract in Database"""
    output_string = StringIO()
    with open(filename, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        dict_metadata = doc.info  # The "Info" metadata
        dict_data = dict_metadata[0]
        dict_data['value'] = str(output_string.getvalue())
        dict_data['nb_page'] = resolve1(doc.catalog['Pages'])['Count']
        last_id = insert_row(**dict_data)
    return last_id

