from . import common


def get_all():
    query = """
    SELECT u.*, g.name as class
    FROM users u
        JOIN group_users gu on u.id = gu.user_id
        JOIN groups g ON gu.group_id = g.id
    ORDER BY u.first_name, u.last_name;
    """
    cursor, conn = common.get_db_connection('DictCursor')
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    return users
