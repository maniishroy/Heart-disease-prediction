"""
Advanced Deep Learning Model for Heart Disease Prediction
Target: 99%+ accuracy using ensemble methods and hyperparameter tuning
"""

import os
import json
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path
import joblib

# Scikit-learn imports
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.ensemble import (
    RandomForestClassifier, 
    GradientBoostingClassifier, 
    AdaBoostClassifier,
    VotingClassifier,
    StackingClassifier
)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    roc_auc_score,
    confusion_matrix,
    classification_report
)

# XGBoost and LightGBM for state-of-the-art gradient boosting
try:
    import xgboost as xgb
    HAS_XGB = True
except ImportError:
    HAS_XGB = False
    print("XGBoost not installed. Install with: pip install xgboost")

try:
    import lightgbm as lgb
    HAS_LGB = True
except ImportError:
    HAS_LGB = False
    print("LightGBM not installed. Install with: pip install lightgbm")

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data' / 'processed'
MODELS_DIR = BASE_DIR / 'models'
MODELS_DIR.mkdir(exist_ok=True)

def load_processed_data():
    """Load preprocessed dataset"""
    csv_path = DATA_DIR / 'processed.csv'
    if not csv_path.exists():
        # Use sample data if processed not available
        csv_path = BASE_DIR / 'data' / 'raw' / 'sample.csv'
    
    df = pd.read_csv(csv_path)
    
    # Encode categorical variables
    categorical_mappings = {}
    
    if 'Sex' in df.columns:
        df['Sex'] = df['Sex'].map({'male': 1, 'female': 0, 'Male': 1, 'Female': 0})
        categorical_mappings['Sex'] = {'male': 1, 'female': 0}
    
    if 'ChestPainType' in df.columns:
        pain_map = {'ATA': 0, 'NAP': 1, 'ASY': 2, 'TA': 3}
        df['ChestPainType'] = df['ChestPainType'].map(pain_map)
    
    if 'RestingECG' in df.columns:
        ecg_map = {'Normal': 0, 'ST': 1, 'LVH': 2, 'normal': 0, 'ST-T wave abnormality': 1, 'left ventricular hypertrophy': 2}
        df['RestingECG'] = df['RestingECG'].map(ecg_map)
    
    if 'ExerciseAngina' in df.columns:
        df['ExerciseAngina'] = df['ExerciseAngina'].map({'N': 0, 'Y': 1, 'No': 0, 'Yes': 1})
    
    if 'ST_Slope' in df.columns:
        slope_map = {'Up': 0, 'Flat': 1, 'Down': 2, 'up': 0, 'flat': 1, 'down': 2}
        df['ST_Slope'] = df['ST_Slope'].map(slope_map)
    
    # Convert boolean columns
    bool_cols = ['FastingBS', 'Smoking', 'Diabetes', 'FamilyHistory']
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].astype(int)
    
    # Separate features and target
    if 'target' in df.columns:
        X = df.drop('target', axis=1)
        y = df['target']
    elif 'HeartDisease' in df.columns:
        X = df.drop('HeartDisease', axis=1)
        y = df['HeartDisease']
    else:
        raise ValueError("Target column not found (expected 'target' or 'HeartDisease')")
    
    return X, y

def create_advanced_features(X):
    """Feature engineering to boost accuracy"""
    X = X.copy()
    
    # Interaction features
    if 'Age' in X.columns and 'MaxHR' in X.columns:
        # Replace zeros to avoid division by zero
        max_hr_safe = X['MaxHR'].replace(0, 1)
        X['Age_HR_ratio'] = X['Age'] / max_hr_safe
    
    if 'RestingBP' in X.columns and 'Cholesterol' in X.columns:
        # Replace zeros
        chol_safe = X['Cholesterol'].replace(0, 1)
        X['BP_Chol_product'] = X['RestingBP'] * chol_safe / 10000
    
    if 'Age' in X.columns and 'Cholesterol' in X.columns:
        chol_safe = X['Cholesterol'].replace(0, 1)
        X['Age_Chol_interaction'] = X['Age'] * chol_safe / 1000
    
    # Polynomial features for key vitals
    if 'Oldpeak' in X.columns:
        X['Oldpeak_squared'] = X['Oldpeak'] ** 2
    
    if 'RestingBP' in X.columns:
        X['BP_risk'] = (X['RestingBP'] > 140).astype(int)
    
    if 'Cholesterol' in X.columns:
        chol_safe = X['Cholesterol'].replace(0, 200)  # Replace zero with normal value
        X['Chol_risk'] = (chol_safe > 240).astype(int)
    
    # Fill any remaining NaN values with column mean
    X = X.fillna(X.mean())
    
    return X

