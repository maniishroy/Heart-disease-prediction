# HeartCheck DL - Quick Start Script (Windows PowerShell)

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  HeartCheck DL - Quick Start Setup" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
try {
    $pythonVersion = python --version
    Write-Host "✓ Found $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found. Please install Python 3.9 or higher." -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host ""
Write-Host "📦 Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host ""
Write-Host "📥 Installing dependencies..." -ForegroundColor Yellow
pip install --upgrade pip | Out-Null
pip install -r requirements.txt

# Prepare sample data
Write-Host ""
Write-Host "🔧 Preparing sample data..." -ForegroundColor Yellow
python training\prepare_data.py --input data\raw\sample.csv --target target

# Train model
Write-Host ""
Write-Host "🧠 Training deep learning model (30 epochs)..." -ForegroundColor Yellow
python training\train_dl.py --model mlp --epochs 30 --batch-size 32

# Check if training succeeded
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "==================================================" -ForegroundColor Green
    Write-Host "  ✓ Setup Complete!" -ForegroundColor Green
    Write-Host "==================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "To start the application:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host '  $env:FLASK_APP = "api/app.py"' -ForegroundColor White
    Write-Host '  $env:FLASK_ENV = "development"' -ForegroundColor White
    Write-Host "  flask run --host=0.0.0.0 --port=5000" -ForegroundColor White
    Write-Host ""
    Write-Host "Then open: http://localhost:5000/" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "==================================================" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Training failed. Please check error messages above." -ForegroundColor Red
    exit 1
}
