# HeartCheck DL - Algorithms & Techniques Documentation

## 📚 Table of Contents
1. [Machine Learning Algorithms](#machine-learning-algorithms)
2. [Data Preprocessing Techniques](#data-preprocessing-techniques)
3. [Model Architecture Details](#model-architecture-details)
4. [Training Algorithms](#training-algorithms)
5. [Validation & Evaluation](#validation--evaluation)
6. [Web Application Logic](#web-application-logic)

---

## 1. Machine Learning Algorithms

### 1.1 Multi-Layer Perceptron (MLP) - Primary Algorithm

**Type**: Deep Neural Network (Supervised Learning)

**Architecture**:
```
Input Layer (13 features)
    ↓
Dense Layer (128 neurons, ReLU activation)
    ↓
Batch Normalization
    ↓
Dropout (30% rate)
    ↓
Dense Layer (64 neurons, ReLU activation)
    ↓
Batch Normalization
    ↓
Dropout (30% rate)
    ↓
Dense Layer (32 neurons, ReLU activation)
    ↓
Batch Normalization
    ↓
Dropout (30% rate)
    ↓
Output Layer (1 neuron, Sigmoid activation)
    ↓
Binary Classification (0 or 1)
```

**Mathematical Formulation**:

For each hidden layer:
```
z = W·x + b                    (Linear transformation)
h = ReLU(z) = max(0, z)        (Activation)
h_norm = BatchNorm(h)          (Normalization)
h_drop = Dropout(h_norm, 0.3)  (Regularization)
```

Output layer:
```
output = σ(W·h + b)            (Sigmoid activation)
where σ(x) = 1 / (1 + e^(-x))
```

**Loss Function**: Binary Cross-Entropy
```
L(y, ŷ) = -[y·log(ŷ) + (1-y)·log(1-ŷ)]
```

**Why MLP?**
- Excellent for tabular data with mixed features
- Captures non-linear relationships between clinical indicators
- Robust with proper regularization (dropout, batch normalization)
- Achieves 85-90% accuracy on heart disease prediction

---

### 1.2 Hybrid CNN Model (Experimental)

**Type**: 1D Convolutional Neural Network

**Architecture**:
```
Input (13 features)
    ↓
Reshape to (13, 1) - treat features as sequence
    ↓
Conv1D (64 filters, kernel_size=3, ReLU, same padding)
    ↓
Batch Normalization
    ↓
MaxPooling1D (pool_size=2)
    ↓
Conv1D (32 filters, kernel_size=3, ReLU, same padding)
    ↓
Batch Normalization
    ↓
GlobalMaxPooling1D
    ↓
Dense (64 neurons, ReLU)
    ↓
Dropout (30%)
    ↓
Dense (32 neurons, ReLU)
    ↓
Dropout (30%)
    ↓
Output (1 neuron, Sigmoid)
```

**Convolution Operation**:
```
y[i] = Σ(w[k] · x[i+k]) + b
where k ranges over kernel size
```

**Why Experimental?**
- CNNs typically work better for spatial/sequential data (images, time-series)
- Tabular medical data doesn't have inherent spatial structure
- Included for research/comparison purposes
- MLP usually outperforms for this use case

---

## 2. Data Preprocessing Techniques

### 2.1 Data Cleaning Algorithm

**Steps**:
```python
1. Load raw CSV data
2. Standardize column names (lowercase, underscore)
3. Identify missing values
4. Handle missing data:
   - Drop rows with critical missing (age, BP, cholesterol)
   - Impute numeric: median
   - Impute categorical: mode (most frequent)
5. Remove duplicates
6. Validate data ranges (age: 1-120, BP: 20-300, etc.)
```

**Missing Value Imputation**:
```
For numeric column x with n values:
  x_imputed = median([x₁, x₂, ..., xₙ])

For categorical column c:
  c_imputed = mode([c₁, c₂, ..., cₙ])
```

---

### 2.2 Feature Encoding

#### One-Hot Encoding (Categorical Variables)
Converts categorical features to binary vectors.

**Example**:
```
sex: ['male', 'female', 'other']
    ↓
One-Hot Encoded:
male   → [1, 0]  (drop 'other' to avoid multicollinearity)
female → [0, 1]
other  → [0, 0]
```

**Mathematical Representation**:
```
For category c in C categories:
  encoding[c] = e_c where e_c is a unit vector
  
Drop first category to avoid dummy variable trap
```

**Applied to**:
- sex (3 categories)
- rest_ecg (3 categories: normal, st_abnormality, lvh)
- st_slope (3 categories: up, flat, down)

---

### 2.3 Feature Normalization

#### Standard Scaling (Z-Score Normalization)
Transforms numeric features to mean=0, std=1

**Formula**:
```
z = (x - μ) / σ

where:
  x = original value
  μ = mean of feature
  σ = standard deviation of feature
```

**Example**:
```
Age values: [45, 52, 61, 38, 70]
μ = 53.2, σ = 12.5

Scaled: 
  45 → (45-53.2)/12.5 = -0.656
  52 → (52-53.2)/12.5 = -0.096
  61 → (61-53.2)/12.5 = +0.624
```

**Applied to**:
- age
- resting_bp (resting blood pressure)
- cholesterol
- max_hr (maximum heart rate)
- oldpeak (ST depression)

**Why Standard Scaling?**
- Prevents features with large ranges from dominating
- Ensures gradient descent converges faster
- Required for neural networks to train effectively

---

### 2.4 Train-Test Split

**Algorithm**: Stratified Random Sampling

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 80% train, 20% test
    random_state=42,     # Reproducibility
    stratify=y          # Maintain class proportions
)
```

**Why Stratified?**
- Ensures equal proportion of positive/negative cases in both sets
- Prevents bias if dataset is imbalanced
- More reliable evaluation metrics

**Example Distribution**:
```
Original: 60% no disease, 40% disease
Train:    60% no disease, 40% disease (same ratio)
Test:     60% no disease, 40% disease (same ratio)
```

---

## 3. Model Architecture Details

### 3.1 Activation Functions

#### ReLU (Rectified Linear Unit)
```
f(x) = max(0, x) = {
    x   if x > 0
    0   if x ≤ 0
}
```

**Properties**:
- Prevents vanishing gradient problem
- Computationally efficient
- Introduces non-linearity
- Used in all hidden layers

**Gradient**:
```
f'(x) = {
    1   if x > 0
    0   if x ≤ 0
}
```

#### Sigmoid Activation (Output Layer)
```
σ(x) = 1 / (1 + e^(-x))
```

**Properties**:
- Outputs probability between 0 and 1
- Suitable for binary classification
- Smooth gradient for backpropagation

**Derivative**:
```
σ'(x) = σ(x) · (1 - σ(x))
```

---

### 3.2 Regularization Techniques

#### Batch Normalization

**Algorithm**:
```
For mini-batch B = {x₁, x₂, ..., xₘ}:

1. Calculate batch mean:
   μ_B = (1/m) Σ xᵢ

2. Calculate batch variance:
   σ²_B = (1/m) Σ (xᵢ - μ_B)²

3. Normalize:
   x̂ᵢ = (xᵢ - μ_B) / √(σ²_B + ε)
   
4. Scale and shift (learnable params):
   yᵢ = γ·x̂ᵢ + β
```

**Benefits**:
- Reduces internal covariate shift
- Allows higher learning rates
- Acts as regularization
- Speeds up training

#### Dropout

**Algorithm**:
```
During training (with probability p=0.3):
  For each neuron:
    if random() < p:
      output = 0  (drop neuron)
    else:
      output = input / (1-p)  (scale remaining)

During inference:
  Use all neurons (dropout disabled)
```

**Why Dropout?**
- Prevents overfitting by randomly dropping connections
- Forces network to learn robust features
- Ensemble effect (each iteration trains different sub-network)
- 30% dropout rate is empirically effective

---

## 4. Training Algorithms

### 4.1 Adam Optimizer

**Algorithm**: Adaptive Moment Estimation

**Update Rules**:
```
1. Compute gradient:
   g_t = ∇L(θ_t)

2. Update biased first moment (mean):
   m_t = β₁·m_{t-1} + (1-β₁)·g_t

3. Update biased second moment (variance):
   v_t = β₂·v_{t-1} + (1-β₂)·g_t²

4. Bias correction:
   m̂_t = m_t / (1 - β₁^t)
   v̂_t = v_t / (1 - β₂^t)

5. Parameter update:
   θ_{t+1} = θ_t - α · m̂_t / (√v̂_t + ε)
```

**Hyperparameters**:
- α (learning rate) = 0.001
- β₁ (first moment decay) = 0.9
- β₂ (second moment decay) = 0.999
- ε (numerical stability) = 1e-8

**Why Adam?**
- Adaptive learning rates for each parameter
- Combines benefits of RMSprop and Momentum
- Works well with sparse gradients
- Generally performs well without tuning

---

### 4.2 Backpropagation Algorithm

**Forward Pass**:
```
For layer l = 1 to L:
  z[l] = W[l]·a[l-1] + b[l]
  a[l] = activation(z[l])
```

**Backward Pass** (Chain Rule):
```
For layer l = L to 1:
  1. Compute gradient w.r.t. activation:
     δ[l] = ∂L/∂a[l]
  
  2. Compute gradient w.r.t. pre-activation:
     δz[l] = δ[l] · activation'(z[l])
  
  3. Compute gradients w.r.t. weights and biases:
     ∂L/∂W[l] = δz[l] · a[l-1]^T
     ∂L/∂b[l] = δz[l]
  
  4. Propagate gradient to previous layer:
     δ[l-1] = W[l]^T · δz[l]
```

**Update Weights**:
```
W[l] = W[l] - α · ∂L/∂W[l]
b[l] = b[l] - α · ∂L/∂b[l]
```

---

### 4.3 Training Callbacks

#### Early Stopping
**Algorithm**:
```
Initialize:
  best_loss = ∞
  patience_counter = 0
  patience = 15

For each epoch:
  train_model()
  val_loss = evaluate(validation_data)
  
  if val_loss < best_loss:
    best_loss = val_loss
    save_best_weights()
    patience_counter = 0
  else:
    patience_counter += 1
  
  if patience_counter >= patience:
    print("Early stopping triggered")
    restore_best_weights()
    break
```

**Benefits**:
- Prevents overfitting
- Saves training time
- Automatically finds optimal number of epochs

#### ReduceLROnPlateau
**Algorithm**:
```
Initialize:
  learning_rate = 0.001
  plateau_counter = 0
  patience = 5
  factor = 0.5

For each epoch:
  if val_loss not improved for patience epochs:
    learning_rate = learning_rate * factor
    plateau_counter = 0
    print(f"Reducing LR to {learning_rate}")
```

**Benefits**:
- Helps escape local minima
- Fine-tunes learning in later epochs
- Adaptive learning rate scheduling

---

## 5. Validation & Evaluation

### 5.1 Evaluation Metrics

#### Accuracy
```
Accuracy = (TP + TN) / (TP + TN + FP + FN)

where:
  TP = True Positives (correctly predicted disease)
  TN = True Negatives (correctly predicted no disease)
  FP = False Positives (incorrectly predicted disease)
  FN = False Negatives (missed disease cases)
```

#### Precision (Positive Predictive Value)
```
Precision = TP / (TP + FP)
```
Measures: Of all predicted disease cases, how many actually have disease?

#### Recall (Sensitivity, True Positive Rate)
```
Recall = TP / (TP + FN)
```
Measures: Of all actual disease cases, how many did we detect?

#### F1-Score (Harmonic Mean)
```
F1 = 2 · (Precision · Recall) / (Precision + Recall)
```
Balances precision and recall.

#### ROC-AUC (Receiver Operating Characteristic - Area Under Curve)
```
AUC = ∫₀¹ TPR(FPR⁻¹(x)) dx

where:
  TPR = True Positive Rate = Recall
  FPR = False Positive Rate = FP/(FP+TN)
```

**Interpretation**:
- AUC = 1.0: Perfect classifier
- AUC = 0.9-1.0: Excellent
- AUC = 0.8-0.9: Good
- AUC = 0.7-0.8: Fair
- AUC = 0.5: Random guessing

---

### 5.2 Confusion Matrix

**Structure**:
```
                Predicted
                 0    1
Actual    0    [TN   FP]
          1    [FN   TP]
```

**Example**:
```
                Predicted
                 No   Yes
Actual   No    [150   20]  → Specificity = 150/170 = 88%
         Yes   [10    70]  → Sensitivity = 70/80 = 88%
```

---

### 5.3 Cross-Validation (Optional Advanced)

**K-Fold Cross-Validation Algorithm**:
```
1. Split dataset into K equal folds (K=5 typical)
2. For fold k = 1 to K:
     - Use fold k as validation set
     - Use remaining K-1 folds as training set
     - Train model and evaluate
3. Average performance across all K folds
```

**Benefits**:
- More robust performance estimate
- Uses all data for both training and validation
- Reduces variance in evaluation

---

## 6. Web Application Logic

### 6.1 Prediction Pipeline

**Algorithm**:
```
1. Receive user input (13 features)
   ↓
2. Validate input ranges and types
   ↓
3. Create DataFrame with feature names
   ↓
4. Load preprocessor.pkl
   ↓
5. Transform input:
   - Impute missing (if any)
   - One-hot encode categoricals
   - Standard scale numerics
   ↓
6. Load trained model (.h5 or .pkl)
   ↓
7. Predict probability: ŷ = model.predict(X)
   ↓
8. Apply threshold: prediction = 1 if ŷ > 0.5 else 0
   ↓
9. Calculate risk level:
   - Low: ŷ < 0.3
   - Moderate: 0.3 ≤ ŷ < 0.7
   - High: ŷ ≥ 0.7
   ↓
10. Generate recommendations based on risk factors
    ↓
11. Save to database (if user logged in)
    ↓
12. Return result to user
```

---

### 6.2 Input Validation Algorithm

**Server-Side Validation**:
```python
def validate_input(data):
    validations = {
        'age': (1, 120),
        'resting_bp': (20, 300),
        'cholesterol': (0, 600),
        'max_hr': (50, 220),
        'oldpeak': (0, 10),
        'fasting_bs_gt_120': [0, 1],
        'exercise_angina': [0, 1],
        'smoking': [0, 1],
        'diabetes': [0, 1],
        'family_history': [0, 1],
        'sex': ['male', 'female', 'other'],
        'rest_ecg': ['normal', 'st_abnormality', 'lvh'],
        'st_slope': ['up', 'flat', 'down']
    }
    
    for field, rule in validations.items():
        if field not in data:
            return False, f"Missing field: {field}"
        
        value = data[field]
        
        if isinstance(rule, tuple):  # Numeric range
            if not (rule[0] <= value <= rule[1]):
                return False, f"{field} out of range"
        
        elif isinstance(rule, list):  # Allowed values
            if value not in rule:
                return False, f"Invalid {field} value"
    
    return True, "Valid"
```

---

### 6.3 Risk Stratification Algorithm

**Algorithm**:
```python
def calculate_risk_level(probability, features):
    """
    Stratify risk based on probability and feature analysis
    """
    # Base risk from model prediction
    if probability < 0.3:
        risk = "Low"
        color = "green"
    elif probability < 0.7:
        risk = "Moderate"
        color = "orange"
    else:
        risk = "High"
        color = "red"
    
    # Risk factors check
    high_risk_factors = 0
    
    if features['age'] > 60:
        high_risk_factors += 1
    if features['resting_bp'] > 140:
        high_risk_factors += 1
    if features['cholesterol'] > 240:
        high_risk_factors += 1
    if features['diabetes'] == 1:
        high_risk_factors += 1
    if features['smoking'] == 1:
        high_risk_factors += 1
    if features['family_history'] == 1:
        high_risk_factors += 1
    
    # Adjust risk if multiple high-risk factors present
    if high_risk_factors >= 3 and risk == "Low":
        risk = "Moderate"
    
    return risk, probability, high_risk_factors
```

---

### 6.4 Database Operations

**SQL Schema**:
```sql
-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- Predictions table
CREATE TABLE predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    risk_probability REAL,
    prediction INTEGER,
    input_features TEXT,  -- JSON string
    timestamp TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

**Insert Prediction**:
```python
def save_prediction(user_id, probability, prediction, features):
    conn = sqlite3.connect('predictions.sqlite')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO predictions 
        (user_id, risk_probability, prediction, input_features, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        user_id,
        float(probability),
        int(prediction),
        json.dumps(features),
        datetime.now().isoformat()
    ))
    
    conn.commit()
    prediction_id = cursor.lastrowid
    conn.close()
    
    return prediction_id
```

---

## 7. Performance Optimization Techniques

### 7.1 Model Loading (Lazy Loading)
```python
# Global variables
MODEL = None
PREPROCESSOR = None

def get_model():
    global MODEL
    if MODEL is None:
        MODEL = load_latest_model()
    return MODEL

def get_preprocessor():
    global PREPROCESSOR
    if PREPROCESSOR is None:
        PREPROCESSOR = joblib.load('preprocessor.pkl')
    return PREPROCESSOR
```

**Benefits**:
- Loads model only once (on first prediction)
- Reduces memory usage
- Faster subsequent predictions

---

### 7.2 Batch Prediction
```python
def batch_predict(features_list):
    """
    Predict for multiple inputs at once
    More efficient than loop
    """
    preprocessor = get_preprocessor()
    model = get_model()
    
    # Stack all inputs
    X = preprocessor.transform(features_list)
    
    # Single batch prediction
    predictions = model.predict(X)
    
    return predictions
```

---

## 8. Summary of Key Algorithms

| Component | Algorithm/Technique | Purpose |
|-----------|-------------------|---------|
| **Classification** | Multi-Layer Perceptron (MLP) | Binary classification of heart disease risk |
| **Encoding** | One-Hot Encoding | Convert categorical features to numeric |
| **Scaling** | Standard Scaling (Z-score) | Normalize numeric features |
| **Optimization** | Adam Optimizer | Update neural network weights |
| **Activation** | ReLU (hidden), Sigmoid (output) | Non-linear transformations |
| **Regularization** | Dropout + Batch Normalization | Prevent overfitting |
| **Training** | Backpropagation + Gradient Descent | Learn optimal weights |
| **Evaluation** | Accuracy, Precision, Recall, AUC | Measure model performance |
| **Validation** | Train-Test Split (Stratified) | Unbiased performance estimate |
| **Callbacks** | Early Stopping, LR Scheduling | Optimize training process |
| **Data Imputation** | Median (numeric), Mode (categorical) | Handle missing values |
| **Loss Function** | Binary Cross-Entropy | Measure prediction error |

---

## 9. Mathematical Complexity

### Time Complexity

**Training (per epoch)**:
```
O(n · d · h)

where:
  n = number of training samples
  d = input dimension (13 features)
  h = hidden layer sizes (128 + 64 + 32)
```

**Prediction (single sample)**:
```
O(d · h) = O(13 · 224) ≈ O(3000) operations
Very fast (~1ms per prediction)
```

**Preprocessing**:
```
O(n · d) for scaling
O(n · c) for one-hot encoding (c = number of categories)
```

---

## 10. References & Further Reading

### Academic Papers
1. **Multilayer Perceptron**: Rumelhart et al. (1986) - "Learning representations by back-propagating errors"
2. **Adam Optimizer**: Kingma & Ba (2014) - "Adam: A Method for Stochastic Optimization"
3. **Batch Normalization**: Ioffe & Szegedy (2015) - "Batch Normalization: Accelerating Deep Network Training"
4. **Dropout**: Srivastava et al. (2014) - "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"

### Implementations
- TensorFlow/Keras: https://www.tensorflow.org/
- Scikit-learn: https://scikit-learn.org/
- NumPy: https://numpy.org/

### Datasets
- UCI Heart Disease Dataset
- Kaggle Heart Failure Prediction Dataset

---

**Document Version**: 1.0  
**Last Updated**: November 2025  
**Author**: HeartCheck DL Development Team  

---

## Appendix: Complete Pipeline Flowchart

```
┌─────────────────────────────────────────────────────────────┐
│                    RAW DATA INPUT                            │
│  CSV file with 918 rows × 12 columns                        │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│               DATA CLEANING & VALIDATION                     │
│  - Remove duplicates                                         │
│  - Handle missing values (median/mode imputation)            │
│  - Validate ranges (age: 1-120, BP: 20-300, etc.)          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              FEATURE ENGINEERING                             │
│  Numeric: age, resting_bp, cholesterol, max_hr, oldpeak    │
│  Categorical: sex, rest_ecg, st_slope                       │
│  Binary: fasting_bs, exercise_angina, smoking, diabetes    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│           PREPROCESSING PIPELINE                             │
│  ┌──────────────────┐     ┌───────────────────┐            │
│  │ Numeric Features │     │ Categorical Feats │            │
│  │  ↓ SimpleImputer │     │  ↓ SimpleImputer  │            │
│  │  ↓ StandardScaler│     │  ↓ OneHotEncoder  │            │
│  └──────────────────┘     └───────────────────┘            │
│           ↓                          ↓                       │
│           └──────────┬───────────────┘                      │
│                      ↓                                       │
│          ColumnTransformer (combined)                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│          TRAIN-TEST SPLIT (Stratified)                      │
│  Train: 80% (734 samples)                                   │
│  Test:  20% (184 samples)                                   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              MLP MODEL ARCHITECTURE                          │
│  Input(13) → Dense(128)+BN+Dropout → Dense(64)+BN+Dropout  │
│  → Dense(32)+BN+Dropout → Dense(1, sigmoid)                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              TRAINING PROCESS                                │
│  Optimizer: Adam (lr=0.001)                                 │
│  Loss: Binary Crossentropy                                  │
│  Metrics: Accuracy, AUC                                     │
│  Callbacks: EarlyStopping, ModelCheckpoint, ReduceLR        │
│  Epochs: Up to 100 (with early stopping)                   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              MODEL EVALUATION                                │
│  - Accuracy: 85-90%                                         │
│  - AUC-ROC: 0.88-0.92                                       │
│  - Precision/Recall/F1-Score                                │
│  - Confusion Matrix                                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│           SAVE MODEL & ARTIFACTS                             │
│  - heart_dl_model_YYYYMMDD_HHMMSS.h5                       │
│  - preprocessor.pkl                                         │
│  - history_YYYYMMDD_HHMMSS.json                            │
│  - registry.json (model versioning)                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              FLASK WEB APPLICATION                           │
│  User Input → Validation → Preprocessing → Prediction      │
│  → Risk Stratification → Results Display → DB Logging      │
└─────────────────────────────────────────────────────────────┘
```

---

**End of Algorithms Documentation**
