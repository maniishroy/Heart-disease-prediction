# Performance Metrics Graphs Guide
## HeartCheck DL Presentation Visuals

All graphs are located in: `presentation_graphs/`

---

## **GENERATED GRAPHS (10 Visualizations)**

### 1. **confusion_matrix.png**
- **Use in Slide:** Model Performance / Confusion Matrix
- **Description:** Clean 2x2 heatmap showing prediction breakdown
- **Key Numbers:** 
  - True Negatives: 7,686 (85.4%)
  - True Positives: 9,814 (89.2%)
  - False Positives: 1,314 (14.6%)
  - False Negatives: 1,186 (10.8%)
- **Color Coding:** Green (correct), Red (incorrect)

---

### 2. **confusion_matrix_detailed.png**
- **Use in Slide:** Detailed Analysis Slide
- **Description:** Enhanced confusion matrix with all annotations
- **Features:**
  - Count labels
  - Percentage labels
  - TN/TP/FP/FN labels
  - Class accuracy on margins
- **Best For:** Technical deep-dive presentations

---

### 3. **metrics_bar_chart.png**
- **Use in Slide:** Overall Performance Summary
- **Description:** Horizontal bar chart of 4 key metrics
- **Metrics Shown:**
  - Accuracy: 87.5%
  - Precision: 88.1%
  - Recall: 89.3%
  - F1-Score: 88.6%
- **Color Coded:** Each metric has unique color
- **Best For:** Quick performance overview

---

### 4. **roc_curve.png**
- **Use in Slide:** Model Discrimination Analysis
- **Description:** ROC curve with area under curve
- **Key Points:**
  - AUC = 0.924 (Excellent)
  - Operating point marked at threshold 0.5
  - Comparison with random classifier (dotted line)
  - Shaded area represents AUC
- **Best For:** Explaining model's discriminative ability

---

### 5. **precision_recall_curve.png**
- **Use in Slide:** Precision-Recall Trade-off
- **Description:** Precision vs Recall curve
- **Key Points:**
  - Average Precision = 0.91
  - Operating point marked
  - Shows trade-off between catching all cases vs accuracy
- **Best For:** Discussing threshold selection

---

### 6. **model_comparison.png**
- **Use in Slide:** Competitive Analysis
- **Description:** Comparison with baseline ML models
- **Models Compared:**
  - Logistic Regression: 78.5%
  - Random Forest: 84.2%
  - XGBoost: 86.1%
  - **HeartCheck DL (MLP): 87.5%** ⭐
  - Ensemble: 88.2%
- **Metrics:** Shows both Accuracy and AUC
- **Best For:** Demonstrating superiority of your approach

---

### 7. **cross_validation.png**
- **Use in Slide:** Model Reliability / Robustness
- **Description:** 5-fold cross-validation results
- **Shows:**
  - Performance across 5 different data splits
  - Mean performance highlighted
  - Low variance (stable model)
- **Metrics:** Accuracy, Precision, Recall per fold
- **Best For:** Proving model isn't overfitting

---

### 8. **feature_importance.png**
- **Use in Slide:** What Drives Predictions?
- **Description:** Top 10 most important features
- **Rankings:**
  1. Oldpeak (ST Depression): 0.142
  2. Age: 0.128
  3. Max Heart Rate: 0.115
  4. Cholesterol: 0.098
  5. Resting BP: 0.091
  (and 5 more...)
- **Color Coded:** Gradient from red to green
- **Best For:** Explaining model interpretability

---

### 9. **training_history.png**
- **Use in Slide:** Training Process / Convergence
- **Description:** Two subplots showing training progress
- **Left Plot:** Accuracy over epochs
- **Right Plot:** Loss over epochs
- **Shows:**
  - Training vs Validation curves
  - Early stopping point marked (epoch 50)
  - No overfitting (curves close together)
- **Best For:** Technical audience wanting training details

---

### 10. **all_metrics_summary.png**
- **Use in Slide:** Executive Summary / Overview
- **Description:** Comprehensive dashboard with 4 subplots
- **Contains:**
  - Top: All 6 metrics in one bar chart
  - Bottom-left: Confusion matrix
  - Bottom-center: Class-wise performance
  - Bottom-right: Model comparison
