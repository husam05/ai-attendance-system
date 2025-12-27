# 🚀 Deployment Guide - AI Attendance System

## 📦 Option 1: GitHub + Railway (Recommended)

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "AI Attendance System - Python Backend"

# Create repository on GitHub (https://github.com/new)
# Then connect and push:
git remote add origin https://github.com/YOUR_USERNAME/ai-attendance-system.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Railway

1. **Go to Railway**: https://railway.app
2. **Sign in with GitHub**
3. **New Project** → **Deploy from GitHub repo**
4. **Select your repository**: `ai-attendance-system`
5. **Configure**:
   - Railway auto-detects Python
   - No environment variables needed
6. **Deploy** - Railway will:
   - Install dependencies from `requirements.txt`
   - Run `python app.py`
   - Assign a public URL

**Your app will be live at**: `https://your-app.railway.app`

---

## 📦 Option 2: GitHub + Render

### Step 1: Push to GitHub (same as above)

### Step 2: Deploy on Render

1. **Go to Render**: https://render.com
2. **New** → **Web Service**
3. **Connect GitHub repository**
4. **Configure**:
   - **Name**: ai-attendance-system
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. **Create Web Service**

**Your app will be live at**: `https://ai-attendance-system.onrender.com`

---

## 📦 Option 3: GitHub + Heroku

### Step 1: Push to GitHub (same as above)

### Step 2: Deploy on Heroku

```bash
# Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create ai-attendance-system

# Deploy
git push heroku main

# Open app
heroku open
```

**Your app will be live at**: `https://ai-attendance-system.herokuapp.com`

---

## 📦 Option 4: Firebase Hosting + Cloud Run (Advanced)

Firebase Hosting can serve your frontend, while Cloud Run hosts the Python backend.

### Step 1: Install Firebase CLI

```bash
npm install -g firebase-tools
firebase login
```

### Step 2: Initialize Firebase

```bash
firebase init hosting

# Select:
# - Use existing project or create new
# - Public directory: . (current directory)
# - Single-page app: No
# - GitHub integration: Yes (optional)
```

### Step 3: Deploy Frontend to Firebase Hosting

```bash
# Deploy static files (HTML, CSS, JS)
firebase deploy --only hosting
```

**Frontend will be at**: `https://your-project.web.app`

### Step 4: Deploy Backend to Cloud Run

```bash
# Build and deploy
gcloud run deploy ai-attendance-api \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### Step 5: Update Frontend API URL

In `js/api.js`, change the API base URL:
```javascript
const API_BASE = 'https://ai-attendance-api-xxx.run.app';
```

---

## 📦 Option 5: Docker Deployment (Any Platform)

### Build Docker Image

```bash
docker build -t ai-attendance .
```

### Run Locally

```bash
docker run -p 8080:8080 -v $(pwd)/data:/app/data ai-attendance
```

### Deploy to Cloud

**Google Cloud Run**:
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/ai-attendance
gcloud run deploy --image gcr.io/PROJECT_ID/ai-attendance --platform managed
```

**AWS ECS/Fargate**:
```bash
# Push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ECR_URL
docker tag ai-attendance:latest YOUR_ECR_URL/ai-attendance:latest
docker push YOUR_ECR_URL/ai-attendance:latest
```

---

## 🔧 Environment Variables (if needed)

For production, you might want to set:

```bash
# Port (Railway/Render auto-set this)
PORT=8080

# CORS origins (restrict in production)
CORS_ORIGINS=https://your-domain.com
```

---

## ✅ Post-Deployment Checklist

After deploying, verify:

1. ✅ **Homepage loads**: Visit your deployment URL
2. ✅ **API works**: Check `/api/status`
3. ✅ **Scanner works**: Test camera access (HTTPS required!)
4. ✅ **Data persists**: Scan a code, refresh, check if record exists
5. ✅ **HTTPS enabled**: Required for camera access

---

## 🔒 Important Notes

### Camera Access Requires HTTPS
- ✅ Railway, Render, Heroku provide HTTPS automatically
- ✅ Firebase Hosting provides HTTPS
- ❌ HTTP-only deployments won't allow camera access

### Data Persistence
- Railway/Render: Use volumes or external database
- Heroku: Use Heroku Postgres or external storage
- Cloud Run: Use Cloud Storage or Firestore

### Free Tier Limits
- **Railway**: 500 hours/month free
- **Render**: 750 hours/month free
- **Heroku**: 550 hours/month free (with credit card)
- **Firebase Hosting**: 10GB storage, 360MB/day transfer

---

## 🎯 Recommended: Railway

**Why Railway?**
- ✅ Easiest setup (1-click deploy)
- ✅ Auto HTTPS
- ✅ Free tier generous
- ✅ Automatic deployments from GitHub
- ✅ Built-in monitoring

**Quick Deploy**:
1. Push to GitHub
2. Import to Railway
3. Done! 🚀

---

## 📞 Need Help?

If deployment fails:
1. Check logs in your platform dashboard
2. Verify `requirements.txt` is correct
3. Ensure `app.py` uses `PORT` environment variable
4. Check CORS settings for your domain

---

**Your AI Attendance System is ready for the world!** 🌍
