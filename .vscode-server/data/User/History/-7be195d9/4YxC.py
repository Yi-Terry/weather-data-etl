import psycopg2

def connect_to_db():
    print('Connectiong to the PostgreSQL DB...')
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5000,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        print(conn)
    except psycopg2.Error as e:
        print(F'DB connection failed: {e}') 
        raise 
connect_to_db()