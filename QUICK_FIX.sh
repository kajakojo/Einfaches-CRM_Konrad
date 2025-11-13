#!/bin/bash
# QUICK FIX - Run these commands in PythonAnywhere Bash Console
# Copy and paste these commands one by one

# 1. Navigate to project and pull latest code
cd /home/kajetankonrad/crmproject
git pull origin main

# 2. Verify app folder is now there
ls -la app/

# 3. Create and activate virtual environment
mkvirtualenv --python=/usr/bin/python3.10 crm-env
workon crm-env

# 4. Install requirements
pip install -r requirements.txt

# 5. Verify installations
pip list | grep -E "Flask|PyMySQL|SQLAlchemy"

# 6. Test if app can be imported
python3 -c "import sys; sys.path.insert(0, '/home/kajetankonrad/crmproject'); from app import create_app; app = create_app(); print('✓ App created successfully')"

echo ""
echo "============================================"
echo "If all commands succeeded, do this:"
echo "============================================"
echo "1. Go to PythonAnywhere Web tab"
echo "2. Open WSGI configuration file"
echo "3. Make sure these lines are correct:"
echo "   project_home = '/home/kajetankonrad/crmproject'"
echo "   (Update MySQL password in DATABASE_URL)"
echo ""
echo "4. Set Virtualenv to:"
echo "   /home/kajetankonrad/.virtualenvs/crm-env"
echo ""
echo "5. Click 'Reload' button"
echo "============================================"
