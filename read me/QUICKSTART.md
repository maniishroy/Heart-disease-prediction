# ⚡ HeartCheck DL — 5-Minute Quick Start

Get HeartCheck DL running on **localhost in 5 minutes** using the sample dataset.

---

## 🚀 Option 1: Automated Setup (Easiest)

### Linux / macOS

```bash
cd HeartCheckDL
chmod +x quick_start.sh
./quick_start.sh
```

### Windows PowerShell

```powershell
cd HeartCheckDL
.\quick_start.ps1
```

**What it does:**
1. ✅ Creates virtual environment
2. ✅ Installs all dependencies
3. ✅ Prepares sample data (15 rows)
4. ✅ Trains MLP model (30 epochs, ~2 min)
5. ✅ Displays run instructions

---

## 🛠️ Option 2: Manual Setup (Step-by-Step)

### Step 1: Setup Environment

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows PowerShell:**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 2: Prepare Data

```bash
python training/prepare_data.py --input data/raw/sample.csv --target target
```

**Expected output:**
```
==================================================
HeartCheck DL - Data Preparation
==================================================
Loading data from: .../data/raw/sample.csv
Loaded 15 rows, 14 columns
...
✓ Data preparation complete!
```

### Step 3: Train Model

```bash
python training/train_dl.py --model mlp --epochs 30 --batch-size 32
```

**Expected output:**
```
==================================================
HeartCheck DL - Model Training
==================================================
...
Epoch 30/30
1/1 [==============================] - 0s 13ms/step
...
✓ Training complete!
Model saved to: .../models/heart_dl_model_YYYYMMDD_HHMMSS.h5
```

### Step 4: Run Application

**Linux/macOS:**
```bash
export FLASK_APP=api/app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

**Windows PowerShell:**
```powershell
$env:FLASK_APP = "api/app.py"
$env:FLASK_ENV = "development"
flask run --host=0.0.0.0 --port=5000
```

### Step 5: Open Browser

Navigate to: **http://localhost:5000/**

---

## 🐳 Option 3: Docker (One Command)

```bash
docker-compose up --build
```

Then open: **http://localhost:5000/**

**Note:** First run trains model inside container (~3-5 minutes).

---

## ✅ Verify Installation

### Check Health Endpoint

```bash
curl http://localhost:5000/api/health
```

**Expected response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "preprocessor_loaded": true,
  "model_info": {
    "model_name": "heart_dl_v1",
    "file": "heart_dl_model_20251120_1530.h5",
    ...
  }
}
```

### Test Prediction API

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 57,
    "sex": "male",
    "resting_bp": 140,
    "cholesterol": 240,
    "fasting_bs_gt_120": 0,
    "rest_ecg": "normal",
    "max_hr": 150,
    "exercise_angina": 0,
    "oldpeak": 1.2,
    "st_slope": "up",
    "smoking": 0,
    "diabetes": 0,
    "family_history": 1
  }'
```

**Expected response:**
```json
{
  "risk_probability": 0.3456,
  "prediction": 0,
  "model": "heart_dl_v1",
  "timestamp": "2025-11-20T16:30:00.000Z"
}
```

---

## 🧪 Test the UI

1. **Home Page:** http://localhost:5000/
   - Click "Start Assessment"

2. **Prediction Form:** http://localhost:5000/predict
   - Fill out all 4 steps
   - Submit form

3. **Results Page:** http://localhost:5000/results
   - View risk score and recommendations

4. **Dataset Page:** http://localhost:5000/dataset
   - Explore sample data

5. **Admin Page:** http://localhost:5000/admin
   - View prediction logs and model registry

---

## 🎯 Sample Test Data

Copy-paste these values into the prediction form:

| Field | Value |
|-------|-------|
| **Age** | 57 |
| **Sex** | Male |
| **Resting BP** | 140 mm Hg |
| **Cholesterol** | 240 mg/dl |
| **Fasting BS > 120** | No (unchecked) |
| **Resting ECG** | Normal |
| **Max Heart Rate** | 150 bpm |
| **Exercise Angina** | No |
| **Oldpeak** | 1.2 |
| **ST Slope** | Upsloping |
| **Smoking** | No (unchecked) |
| **Diabetes** | No (unchecked) |
| **Family History** | Yes (checked) |

**Expected result:** Low-to-moderate risk (~30-40%)

---

## 🔧 Common Issues & Fixes

### Issue: "Port 5000 already in use"

**Solution 1:** Use different port
```bash
flask run --host=0.0.0.0 --port=8080
```

**Solution 2 (Kill process):**
```bash
# Linux/macOS
lsof -ti:5000 | xargs kill -9

# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Issue: "Model not available"

**Cause:** Training not completed

**Solution:**
```bash
python training/prepare_data.py --input data/raw/sample.csv --target target
python training/train_dl.py --epochs 30
```

### Issue: "Module not found"

**Cause:** Virtual environment not activated

**Solution:**
```bash
# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\Activate.ps1
```

### Issue: "Kaggle API error" (when downloading full dataset)

**Cause:** Missing Kaggle credentials

**Solution:**
1. Go to kaggle.com/account
2. Create API token
3. Save `kaggle.json` to:
   - Linux/macOS: `~/.kaggle/kaggle.json`
   - Windows: `%USERPROFILE%\.kaggle\kaggle.json`
4. Set permissions (Linux/macOS): `chmod 600 ~/.kaggle/kaggle.json`

---

## 📊 What's Running?

After `flask run`, these endpoints are active:

| URL | Description |
|-----|-------------|
| http://localhost:5000/ | Home page |
| http://localhost:5000/predict | Prediction form |
| http://localhost:5000/results | Results page |
| http://localhost:5000/dataset | Dataset insights |
| http://localhost:5000/about | Project info |
| http://localhost:5000/admin | Admin dashboard |
| http://localhost:5000/api/predict | JSON API |
| http://localhost:5000/api/health | Health check |

---

## 🎓 Next Steps

### 1. Download Full Kaggle Dataset

```bash
# Setup Kaggle credentials first
python training/download_data.py --dataset fedesoriano/heart-failure-prediction

# Retrain with full dataset
python training/prepare_data.py --input data/raw/heart.csv --target HeartDisease
python training/train_dl.py --model mlp --epochs 100
```

### 2. Customize the Model

Edit `training/train_dl.py` to adjust:
- Hidden layer sizes
- Dropout rate
- Learning rate
- Number of epochs
- Batch size

### 3. Deploy to Production

See `README.md` for:
- Security hardening
- Nginx reverse proxy setup
- HTTPS configuration
- Database migration (SQLite → PostgreSQL)

### 4. Add Features

Ideas:
- User authentication
- Email reports
- PDF export
- Historical tracking
- Advanced visualizations

---

## 🆘 Need Help?

1. **Read full docs:** `README.md`
2. **Check architecture:** `PROJECT_SUMMARY.md`
3. **Report issues:** GitHub Issues
4. **API reference:** See `/api/health` and `/api/predict` endpoints

---

## ✅ Quick Validation Checklist

After setup, verify:

- [ ] Virtual environment activated (`which python` shows venv path)
- [ ] All dependencies installed (`pip list` shows Flask, TensorFlow)
- [ ] Model trained (check `models/` folder for `.h5` file)
- [ ] Flask server running (see "Running on http://0.0.0.0:5000")
- [ ] Home page loads (no 404 errors)
- [ ] Prediction form accessible
- [ ] Sample prediction works (submit test data)
- [ ] Results display correctly
- [ ] Admin page shows logs (after first prediction)

---

## 🎉 Success Indicators

You'll know it's working when:

✅ Flask startup message shows:
```
* Running on http://0.0.0.0:5000
* Model loaded: heart_dl_v1
```

✅ Browser shows HeartCheck DL home page with:
- Navigation menu
- Hero section
- Feature cards
- "Start Assessment" button

✅ Prediction works and displays:
- Risk percentage (e.g., 34.6%)
- Risk level (Low/Moderate/High)
- Color-coded meter
- Personalized recommendations

---

**Time to complete:** ~5 minutes (with sample data)  
**Lines of code:** 3,500+  
**Files created:** 22  
**Ready for:** localhost deployment & testing

🚀 **Happy Predicting!**
