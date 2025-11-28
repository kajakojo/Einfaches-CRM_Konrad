# 🔧 COMPLETE FIX GUIDE - Everything You Need To Do

## THE PROBLEM
Your app/templates/static folders weren't uploaded to PythonAnywhere because you only did `git pull` but the files are in git.

## THE SOLUTION - Follow These Steps EXACTLY

### STEP 1: Run Commands in PythonAnywhere Bash Console

Open PythonAnywhere Bash Console and run these commands **one by one**:

```bash
# Go to project directory
cd /home/kajetankonrad/crmproject

# Pull the latest code (this will get app/, templates/, static/ folders)
git pull origin main

# Verify app folder is there now
ls -la app/
```

**Expected output:** You should see files like `__init__.py`, `models.py`, `routes.py`, `extensions.py`

**If you don't see these files**, the git pull didn't work. Then do:
```bash
# Check git status
git status

# Try pulling again
git fetch origin
git reset --hard origin/main
```

---

### STEP 2: Create Virtual Environment

```bash
# Create virtualenv (if not already created)
mkvirtualenv --python=/usr/bin/python3.10 crm-env

# Activate it
workon crm-env

# Install all requirements
pip install -r requirements.txt

# Verify critical packages are installed
pip list | grep -E "Flask|PyMySQL|SQLAlchemy"
```

**Expected output:** You should see Flask, PyMySQL, and Flask-SQLAlchemy listed

---

### STEP 3: Test If App Can Be Imported

```bash
# Test import (all one line)
python3 -c "import sys; sys.path.insert(0, '/home/kajetankonrad/crmproject'); from app import create_app; print('SUCCESS: App imported correctly')"
```

**Expected output:** `SUCCESS: App imported correctly`

**If you get an error**, copy the full error message and we'll fix it.

---

### STEP 4: Update WSGI Configuration File

1. Go to **PythonAnywhere Web Tab**
2. Click on the link to your WSGI configuration file:
   `/var/www/kajetankonrad_pythonanywhere_com_wsgi.py`
3. **DELETE ALL CONTENT** in that file
4. **COPY AND PASTE** this complete code:

```python
# +++++++++++ FLASK +++++++++++
# WSGI Configuration for PythonAnywhere

import sys
import os

# ===================================================================
# PATH CONFIGURATION
# ===================================================================
project_home = '/home/kajetankonrad/crmproject'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# ===================================================================
# ENVIRONMENT VARIABLES
# ===================================================================

# Flask Secret Key - CHANGE THIS TO A SECURE RANDOM STRING!
os.environ['SECRET_KEY'] = 'CHANGE-THIS-TO-SOMETHING-SECURE-AND-RANDOM-abcdef123456'

# Flask Environment
os.environ['FLASK_ENV'] = 'production'
os.environ['DEBUG'] = 'False'

# MySQL Database Connection
# IMPORTANT: Replace 'YOUR_MYSQL_PASSWORD_HERE' with your actual MySQL password!
os.environ['DATABASE_URL'] = 'mysql+pymysql://kajetankonrad:YOUR_MYSQL_PASSWORD_HERE@kajetankonrad.mysql.pythonanywhere-services.com/kajetankonrad$crm'

# ===================================================================
# LOAD FLASK APP
# ===================================================================
from app import create_app

application = create_app()
```

5. **IMPORTANT:** Change these two things in the code above:
   - Line 20: Change `SECRET_KEY` to a random secure string (at least 32 characters)
   - Line 27: Replace `YOUR_MYSQL_PASSWORD_HERE` with your actual MySQL password

6. **Save** the file (Ctrl+S or click Save button)

---

### STEP 5: Configure Virtualenv in Web Tab

1. Still in the **Web Tab**
2. Scroll down to find the **"Virtualenv"** section
3. Enter this path:
   ```
   /home/kajetankonrad/.virtualenvs/crm-env
   ```
4. Click the checkmark/tick to save

---

### STEP 6: Configure Static Files

1. Still in **Web Tab**
2. Scroll down to **"Static files"** section
3. Add a new static file mapping:
   - **URL:** `/static/`
   - **Directory:** `/home/kajetankonrad/crmproject/static`
4. Click the checkmark to save

---

### STEP 7: Reload Your Web App

1. Scroll to the top of the **Web Tab**
2. Click the big green **"Reload kajetankonrad.pythonanywhere.com"** button
3. Wait for it to finish reloading

---

### STEP 8: Test Your Website

1. Open: https://kajetankonrad.pythonanywhere.com
2. You should see your CRM app!

---

## 🚨 IF IT STILL SHOWS "Something went wrong"

Check the error log:

```bash
# In PythonAnywhere Bash Console
tail -n 50 /var/log/kajetankonrad.pythonanywhere.com.error.log
```

**Copy the entire error log output and send it to me**, I'll help you fix it.

---

## ✅ CHECKLIST - Make Sure You Did All Of This:

- [ ] Ran `git pull origin main` in `/home/kajetankonrad/crmproject`
- [ ] Verified `app/` folder exists with `ls -la app/`
- [ ] Created virtualenv `crm-env`
- [ ] Installed requirements with `pip install -r requirements.txt`
- [ ] Updated WSGI file with correct path: `/home/kajetankonrad/crmproject`
- [ ] Changed MySQL password in WSGI file
- [ ] Changed SECRET_KEY in WSGI file
- [ ] Set virtualenv path: `/home/kajetankonrad/.virtualenvs/crm-env`
- [ ] Set static files path: `/home/kajetankonrad/crmproject/static`
- [ ] Clicked "Reload" button
- [ ] Tested the website

---

## 📝 QUICK COMMAND SUMMARY

Copy all these commands and run them in PythonAnywhere Bash:

```bash
cd /home/kajetankonrad/crmproject
git pull origin main
ls -la app/
mkvirtualenv --python=/usr/bin/python3.10 crm-env
workon crm-env
pip install -r requirements.txt
pip list | grep -E "Flask|PyMySQL"
python3 -c "import sys; sys.path.insert(0, '/home/kajetankonrad/crmproject'); from app import create_app; print('✓ SUCCESS')"
```

If all commands succeed without errors, then:
1. Update WSGI file (see STEP 4 above)
2. Set virtualenv path (see STEP 5 above)
3. Set static files (see STEP 6 above)
4. Reload (see STEP 7 above)

---

**That's it! Your CRM should work after following all these steps.** 🎉

If you still have issues, send me the error log output!
