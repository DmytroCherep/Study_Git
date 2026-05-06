import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="postgres",
        host="postgres_db",
        port="5432"
    )


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT,
                    age INT
                );
            """)


def insert_user(name, age):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name, age) VALUES (%s, %s)",
                (name, age)
            )


def get_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            return cur.fetchall()


def update_user(user_id, new_name):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE users SET name=%s WHERE id=%s",
                (new_name, user_id)
            )


def delete_user(user_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id=%s", (user_id,))


# --- DEMO ---
if __name__ == "__main__":
    create_table()

    insert_user("Dmytro", 25)

    users = get_users()
    print("USERS:", users)

    if users:
        user_id = users[0][0]

        update_user(user_id, "Updated")
        print("AFTER UPDATE:", get_users())

        delete_user(user_id)
        print("AFTER DELETE:", get_users())