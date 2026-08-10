"""
Generate synthetic heart disease dataset for training
Based on real heart disease correlations and distributions
"""

import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

def generate_heart_disease_dataset(n_samples=1000):
    """Generate realistic synthetic heart disease data"""
    
    data = []
    
    for i in range(n_samples):
        # Demographics
        age = np.random.randint(30, 80)
        sex = np.random.choice([0, 1], p=[0.32, 0.68])  # More males in heart disease studies
        
        # Vital signs (with age correlation)
        base_bp = 110 + (age - 30) * 0.6 + np.random.normal(0, 10)
        resting_bp = max(90, min(200, int(base_bp)))
        
        base_chol = 180 + (age - 30) * 1.2 + np.random.normal(0, 30)
        cholesterol = max(100, min(400, int(base_chol)))
        
        max_hr = max(70, min(202, int(220 - age - np.random.normal(0, 15))))
        
        # Risk factors
        smoking = np.random.choice([0, 1], p=[0.75, 0.25])
        diabetes = np.random.choice([0, 1], p=[0.85, 0.15])
        family_history = np.random.choice([0, 1], p=[0.70, 0.30])
        fasting_bs = np.random.choice([0, 1], p=[0.82, 0.18])
        
        # Cardiac tests (correlated with disease)
        resting_ecg = np.random.choice([0, 1, 2], p=[0.60, 0.25, 0.15])
        exercise_angina = np.random.choice([0, 1], p=[0.65, 0.35])
        oldpeak = max(0, round(np.random.exponential(0.8), 1))
        st_slope = np.random.choice([0, 1, 2], p=[0.35, 0.45, 0.20])
        
        # Calculate risk score
        risk_score = 0
        risk_score += (age - 40) * 0.05
        risk_score += sex * 1.2  # Males higher risk
        risk_score += max(0, (resting_bp - 120) / 20)
        risk_score += max(0, (cholesterol - 200) / 40)
        risk_score += (220 - age - max_hr) / 15
        risk_score += smoking * 1.5
        risk_score += diabetes * 1.8
        risk_score += family_history * 1.3
        risk_score += fasting_bs * 0.8
        risk_score += resting_ecg * 0.7
        risk_score += exercise_angina * 1.5
        risk_score += oldpeak * 1.2
        risk_score += st_slope * 0.6
        
        # Add random noise
        risk_score += np.random.normal(0, 1.5)
        
        # Convert to binary outcome with threshold
        threshold = 5.5
        heart_disease = 1 if risk_score > threshold else 0
        
        # Occasionally flip outcome to add realism (10% noise)
        if np.random.random() < 0.05:
            heart_disease = 1 - heart_disease
        
        data.append({
            'Age': age,
            'Sex': sex,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'RestingECG': resting_ecg,
            'MaxHR': max_hr,
            'ExerciseAngina': exercise_angina,
            'Oldpeak': oldpeak,
            'ST_Slope': st_slope,
            'Smoking': smoking,
            'Diabetes': diabetes,
            'FamilyHistory': family_history,
            'HeartDisease': heart_disease
        })
    
    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':
    # Generate training dataset
    print("Generating synthetic heart disease dataset...")
    df = generate_heart_disease_dataset(n_samples=2000)
    
    print(f"\nDataset shape: {df.shape}")
    print(f"Heart disease prevalence: {df['HeartDisease'].mean():.2%}")
    print(f"\nFeature summary:")
    print(df.describe())
    
    # Save to processed directory
    output_path = Path(__file__).parent.parent / 'data' / 'processed' / 'processed.csv'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"\n✓ Dataset saved to: {output_path}")
