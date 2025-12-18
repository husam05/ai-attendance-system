# 🚀 Quick GitHub Deployment Guide

## Step 1: Prepare Your Repository

### On GitHub.com:
1. Go to https://github.com
2. Click the **"+"** button (top right)
3. Select **"New repository"**
4. Repository name: `ai-attendance-system`
5. Make it **Public**
6. ❌ DON'T check "Add README" or any other options
7. Click **"Create repository"**

## Step 2: Deploy Using Terminal

Open terminal and run these commands:

```bash
# Navigate to project folder
cd /home/jet/Desktop/Ai-Dept

# Run the deployment script
chmod +x deploy-to-github.sh
./deploy-to-github.sh
```

The script will ask for:
- Your GitHub username
- Your GitHub email

Then follow the on-screen instructions!

## Step 3: Push to GitHub

After the script finishes, run these commands (replace USERNAME with yours):

```bash
git branch -M main
git remote add origin https://github.com/USERNAME/ai-attendance-system.git
git push -u origin main
```

You'll be asked for:
- Username: your GitHub username
- Password: your GitHub **Personal Access Token** (not your password)

### Getting Personal Access Token:
1. Go to GitHub.com > Settings > Developer settings
2. Personal access tokens > Tokens (classic)
3. Generate new token (classic)
4. Select: `repo` scope
5. Generate token and copy it
6. Use this token as password when pushing

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** tab
3. Click **"Pages"** in the left sidebar
4. Under "Source", select **"Deploy from a branch"**
5. Branch: **main**, Folder: **/ (root)**
6. Click **"Save"**
7. Wait 1-2 minutes

## Step 5: Access Your Site! 🎉

Your attendance system will be live at:
```
https://YOUR-USERNAME.github.io/ai-attendance-system
```

Direct links:
- Main page: `https://YOUR-USERNAME.github.io/ai-attendance-system/`
- Student QR: `https://YOUR-USERNAME.github.io/ai-attendance-system/student-qr-generator.html`
- Teacher Scanner: `https://YOUR-USERNAME.github.io/ai-attendance-system/teacher-qr-scanner.html`
- Reports: `https://YOUR-USERNAME.github.io/ai-attendance-system/attendance-report.html`

## Updating Your Site Later

Whenever you make changes:

```bash
cd /home/jet/Desktop/Ai-Dept
git add .
git commit -m "Update attendance system"
git push
```

Changes will appear on your site in 1-2 minutes.

## Troubleshooting

**Problem: Git asks for password**
Solution: Use Personal Access Token, not your GitHub password

**Problem: Permission denied**
Solution: Check your token has `repo` permissions

**Problem: Site not showing**
Solution: Wait 2-3 minutes, GitHub Pages takes time to deploy

**Problem: Camera not working**
Solution: GitHub Pages uses HTTPS, so camera should work. Check browser permissions.

---

**Ready to deploy? Run the script now!** 🚀
