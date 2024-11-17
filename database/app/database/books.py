from . import database as db

def get_all():
    cursor, conn = db.get_db_connection()
    query = "SELECT * FROM books;"
    cursor.execute(query)
    books = cursor.fetchall()
    cursor.close()
    return books