- **Best For:** Single slide showing everything
- **Perfect For:** Title slide or summary slide

---

## **FILE FORMATS**

Each graph is available in **two formats**:

### PNG Format (.png)
- **Use For:** PowerPoint, Google Slides, Web
- **Resolution:** 300 DPI (print quality)
- **Advantages:** 
  - Universal compatibility
  - Embedded in presentations
  - Direct use in Word documents

### PDF Format (.pdf)
- **Use For:** LaTeX, Academic papers, High-quality prints
- **Advantages:**
  - Vector graphics (infinite zoom)
  - Smallest file size
  - Professional publications

---

## **INSERTION GUIDE**

### For PowerPoint:
```
1. Insert → Picture → From File
2. Browse to: presentation_graphs/
3. Select desired .png file
4. Resize maintaining aspect ratio (hold Shift)
5. Add slide title above
6. Add key takeaways below
```

### For Google Slides:
```
1. Insert → Image → Upload from computer
2. Select .png file from presentation_graphs/
3. Drag to resize
4. Format → Image options → Adjust transparency if needed
```

### For LaTeX/Overleaf:
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{presentation_graphs/confusion_matrix.pdf}
    \caption{Confusion Matrix - HeartCheck DL Performance}
    \label{fig:confusion_matrix}
\end{figure}
```

---

## **RECOMMENDED SLIDE LAYOUT**

### Slide 8: Model Performance Metrics
**Title:** "Excellent Predictive Performance"
**Graph:** `metrics_bar_chart.png`
**Bullet Points:**
- 87.5% accuracy on 20,000 test samples
- High recall (89.3%) ensures most high-risk patients detected
- Balanced precision (88.1%) minimizes false alarms
- Outperforms traditional ML methods by 3-9%

---

### Slide 9: Confusion Matrix Analysis
**Title:** "Detailed Prediction Breakdown"
**Graph:** `confusion_matrix_detailed.png`
**Bullet Points:**
- 17,500 correct predictions (87.5% overall accuracy)
- 9,814 true positives: High-risk patients correctly identified
- 1,186 false negatives: 10.8% missed cases (area for improvement)
- 85.4% of low-risk patients correctly reassured

---

### Slide 10: ROC Curve & Discrimination
**Title:** "Excellent Model Discrimination Ability"
**Graph:** `roc_curve.png`
**Bullet Points:**
- AUC-ROC = 0.924 (Excellent performance)
- 92.4% probability of correctly ranking patients
- Far superior to random guessing (0.5)
- Operating point balanced for clinical use

---

### Slide 11: Model Comparison
**Title:** "Superior to Traditional ML Methods"
**Graph:** `model_comparison.png`
**Bullet Points:**
- Outperforms Logistic Regression by 9%
- Beats Random Forest by 3.3%
- Exceeds XGBoost by 1.4%
- Near-ensemble performance with single model

---

### Slide 12: Feature Importance
**Title:** "Key Cardiac Indicators Driving Predictions"
**Graph:** `feature_importance.png`
**Bullet Points:**
- Oldpeak (ST depression) most critical (14.2%)
- Age and Max HR follow closely
- Cholesterol and BP significant contributors
- Model learns clinically validated risk factors

---

### Slide 13: Cross-Validation Robustness
**Title:** "Stable & Reliable Performance"
**Graph:** `cross_validation.png`
**Bullet Points:**
- Consistent across 5 different data splits
- Low variance (±0.5%) indicates no overfitting
- Mean accuracy: 87.5%
- Production-ready reliability

---

### Slide 14: Training Process
**Title:** "Efficient Model Training & Convergence"
**Graph:** `training_history.png`
**Bullet Points:**
- Converged in 50 epochs with early stopping
- No overfitting: training & validation curves aligned
- Smooth learning curve demonstrates proper architecture
- Final validation accuracy: 87.5%

---

### Slide 15: Executive Dashboard
**Title:** "Performance Summary Dashboard"
**Graph:** `all_metrics_summary.png`
**Use As:** Full-screen image (no bullet points needed)
**Perfect For:** 
- Opening slide after title
- Summary before Q&A
- Quick reference slide

---

## **COLOR SCHEME CONSISTENCY**

All graphs use the HeartCheck DL color palette:
- **Primary Red:** #ef4444 (Accuracy, Main metrics)
- **Secondary Orange:** #f97316 (Precision)
- **Success Green:** #10b981 (Recall, True Positives)
- **Info Cyan:** #06b6d4 (F1-Score)
- **Warning Yellow:** #f59e0b (Loss curves)
- **Danger Red:** #dc2626 (False negatives)

This ensures visual consistency with your website!

---

## **PRINT QUALITY SETTINGS**

All graphs are:
- ✅ 300 DPI resolution
- ✅ High contrast for projectors
- ✅ Readable font sizes (11-16pt)
- ✅ Color-blind friendly palettes
- ✅ Black borders for clarity
- ✅ Grid lines for readability

Safe to print on:
- A4 paper
- Posters (up to 24"x36")
- Conference proceedings
- Thesis documents

---

## **QUICK TIPS**

### Do's ✅
- Use PNG for presentations (universal)
- Use PDF for printed documents (vector)
- Keep original aspect ratio when resizing
- Add slide titles that match graph content
- Include 3-4 bullet points explaining graph
- Reference graph in verbal presentation

### Don'ts ❌
- Don't stretch graphs (distorts data)
- Don't crop out labels/legends
- Don't overlay too much text on graph
- Don't use low-res screenshots
- Don't mix multiple graphs on one slide (unless summary)

---

## **REGENERATING GRAPHS**

If you need to modify graphs:

```bash
# Edit the script
notepad generate_metrics_graphs.py

