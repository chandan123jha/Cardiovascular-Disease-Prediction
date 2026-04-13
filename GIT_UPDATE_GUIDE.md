# Git Update Guide

This guide shows how to push your changes to the GitHub repository.

## Step 1: Check Current Status

```bash
cd c:\Users\CHANDAN\Downloads\Cardiovascular-Disease-Prediction-main
git status
```

**Expected Output:**
- Modified: `README.md`
- New file: `.gitignore`
- Deleted: Old GUI files (if not already in git history)

---

## Step 2: Stage All Changes

```bash
# Stage everything
git add -A

# Or stage specific files
git add README.md .gitignore
git add app.py templates/ static/
git add "Cardiovascular-Disease Prediction/new.csv"
git add "Cardiovascular-Disease Prediction/HEART_DISEASE_MODEL.joblib"
git add run.ps1 run.bat requirements.txt Procfile
```

---

## Step 3: Check Staged Changes

```bash
git status

# Or see detailed diff
git diff --cached README.md
```

---

## Step 4: Commit Changes

```bash
# Comprehensive commit message
git commit -m "Refactor: Migrate from Tkinter GUI to Flask web app

- Remove legacy Tkinter GUI files (Heart.py, heartGUI_main.py, etc.)
- Remove old pickle model files (clf_DST.pkl, clf_NB.pkl)
- Remove test files (temp_pdf_test.py, Report.txt)
- Clean up .venv-1 and .venv-2 virtual environments
- Update README with comprehensive Flask setup documentation
- Add .gitignore for Python, virtual environments, and project files
- Improve project structure and organization
- Add usage guide and parameter documentation
- Include architecture and database schema details"
```

**Or use a simpler message:**

```bash
git commit -m "Update: Flask web app with improved UI and documentation"
```

---

## Step 5: View Commit History

```bash
# See your commits
git log --oneline -5

# See what changed
git show HEAD
```

---

## Step 6: Push to GitHub

```bash
# If using HTTPS (will prompt for credentials)
git push origin main

# If using SSH (ensure SSH keys are set up)
git push origin main
```

**If you get an error about authentication:**

```bash
# Use Personal Access Token (PAT) instead of password
# GitHub will prompt: use your username and paste the PAT as password
git push origin main
```

---

## Step 7: Verify on GitHub

1. Go to https://github.com/chandan123jha/Cardiovascular-Disease-Prediction
2. Verify your commit appears in commit history
3. Check that files are properly updated
4. Confirm README renders correctly

---

## Common Issues & Solutions

### Issue: "remote: Repository not found"
```bash
# Check repository URL
git remote -v

# Update if wrong
git remote set-url origin https://github.com/chandan123jha/Cardiovascular-Disease-Prediction.git
```

### Issue: "You have divergent branches"
```bash
# Rebase your changes on top of remote
git pull --rebase origin main
git push origin main
```

### Issue: "Permission denied" (SSH)
```bash
# Ensure SSH key is added to ssh-agent
ssh-add ~/.ssh/id_rsa

# Test SSH connection
ssh -T git@github.com
```

### Issue: Large files or LFS needed
```bash
# See file sizes
git ls-files --size

# Remove local cache if needed
git rm --cached -r .
git add .
```

---

## Full Automated Script

Copy and run in PowerShell:

```powershell
# Navigate to repo
cd c:\Users\CHANDAN\Downloads\Cardiovascular-Disease-Prediction-main

# Stage changes
git add -A

# Commit
git commit -m "Update: Flask web app with improved UI and documentation"

# Push
git push origin main

# Verify
git log --oneline -5
```

---

## Verify Changes Locally Before Pushing

```bash
# See what will be committed
git diff --cached

# See status
git status

# See commits that will be pushed
git log --oneline origin/main..HEAD
```

---

## Undo Last Commit (if needed)

```bash
# Undo commit but keep changes staged
git reset --soft HEAD~1

# Undo commit and unstage changes
git reset HEAD~1

# Completely undo last commit and changes
git reset --hard HEAD~1
```

---

## Best Practices

✅ **DO:**
- Write clear, descriptive commit messages
- Test locally before pushing
- Use `git status` frequently
- Push regularly (don't wait for huge commits)
- Pull before pushing (esp. in teams)

❌ **DON'T:**
- `git commit -m "update"` (be specific)
- Force push (`git push -f`) unless necessary
- Commit large binary files
- Commit sensitive data (API keys, passwords)

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `git status` | See what changed |
| `git add -A` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
| `git push origin main` | Push to GitHub |
| `git pull origin main` | Pull latest from GitHub |
| `git log --oneline` | See commit history |
| `git diff` | See file differences |
| `git restore <file>` | Discard changes in file |

---

**Need help?** Check GitHub's official guides: https://docs.github.com/en/get-started
