import os
import psycopg2

def get_database_connection():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

def create_table():
    conn = get_database_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS team_members
                   (id SERIAL PRIMARY KEY, name TEXT UNIQUE)''')
    conn.commit()
    cur.close()
    conn.close()
