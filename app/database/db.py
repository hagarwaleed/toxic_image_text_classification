import sqlite3
from datetime import datetime

DB_NAME = "predictions.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_type TEXT,
        content TEXT,
        predicted_label TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_prediction(input_type, content, predicted_label):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO predictions (input_type, content, predicted_label, timestamp)
    VALUES (?, ?, ?, ?)
    """, (input_type, content, predicted_label, timestamp))

    conn.commit()
    conn.close()