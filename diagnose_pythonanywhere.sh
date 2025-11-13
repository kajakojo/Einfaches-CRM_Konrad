#!/bin/bash

# PythonAnywhere Diagnostic Script for CRM App
# Run this in your PythonAnywhere Bash Console

echo "============================================================"
echo "PYTHONANYWHERE CRM APP DIAGNOSTIC SCRIPT"
echo "============================================================"
echo ""

# 1. Check home directory contents
echo "1. Checking home directory contents..."
echo "   Path: /home/kajetankonrad/"
cd /home/kajetankonrad
ls -la
echo ""

# 2. Search for app folder
echo "2. Searching for 'app' folder..."
find /home/kajetankonrad -type d -name "app" 2>/dev/null
echo ""

# 3. Check common project locations
echo "3. Checking common project locations..."
for dir in "Einfaches-CRM_Konrad" "mysite" "einfaches-crm_konrad" "crm" "CRM"; do
    if [ -d "/home/kajetankonrad/$dir" ]; then
        echo "   ✓ Found: /home/kajetankonrad/$dir"
        ls -la "/home/kajetankonrad/$dir" | head -n 15
        echo ""
        
        # Check if app folder exists inside
        if [ -d "/home/kajetankonrad/$dir/app" ]; then
            echo "   ✓✓ Found app folder inside!"
            ls -la "/home/kajetankonrad/$dir/app"
            echo ""
            echo "   >>> USE THIS PATH IN WSGI: /home/kajetankonrad/$dir"
            echo ""
        else
            echo "   ✗ No 'app' folder found inside $dir"
            echo ""
        fi
    else
        echo "   ✗ Not found: /home/kajetankonrad/$dir"
    fi
done

# 4. Check Python version
echo "4. Checking Python version..."
python3 --version
echo ""

# 5. Check virtualenvs
echo "5. Checking virtual environments..."
if [ -d "/home/kajetankonrad/.virtualenvs" ]; then
    echo "   Virtual environments found:"
    ls -la /home/kajetankonrad/.virtualenvs/
    echo ""
else
    echo "   ✗ No virtual environments found at /home/kajetankonrad/.virtualenvs"
    echo ""
fi

# 6. Check if requirements.txt exists
echo "6. Searching for requirements.txt..."
find /home/kajetankonrad -name "requirements.txt" -type f 2>/dev/null
echo ""

echo "============================================================"
echo "DIAGNOSTIC COMPLETE"
echo "============================================================"
echo ""
echo "NEXT STEPS:"
echo "1. Look at the output above and find the correct project path"
echo "2. Update the WSGI file with the correct path"
echo "3. If no project found, you need to upload your files first"
echo ""
