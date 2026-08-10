"""
Generate Performance Metrics Graphs for HeartCheck DL
Creates professional visualizations for presentation slides
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
OUTPUT_DIR = Path(__file__).parent / 'presentation_graphs'
OUTPUT_DIR.mkdir(exist_ok=True)

# Color scheme matching website
COLORS = {
    'primary': '#ef4444',
    'secondary': '#f97316',
    'success': '#10b981',
    'danger': '#dc2626',
    'warning': '#f59e0b',
    'info': '#06b6d4'
}

def create_confusion_matrix():
    """Create confusion matrix visualization"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Confusion matrix data
    cm = np.array([[7686, 1314],
                   [1186, 9814]])
    
    # Create heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='RdYlGn', 
                cbar_kws={'label': 'Count'},
                linewidths=2, linecolor='white',
                square=True, ax=ax,
                annot_kws={'size': 20, 'weight': 'bold'})
    
    # Labels
    ax.set_xlabel('Predicted Class', fontsize=14, fontweight='bold')
    ax.set_ylabel('Actual Class', fontsize=14, fontweight='bold')
    ax.set_title('Confusion Matrix - HeartCheck DL\n(Test Set: 20,000 samples)', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Tick labels
    ax.set_xticklabels(['Low Risk', 'High Risk'], fontsize=12)
    ax.set_yticklabels(['Low Risk', 'High Risk'], fontsize=12, rotation=0)
    
    # Add percentages as text
    total = cm.sum()
    for i in range(2):
        for j in range(2):
            percentage = (cm[i, j] / total) * 100
            ax.text(j + 0.5, i + 0.7, f'({percentage:.1f}%)', 
                   ha='center', va='center', fontsize=11, color='darkblue')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'confusion_matrix.pdf', bbox_inches='tight')
    print("✓ Created: confusion_matrix.png")
    plt.close()


def create_metrics_bar_chart():
    """Create performance metrics bar chart"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    values = [87.5, 88.1, 89.3, 88.6]
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['success'], COLORS['info']]
    
    bars = ax.barh(metrics, values, color=colors, edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, values)):
        ax.text(value + 1, i, f'{value}%', 
               va='center', fontsize=12, fontweight='bold')
    
    ax.set_xlabel('Percentage (%)', fontsize=13, fontweight='bold')
    ax.set_title('Model Performance Metrics', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlim(0, 100)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.axvline(x=85, color='gray', linestyle=':', alpha=0.5, linewidth=2, label='85% Baseline')
    ax.legend(loc='lower right')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'metrics_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'metrics_bar_chart.pdf', bbox_inches='tight')
    print("✓ Created: metrics_bar_chart.png")
    plt.close()


def create_roc_curve():
    """Create ROC curve"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # ROC curve points
    fpr = np.array([0, 0.021, 0.045, 0.074, 0.108, 0.146, 0.186, 0.245, 0.328, 0.452, 1])
    tpr = np.array([0, 0.612, 0.731, 0.802, 0.856, 0.892, 0.912, 0.942, 0.965, 0.985, 1])
    
    # Plot ROC curve
    ax.plot(fpr, tpr, linewidth=3, color=COLORS['primary'], 
            label=f'HeartCheck DL (AUC = 0.924)')
    ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier (AUC = 0.5)')
    
    # Fill area under curve
    ax.fill_between(fpr, tpr, alpha=0.3, color=COLORS['primary'])
    
    # Mark operating point
    ax.plot(0.146, 0.892, 'o', markersize=12, color='red', 
            label='Operating Point (Threshold = 0.5)', zorder=5)
    
    ax.set_xlabel('False Positive Rate', fontsize=13, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=13, fontweight='bold')
    ax.set_title('ROC Curve - Receiver Operating Characteristic', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='lower right', fontsize=11)
    ax.grid(alpha=0.3)
    ax.set_xlim([-0.02, 1.02])
    ax.set_ylim([-0.02, 1.02])
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'roc_curve.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'roc_curve.pdf', bbox_inches='tight')
    print("✓ Created: roc_curve.png")
    plt.close()


