from fastapi import FastAPI, Depends
from pydantic import BaseModel
import joblib
import psycopg2
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

# Load ML Model
MODEL_PATH = "insider_threat_model.pkl"
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

# Database Connection
conn = psycopg2.connect(
    database=os.getenv("DB_NAME"), 
    user=os.getenv("DB_USER"), 
    password=os.getenv("DB_PASS"), 
    host=os.getenv("DB_HOST"), 
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

class UserActivity(BaseModel):
    user_id: int
    login_time: int
    file_access_count: int
    privilege_escalation_attempts: int
    network_traffic_volume: float

@app.post("/detect")
def detect_threat(activity: UserActivity):
    data = [[activity.login_time, activity.file_access_count, activity.privilege_escalation_attempts, activity.network_traffic_volume]]
    prediction = model.predict(data)
    threat_status = "Suspicious" if prediction[0] == 1 else "Normal"
    
    cursor.execute("""
        INSERT INTO user_activity (user_id, login_time, file_access_count, privilege_escalation_attempts, network_traffic_volume, threat_status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (activity.user_id, activity.login_time, activity.file_access_count, activity.privilege_escalation_attempts, activity.network_traffic_volume, threat_status))
    conn.commit()
    return {"user_id": activity.user_id, "threat_status": threat_status}

@app.get("/logs")
def get_logs():
    cursor.execute("SELECT * FROM user_activity")
    logs = cursor.fetchall()
    return {"logs": logs}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)