# Firebase Setup Instructions for AI Attendance System

## Important: You Need to Create Your Own Firebase Project

The Firebase configuration in the code uses **placeholder values**. You must replace them with your actual Firebase project credentials.

## Step-by-Step Setup:

### 1. Create Firebase Project
1. Go to https://console.firebase.google.com/
2. Click "Add project" (أضف مشروع)
3. Name it: `ai-attendance-husam` or any name you prefer
4. Continue through the setup wizard

### 2. Enable Realtime Database
1. In your Firebase project, go to **Realtime Database** from the left menu
2. Click "Create Database"
3. Choose your location (preferably closest to Iraq)
4. Start in **Test Mode** for now (we'll add security rules later)
5. Click "Enable"

### 2.5 Enable Anonymous Authentication (CRITICAL)
1. In the left menu, go to **Authentication**
2. Click the **Sign-in method** tab
3. Click **Add new provider**
4. Select **Anonymous** (مجهول)
5. Toggle the switch to **Enable** and click **Save**
*Without this step, the scanner will show "Authentication Error" (خطأ في المصادقة).*

### 3. Get Your Firebase Configuration
1. In Firebase Console, click the ⚙️ (Settings) icon
2. Go to "Project settings"
3. Scroll down to "Your apps" section
4. Click the **</> Web** icon to add a web app
5. Register your app (name it anything)
6. Copy the `firebaseConfig` object shown

### 4. Update the Code
Open each of these files and replace the Firebase config:
- `teacher-qr-scanner.html`
- `attendance-management.html`
- `attendance-report.html`
- `temp-scanner.html`

Find this section:
```javascript
const firebaseConfig = {
    apiKey: "AIzaSyDqC9X6K8yZ5nF0mR3tL7wH4pJ2vB8uE9g",
    authDomain: "ai-attendance-husam.firebaseapp.com",
    databaseURL: "https://ai-attendance-husam-default-rtdb.firebaseio.com",
    projectId: "ai-attendance-husam",
    storageBucket: "ai-attendance-husam.appspot.com",
    messagingSenderId: "123456789012",
    appId: "1:123456789012:web:abc123def456ghi789"
};
```

Replace it with YOUR actual config from Firebase.

### 5. Set Database Rules (Important for Security)
1. In Firebase Console, go to **Realtime Database**
2. Click on the "Rules" tab
3. Replace the rules with:

```json
{
  "rules": {
    "attendanceRecords": {
      ".read": true,
      ".write": true,
      "$recordId": {
        ".validate": "newData.hasChildren(['studentId', 'studentName', 'subject', 'date', 'time', 'timestamp'])"
      }
    }
  }
}
```

4. Click "Publish"

**Note:** These rules allow anyone to read/write. For production, add authentication.

### 6. Test the System
1. Open `teacher-qr-scanner.html`
2. Scan a student QR code
3. Go to Firebase Console → Realtime Database
4. You should see the data appearing in real-time!

### 7. Deploy to GitHub Pages
After updating the Firebase config:
```bash
cd /home/jet/Desktop/Ai-Dept
git add .
git commit -m "Add Firebase integration with real config"
git push origin main
```

## Features Added:

✅ **Online Data Storage**: All attendance records saved to Firebase Realtime Database
✅ **Real-time Sync**: Data syncs across all devices automatically
✅ **Backup**: localStorage still used as fallback
✅ **Fixed Subject Reports**: Subjects now always show in dropdown (predefined list)

## How It Works:

1. **Teacher scans QR** → Data saved to Firebase + localStorage
2. **Attendance Management** → Reads from Firebase (with localStorage fallback)
3. **Reports** → Loads from Firebase, subjects always available (6 subjects predefined)

## Troubleshooting:

**Problem**: Data not syncing
- **Solution**: Check Firebase config is correct
- Verify database URL matches your Firebase project
- Check browser console for errors

**Problem**: "Permission denied" error
- **Solution**: Update database rules (step 5)
- Make sure rules allow read/write

**Problem**: "Authentication Error" (خطأ في المصادقة)
- **Solution**: Go to Firebase Console → Authentication → Sign-in method and **Enable Anonymous provider**.
- Check if your API Key is correct in the config.

**Problem**: Old data still showing from localStorage
- **Solution**: Clear browser cache and localStorage
- Open DevTools (F12) → Application → Local Storage → Delete all

## Need Help?

Contact me or check:
- Firebase Documentation: https://firebase.google.com/docs/database
- Firebase Console: https://console.firebase.google.com/
