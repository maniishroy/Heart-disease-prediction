"""
Advanced High-Accuracy Heart Disease Prediction Model
Target: >99% accuracy using ensemble methods and feature engineering
"""

import pandas as pd
import numpy as np
from pathlib import Path
import joblib
import json
from datetime import datetime
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import warnings
warnings.filterwarnings('ignore')

def load_and_prepare_data():
    """Load and prepare the combined dataset"""
    print("=" * 70)
    print("LOADING DATA")
    print("=" * 70)
    
    data_path = Path(__file__).parent.parent / "data" / "raw" / "combined_heart_disease.csv"
    
    if not data_path.exists():
        print(f"⚠ Dataset not found at {data_path}")
        print("Run: python training/download_multiple_datasets.py first")
        return None, None, None, None
    
    df = pd.read_csv(data_path)
    print(f"✓ Loaded {len(df):,} records")
    print(f"  Shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    
    return df

def advanced_feature_engineering(df):
    """Create advanced features for better accuracy"""
    print("\n" + "=" * 70)
    print("FEATURE ENGINEERING")
    print("=" * 70)
    
    df = df.copy()
    
    # Handle different column name variations
    col_mapping = {
        'age': 'Age',
        'sex': 'Sex',
        'cp': 'ChestPainType',
        'trestbps': 'RestingBP',
        'chol': 'Cholesterol',
        'fbs': 'FastingBS',
        'restecg': 'RestingECG',
        'thalach': 'MaxHR',
        'exang': 'ExerciseAngina',
        'oldpeak': 'Oldpeak',
        'slope': 'ST_Slope',
        'target': 'HeartDisease',
        'output': 'HeartDisease',
        'num': 'HeartDisease'
    }
    
    df.rename(columns={k: v for k, v in col_mapping.items() if k in df.columns}, inplace=True)
    
    # Standardize column names (lowercase)
    df.columns = df.columns.str.lower()
    
    # Ensure target column
    if 'heartdisease' not in df.columns:
        if 'target' in df.columns:
            df['heartdisease'] = df['target']
        elif 'output' in df.columns:
            df['heartdisease'] = df['output']
        elif 'num' in df.columns:
            df['heartdisease'] = (df['num'] > 0).astype(int)
    
    # Convert binary target
    if df['heartdisease'].max() > 1:
        df['heartdisease'] = (df['heartdisease'] > 0).astype(int)
    
    print(f"\n✓ Standardized columns: {list(df.columns)}")
    print(f"✓ Target distribution: {df['heartdisease'].value_counts().to_dict()}")
    
    # Feature engineering
    print("\nCreating engineered features...")
    
    # Age-based features
    if 'age' in df.columns:
        df['age_group'] = pd.cut(df['age'], bins=[0, 40, 55, 70, 120], labels=[0, 1, 2, 3])
        df['age_squared'] = df['age'] ** 2
        print("  ✓ Age features")
    
    # Blood pressure features
    if 'restingbp' in df.columns:
        df['bp_category'] = pd.cut(df['restingbp'], bins=[0, 120, 140, 180, 300], labels=[0, 1, 2, 3])
        df['high_bp'] = (df['restingbp'] > 140).astype(int)
        print("  ✓ BP features")
    
    # Cholesterol features
    if 'cholesterol' in df.columns:
        # Handle zero cholesterol (missing values)
        df['cholesterol'] = df['cholesterol'].replace(0, df['cholesterol'][df['cholesterol'] > 0].median())
        df['high_chol'] = (df['cholesterol'] > 240).astype(int)
        df['chol_category'] = pd.cut(df['cholesterol'], bins=[0, 200, 240, 300, 600], labels=[0, 1, 2, 3])
        print("  ✓ Cholesterol features")
    
    # Heart rate features
    if 'maxhr' in df.columns:
        df['hr_reserve'] = 220 - df['age'] - df['maxhr'] if 'age' in df.columns else 0
        df['low_max_hr'] = (df['maxhr'] < 120).astype(int)
        print("  ✓ Heart rate features")
    
    # Interaction features
    if 'age' in df.columns and 'cholesterol' in df.columns:
        df['age_chol_interaction'] = df['age'] * df['cholesterol'] / 1000
        print("  ✓ Interaction features")
    
    if 'age' in df.columns and 'maxhr' in df.columns:
        df['age_hr_ratio'] = df['age'] / (df['maxhr'] + 1)
        print("  ✓ Age-HR ratio")
    
    # Risk score (composite feature)
    risk_score = 0
    if 'age' in df.columns:
        risk_score += (df['age'] > 60).astype(int)
    if 'cholesterol' in df.columns:
        risk_score += (df['cholesterol'] > 240).astype(int)
    if 'restingbp' in df.columns:
        risk_score += (df['restingbp'] > 140).astype(int)
    if 'fastingbs' in df.columns:
        risk_score += df['fastingbs']
    if 'exerciseangina' in df.columns:
        if df['exerciseangina'].dtype == 'object':
            risk_score += (df['exerciseangina'] == 'Y').astype(int)
        else:
            risk_score += df['exerciseangina']
    
    df['risk_score'] = risk_score
    print("  ✓ Composite risk score")
    
    print(f"\n✓ Total features: {len(df.columns)}")
    
    return df

def prepare_features(df):
    """Prepare features for training"""
    print("\n" + "=" * 70)
    print("PREPARING FEATURES")
    print("=" * 70)
    
    # Separate features and target
    y = df['heartdisease']
    X = df.drop('heartdisease', axis=1)
    
    # Encode categorical features
    le = LabelEncoder()
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    
    print(f"\nEncoding {len(categorical_cols)} categorical columns:")
    for col in categorical_cols:
        print(f"  - {col}: {X[col].nunique()} unique values")
        X[col] = le.fit_transform(X[col].astype(str))
    
    # Handle missing values (only for numeric columns)
    numeric_cols = X.select_dtypes(include=[np.number]).columns
    X[numeric_cols] = X[numeric_cols].fillna(X[numeric_cols].median())
    
    print(f"\n✓ Final feature shape: {X.shape}")
    print(f"✓ Target shape: {y.shape}")
    print(f"✓ Target distribution: {y.value_counts().to_dict()}")
    
    return X, y

def train_super_ensemble(X_train, X_test, y_train, y_test):
    """Train super ensemble for maximum accuracy"""
    print("\n" + "=" * 70)
    print("TRAINING SUPER ENSEMBLE")
    print("=" * 70)
    
    # Individual models with optimized hyperparameters
    models = {
        'XGBoost': XGBClassifier(
            n_estimators=500,
            max_depth=7,
            learning_rate=0.01,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            eval_metric='logloss'
        ),
        'LightGBM': LGBMClassifier(
            n_estimators=500,
            max_depth=7,
            learning_rate=0.01,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            verbose=-1
        ),
        'RandomForest': RandomForestClassifier(
            n_estimators=300,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        ),
        'GradientBoosting': GradientBoostingClassifier(
            n_estimators=300,
            max_depth=5,
            learning_rate=0.01,
            random_state=42
        )
    }
    
    trained_models = {}
    
    print("\nTraining individual models:")
    for name, model in models.items():
        print(f"\n{name}:")
        print(f"  Training...")
        model.fit(X_train, y_train)
        
        y_pred_train = model.predict(X_train)
        y_pred_test = model.predict(X_test)
        
        train_acc = accuracy_score(y_train, y_pred_train)
        test_acc = accuracy_score(y_test, y_pred_test)
        
        print(f"  Train Accuracy: {train_acc:.4f} ({train_acc*100:.2f}%)")
        print(f"  Test Accuracy:  {test_acc:.4f} ({test_acc*100:.2f}%)")
        
        # Cross-validation
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        cv_scores = cross_val_score(model, X_train, y_train, cv=cv, scoring='accuracy', n_jobs=-1)
        print(f"  CV Accuracy:    {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")
        
        trained_models[name] = {
            'model': model,
            'train_acc': train_acc,
            'test_acc': test_acc,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std()
        }
    
    # Create voting ensemble
    print("\n" + "-" * 70)
    print("VOTING ENSEMBLE")
    print("-" * 70)
    
    voting_clf = VotingClassifier(
        estimators=[(name, info['model']) for name, info in trained_models.items()],
        voting='soft',
        n_jobs=-1
    )
    
    print("\nTraining voting ensemble...")
    voting_clf.fit(X_train, y_train)
    
    y_pred_train = voting_clf.predict(X_train)
    y_pred_test = voting_clf.predict(X_test)
    y_pred_proba = voting_clf.predict_proba(X_test)[:, 1]
    
    train_acc = accuracy_score(y_train, y_pred_train)
    test_acc = accuracy_score(y_test, y_pred_test)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    print(f"\n{'='*70}")
    print("FINAL ENSEMBLE RESULTS")
    print('='*70)
    print(f"Train Accuracy: {train_acc:.4f} ({train_acc*100:.2f}%)")
    print(f"Test Accuracy:  {test_acc:.4f} ({test_acc*100:.2f}%)")
    print(f"ROC-AUC Score:  {roc_auc:.4f}")
    
    print(f"\n{'-'*70}")
    print("Classification Report:")
    print('-'*70)
    print(classification_report(y_test, y_pred_test, target_names=['No Disease', 'Heart Disease']))
    
    print(f"\n{'-'*70}")
    print("Confusion Matrix:")
    print('-'*70)
    cm = confusion_matrix(y_test, y_pred_test)
    print(cm)
    print(f"\nTrue Negatives:  {cm[0, 0]}")
    print(f"False Positives: {cm[0, 1]}")
    print(f"False Negatives: {cm[1, 0]}")
    print(f"True Positives:  {cm[1, 1]}")
    
    return voting_clf, {
        'train_accuracy': train_acc,
        'test_accuracy': test_acc,
        'roc_auc': roc_auc,
        'confusion_matrix': cm.tolist(),
        'individual_models': {name: info['test_acc'] for name, info in trained_models.items()}
    }

def save_model(model, scaler, feature_names, metrics):
    """Save trained model and metadata"""
    print("\n" + "=" * 70)
    print("SAVING MODEL")
    print("=" * 70)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    models_dir = Path(__file__).parent.parent / "models"
    models_dir.mkdir(exist_ok=True)
    
    # Save model
    model_path = models_dir / f"heart_super_ensemble_{timestamp}.pkl"
    joblib.dump(model, model_path)
    print(f"✓ Model saved: {model_path}")
    
    # Save scaler
    scaler_path = models_dir / f"scaler_{timestamp}.pkl"
    joblib.dump(scaler, scaler_path)
    print(f"✓ Scaler saved: {scaler_path}")
    
    # Save metadata
    metadata = {
        'timestamp': timestamp,
        'model_type': 'super_ensemble',
        'model_file': model_path.name,
        'scaler_file': scaler_path.name,
        'feature_names': feature_names,
        'metrics': metrics,
        'target_accuracy': '>99%',
        'training_date': datetime.now().isoformat()
    }
    
    metadata_path = models_dir / f"heart_super_ensemble_{timestamp}_metadata.json"
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"✓ Metadata saved: {metadata_path}")
    
    # Update registry
    registry_path = models_dir / "registry.json"
    if registry_path.exists():
        with open(registry_path, 'r') as f:
            registry = json.load(f)
    else:
        registry = {'models': []}
    
    registry['models'].insert(0, metadata)
    registry['latest'] = metadata
    
    with open(registry_path, 'w') as f:
        json.dump(registry, f, indent=2)
    print(f"✓ Registry updated: {registry_path}")
    
    return model_path

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("HIGH-ACCURACY HEART DISEASE PREDICTION MODEL TRAINING")
    print("Target: >99% Accuracy")
    print("=" * 70)
    
    # Load data
    df = load_and_prepare_data()
    if df is None:
        sys.exit(1)
    
    # Feature engineering
    df = advanced_feature_engineering(df)
    
    # Prepare features
    X, y = prepare_features(df)
    
    # Split data
    print("\n" + "=" * 70)
    print("SPLITTING DATA")
    print("=" * 70)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Train set: {X_train.shape[0]:,} samples")
    print(f"Test set:  {X_test.shape[0]:,} samples")
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model, metrics = train_super_ensemble(X_train_scaled, X_test_scaled, y_train, y_test)
    
    # Save model
    model_path = save_model(model, scaler, list(X.columns), metrics)
    
    print("\n" + "=" * 70)
    print("TRAINING COMPLETE!")
    print("=" * 70)
    print(f"\nFinal Test Accuracy: {metrics['test_accuracy']*100:.2f}%")
    print(f"Model saved to: {model_path}")
    print("\nNext step: Run the Flask app to use the model")
    print("  flask run --host=0.0.0.0 --port=5000")
    print("=" * 70 + "\n")
