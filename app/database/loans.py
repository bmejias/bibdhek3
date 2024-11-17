from . import common


def get_all():
    query = "SELECT * FROM loans;"
    return common.select_query(query, 'DictCursor')


def get_open_loans():
    query = """
    SELECT
          l.id
        , l.user_id
        , u.first_name
        , u.last_name
        , g.name as class
        , l.date_return
        , b.title
        , b.author
    FROM users u
        JOIN loans l ON u.id = l.user_id
        JOIN copies c ON l.copy_id = c.id
        JOIN books b ON c.book_id = b.id
        JOIN group_users gu ON u.id = gu.user_id
        JOIN groups g ON gu.group_id = g.id
    WHERE l.status='lent'
    ORDER BY b.title;
    """
    return common.select_query(query, 'DictCursor')