def build_ensemble_model():
    """
    Build advanced ensemble model using stacking and voting
    Target: 99%+ accuracy
    """
    
    # Base models with optimized hyperparameters
    base_models = []
    
    # 1. Random Forest with deep trees
    rf = RandomForestClassifier(
        n_estimators=500,
        max_depth=20,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features='sqrt',
        bootstrap=True,
        class_weight='balanced',
        random_state=42,
        n_jobs=-1
    )
    base_models.append(('rf', rf))
    
    # 2. Gradient Boosting
    gb = GradientBoostingClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=7,
        min_samples_split=3,
        min_samples_leaf=2,
        subsample=0.9,
        random_state=42
    )
    base_models.append(('gb', gb))
    
    # 3. XGBoost (if available)
    if HAS_XGB:
        xgb_model = xgb.XGBClassifier(
            n_estimators=500,
            learning_rate=0.03,
            max_depth=8,
            min_child_weight=1,
            gamma=0,
            subsample=0.9,
            colsample_bytree=0.9,
            reg_alpha=0.1,
            reg_lambda=1,
            scale_pos_weight=1,
            random_state=42,
            use_label_encoder=False,
            eval_metric='logloss'
        )
        base_models.append(('xgb', xgb_model))
    
    # 4. LightGBM (if available)
    if HAS_LGB:
        lgb_model = lgb.LGBMClassifier(
            n_estimators=500,
            learning_rate=0.03,
            max_depth=8,
            num_leaves=31,
            min_child_samples=20,
            subsample=0.9,
            colsample_bytree=0.9,
            reg_alpha=0.1,
            reg_lambda=1,
            random_state=42,
            verbose=-1
        )
        base_models.append(('lgb', lgb_model))
    
    # 5. Support Vector Machine
    svm = SVC(
        kernel='rbf',
        C=10,
        gamma='scale',
        probability=True,
        class_weight='balanced',
        random_state=42
    )
    base_models.append(('svm', svm))
    
    # 6. Neural Network
    mlp = MLPClassifier(
        hidden_layer_sizes=(128, 64, 32),
        activation='relu',
        solver='adam',
        alpha=0.001,
        learning_rate='adaptive',
        max_iter=1000,
        random_state=42,
        early_stopping=True,
        validation_fraction=0.1
    )
    base_models.append(('mlp', mlp))
    
    # 7. AdaBoost
    ada = AdaBoostClassifier(
        n_estimators=200,
        learning_rate=0.5,
        random_state=42
    )
    base_models.append(('ada', ada))
    
    # Meta-model: Logistic Regression with stronger regularization
    meta_model = LogisticRegression(
        C=0.1,
        max_iter=2000,
        class_weight='balanced',
        random_state=42
    )
    
    # Create stacking ensemble
    stacking_model = StackingClassifier(
        estimators=base_models,
        final_estimator=meta_model,
        cv=5,
        n_jobs=-1
    )
    
    return stacking_model

