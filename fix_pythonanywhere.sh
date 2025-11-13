#!/bin/bash
# Complete Fix Script for PythonAnywhere Deployment
# Run this in PythonAnywhere Bash Console

echo "============================================================"
echo "PYTHONANYWHERE CRM FIX SCRIPT"
echo "============================================================"
echo ""

# Set variables
PROJECT_DIR="/home/kajetankonrad/crmproject"
VENV_NAME="crm-env"
VENV_PATH="/home/kajetankonrad/.virtualenvs/$VENV_NAME"

# Step 1: Check if project directory exists
echo "Step 1: Checking project directory..."
if [ ! -d "$PROJECT_DIR" ]; then
    echo "ERROR: Project directory not found at $PROJECT_DIR"
    echo "Please create it first or adjust the PROJECT_DIR variable"
    exit 1
fi
cd "$PROJECT_DIR"
echo "✓ Project directory exists"
echo ""

# Step 2: Check for app folder
echo "Step 2: Checking for app folder..."
if [ ! -d "$PROJECT_DIR/app" ]; then
    echo "✗ ERROR: app folder is missing!"
    echo ""
    echo "You need to upload these folders manually:"
    echo "  - app/"
    echo "  - templates/"
    echo "  - static/"
    echo ""
    echo "Go to PythonAnywhere Files tab and upload them to:"
    echo "  $PROJECT_DIR/"
    echo ""
    echo "After uploading, run this script again."
    exit 1
fi
echo "✓ app folder exists"
echo ""

# Step 3: Check for required files in app folder
echo "Step 3: Checking app folder contents..."
REQUIRED_FILES=("__init__.py" "models.py" "routes.py" "extensions.py")
MISSING_FILES=()

for file in "${REQUIRED_FILES[@]}"; do
    if [ ! -f "$PROJECT_DIR/app/$file" ]; then
        MISSING_FILES+=("$file")
        echo "✗ Missing: app/$file"
    else
        echo "✓ Found: app/$file"
    fi
done

if [ ${#MISSING_FILES[@]} -gt 0 ]; then
    echo ""
    echo "ERROR: Some required files are missing in app folder!"
    echo "Please upload them and run this script again."
    exit 1
fi
echo ""

# Step 4: Check for templates and static folders
echo "Step 4: Checking templates and static folders..."
if [ ! -d "$PROJECT_DIR/templates" ]; then
    echo "✗ WARNING: templates folder is missing!"
else
    echo "✓ templates folder exists"
fi

if [ ! -d "$PROJECT_DIR/static" ]; then
    echo "✗ WARNING: static folder is missing!"
else
    echo "✓ static folder exists"
fi
echo ""

# Step 5: Create or activate virtual environment
echo "Step 5: Setting up virtual environment..."
if [ ! -d "$VENV_PATH" ]; then
    echo "Creating new virtual environment: $VENV_NAME"
    mkvirtualenv --python=/usr/bin/python3.10 "$VENV_NAME"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtualenv
source "$VENV_PATH/bin/activate"
echo "✓ Virtual environment activated"
echo ""

# Step 6: Install requirements
echo "Step 6: Installing Python packages..."
if [ -f "$PROJECT_DIR/requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✓ Requirements installed"
else
    echo "✗ WARNING: requirements.txt not found"
    echo "Installing essential packages manually..."
    pip install Flask Flask-SQLAlchemy Flask-Migrate PyMySQL python-dotenv
fi
echo ""

# Step 7: Check installed packages
echo "Step 7: Verifying installed packages..."
echo "Flask version:"
pip show Flask | grep Version
echo "PyMySQL installed:"
pip list | grep PyMySQL
echo ""

# Step 8: Test imports
echo "Step 8: Testing Python imports..."
python3 << 'PYEOF'
import sys
sys.path.insert(0, '/home/kajetankonrad/crmproject')

try:
    from app import create_app
    print("✓ Successfully imported create_app")
    
    # Try to create the app
    app = create_app()
    print("✓ Successfully created Flask app")
    print(f"  App name: {app.name}")
    print(f"  App debug: {app.debug}")
    
except Exception as e:
    print(f"✗ ERROR during import: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
PYEOF

if [ $? -eq 0 ]; then
    echo "✓ All imports successful"
else
    echo "✗ Import test failed - check errors above"
    exit 1
fi
echo ""

# Step 9: Summary
echo "============================================================"
echo "FIX SCRIPT COMPLETE"
echo "============================================================"
echo ""
echo "✓ Project files verified"
echo "✓ Virtual environment ready at: $VENV_PATH"
echo "✓ Python packages installed"
echo "✓ App imports successfully"
echo ""
echo "NEXT STEPS:"
echo ""
echo "1. Update your WSGI configuration file:"
echo "   - Go to Web tab in PythonAnywhere"
echo "   - Click on the WSGI configuration file link"
echo "   - Set project_home = '$PROJECT_DIR'"
echo "   - Set DATABASE_URL with your MySQL password"
echo "   - Set a secure SECRET_KEY"
echo ""
echo "2. Set the virtualenv in Web tab:"
echo "   - Virtualenv path: $VENV_PATH"
echo ""
echo "3. Configure Static files in Web tab:"
echo "   - URL: /static/"
echo "   - Directory: $PROJECT_DIR/static"
echo ""
echo "4. Click the green 'Reload' button"
echo ""
echo "5. Check the error log if issues persist:"
echo "   tail -n 50 /var/log/kajetankonrad.pythonanywhere.com.error.log"
echo ""
echo "============================================================"
