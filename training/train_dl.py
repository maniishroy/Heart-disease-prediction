"""
HeartCheck DL - Deep Learning Training Script
Trains TensorFlow/Keras model with callbacks and saves best model
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / 'data' / 'processed'
MODELS_DIR = BASE_DIR / 'models'

def load_processed_data():
    """Load preprocessed training data"""
    print("Loading processed data...")
    X_train = np.load(DATA_DIR / 'X_train.npy')
    X_test = np.load(DATA_DIR / 'X_test.npy')
    y_train = np.load(DATA_DIR / 'y_train.npy')
    y_test = np.load(DATA_DIR / 'y_test.npy')
    
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_train shape: {y_train.shape}")
    print(f"y_test shape: {y_test.shape}")
    
    return X_train, X_test, y_train, y_test

def build_mlp_model(input_dim, hidden_layers=[128, 64, 32], dropout=0.3):
    """
    Build Multi-Layer Perceptron (MLP) model
    
    Args:
        input_dim: Number of input features
        hidden_layers: List of hidden layer sizes
        dropout: Dropout rate
    """
    model = keras.Sequential(name='HeartCheck_MLP')
    
    # Input layer
    model.add(layers.Input(shape=(input_dim,)))
    
    # Hidden layers
    for i, units in enumerate(hidden_layers):
        model.add(layers.Dense(units, activation='relu', name=f'dense_{i+1}'))
        model.add(layers.BatchNormalization(name=f'bn_{i+1}'))
        model.add(layers.Dropout(dropout, name=f'dropout_{i+1}'))
    
    # Output layer (binary classification)
    model.add(layers.Dense(1, activation='sigmoid', name='output'))
    
    return model

def build_hybrid_model(input_dim):
    """
    Build Hybrid CNN-inspired model (1D convolutions on tabular data)
    
    Note: This is experimental - reshaping tabular data for CNN.
    For tabular data, MLP or Gradient Boosting usually works better.
    """
    inputs = layers.Input(shape=(input_dim,))
    
    # Reshape for 1D conv (treat features as sequence)
    x = layers.Reshape((input_dim, 1))(inputs)
    
    # 1D Convolutional layers
    x = layers.Conv1D(64, 3, activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling1D(2)(x)
    
    x = layers.Conv1D(32, 3, activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.GlobalMaxPooling1D()(x)
    
    # Dense layers
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(32, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    
    # Output
    outputs = layers.Dense(1, activation='sigmoid')(x)
    
    model = keras.Model(inputs=inputs, outputs=outputs, name='HeartCheck_Hybrid')
    return model

def train_model(model, X_train, y_train, X_test, y_test, epochs=100, batch_size=32):
    """Train model with callbacks"""
    
    # Compile model
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc')]
    )
    
    print("\nModel architecture:")
    model.summary()
    
    # Callbacks
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    model_filename = f'heart_dl_model_{timestamp}.h5'
    model_path = MODELS_DIR / model_filename
    
    callbacks = [
        EarlyStopping(
            monitor='val_loss',
            patience=15,
            restore_best_weights=True,
            verbose=1
        ),
        ModelCheckpoint(
            filepath=str(model_path),
            monitor='val_auc',
            mode='max',
            save_best_only=True,
            verbose=1
        ),
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            min_lr=1e-7,
            verbose=1
        )
    ]
    
    print(f"\nTraining model...")
    print(f"Epochs: {epochs}, Batch size: {batch_size}")
    
    # Train
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=callbacks,
        verbose=1
    )
    
    return history, model_path, model_filename

def evaluate_model(model, X_test, y_test):
    """Evaluate model and return metrics"""
    print("\nEvaluating model...")
    
    # Predict
    y_pred_prob = model.predict(X_test)
    y_pred = (y_pred_prob > 0.5).astype(int).flatten()
    
    # Metrics
    test_loss, test_acc, test_auc = model.evaluate(X_test, y_test, verbose=0)
    
    print(f"\nTest Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")
    print(f"Test AUC: {test_auc:.4f}")
    
    # Classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Confusion matrix
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # ROC AUC
    try:
        roc_auc = roc_auc_score(y_test, y_pred_prob)
        print(f"ROC AUC Score: {roc_auc:.4f}")
    except:
        roc_auc = test_auc
    
    return {
        'test_loss': float(test_loss),
        'test_accuracy': float(test_acc),
        'test_auc': float(test_auc),
        'roc_auc': float(roc_auc)
    }

def save_training_info(history, model_filename, metrics):
    """Save training history and update model registry"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save history
    history_filename = f'history_{timestamp}.json'
    history_path = MODELS_DIR / history_filename
    
    history_dict = {
        'loss': [float(x) for x in history.history['loss']],
        'accuracy': [float(x) for x in history.history['accuracy']],
        'auc': [float(x) for x in history.history['auc']],
        'val_loss': [float(x) for x in history.history['val_loss']],
        'val_accuracy': [float(x) for x in history.history['val_accuracy']],
        'val_auc': [float(x) for x in history.history['val_auc']]
    }
    
    with open(history_path, 'w') as f:
        json.dump(history_dict, f, indent=2)
    print(f"\n✓ Saved training history to: {history_path}")
    
    # Update model registry
    registry_path = MODELS_DIR / 'registry.json'
    
    if registry_path.exists():
        with open(registry_path, 'r') as f:
            registry = json.load(f)
    else:
        registry = []
    
    registry.append({
        'model_name': f'heart_dl_v{len(registry) + 1}',
        'file': model_filename,
        'history_file': history_filename,
        'timestamp': timestamp,
        'metrics': metrics,
        'dataset': 'fedesoriano/heart-failure-prediction',
        'notes': 'Deep learning model trained with TensorFlow/Keras'
    })
    
    with open(registry_path, 'w') as f:
        json.dump(registry, f, indent=2)
    print(f"✓ Updated model registry: {registry_path}")

