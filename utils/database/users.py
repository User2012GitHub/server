import psycopg2

def connect_db():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='group3',
        user='postgres',
        password='2012'
    )
    conn.autocommit = True
    return conn

def close_db(conn):
    if conn:
        conn.close()


def create_user(fio, chat_id, username):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"INSERT INTO users (chat_id, username) VALUES ({chat_id}, '{username}')",
        )

def update_user(fio, username, chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE INTO users (fio, chat_id, username) VALUES ('{fio}', {chat_id}, '{username}')",
        )

def update_fio(fio, username, chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE INTO users (fio, chat_id, username) VALUES ('{fio}', {chat_id}, '{username}')",
        )


def delete_user(chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"DELETE FROM users where chat_id='{chat_id}';",
        )

def get_users(chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM users where chat_id='{chat_id}';",
        )
        result = cursor.fetchone()
    close_db(conn)

    return result

def get_users_all():
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM users;",
        )
        result = cursor.fetchall()
    close_db(conn)
    return result

def about_me(chat_id):
    conn = connect_db()
    with conn.cursor() as cursor:
        cursor.execute(f"select * from users where chat_id='{chat_id}';")
        result = cursor.fetchall()

    def about_me(chat_id):
        conn = connect_db()
        with conn.cursor() as cursor:
            cursor.execute(f"select * from users where chat_id='{chat_id}';")
            result = cursor.fetchall()

        close_db(conn)
        return result