def train_and_evaluate():
    """Main training pipeline with cross-validation"""
    
    print("="*70)
    print("ADVANCED HEART DISEASE PREDICTION MODEL TRAINING")
    print("Target: 99%+ Accuracy")
    print("="*70)
    
    # Load data
    print("\n[1/6] Loading data...")
    X, y = load_processed_data()
    print(f"   Dataset shape: {X.shape}")
    print(f"   Positive class ratio: {y.mean():.2%}")
    
    # Feature engineering
    print("\n[2/6] Creating advanced features...")
    X_enhanced = create_advanced_features(X)
    print(f"   Enhanced features: {X_enhanced.shape[1]} (added {X_enhanced.shape[1] - X.shape[1]} new features)")
    
    # Split data
    print("\n[3/6] Splitting data (80/20 train/test)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_enhanced, y, 
        test_size=0.2, 
        random_state=42, 
        stratify=y
    )
    
    # Scale features using RobustScaler (better for outliers)
    print("\n[4/6] Scaling features...")
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Build and train model
    print("\n[5/6] Building and training ensemble model...")
    print("   This may take several minutes...")
    model = build_ensemble_model()
    
    # Cross-validation on training set
    print("\n   Performing 5-fold cross-validation...")
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy', n_jobs=-1)
    print(f"   CV Accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
    
    # Train on full training set
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    print("\n[6/6] Evaluating model...")
    
    # Training metrics
    y_train_pred = model.predict(X_train_scaled)
    train_acc = accuracy_score(y_train, y_train_pred)
    
    # Test metrics
    y_test_pred = model.predict(X_test_scaled)
    y_test_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    test_acc = accuracy_score(y_test, y_test_pred)
    test_precision = precision_score(y_test, y_test_pred, zero_division=0)
    test_recall = recall_score(y_test, y_test_pred, zero_division=0)
    test_f1 = f1_score(y_test, y_test_pred, zero_division=0)
    test_auc = roc_auc_score(y_test, y_test_proba)
    
    print("\n" + "="*70)
    print("TRAINING RESULTS")
    print("="*70)
    print(f"Training Accuracy:   {train_acc:.4f} ({train_acc*100:.2f}%)")
    print(f"Test Accuracy:       {test_acc:.4f} ({test_acc*100:.2f}%)")
    print(f"Precision:           {test_precision:.4f}")
    print(f"Recall:              {test_recall:.4f}")
    print(f"F1 Score:            {test_f1:.4f}")
    print(f"AUC-ROC:             {test_auc:.4f}")
    print("="*70)
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_test_pred)
    print("\nConfusion Matrix:")
    print(f"   TN: {cm[0,0]:4d}  |  FP: {cm[0,1]:4d}")
    print(f"   FN: {cm[1,0]:4d}  |  TP: {cm[1,1]:4d}")
    
    # Classification report
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_test_pred, target_names=['No Disease', 'Disease']))
    
    # Save model and scaler
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    model_name = f'heart_advanced_ensemble_{timestamp}'
    
    print(f"\n[SAVING] Model: {model_name}")
    joblib.dump(model, MODELS_DIR / f'{model_name}.pkl')
    joblib.dump(scaler, MODELS_DIR / f'scaler_{timestamp}.pkl')
    
    # Save metadata
    metadata = {
        'model_name': model_name,
        'timestamp': timestamp,
        'train_accuracy': float(train_acc),
        'test_accuracy': float(test_acc),
        'precision': float(test_precision),
        'recall': float(test_recall),
        'f1_score': float(test_f1),
        'auc_roc': float(test_auc),
        'cv_mean': float(cv_scores.mean()),
        'cv_std': float(cv_scores.std()),
        'n_features': int(X_enhanced.shape[1]),
        'feature_names': list(X_enhanced.columns),
        'model_type': 'StackingEnsemble',
        'base_models': [name for name, _ in model.estimators],
        'dataset_shape': list(X.shape),
        'test_size': int(len(y_test)),
        'notes': 'Advanced ensemble with XGBoost, LightGBM, SVM, MLP, and meta-learner'
    }
    
    with open(MODELS_DIR / f'{model_name}_metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    # Update registry
    registry_path = MODELS_DIR / 'registry.json'
    if registry_path.exists():
        with open(registry_path, 'r') as f:
            registry = json.load(f)
    else:
        registry = {'models': []}
    
    registry['models'].insert(0, metadata)
    registry['latest'] = model_name
    
    with open(registry_path, 'w') as f:
        json.dump(registry, f, indent=2)
    
    print(f"\n✓ Model saved to: {MODELS_DIR / model_name}.pkl")
    print(f"✓ Scaler saved to: {MODELS_DIR / f'scaler_{timestamp}.pkl'}")
    print(f"✓ Metadata saved to: {MODELS_DIR / f'{model_name}_metadata.json'}")
    print(f"✓ Registry updated")
    
    if test_acc >= 0.99:
        print("\n" + "="*70)
        print("🎯 TARGET ACHIEVED: 99%+ ACCURACY!")
        print("="*70)
    else:
        print(f"\n⚠️  Current accuracy: {test_acc*100:.2f}% (target: 99.00%)")
        print("   Consider: more data, hyperparameter tuning, or different features")
    
    return model, scaler, metadata

if __name__ == '__main__':
    model, scaler, metadata = train_and_evaluate()
