import sqlite3

def create_database():
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            timestamp TEXT,
            application TEXT,
            category TEXT,
            cpu REAL,
            memory REAL
        )
    """)
    conn.commit()
    conn.close()

def log_activity(timestamp, application, category, cpu, memory):
    conn = sqlite3.connect('activity_logs.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (timestamp, application, category, cpu, memory) VALUES (?, ?, ?, ?, ?)",
                   (timestamp, application, category, cpu, memory))
    conn.commit()
    conn.close()
