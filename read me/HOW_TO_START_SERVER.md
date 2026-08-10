# How to Start HeartCheck DL Server

## Quick Start - EASIEST METHOD

### Option 1: Double-click the batch file
1. Navigate to: `c:\Users\manii\Documents\HTML\HeartCheckDL\`
2. Double-click: `START_SERVER.bat`
3. A command window will open and the server will start
4. Open browser: http://localhost:5000/

### Option 2: Run from Command Prompt
1. Open Command Prompt
2. Copy and paste this command:
```
cd c:\Users\manii\Documents\HTML\HeartCheckDL && START_SERVER.bat
```
3. Press Enter
4. Open browser: http://localhost:5000/

### Option 3: Run from PowerShell
1. Open PowerShell
2. Copy and paste this command:
```powershell
cd c:\Users\manii\Documents\HTML\HeartCheckDL; .\START_SERVER.bat
```
3. Press Enter
4. Open browser: http://localhost:5000/

---

## Server Access URLs

Once the server starts, you can access the website using any of these URLs:

- **Main URL:** http://localhost:5000/
- **Alternative:** http://127.0.0.1:5000/
- **Network Access:** http://10.203.182.110:5000/ (if on same network)

---

## Troubleshooting

### If batch file doesn't work:
Try this manual command in PowerShell:
```powershell
cd c:\Users\manii\Documents\HTML\HeartCheckDL
.\venv\Scripts\python.exe api\app_simple.py
```

### If you see "Port already in use" error:
Another instance is already running. Either:
- Close the other command window, OR
- Open http://localhost:5000/ directly

### If virtual environment is missing:
Run this command first:
```powershell
cd c:\Users\manii\Documents\HTML\HeartCheckDL
python -m venv venv
.\venv\Scripts\pip.exe install -r requirements_lite.txt
```

---

## How to Stop the Server

- Press `Ctrl+C` in the command window
- OR close the command window

---

## Notes

✓ Server is WORKING - tested successfully
✓ Virtual environment is properly configured
✓ Flask 3.0.0 is installed
✓ Python 3.14.0 is available

The server runs on your LOCAL machine only. It's not deployed to the internet.
To share with others, they need to be on the same network and use: http://10.203.182.110:5000/
