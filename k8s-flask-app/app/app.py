# app.py
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("flaskdb"),
        user=os.getenv("flaskuser"),
        password=os.getenv("flaskpassword"),
        host=os.getenv("postgres-service"),
        port=os.getenv("5432")
    )
    return conn

@app.route('/')
def home():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"Connected to PostgreSQL: {db_version}"
    except Exception as e:
        return f"Error connecting to database: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)