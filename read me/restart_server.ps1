Write-Host "🔄 Restarting HeartCheck DL Server..." -ForegroundColor Cyan

# Find and kill any existing Flask processes on port 5000
$processes = Get-NetTCPConnection -LocalPort 5000 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -Unique
if ($processes) {
    Write-Host "⏹️  Stopping existing server..." -ForegroundColor Yellow
    foreach ($proc in $processes) {
        try {
            Stop-Process -Id $proc -Force -ErrorAction SilentlyContinue
            Write-Host "   Stopped process $proc" -ForegroundColor Gray
        } catch {
            # Process might have already exited
        }
    }
    Start-Sleep -Seconds 2
}

# Activate venv and start server
Write-Host "🚀 Starting server on http://localhost:5000/" -ForegroundColor Green
Set-Location $PSScriptRoot
& ".\venv\Scripts\python.exe" "api\app.py"
