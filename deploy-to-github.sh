#!/bin/bash

# Quick GitHub Pages Deployment Script
# For AI Department Attendance System

echo "🚀 GitHub Pages Deployment Setup"
echo "================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y git
fi

# Navigate to project directory
cd /home/jet/Desktop/Ai-Dept

# Initialize git repository
echo "📦 Initializing Git repository..."
git init

# Configure git (update these with your info)
echo ""
echo "⚙️  Please enter your GitHub username:"
read github_username

echo "⚙️  Please enter your GitHub email:"
read github_email

git config user.name "$github_username"
git config user.email "$github_email"

# Create .gitignore
echo "📝 Creating .gitignore..."
cat > .gitignore << EOL
# OS files
.DS_Store
Thumbs.db

# Backup files
*.bak
*~

# Log files
*.log

# Temporary files
*.tmp
EOL

# Add all files
echo "➕ Adding files to git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: AI Department Attendance System with QR Code"

echo ""
echo "✅ Git repository initialized successfully!"
echo ""
echo "📋 Next Steps:"
echo "=============="
echo ""
echo "1. Go to GitHub.com and create a new repository named: ai-attendance-system"
echo "   - Make it PUBLIC"
echo "   - Don't add README, .gitignore, or license"
echo ""
echo "2. After creating the repository, run these commands:"
echo ""
echo "   git branch -M main"
echo "   git remote add origin https://github.com/$github_username/ai-attendance-system.git"
echo "   git push -u origin main"
echo ""
echo "3. Enable GitHub Pages:"
echo "   - Go to repository Settings > Pages"
echo "   - Source: Deploy from branch 'main'"
echo "   - Click Save"
echo ""
echo "4. Your site will be live at:"
echo "   https://$github_username.github.io/ai-attendance-system"
echo ""
echo "📌 Commands are also saved in: github-commands.txt"

# Save commands to file
cat > github-commands.txt << EOL
GitHub Deployment Commands
==========================

After creating repository on GitHub, run:

git branch -M main
git remote add origin https://github.com/$github_username/ai-attendance-system.git
git push -u origin main

Your site URL will be:
https://$github_username.github.io/ai-attendance-system

To update the site in future:
git add .
git commit -m "Update files"
git push
EOL

echo ""
echo "🎉 Setup complete! Follow the steps above to deploy."
