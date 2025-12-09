from api_request import mock_fetch_data

def connect_to_db():
    print('Connectiong to the PostgreSQL DB...')
    try:
        psycopg2