import psycopg2
import psycopg2.extras
import os

from . import books


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
        cursor = conn.cursor(cursor_type=psycopg2.extras.DictCursor)
    else:
        raise Exception("ERROR: Invalid cursor type", cursor_type)
    return cursor, conn


__all__ = [get_db_connection, "books"]