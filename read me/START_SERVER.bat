@echo off
echo ============================================================
echo   HeartCheck DL - Starting Flask Server
echo ============================================================
echo.

cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Flask server on http://localhost:5000/
echo.
echo Press Ctrl+C to stop the server
echo ============================================================
echo.

set FLASK_APP=api\app_simple.py
set FLASK_ENV=development

python api\app_simple.py

pause
