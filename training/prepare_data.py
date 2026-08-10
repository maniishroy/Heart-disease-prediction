"""
HeartCheck DL - Data Preparation Script
Loads raw data, cleans, encodes categoricals, normalizes numerics, and saves preprocessor
"""

import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data'
MODELS_DIR = BASE_DIR / 'models'

def load_raw_data(input_path):
    """Load raw CSV data"""
    print(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} rows, {len(df.columns)} columns")
    print(f"Columns: {df.columns.tolist()}")
    return df

def clean_and_prepare(df):
    """
    Clean and prepare dataset
    
    Assumes columns similar to:
    - Age, Sex, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, 
      ExerciseAngina, Oldpeak, ST_Slope, HeartDisease (target)
    
    Adjust column names based on actual dataset
    """
    print("\nCleaning data...")
    
    # Standardize column names (lowercase, underscore)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Common column name mappings
    rename_map = {
        'restingbp': 'resting_bp',
        'fastingbs': 'fasting_bs_gt_120',
        'restingecg': 'rest_ecg',
        'maxhr': 'max_hr',
        'exerciseangina': 'exercise_angina',
        'st_slope': 'st_slope',
        'heartdisease': 'target'
    }
    df.rename(columns=rename_map, inplace=True)
    
    # Handle missing values
    print(f"Missing values before cleaning:\n{df.isnull().sum()}")
    
    # Drop rows with critical missing values
    df.dropna(subset=['age', 'resting_bp', 'cholesterol'], inplace=True)
    
    # Fill other missing with median/mode
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().any():
            df[col].fillna(df[col].median(), inplace=True)
    
    for col in df.select_dtypes(include=[object]).columns:
        if df[col].isnull().any():
            df[col].fillna(df[col].mode()[0], inplace=True)
    
    print(f"Missing values after cleaning:\n{df.isnull().sum()}")
    print(f"Final shape: {df.shape}")
    
    return df

def encode_and_normalize(df, target_col='target'):
    """
    Encode categorical variables and normalize numeric features
    Returns: X_train, X_test, y_train, y_test, preprocessor
    """
    print("\nEncoding and normalizing features...")
    
    # Separate features and target
    if target_col in df.columns:
        y = df[target_col]
        X = df.drop(columns=[target_col])
    else:
        print(f"WARNING: Target column '{target_col}' not found. Using placeholder.")
        y = np.zeros(len(df))
        X = df
    
    # Identify numeric and categorical columns
    numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = X.select_dtypes(include=[object]).columns.tolist()
    
    print(f"Numeric features: {numeric_features}")
    print(f"Categorical features: {categorical_features}")
    
    # Create preprocessor pipeline
    from sklearn.pipeline import Pipeline
    from sklearn.impute import SimpleImputer
    
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y if len(np.unique(y)) > 1 else None
    )
    
    print(f"\nTrain set: {X_train.shape}, Test set: {X_test.shape}")
    
    # Fit and transform
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    
    print(f"Processed shape: {X_train_processed.shape}")
    
    return X_train_processed, X_test_processed, y_train, y_test, preprocessor

def save_processed_data(X_train, X_test, y_train, y_test, preprocessor):
    """Save processed data and preprocessor"""
    MODELS_DIR.mkdir(exist_ok=True)
    processed_dir = DATA_DIR / 'processed'
    processed_dir.mkdir(exist_ok=True)
    
    # Save preprocessor
    preprocessor_path = MODELS_DIR / 'preprocessor.pkl'
    joblib.dump(preprocessor, preprocessor_path)
    print(f"\n✓ Saved preprocessor to: {preprocessor_path}")
    
    # Save processed arrays
    np.save(processed_dir / 'X_train.npy', X_train)
    np.save(processed_dir / 'X_test.npy', X_test)
    np.save(processed_dir / 'y_train.npy', y_train)
    np.save(processed_dir / 'y_test.npy', y_test)
    print(f"✓ Saved processed data to: {processed_dir}")
    
    # Create a simple processed CSV for inspection
    processed_df = pd.DataFrame(X_train[:1000])  # Sample for inspection
    processed_df['target'] = y_train[:1000]
    processed_df.to_csv(processed_dir / 'processed_sample.csv', index=False)
    print(f"✓ Saved sample processed CSV")

def main():
    parser = argparse.ArgumentParser(description='Prepare and preprocess heart disease data')
    parser.add_argument('--input', '-i',
                       default='data/raw/heart.csv',
                       help='Input raw CSV file')
    parser.add_argument('--target', '-t',
                       default='target',
                       help='Target column name')
    
    args = parser.parse_args()
    
    print("="*60)
    print("HeartCheck DL - Data Preparation")
    print("="*60)
    
    input_path = BASE_DIR / args.input
    if not input_path.exists():
        print(f"\nERROR: Input file not found: {input_path}")
        print("\nAvailable files in data/raw/:")
        for file in (DATA_DIR / 'raw').glob('*.csv'):
            print(f"  - {file.name}")
        return
    
    # Load and clean
    df = load_raw_data(input_path)
    df_clean = clean_and_prepare(df)
    
    # Encode and normalize
    X_train, X_test, y_train, y_test, preprocessor = encode_and_normalize(df_clean, args.target)
    
    # Save
    save_processed_data(X_train, X_test, y_train, y_test, preprocessor)
    
    print("\n" + "="*60)
    print("✓ Data preparation complete!")
    print("="*60)
    print("\nNext step:")
    print("  python training/train_dl.py")

if __name__ == '__main__':
    main()