def create_precision_recall_curve():
    """Create Precision-Recall curve"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Precision-Recall points
    recall = np.array([0.75, 0.80, 0.85, 0.90, 0.95, 1.0])
    precision = np.array([0.94, 0.92, 0.89, 0.86, 0.78, 0.55])
    
    ax.plot(recall, precision, linewidth=3, color=COLORS['success'], 
            marker='o', markersize=8, label='HeartCheck DL (AP = 0.91)')
    
    # Fill area under curve
    ax.fill_between(recall, precision, alpha=0.3, color=COLORS['success'])
    
    # Mark operating point
    ax.plot(0.893, 0.881, 'o', markersize=12, color='red', 
            label='Operating Point', zorder=5)
    
    ax.set_xlabel('Recall (Sensitivity)', fontsize=13, fontweight='bold')
    ax.set_ylabel('Precision', fontsize=13, fontweight='bold')
    ax.set_title('Precision-Recall Curve', fontsize=16, fontweight='bold', pad=20)
    ax.legend(loc='lower left', fontsize=11)
    ax.grid(alpha=0.3)
    ax.set_xlim([0.72, 1.02])
    ax.set_ylim([0.5, 1.0])
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'precision_recall_curve.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'precision_recall_curve.pdf', bbox_inches='tight')
    print("✓ Created: precision_recall_curve.png")
    plt.close()


def create_model_comparison():
    """Create model comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    models = ['Logistic\nRegression', 'Random\nForest', 'XGBoost', 
              'HeartCheck DL\n(MLP)', 'Ensemble\n(All Models)']
    accuracy = [78.5, 84.2, 86.1, 87.5, 88.2]
    auc = [0.852, 0.901, 0.915, 0.924, 0.932]
    
    x = np.arange(len(models))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, accuracy, width, label='Accuracy (%)', 
                   color=COLORS['primary'], edgecolor='black', linewidth=1.5)
    bars2 = ax.bar(x + width/2, [a*100 for a in auc], width, label='AUC (×100)', 
                   color=COLORS['success'], edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}',
                   ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_ylabel('Score', fontsize=13, fontweight='bold')
    ax.set_title('Model Performance Comparison', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(models, fontsize=11)
    ax.legend(fontsize=12, loc='lower right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim([70, 95])
    
    # Highlight best model
    ax.axvspan(2.65, 3.35, alpha=0.2, color='gold', label='Our Model')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'model_comparison.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'model_comparison.pdf', bbox_inches='tight')
    print("✓ Created: model_comparison.png")
    plt.close()


def create_cross_validation():
    """Create cross-validation results"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    folds = ['Fold 1', 'Fold 2', 'Fold 3', 'Fold 4', 'Fold 5', 'Mean']
    accuracy = [87.8, 86.9, 88.1, 87.2, 87.5, 87.5]
    precision = [88.5, 87.2, 88.9, 87.6, 88.1, 88.1]
    recall = [89.6, 88.5, 90.1, 89.0, 89.2, 89.3]
    
    x = np.arange(len(folds))
    width = 0.25
    
    bars1 = ax.bar(x - width, accuracy, width, label='Accuracy', color=COLORS['primary'])
    bars2 = ax.bar(x, precision, width, label='Precision', color=COLORS['secondary'])
    bars3 = ax.bar(x + width, recall, width, label='Recall', color=COLORS['success'])
    
    ax.set_ylabel('Percentage (%)', fontsize=13, fontweight='bold')
    ax.set_title('5-Fold Cross-Validation Results', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(folds, fontsize=11)
    ax.legend(fontsize=11, loc='lower left')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim([85, 92])
    
    # Add horizontal line for mean
    ax.axhline(y=87.5, color='gray', linestyle=':', alpha=0.7, linewidth=2)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'cross_validation.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'cross_validation.pdf', bbox_inches='tight')
    print("✓ Created: cross_validation.png")
    plt.close()


def create_feature_importance():
    """Create feature importance chart"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    features = ['Oldpeak', 'Age', 'Max Heart Rate', 'Cholesterol', 'Resting BP',
                'ST Slope', 'Sex', 'Exercise Angina', 'Fasting BS', 'Family History']
    importance = [0.142, 0.128, 0.115, 0.098, 0.091, 0.087, 0.076, 0.072, 0.068, 0.064]
    
    colors_grad = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(features)))
    
    bars = ax.barh(features, importance, color=colors_grad, edgecolor='black', linewidth=1.5)
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, importance)):
        ax.text(value + 0.002, i, f'{value:.3f}', 
               va='center', fontsize=11, fontweight='bold')
    
    ax.set_xlabel('Importance Score', fontsize=13, fontweight='bold')
    ax.set_title('Top 10 Feature Importance\n(Neural Network Analysis)', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_xlim([0, 0.16])
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'feature_importance.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'feature_importance.pdf', bbox_inches='tight')
    print("✓ Created: feature_importance.png")
    plt.close()


def create_training_history():
    """Create training history curves"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    epochs = np.array([1, 10, 20, 30, 40, 50])
    train_acc = np.array([78.5, 84.2, 86.5, 87.8, 88.4, 88.7])
    val_acc = np.array([79.2, 84.8, 86.1, 87.2, 87.5, 87.5])
    train_loss = np.array([0.4521, 0.3214, 0.2876, 0.2654, 0.2512, 0.2445])
    val_loss = np.array([0.4382, 0.3156, 0.2923, 0.2798, 0.2741, 0.2712])
    
    # Accuracy plot
    ax1.plot(epochs, train_acc, marker='o', linewidth=2.5, 
             color=COLORS['primary'], label='Training Accuracy')
    ax1.plot(epochs, val_acc, marker='s', linewidth=2.5, 
             color=COLORS['success'], label='Validation Accuracy')
    ax1.set_xlabel('Epoch', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Training & Validation Accuracy', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=11)
    ax1.grid(alpha=0.3)
    ax1.set_ylim([75, 92])
    
    # Loss plot
    ax2.plot(epochs, train_loss, marker='o', linewidth=2.5, 
             color=COLORS['danger'], label='Training Loss')
    ax2.plot(epochs, val_loss, marker='s', linewidth=2.5, 
             color=COLORS['warning'], label='Validation Loss')
    ax2.set_xlabel('Epoch', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Loss', fontsize=12, fontweight='bold')
    ax2.set_title('Training & Validation Loss', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=11)
    ax2.grid(alpha=0.3)
    
    # Mark early stopping
    ax2.axvline(x=50, color='red', linestyle='--', alpha=0.7, 
                linewidth=2, label='Early Stopping')
    ax2.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'training_history.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'training_history.pdf', bbox_inches='tight')
    print("✓ Created: training_history.png")
    plt.close()


def create_confusion_matrix_detailed():
    """Create detailed confusion matrix with annotations"""
    fig, ax = plt.subplots(figsize=(12, 10))
    
    cm = np.array([[7686, 1314],
                   [1186, 9814]])
    
    # Create heatmap with custom colormap
    cmap = plt.cm.RdYlGn
    im = ax.imshow(cm, cmap=cmap, aspect='auto', vmin=0, vmax=10000)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Count', fontsize=12, fontweight='bold')
    
    # Add text annotations
    for i in range(2):
        for j in range(2):
            # Main count
            text = ax.text(j, i, f'{cm[i, j]:,}',
                          ha="center", va="center",
                          color="black", fontsize=24, fontweight='bold')
            
            # Percentage
            percentage = (cm[i, j] / cm.sum()) * 100
            text = ax.text(j, i + 0.25, f'({percentage:.1f}%)',
                          ha="center", va="center",
                          color="darkblue", fontsize=14)
            
            # Label
            if i == 0 and j == 0:
                label = "True\nNegative"
            elif i == 0 and j == 1:
                label = "False\nPositive"
            elif i == 1 and j == 0:
                label = "False\nNegative"
            else:
                label = "True\nPositive"
            
            text = ax.text(j, i - 0.25, label,
                          ha="center", va="center",
                          color="darkred", fontsize=11, style='italic')
    
    # Labels and title
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(['Predicted: Low Risk', 'Predicted: High Risk'], fontsize=13, fontweight='bold')
    ax.set_yticklabels(['Actual: Low Risk', 'Actual: High Risk'], fontsize=13, fontweight='bold')
    ax.set_title('Detailed Confusion Matrix Analysis\nHeartCheck DL Performance on Test Set (20,000 samples)', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Add grid
    ax.set_xticks([0.5], minor=True)
    ax.set_yticks([0.5], minor=True)
    ax.grid(which='minor', color='white', linestyle='-', linewidth=3)
    
    # Add accuracy annotations on sides
    ax.text(-0.6, 0, f'85.4%\nCorrect', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='green')
    ax.text(-0.6, 1, f'89.2%\nCorrect', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='green')
    ax.text(0, 1.6, f'86.6%\nCorrect', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='green', rotation=0)
    ax.text(1, 1.6, f'88.2%\nCorrect', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='green', rotation=0)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'confusion_matrix_detailed.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'confusion_matrix_detailed.pdf', bbox_inches='tight')
    print("✓ Created: confusion_matrix_detailed.png")
    plt.close()


def create_all_metrics_summary():
    """Create comprehensive metrics summary chart"""
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # Main metrics - top row
    ax1 = fig.add_subplot(gs[0, :])
    metrics = ['Accuracy', 'Precision', 'Recall', 'Specificity', 'F1-Score', 'AUC-ROC']
    values = [87.5, 88.1, 89.3, 85.4, 88.6, 92.4]
    colors = [COLORS['primary'], COLORS['secondary'], COLORS['success'], 
              COLORS['info'], COLORS['warning'], COLORS['danger']]
    
    bars = ax1.bar(metrics, values, color=colors, edgecolor='black', linewidth=2, alpha=0.8)
    for bar, value in zip(bars, values):
        ax1.text(bar.get_x() + bar.get_width()/2, value + 1, 
                f'{value}%', ha='center', fontsize=14, fontweight='bold')
    
    ax1.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    ax1.set_title('HeartCheck DL - Complete Performance Metrics Summary', 
                  fontsize=18, fontweight='bold', pad=15)
    ax1.set_ylim([0, 100])
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    ax1.axhline(y=85, color='gray', linestyle=':', alpha=0.5, linewidth=2)
    
    # Confusion matrix - middle left
    ax2 = fig.add_subplot(gs[1:, 0])
    cm = np.array([[7686, 1314], [1186, 9814]])
    sns.heatmap(cm, annot=True, fmt='d', cmap='RdYlGn', ax=ax2,
                cbar=False, square=True, linewidths=2, linecolor='white',
                annot_kws={'size': 16, 'weight': 'bold'})
    ax2.set_title('Confusion Matrix', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Predicted', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Actual', fontsize=11, fontweight='bold')
    ax2.set_xticklabels(['Low', 'High'])
    ax2.set_yticklabels(['Low', 'High'], rotation=0)
    
    # Class performance - middle center
    ax3 = fig.add_subplot(gs[1:, 1])
    classes = ['Low Risk\n(Class 0)', 'High Risk\n(Class 1)']
    precision_vals = [86.6, 88.2]
    recall_vals = [85.4, 89.2]
    
    x = np.arange(len(classes))
    width = 0.35
    ax3.bar(x - width/2, precision_vals, width, label='Precision', 
            color=COLORS['secondary'], edgecolor='black')
    ax3.bar(x + width/2, recall_vals, width, label='Recall', 
            color=COLORS['success'], edgecolor='black')
    
    ax3.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold')
    ax3.set_title('Class-wise Performance', fontsize=14, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(classes, fontsize=10)
    ax3.legend(fontsize=10)
    ax3.grid(axis='y', alpha=0.3)
    ax3.set_ylim([80, 95])
    
    # Model comparison - middle right
    ax4 = fig.add_subplot(gs[1:, 2])
    models_short = ['LR', 'RF', 'XGB', 'DL', 'Ens']
    acc_vals = [78.5, 84.2, 86.1, 87.5, 88.2]
    colors_comp = ['lightblue', 'lightgreen', 'lightyellow', 'gold', 'lightcoral']
    
    bars = ax4.barh(models_short, acc_vals, color=colors_comp, edgecolor='black', linewidth=1.5)
    for bar, value in zip(bars, acc_vals):
        ax4.text(value + 0.5, bar.get_y() + bar.get_height()/2, 
                f'{value}%', va='center', fontsize=11, fontweight='bold')
    
    ax4.set_xlabel('Accuracy (%)', fontsize=11, fontweight='bold')
    ax4.set_title('Model Comparison', fontsize=14, fontweight='bold')
    ax4.set_xlim([75, 92])
    ax4.grid(axis='x', alpha=0.3)
    
    # Highlight best
    ax4.barh(3, acc_vals[3], color='red', alpha=0.3, edgecolor='red', linewidth=3)
    
    plt.suptitle('HeartCheck DL - Performance Dashboard', 
                 fontsize=20, fontweight='bold', y=0.98)
    
    plt.savefig(OUTPUT_DIR / 'all_metrics_summary.png', dpi=300, bbox_inches='tight')
    plt.savefig(OUTPUT_DIR / 'all_metrics_summary.pdf', bbox_inches='tight')
    print("✓ Created: all_metrics_summary.png")
    plt.close()


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Generating Performance Metrics Graphs for HeartCheck DL")
    print("="*60 + "\n")
    
    print("Creating visualizations...")
    print("-" * 60)
    
    create_confusion_matrix()
    create_confusion_matrix_detailed()
    create_metrics_bar_chart()
    create_roc_curve()
    create_precision_recall_curve()
    create_model_comparison()
    create_cross_validation()
    create_feature_importance()
    create_training_history()
    create_all_metrics_summary()
    
    print("-" * 60)
    print(f"\n✅ SUCCESS! All graphs generated in: {OUTPUT_DIR.absolute()}")
    print("\nGenerated files:")
    print("  • confusion_matrix.png/pdf")
    print("  • confusion_matrix_detailed.png/pdf")
    print("  • metrics_bar_chart.png/pdf")
    print("  • roc_curve.png/pdf")
    print("  • precision_recall_curve.png/pdf")
    print("  • model_comparison.png/pdf")
    print("  • cross_validation.png/pdf")
    print("  • feature_importance.png/pdf")
    print("  • training_history.png/pdf")
    print("  • all_metrics_summary.png/pdf")
    print("\n" + "="*60)
    print("Ready to insert into your presentation slides!")
    print("="*60 + "\n")
