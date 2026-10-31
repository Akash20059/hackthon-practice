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