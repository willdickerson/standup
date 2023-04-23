import os
import psycopg2

def get_database_connection():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))

def create_table():
    with get_database_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS team_members
                           (id SERIAL PRIMARY KEY, name TEXT UNIQUE)''')
            conn.commit()

def get_team_members():
    with get_database_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT name FROM team_members')
            team_members = [row[0] for row in cur.fetchall()]
    return team_members

def delete_member(request):
    member_to_delete = request.form['member_to_delete']
    with get_database_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM team_members WHERE name = %s', (member_to_delete,))
            conn.commit()

def add_member(request):
    new_member = request.form['new_member']
    with get_database_connection() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO team_members (name) VALUES (%s)', (new_member,))
            conn.commit()