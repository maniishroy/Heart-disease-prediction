# HeartCheck DL — Full-Stack Deep Learning Heart Disease Detector

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A **multi-page**, production-ready web application for heart disease risk prediction powered by deep learning. Built with Flask, TensorFlow/Keras, and served on **localhost** with Docker support.

---

## 🎯 Project Overview

HeartCheck DL is a comprehensive full-stack application that:
- Collects 13 clinical and lifestyle indicators through an intuitive multi-step form
- Processes data using scikit-learn preprocessing pipelines
- Predicts heart disease risk using TensorFlow/Keras deep learning models
- Displays results with personalized recommendations and downloadable reports
- Provides dataset insights and model management through an admin dashboard

**⚠️ IMPORTANT MEDICAL DISCLAIMER:** This tool is for **educational and research purposes only**. It is NOT a medical device and should NOT be used for clinical diagnosis or treatment decisions. Always consult qualified healthcare professionals.

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Flask 3.0 + Jinja2 (Python 3.11+) |
| **Deep Learning** | TensorFlow 2.15 / Keras (MLP + Hybrid CNN models) |
| **Data Processing** | Pandas, NumPy, Scikit-learn |
| **Frontend** | Server-rendered HTML5/CSS3/JavaScript |
| **Database** | SQLite (prediction logs) |
| **Dataset** | Kaggle API (fedesoriano/heart-failure-prediction) |
| **Containerization** | Docker + Docker Compose |
| **Production Server** | Gunicorn |

---

## 📁 Repository Structure

```
HeartCheckDL/
├── api/
│   └── app.py                  # Flask application (routes, API, inference)
├── templates/
│   ├── base.html               # Base template with navigation
│   ├── home.html               # Landing page
│   ├── predict.html            # Multi-step prediction form
│   ├── results.html            # Risk assessment results
│   ├── dataset.html            # Dataset insights & visualizations
│   ├── about.html              # Project info & ethics
│   └── admin.html              # Model management & logs
├── static/
│   ├── css/
│   │   └── styles.css          # Complete styling (Poppins + Inter fonts)
│   └── js/
│       └── app.js              # Client-side validation & API helpers
├── data/
│   ├── raw/
│   │   └── sample.csv          # Sample dataset (15 rows for testing)
│   └── processed/
│       ├── X_train.npy         # Preprocessed training data
│       ├── X_test.npy          # Preprocessed test data
│       └── processed_sample.csv
├── models/
│   ├── preprocessor.pkl        # Saved scikit-learn pipeline
│   ├── heart_dl_model_*.h5     # Trained Keras models
│   ├── history_*.json          # Training histories
│   └── registry.json           # Model versioning registry
├── training/
│   ├── download_data.py        # Kaggle dataset downloader
│   ├── prepare_data.py         # Data cleaning & preprocessing
│   └── train_dl.py             # TensorFlow/Keras training script
├── db/
│   └── predictions.sqlite      # SQLite database (created on first run)
├── docker-compose.yml          # Docker multi-service config
├── Dockerfile                  # Container definition
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

---

## 🚀 Quick Start (Localhost)

### Prerequisites

- **Python 3.11+** (3.9+ supported)
- **pip** package manager
- **Kaggle account** (optional, for downloading datasets)
- **Docker** (optional, for containerized hosting)

### Method 1: Local Development (Linux/macOS)

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/HeartCheckDL.git
cd HeartCheckDL

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Download dataset from Kaggle
# Setup Kaggle API credentials first:
# Place kaggle.json in ~/.kaggle/ or set KAGGLE_USERNAME and KAGGLE_KEY
python training/download_data.py --dataset fedesoriano/heart-failure-prediction

# 5. Prepare data (can use sample.csv if Kaggle download skipped)
python training/prepare_data.py --input data/raw/sample.csv

# 6. Train model (use sample data or full dataset)
python training/train_dl.py --model mlp --epochs 50

# 7. Run Flask application
export FLASK_APP=api/app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000

# 8. Open browser
# Navigate to: http://localhost:5000/
```

### Method 2: Windows PowerShell

```powershell
# 1. Clone repository
git clone https://github.com/yourusername/HeartCheckDL.git
cd HeartCheckDL

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Download dataset
# Setup Kaggle credentials: %USERPROFILE%\.kaggle\kaggle.json
python training\download_data.py --dataset fedesoriano/heart-failure-prediction

# 5. Prepare data
python training\prepare_data.py --input data\raw\sample.csv

# 6. Train model
python training\train_dl.py --model mlp --epochs 50

# 7. Set environment variables and run
$env:FLASK_APP = "api/app.py"
$env:FLASK_ENV = "development"
flask run --host=0.0.0.0 --port=5000

# 8. Open http://localhost:5000/ in browser
```

