from . import common


def get_all():
    query = """
    SELECT id, title, author
    FROM books
    ORDER BY title;
    """
    return common.select_query(query, 'DictCursor')