def main():
    parser = argparse.ArgumentParser(description='Train deep learning model for heart disease prediction')
    parser.add_argument('--model', '-m',
                       choices=['mlp', 'hybrid'],
                       default='mlp',
                       help='Model architecture (default: mlp)')
    parser.add_argument('--epochs', '-e',
                       type=int,
                       default=100,
                       help='Number of training epochs (default: 100)')
    parser.add_argument('--batch-size', '-b',
                       type=int,
                       default=32,
                       help='Batch size (default: 32)')
    
    args = parser.parse_args()
    
    print("="*60)
    print("HeartCheck DL - Model Training")
    print("="*60)
    
    # Check for processed data
    if not DATA_DIR.exists():
        print(f"\nERROR: Processed data not found at {DATA_DIR}")
        print("Please run: python training/prepare_data.py")
        return
    
    # Load data
    X_train, X_test, y_train, y_test = load_processed_data()
    
    # Build model
    input_dim = X_train.shape[1]
    if args.model == 'mlp':
        print(f"\nBuilding MLP model (input_dim={input_dim})...")
        model = build_mlp_model(input_dim)
    else:
        print(f"\nBuilding Hybrid CNN model (input_dim={input_dim})...")
        model = build_hybrid_model(input_dim)
    
    # Train model
    history, model_path, model_filename = train_model(
        model, X_train, y_train, X_test, y_test,
        epochs=args.epochs,
        batch_size=args.batch_size
    )
    
    # Evaluate
    metrics = evaluate_model(model, X_test, y_test)
    
    # Save info
    save_training_info(history, model_filename, metrics)
    
    print("\n" + "="*60)
    print("✓ Training complete!")
    print("="*60)
    print(f"\nModel saved to: {model_path}")
    print("\nNext step:")
    print("  flask run --host=0.0.0.0 --port=5000")
    print("  OR")
    print("  docker-compose up --build")

if __name__ == '__main__':
    # Set random seeds for reproducibility
    np.random.seed(42)
    tf.random.set_seed(42)
    
    # Enable GPU if available
    print(f"TensorFlow version: {tf.__version__}")
    print(f"GPU available: {tf.config.list_physical_devices('GPU')}")
    
    MODELS_DIR.mkdir(exist_ok=True)
    main()
