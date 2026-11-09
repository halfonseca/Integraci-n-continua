import os

import psycopg2
from flask import Flask

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )


@app.route("/")
def index():
    connection = get_connection()
    try:
        with connection, connection.cursor() as cursor:
            cursor.execute("INSERT INTO visitas DEFAULT VALUES;")
            cursor.execute("SELECT COUNT(*) FROM visitas;")
            total = cursor.fetchone()[0]
    finally:
        connection.close()
    return f"Visitas registradas: {total}\n"
