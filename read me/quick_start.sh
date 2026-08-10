#!/bin/bash
# HeartCheck DL - Quick Start Script (Linux/macOS)

echo "=================================================="
echo "  HeartCheck DL - Quick Start Setup"
echo "=================================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.9 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d ' ' -f 2 | cut -d '.' -f 1,2)
echo "✓ Found Python $PYTHON_VERSION"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

# Prepare sample data
echo ""
echo "🔧 Preparing sample data..."
python training/prepare_data.py --input data/raw/sample.csv --target target

# Train model
echo ""
echo "🧠 Training deep learning model (30 epochs)..."
python training/train_dl.py --model mlp --epochs 30 --batch-size 32

# Check if training succeeded
if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "  ✓ Setup Complete!"
    echo "=================================================="
    echo ""
    echo "To start the application:"
    echo ""
    echo "  export FLASK_APP=api/app.py"
    echo "  export FLASK_ENV=development"
    echo "  flask run --host=0.0.0.0 --port=5000"
    echo ""
    echo "Then open: http://localhost:5000/"
    echo ""
    echo "=================================================="
else
    echo ""
    echo "❌ Training failed. Please check error messages above."
    exit 1
fi
