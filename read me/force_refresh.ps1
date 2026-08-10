# Force Browser Cache Refresh Script
Write-Host "🔄 Forcing Browser Cache Refresh..." -ForegroundColor Cyan
Write-Host ""

# Stop Flask if running
Write-Host "1️⃣ Stopping Flask server..." -ForegroundColor Yellow
Get-Process python -ErrorAction SilentlyContinue | Where-Object {$_.CommandLine -like "*flask*"} | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2

# Start Flask with new cache version
Write-Host "2️⃣ Starting Flask with new cache version..." -ForegroundColor Yellow
cd "c:\Users\manii\Documents\HTML\HeartCheckDL"
.\venv\Scripts\Activate.ps1
$env:FLASK_APP = "api/app.py"
$env:FLASK_ENV = "development"

Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'c:\Users\manii\Documents\HTML\HeartCheckDL'; .\venv\Scripts\Activate.ps1; `$env:FLASK_APP='api/app.py'; `$env:FLASK_ENV='development'; python -m flask run --host=0.0.0.0 --port=5000"

Start-Sleep -Seconds 5

Write-Host ""
Write-Host "✅ Server started!" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Open your browser and go to: http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "🔑 To see changes, press:" -ForegroundColor Yellow
Write-Host "   Windows: Ctrl + Shift + R" -ForegroundColor White
Write-Host "   or" -ForegroundColor Gray
Write-Host "   Chrome: F12 → Right-click refresh → Empty Cache and Hard Reload" -ForegroundColor White
Write-Host ""
Write-Host "💡 Or open in Incognito mode: Ctrl + Shift + N" -ForegroundColor Green
Write-Host ""
Write-Host "Press any key to open browser..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

Start-Process "http://localhost:5000"
