from . import common


def get_all():
    query = """
    SELECT id, title, author
    FROM books
    ORDER BY title;
    """
    cursor, conn = common.get_db_connection('DictCursor')
    cursor.execute(query)
    books = cursor.fetchall()
    cursor.close()
    return books
