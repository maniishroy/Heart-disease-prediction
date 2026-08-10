# Website Screenshots Guide for Report

## Instructions for Capturing Screenshots

To capture screenshots for your project report, follow these steps:

### How to Take Screenshots on Windows:
1. **Full Page Screenshot**: Press `Windows + Shift + S` to open Snipping Tool
2. **Specific Area**: Use Snipping Tool to select the area you want
3. **Full Screen**: Press `Print Screen` key and paste in Paint/Word
4. **Browser Extension**: Use browser extensions like "Full Page Screenshot" for entire pages

---

## Required Screenshots for Report

### 1. **Home Page - Landing Section**
**File Name**: `01_home_landing.png`
- URL: `http://localhost:5000/`
- **What to Capture**: 
  - Hero section with gradient background
  - "Heart Disease Prediction" title
  - "Get Started" button
  - Animated heartbeat icon
  - Navigation bar

**Purpose**: Show the main landing page and primary interface

---

### 2. **Home Page - Model Architecture Section**
**File Name**: `02_model_architecture.png`
- Scroll down on home page
- **What to Capture**:
  - "Model Architecture" section
  - Deep Learning Model diagram with layers
  - Input Features → Hidden Layers → Output visualization
  - Technical specifications (93.2% accuracy, 100k+ dataset)

**Purpose**: Demonstrate the deep learning model architecture

---

### 3. **Home Page - Dataset Statistics**
**File Name**: `03_dataset_statistics.png`
- Scroll to dataset section on home page
- **What to Capture**:
  - "Training Data & Datasets" heading
  - Statistics showing "100,000+ Training Samples"
  - Dataset cards (Cleveland, Heart Failure, etc.)
  - Data source information

**Purpose**: Show the large dataset size and sources used

---

### 4. **Assessment/Prediction Form - Part 1**
**File Name**: `04_assessment_form_top.png`
- Click "Get Started" button
- **What to Capture**:
  - Form title "Heart Disease Risk Assessment"
  - Personal Information section
  - First few input fields (Age, Gender, etc.)
  - Clean form design

**Purpose**: Show the user input interface (top section)

---

### 5. **Assessment Form - Part 2**
**File Name**: `05_assessment_form_middle.png`
- Scroll down on assessment page
- **What to Capture**:
  - Clinical Measurements section
  - Cholesterol, Blood Pressure fields
  - ECG Results dropdown
  - Heart Rate input

**Purpose**: Show clinical parameter inputs

---

### 6. **Assessment Form - Part 3**
**File Name**: `06_assessment_form_bottom.png`
- Scroll to bottom of assessment form
- **What to Capture**:
  - Medical History section
  - Lifestyle Factors section
  - "Predict Risk" button
  - Form validation messages (if any)

**Purpose**: Show complete form with submit button

---

### 7. **Results Page - Low Risk**
**File Name**: `07_results_low_risk.png`
- Fill form with low-risk values and submit
- **What to Capture**:
  - Risk level indicator showing "Low Risk"
  - Probability score
  - Circular progress indicator
  - Risk factor breakdown
  - Recommendations section

**Purpose**: Demonstrate low-risk prediction output

---

### 8. **Results Page - High Risk**
**File Name**: `08_results_high_risk.png`
- Fill form with high-risk values and submit
- **What to Capture**:
  - Risk level indicator showing "High Risk"
  - High probability score
  - Warning colors/indicators
  - Detailed recommendations
  - "Download Report" button

**Purpose**: Demonstrate high-risk prediction output

---

### 9. **Results Page - Risk Factor Analysis**
**File Name**: `09_risk_factor_breakdown.png`
- Scroll down on results page
- **What to Capture**:
  - Risk Factor Contribution chart
  - Individual factor scores
  - Visual representation (charts/graphs)
  - Key risk factors highlighted

**Purpose**: Show detailed risk analysis breakdown

---

### 10. **Results Page - Recommendations**
**File Name**: `10_recommendations.png`
- Scroll to recommendations section
- **What to Capture**:
  - Personalized health recommendations
  - Lifestyle modification suggestions
  - Medical advice
  - Action items

**Purpose**: Show personalized recommendations feature

---

### 11. **Login/Signup Page**
**File Name**: `11_login_page.png`
- Navigate to login page (if available)
- **What to Capture**:
  - Login form
  - Email and password fields
  - "Sign Up" option
  - Authentication interface

**Purpose**: Show user authentication feature

---

### 12. **History/Dashboard Page**
**File Name**: `12_history_dashboard.png`
- After login, view history page
- **What to Capture**:
  - Previous predictions list
  - Assessment history
  - Date/time stamps
  - Quick view of past results

**Purpose**: Show assessment history tracking feature

---

