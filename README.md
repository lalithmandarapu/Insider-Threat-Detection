#  Insider Threat Detection System

##  Overview
The **Insider Threat Detection System** is a cybersecurity project that leverages **Machine Learning (ML) & FastAPI** to identify suspicious user behavior within an organization. It monitors login activity, file access patterns, privilege escalation attempts, and network traffic anomalies to detect potential insider threats in real-time.

##  Features
 **ML-based Threat Detection** – Identifies insider threats using a trained RandomForest model.  
 **FastAPI Backend** – Provides RESTful API endpoints for data processing and threat detection.  
 **PostgreSQL Database** – Stores user behavior logs for monitoring and auditing.  
 **React.js Dashboard** – Real-time visualization of security threats.  
 **Docker Support** – Easy deployment using Docker.  
 **Scalable & Secure** – Designed for corporate, government, and institutional use cases.  

---

##  Project Structure
```plaintext
 insider-threat-detection  
 ├──  backend                 # FastAPI Backend  
 │   ├── main.py               # API Endpoints  
 │   ├── model_training.py      # ML Model Training  
 │   ├── database.py            # Database Connection  
 │   ├── requirements.txt       # Dependencies  
 │   ├── insider_threat_model.pkl # Trained ML Model  
 │   ├── .env                   # Environment Variables  
 ├──  frontend                # React.js Dashboard  
 │   ├── src/  
 │   │   ├── components/  
 │   │   ├── pages/  
 │   │   ├── App.js  
 │   │   ├── index.js  
 │   ├── package.json           # React Dependencies  
 ├── docker-compose.yml         # Docker Setup (Optional)  
 ├── README.md                  # Documentation  
```

---

##  Installation & Setup

### **1️ Backend (FastAPI + ML Model)**
```sh
# Navigate to backend folder
cd backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Train the ML model
python model_training.py

# Run FastAPI server
uvicorn main:app --reload
```
 **API Running at:** `http://127.0.0.1:8000`

### **2️ Frontend (React.js Dashboard)**
```sh
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start React App
npm start
```
 **Dashboard Running at:** `http://localhost:3000`

### **3️ Database (PostgreSQL Setup)**
```sh
# Start PostgreSQL
sudo service postgresql start  # Linux/macOS

# Create Database
psql -U postgres
CREATE DATABASE cybersecurity_db;
\c cybersecurity_db

# Create Table
CREATE TABLE user_activity (
    id SERIAL PRIMARY KEY,
    user_id INT,
    login_time INT,
    file_access_count INT,
    privilege_escalation_attempts INT,
    network_traffic_volume FLOAT,
    threat_status TEXT
);
```

### **4️ Run with Docker (Optional)**
```sh
# Navigate to the project root folder
cd insider-threat-detection

# Build & Start Containers
docker-compose up --build
```

---


---

##  Technologies Used
- **Backend:** FastAPI, Python, Scikit-learn, Joblib
- **Frontend:** React.js, Tailwind CSS
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker-Compose

---


