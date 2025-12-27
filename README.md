# 🚀 AI Attendance System

**Modern attendance tracking system with QR code scanning, built with Python/FastAPI backend.**

## ✨ Features

- 📱 **QR Code Scanner** - Ultra-fast scanning with duplicate prevention
- 🎫 **ID Card Generator** - Professional student cards with QR codes
- 📊 **Analytics Dashboard** - Real-time attendance reports and charts
- 💾 **Local Storage** - JSON-based persistence, no cloud dependencies
- 🎨 **Deep AI Theme** - Modern, premium dark UI design
- 📴 **Offline Ready** - All libraries local, works without internet

## 🚀 Quick Start

### Run Locally
```bash
# Install dependencies
pip install fastapi uvicorn

# Start server
python app.py
```

Visit: **http://localhost:8080**

### Docker
```bash
docker build -t ai-attendance .
docker run -p 8080:8080 -v $(pwd)/data:/app/data ai-attendance
```

## 📁 Project Structure

```
Ai-Dept/
├── app.py                      # FastAPI backend
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container config
├── data/
│   └── database.json          # Data storage
├── js/
│   ├── api.js                 # Backend adapter
│   ├── qr-scanner.umd.min.js  # Scanner library
│   ├── qrious.min.js          # QR generator
│   └── html-to-image.min.js   # Card export
├── index.html                  # Dashboard
├── teacher-qr-scanner.html     # Scanner page
├── student-qr-generator.html   # ID generator
├── attendance-management.html  # Records manager
├── attendance-report.html      # Analytics
└── style.css                   # Deep AI theme
```

## 🔌 API Endpoints

- `GET /api/status` - System health check
- `GET /api/students` - List all students
- `POST /api/students` - Update student list
- `GET /api/attendance` - Get attendance records
- `POST /api/attendance` - Add attendance record
- `DELETE /api/attendance/{id}` - Delete record

## 🌐 Deploy

### Railway
```bash
# Connect repo and deploy automatically
# Set PORT=8080 in environment variables
```

### Render
```bash
# Build: pip install -r requirements.txt
# Start: python app.py
```

### Heroku
```bash
git push heroku main
```

## 📊 Data Format

### Student List
```json
["Student Name 1", "Student Name 2", ...]
```

### Attendance Record
```json
{
  "id": "rec_1735358400000",
  "studentId": "2025-AI-001",
  "studentName": "يوسف ميثاق طالب عجيل",
  "subject": "Data Structures",
  "lectureType": "Theory",
  "date": "2025-12-28",
  "time": "10:30",
  "timestamp": 1735358400000,
  "engine": "Python_v1"
}
```

## 🔧 Configuration

Change port in `app.py`:
```python
PORT = int(os.environ.get("PORT", 8080))
```

## 🐛 Troubleshooting

**Scanner not working?**
- Check camera permissions
- Ensure `js/qr-scanner-worker.min.js` exists
- Hard refresh (Ctrl+Shift+R)

**Server won't start?**
- Check Python version: `python --version` (need 3.9+)
- Reinstall: `pip install fastapi uvicorn --force-reinstall`

## 📝 License

Built for **Almustafa University - AI Department**

---

**Made with ❤️ by Dr. Husam Salah Mahdi's Team**
