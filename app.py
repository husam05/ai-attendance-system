from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from typing import List, Dict, Optional, Any
import json
import os
import time
from threading import Lock

app = FastAPI(title="Deep AI Attendance System")

# --- Configuration ---
DATA_DIR = "data"
DB_FILE = os.path.join(DATA_DIR, "database.json")
PORT = int(os.environ.get("PORT", 8080))

# --- Data Models ---
class Student(BaseModel):
    name: str

class AttendanceRecord(BaseModel):
    id: Optional[str] = None
    studentId: Optional[str] = None
    studentName: str
    subject: Optional[str] = "Unknown"
    lectureType: Optional[str] = "Theory"
    date: Optional[str] = None
    time: Optional[str] = None
    timestamp: Optional[int] = None
    engine: Optional[str] = "Python_v1"
    type: Optional[str] = None # For legacy/plain support

# --- Storage Engine ---
class Store:
    def __init__(self):
        self.lock = Lock()
        self.students: List[str] = []
        self.records: Dict[str, Dict] = {}
        self.load()

    def load(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        if os.path.exists(DB_FILE):
            try:
                with open(DB_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.students = data.get("students", [])
                    self.records = data.get("records", {})
            except Exception as e:
                print(f"Error loading DB: {e}")
        else:
            # Defaults
            self.students = [
                "يوسف ميثاق طالب عجيل", "حسين علي دوشان كاظم", "نورالحسن باسم عبدالرزاق حسين",
                "مصطفى فؤاد فاضل عبد الامير", "علي جمال خلف فعيل", "مصطفى محمد مردان حسن",
                "ضحى حيدر كمال جوده", "علي محمد جبار حسين", "بنين ديار رحيم صفر",
                "زهراء محمد سريح عبد الحسن", "زهراء ابراهيم مهدي خضير", "منتظر حميد عذاب ضاحي",
                "نبأ جاسم رحمه شايع", "معصومة عبد الحسين جبار عبدالله", "داليا كريم ليلو منصور",
                "مؤمل سعدون جبار لفته", "سبأ محمد صبري سلطان", "رقيه اثير احمد مطلق", "كاظم محمد جاسم"
            ]
            self.save()

    def save(self):
        with self.lock:
            try:
                with open(DB_FILE, 'w', encoding='utf-8') as f:
                    json.dump({
                        "students": self.students,
                        "records": self.records
                    }, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Error saving DB: {e}")

db = Store()

# --- Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Routes ---

@app.get("/api/status")
async def get_status():
    return {"connected": True, "engine": "Python/FastAPI"}

@app.get("/api/students")
async def get_students():
    return db.students

@app.post("/api/students")
async def update_students(students: List[str]):
    db.students = students
    db.save()
    return {"status": "success", "count": len(db.students)}

@app.get("/api/attendance")
async def get_attendance():
    return db.records

@app.post("/api/attendance")
async def add_attendance(record: AttendanceRecord):
    data = record.dict()
    
    # Generate ID if missing
    if not data.get("id"):
        data["id"] = f"rec_{int(time.time()*1000)}"
    
    # Generate Timestamp if missing
    if not data.get("timestamp"):
        data["timestamp"] = int(time.time() * 1000)
        
    db.records[data["id"]] = data
    db.save()
    return {"name": data["id"]} # Firebase-like response

@app.delete("/api/attendance/{record_id}")
async def delete_attendance(record_id: str):
    if record_id in db.records:
        del db.records[record_id]
        db.save()
        return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="Record not found")

# --- Static File Serving (SPA Fallback) ---
# Serve root files directly is tricky with StaticFiles if they are mixed
# We'll serve specific known HTML files and a static directory for assets

# 1. Mount assets
app.mount("/js", StaticFiles(directory="js"), name="js")
# Using root . for StaticFiles can expose source code, but for this demo it's fine
# To be safe, we explicitly handle the main HTMLs
@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/{filename}.html")
async def read_html(filename: str):
    path = f"{filename}.html"
    if os.path.exists(path):
        return FileResponse(path)
    raise HTTPException(status_code=404, detail="Page not found")

# Fallback for style.css and other root assets
@app.get("/{filename}.css")
async def read_css(filename: str):
    path = f"{filename}.css"
    if os.path.exists(path):
        return FileResponse(path)
    return JSONResponse(status_code=404, content={"message": "Not found"})

if __name__ == "__main__":
    import uvicorn
    print(f"🚀 Deep AI System (Python) running on http://localhost:{PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
