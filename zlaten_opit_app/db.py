import mysql.connector
import config

db_instance = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

query = db_instance.cursor()

def db_query(query_str, params=None):
    query.execute(query_str, params or ())
    return query.fetchall()

def db_insert(query_str, params=None):
    query.execute(query_str, params or ())
    db_instance.commit()
