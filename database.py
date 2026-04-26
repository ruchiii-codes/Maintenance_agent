import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_path="maintenance.db"):
        self.db_path = db_path
        self.create_table()
    
    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS complaints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                complaint TEXT NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL,
                confidence REAL,
                timestamp TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    
    def reset(self):
        """Delete all records and reset auto-increment"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("DELETE FROM complaints")
        conn.execute("DELETE FROM sqlite_sequence WHERE name='complaints'")
        conn.commit()
        conn.close()
    
    def save(self, complaint, category, priority, confidence):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.execute(
            """INSERT INTO complaints 
               (complaint, category, priority, confidence, timestamp) 
               VALUES (?, ?, ?, ?, ?)""",
            (complaint, category, priority, confidence, datetime.now().isoformat())
        )
        conn.commit()
        record_id = cursor.lastrowid
        conn.close()
        return record_id
    
    def get_all(self):
        conn = sqlite3.connect(self.db_path)
        complaints = conn.execute(
            "SELECT * FROM complaints ORDER BY timestamp DESC"
        ).fetchall()
        conn.close()
        return complaints
    
    def get_stats(self):
        conn = sqlite3.connect(self.db_path)
        
        categories = dict(conn.execute(
            "SELECT category, COUNT(*) FROM complaints GROUP BY category"
        ).fetchall())
        
        priorities = dict(conn.execute(
            "SELECT priority, COUNT(*) FROM complaints GROUP BY priority"
        ).fetchall())
        
        total = conn.execute("SELECT COUNT(*) FROM complaints").fetchone()[0]
        conn.close()
        
        return {
            "total": total,
            "categories": categories,
            "priorities": priorities
        }