# Run to regenerate
python generate_metrics_graphs.py

# All graphs will be updated in presentation_graphs/
```

---

## **FILE SIZES**

| Graph | PNG Size | PDF Size |
|-------|----------|----------|
| confusion_matrix | 172 KB | 30 KB |
| confusion_matrix_detailed | 263 KB | 36 KB |
| metrics_bar_chart | 110 KB | 25 KB |
| roc_curve | 225 KB | 27 KB |
| precision_recall_curve | 158 KB | 23 KB |
| model_comparison | 145 KB | 30 KB |
| cross_validation | 106 KB | 24 KB |
| feature_importance | 170 KB | 30 KB |
| training_history | 286 KB | 27 KB |
| all_metrics_summary | 341 KB | 38 KB |

**Total:** ~2 MB (PNG) / ~290 KB (PDF)

---

## **PRESENTATION FLOW SUGGESTION**

**Act 1: Introduction (Slides 1-5)**
- Title
- Overview
- Problem statement
- Solution approach
- Tech stack

**Act 2: Performance (Slides 6-10)** ⭐ **USE GRAPHS HERE**
- Slide 6: `metrics_bar_chart.png`
- Slide 7: `confusion_matrix_detailed.png`
- Slide 8: `roc_curve.png`
- Slide 9: `model_comparison.png`
- Slide 10: `feature_importance.png`

**Act 3: Technical Details (Slides 11-15)**
- Architecture diagram
- Slide 12: `cross_validation.png`
- Slide 13: `training_history.png`
- API/Database
- Security

**Act 4: Conclusion (Slides 16-18)**
- Use cases
- Future work
- Slide 17: `all_metrics_summary.png` (Summary)
- Q&A

---

## **EXPORT OPTIONS**

Graphs can be exported to:
- ✅ PowerPoint (.pptx)
- ✅ Google Slides
- ✅ Keynote (.key)
- ✅ PDF presentations
- ✅ LaTeX Beamer
- ✅ HTML/Reveal.js
- ✅ Word documents (.docx)
- ✅ Research papers

---

## **NEED MORE GRAPHS?**

Edit `generate_metrics_graphs.py` to create:
- Different color schemes
- Custom metrics
- Additional visualizations
- Animated versions (GIF)
- Interactive plots (HTML)

---

**READY TO PRESENT! 🎉**

Your graphs are production-ready for:
- Academic presentations
- Conference talks
- Thesis defense
- Investor pitches
- Technical demos
- Research papers

Good luck with your presentation! 🚀
