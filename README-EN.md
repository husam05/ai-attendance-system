# QR Code Attendance System - Quick Start Guide
## AI Department, Al-Mustafa University

---

## 🚀 System Overview

A complete QR code-based attendance system with 4 main modules:

1. **Student QR Generator** - Generate unique QR codes for each student
2. **Teacher Scanner** - Scan QR codes to record attendance
3. **Attendance Management** - View and manage all attendance records
4. **Smart Reports** - Generate comprehensive 3-month reports

---

## 📖 Quick Start Steps

### Step 1: Generate Student QR Codes
1. Open `student-qr-generator.html`
2. QR codes are automatically generated for all 18 students
3. Print or save the codes

### Step 2: Record Attendance
1. Open `teacher-qr-scanner.html`
2. Select subject, lecture type, date, and time
3. Click "Start Scan" and allow camera access
4. Scan each student's QR code
5. System records attendance with timestamp

### Step 3: View Records
1. Open `attendance-management.html`
2. View all records with filters
3. Export data to CSV or JSON
4. View statistics and charts

### Step 4: Generate Reports
1. Open `attendance-report.html`
2. Choose report type (all students, individual, by subject)
3. Select date range (default: 3 months)
4. Generate and print reports

---

## 📁 File Structure

```
index.html                    # Main dashboard
student-qr-generator.html     # QR code generator
teacher-qr-scanner.html       # Attendance scanner
attendance-management.html    # Record management
attendance-report.html        # Smart reports
students-Ai-dep.txt          # Student list
README.md                    # Documentation (Arabic)
README-EN.md                 # This file
```

---

## 🎯 Key Features

- ⚡ Fast scanning and recording
- 🔒 Secure local storage
- 📱 Mobile-friendly
- 📊 Detailed analytics
- 💾 Export to CSV/JSON/PDF
- 🎨 Modern UI with Arabic RTL support
- ☁️ Works offline after first load

---

## 💾 Data Management

**Storage:** Browser localStorage (local device)
**Backup:** Export JSON or CSV files
**Restore:** Import JSON files
**Security:** Data never leaves your device

---

## 🔧 Technical Details

**Technologies:**
- HTML5, CSS3, JavaScript
- QRCode.js (generation)
- Html5-QRCode (scanning)
- Chart.js (analytics)

**Supported Browsers:**
- Chrome (recommended)
- Firefox
- Edge
- Safari

**Devices:**
- Desktop computers
- Smartphones
- Tablets

---

## 📊 Students List

| # | Student Name | ID |
|:-:|:------------|:---|
| 1-18 | [See Arabic README] | 2025-AI-001 to 018 |

Total: **18 students** in AI Department

---

## ⚙️ Configuration

### Adding New Subjects:
Edit `teacher-qr-scanner.html` line 228 (subject dropdown)

### Adding New Students:
1. Update `students-Ai-dep.txt`
2. Update student arrays in all HTML files

### Changing Report Period:
Default is 3 months, adjustable in reports page

---

## 🆘 Troubleshooting

**Camera not working?**
- Allow camera permissions in browser
- Check camera is not used by another app
- Try different browser

**Data not saving?**
- Check localStorage is enabled
- Export data regularly as backup

**QR code not scanning?**
- Ensure good lighting
- Hold code steady
- Clean camera lens

---

## 📞 Support

**Department:** AI Sciences
**University:** Al-Mustafa University
**Contact:** [To be added]

---

## 📄 License

Developed for AI Department, Al-Mustafa University
© 2025 All Rights Reserved

---

**Happy Teaching! 🎓✨**
