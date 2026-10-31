from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {"message": "Banking Application is running"}


import sqlite3

def get_db_connection():
    conn = sqlite3.connect("banking.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


create_tables()