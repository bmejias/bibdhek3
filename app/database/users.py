from . import common


def get_all():
    query = """
    SELECT u.*, g.name as class
    FROM users u
        JOIN group_users gu on u.id = gu.user_id
        JOIN groups g ON gu.group_id = g.id
    ORDER BY u.first_name, u.last_name;
    """
    return common.select_query(query)
