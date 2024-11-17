import psycopg2
import psycopg2.extras
import os


def get_db_connection(cursor_type='default'):
    conn = psycopg2.connect(host="localhost",
                            port="5417",
                            database="bibdhek",
                            user=os.getenv('BIBDHEK_DBUSER'),
                            password=os.getenv('BIBDHEK_DBPASS'),
                            options="-c search_path=bibdhek")
    if cursor_type == 'default':
        cursor = conn.cursor()
    elif cursor_type == 'DictCursor':
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    else:
        raise Exception("ERROR: Invalid cursor type", cursor_type)
    return cursor, conn


def select_query(query, cursor_type='default'):
    cursor, conn = get_db_connection(cursor_type)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