### 13. **Mobile Responsive View - Home**
**File Name**: `13_mobile_home.png`
- Resize browser to mobile size (375px width) or use Developer Tools (F12)
- **What to Capture**:
  - Home page on mobile view
  - Responsive navigation (hamburger menu)
  - Mobile-optimized layout

**Purpose**: Demonstrate responsive design

---

### 14. **Mobile Responsive View - Form**
**File Name**: `14_mobile_assessment.png`
- Assessment form in mobile view
- **What to Capture**:
  - Mobile-optimized form fields
  - Touch-friendly buttons
  - Vertical layout

**Purpose**: Show mobile-friendly input interface

---

### 15. **Database/Admin View** (If applicable)
**File Name**: `15_database_view.png`
- If you have admin panel showing database records
- **What to Capture**:
  - Database entries
  - User records
  - Assessment data storage

**Purpose**: Show backend data management

---

## Additional Screenshots (Optional but Recommended)

### 16. **Code Editor - Model Training**
**File Name**: `16_code_model.png`
- Open your model training file
- **What to Capture**:
  - Python code for model architecture
  - Training code
  - Commented sections

### 17. **Code Editor - Flask App**
**File Name**: `17_code_flask.png`
- Open app.py or main Flask file
- **What to Capture**:
  - Flask routes
  - API endpoints
  - Application logic

### 18. **Performance Metrics Graphs**
**File Name**: `18_performance_graphs.png`
- Open the generated metrics graphs
- **What to Capture**:
  - Accuracy/Loss curves
  - Confusion matrix
  - ROC curve

### 19. **Project Structure**
**File Name**: `19_project_structure.png`
- File explorer showing project directory
- **What to Capture**:
  - Folder structure
  - Key files and directories
  - Organized project layout

### 20. **Terminal - Running Application**
**File Name**: `20_terminal_running.png`
- Terminal/Command Prompt with server running
- **What to Capture**:
  - Flask server output
  - "Running on http://localhost:5000"
  - No errors in console

---

## Screenshot Quality Guidelines

1. **Resolution**: Minimum 1920x1080 or your screen's native resolution
2. **Format**: Save as PNG for best quality
3. **File Size**: Try to keep under 5MB each
4. **Clarity**: Ensure text is readable when zoomed in
5. **Content**: Avoid personal/sensitive information
6. **Borders**: Include relevant UI elements but crop unnecessary parts
7. **Consistency**: Use same zoom level across similar screenshots

---

## How to Start the Application for Screenshots

1. Open Command Prompt/PowerShell in project directory
2. Activate virtual environment:
   ```
   venv\Scripts\activate
   ```
3. Run the application:
   ```
   python api\app.py
   ```
4. Open browser and go to: `http://localhost:5000`

---

## Organizing Screenshots in Report

### Suggested Report Structure:

**Chapter 1: Introduction**
- Screenshot #1 (Home Landing)

**Chapter 2: Literature Survey**
- No screenshots needed

**Chapter 3: Problem Statement**
- Screenshot #3 (Dataset Statistics)

**Chapter 4: System Requirements**
- Screenshot #19 (Project Structure)

**Chapter 5: System Design**
- Screenshot #2 (Model Architecture)
- Screenshot #18 (Performance Graphs)

**Chapter 6: Implementation**
- Screenshots #4, #5, #6 (Assessment Forms)
- Screenshots #16, #17 (Code)

**Chapter 7: Results**
- Screenshots #7, #8, #9, #10 (Results Pages)

**Chapter 8: Testing**
- Screenshots #13, #14 (Mobile Views)
- Screenshot #20 (Running Application)

**Chapter 9: Conclusion**
- Any summary screenshot

---

## Tips for Better Screenshots

1. **Clean Browser**: Clear unnecessary browser extensions from view
2. **Full Screen**: Use F11 for clean full-screen captures
3. **Sample Data**: Use realistic but not real patient data
4. **Multiple Attempts**: Take 2-3 screenshots of each section
5. **Annotations**: You can add arrows/highlights later in PowerPoint
6. **Consistent Time**: Take all at once for consistency

---

## Screenshot Editing Tools

- **Windows Snipping Tool** (Built-in)
- **Paint** (For basic cropping)
- **PowerPoint** (For annotations)
- **Greenshot** (Free tool - recommended)
- **LightShot** (Free screenshot tool)

---

## Contact for Issues

If you encounter any issues while taking screenshots:
1. Ensure the server is running (`python api\app.py`)
2. Check browser console for errors (F12)
3. Try different browsers (Chrome, Firefox, Edge)
4. Clear browser cache if styling looks wrong

---

**Note**: This guide is specifically tailored for the HeartCheck DL project. Make sure your application is running properly before taking screenshots.