### Method 3: Docker (One-Command Local Hosting)

```bash
# 1. Clone repository
git clone https://github.com/yourusername/HeartCheckDL.git
cd HeartCheckDL

# 2. Build and run with Docker Compose
docker-compose up --build

# 3. Access application
# Navigate to: http://localhost:5000/

# To stop:
# Press Ctrl+C, then:
docker-compose down
```

---

## 📊 Dataset Setup

### Using Sample Data (No Kaggle Required)

The repository includes `data/raw/sample.csv` with 15 sample records. Perfect for testing without Kaggle credentials:

```bash
python training/prepare_data.py --input data/raw/sample.csv
python training/train_dl.py --epochs 30
```

### Downloading Full Kaggle Dataset

**Step 1: Get Kaggle API Credentials**

1. Go to [kaggle.com/account](https://www.kaggle.com/account)
2. Scroll to "API" section
3. Click "Create New API Token"
4. Save `kaggle.json` to:
   - **Linux/macOS:** `~/.kaggle/kaggle.json`
   - **Windows:** `%USERPROFILE%\.kaggle\kaggle.json`
5. Set permissions (Linux/macOS): `chmod 600 ~/.kaggle/kaggle.json`

**Step 2: Download Dataset**

```bash
python training/download_data.py --dataset fedesoriano/heart-failure-prediction --out data/raw
```

**Step 3: Process and Train**

```bash
python training/prepare_data.py --input data/raw/heart.csv --target HeartDisease
python training/train_dl.py --model mlp --epochs 100 --batch-size 32
```

---

## 🧠 Model Training

### Training Options

```bash
# Basic MLP model (recommended)
python training/train_dl.py --model mlp --epochs 100 --batch-size 32

# Hybrid CNN model (experimental)
python training/train_dl.py --model hybrid --epochs 150 --batch-size 16
```

### Model Architecture (MLP)

```
Input (13 features)
    ↓
Dense(128, relu) + BatchNorm + Dropout(0.3)
    ↓
Dense(64, relu) + BatchNorm + Dropout(0.3)
    ↓
Dense(32, relu) + BatchNorm + Dropout(0.3)
    ↓
Dense(1, sigmoid) → Risk Probability [0-1]
```

**Callbacks:**
- Early Stopping (patience=15)
- Model Checkpoint (saves best model)
- ReduceLROnPlateau (adaptive learning rate)

### PyTorch Alternative

To use PyTorch instead of TensorFlow:

1. Replace in `requirements.txt`:
   ```
   torch==2.1.0
   torchvision==0.16.0
   ```

2. Modify `training/train_dl.py` to use PyTorch `nn.Module` classes
3. Update `api/app.py` inference to use `torch.load()` and `model.eval()`

---

## 🌐 API Endpoints

### Web Pages (GET)

| Route | Description |
|-------|-------------|
| `/` | Home page with overview |
| `/predict` | Multi-step prediction form |
| `/results` | Risk assessment results |
| `/dataset` | Dataset insights & visualizations |
| `/about` | Project info & ethics disclaimer |
| `/admin` | Model management & prediction logs |

### JSON API (POST)

**`POST /api/predict`**

**Request Body:**
```json
{
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
}
```

**Response:**
```json
{
  "risk_probability": 0.3456,
  "prediction": 0,
  "model": "heart_dl_v1",
  "timestamp": "2025-11-20T16:30:00.000Z"
}
```

**Health Check:**
```bash
curl http://localhost:5000/api/health
```

---

## 🧪 Testing the Application

### Manual Testing

1. Start the server: `flask run --host=0.0.0.0 --port=5000`
2. Navigate to `http://localhost:5000/predict`
3. Fill out the form with sample data:
   - Age: 57
   - Sex: Male
   - Resting BP: 140 mm Hg
   - Cholesterol: 240 mg/dl
   - Fasting BS > 120: No
   - Resting ECG: Normal
   - Max HR: 150 bpm
   - Exercise Angina: No
   - Oldpeak: 1.2
   - ST Slope: Upsloping
   - Smoking: No
   - Diabetes: No
   - Family History: Yes
4. Submit and view results

### API Testing with cURL

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

---

## 🔧 Troubleshooting

### Port 5000 Already in Use

**Solution 1:** Use a different port
```bash
flask run --host=0.0.0.0 --port=8080
```

**Solution 2 (Linux/macOS):** Find and kill process
```bash
lsof -ti:5000 | xargs kill -9
```

**Solution 3 (Windows):**
```powershell
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Virtual Environment Activation Issues

**Windows (Execution Policy):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### Kaggle API "401 Unauthorized"

- Verify `kaggle.json` is in correct location
- Check file permissions: `chmod 600 ~/.kaggle/kaggle.json` (Linux/macOS)
- Confirm Kaggle account is verified (phone number required)

### "Model not available" Error

**Cause:** No trained model found

**Solution:**
```bash
python training/prepare_data.py --input data/raw/sample.csv
python training/train_dl.py --epochs 30
```

### TensorFlow GPU Not Detected

**Install CUDA-enabled TensorFlow:**
```bash
pip install tensorflow[and-cuda]==2.15.0
```

**Verify GPU:**
```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

---

## 📈 Model Performance

Expected performance on full dataset (train/test split 80/20):

| Metric | MLP Model | Hybrid CNN Model |
|--------|-----------|------------------|
| Accuracy | 85-90% | 82-87% |
| AUC-ROC | 0.88-0.92 | 0.85-0.90 |
| Precision | 0.84-0.89 | 0.81-0.86 |
| Recall | 0.86-0.91 | 0.83-0.88 |

**Note:** Performance varies based on dataset, hyperparameters, and random seed.

---

## 🔐 Security & Privacy

### Development vs. Production

**Current Setup (Development):**
- ✅ Runs on localhost
- ✅ CORS enabled for development
- ✅ Debug mode enabled
- ❌ **NOT production-ready**

**For Production Deployment:**

1. **Disable Debug Mode:**
   ```python
   # api/app.py
   app.config['DEBUG'] = False
   app.config['ENV'] = 'production'
   ```

2. **Change Secret Key:**
   ```bash
   export SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
   ```

3. **Use HTTPS:**
   - Deploy behind reverse proxy (Nginx)
   - Enable SSL/TLS certificates

4. **Disable CORS:**
   ```python
   # Remove @app.after_request CORS headers
   ```

5. **Add Rate Limiting:**
   ```bash
   pip install flask-limiter
   ```

6. **HIPAA/GDPR Compliance:**
   - Implement proper data encryption
   - Add user consent mechanisms
   - Anonymize all stored data
   - Regular security audits

### Data Protection

- **No PII stored:** Only clinical metrics logged
- **Anonymized logs:** No names, emails, or identifiers
- **Local processing:** All predictions on your server
- **SQLite database:** Easily auditable and portable

---

## 📚 Citation & Attribution

**Dataset:**
```
fedesoriano. (September 2021). Heart Failure Prediction Dataset.
Retrieved from https://www.kaggle.com/fedesoriano/heart-failure-prediction
```

**Original Data Sources:**
1. Cleveland Clinic Foundation
2. Hungarian Institute of Cardiology, Budapest
3. University Hospital, Zurich, Switzerland
4. University Hospital, Basel, Switzerland
5. V.A. Medical Center, Long Beach, CA

---

## 🤝 Contributing

Contributions welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'feat: add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Add docstrings to all functions
- Write unit tests for new features
- Update README for major changes

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- TensorFlow/Keras team for deep learning framework
- Flask community for excellent web framework
- Kaggle for hosting the heart disease dataset
- Contributors to scikit-learn and pandas

---

## 📞 Contact & Support

- **GitHub Issues:** [Report bugs or request features](https://github.com/yourusername/HeartCheckDL/issues)
- **Documentation:** This README and inline code comments
- **Academic Inquiries:** Contact via GitHub profile

---

## 📝 Suggested Commit Message

```
feat(fullstack): add multi-page HeartCheck DL app, Kaggle downloader, DL training pipeline, Flask API, and localhost hosting

- Implement Flask multi-page app with Jinja2 templates (home, predict, results, dataset, about, admin)
- Add TensorFlow/Keras training pipeline with MLP and hybrid CNN architectures
- Include Kaggle dataset downloader and scikit-learn preprocessing
- Implement SQLite prediction logging and model versioning registry
- Add Docker + docker-compose for containerized local hosting
- Include comprehensive localhost setup instructions for Linux/macOS/Windows
- Add API endpoints for programmatic predictions
- Implement multi-step form with client-side validation
- Style with modern CSS (Poppins + Inter fonts, glassmorphism, gradient accents)
- Include sample dataset (15 rows) for testing without Kaggle credentials
- Add medical disclaimer and ethics documentation
```

---

**Built with ❤️ for educational and research purposes. Always consult healthcare professionals for medical decisions.**
