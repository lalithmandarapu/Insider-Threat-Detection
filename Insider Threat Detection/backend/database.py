import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(
    database=os.getenv("DB_NAME"), 
    user=os.getenv("DB_USER"), 
    password=os.getenv("DB_PASS"), 
    host=os.getenv("DB_HOST"), 
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_activity (
        id SERIAL PRIMARY KEY,
        user_id INT,
        login_time INT,
        file_access_count INT,
        privilege_escalation_attempts INT,
        network_traffic_volume FLOAT,
        threat_status TEXT
    )
""")
conn.commit()