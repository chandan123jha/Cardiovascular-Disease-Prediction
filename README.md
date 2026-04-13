# Cardiovascular Disease Prediction System

## Overview

A modern **Flask-based web application** for cardiovascular disease prediction using machine learning. The system provides users with an intuitive interface to input medical parameters and receive real-time predictions with detailed PDF reports.

**Model Accuracy:** 97.40% (SVM-based classifier)

## Key Features

- 🌐 **Responsive Web Interface** – Built with Flask, HTML5, and modern CSS
- 🔐 **User Authentication** – Secure registration and login system with SQLite database
- 🏥 **Medical Input Form** – Comprehensive cardiovascular health parameters
- 📊 **ML Prediction Engine** – Trained SVM model for disease detection
- 📄 **PDF Report Generation** – Auto-generated patient reports with recommendations
- 🎨 **Professional UI** – Dark theme with background images and intuitive form layout

## Project Structure

```
├── app.py                          # Flask application (main entry point)
├── run.ps1                         # PowerShell startup script
├── run.bat                         # Windows batch startup
├── requirements.txt                # Python dependencies
├── evaluation.db                   # SQLite user database
│
├── Cardiovascular-Disease Prediction/
│   ├── HEART_DISEASE_MODEL.joblib # Trained ML model (SVM)
│   ├── new.csv                    # Training dataset
│   ├── images/                    # Reference images
│   └── requirements.txt           # Dependencies for legacy code
│
├── templates/                     # HTML templates
│   ├── home.html                 # Landing page
│   ├── login.html                # User login
│   ├── register.html             # User registration
│   ├── predict.html              # Prediction form
│   └── result.html               # Prediction result page
│
└── static/                        # Static assets
    └── images/                    # Background images and UI assets
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone Repository
```bash
git clone https://github.com/chandan123jha/Cardiovascular-Disease-Prediction.git
cd Cardiovascular-Disease-Prediction
```

### Step 2: Create & Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r Cardiovascular-Disease\ Prediction/requirements.txt
```

### Step 4: Run Application
**Option A: Using PowerShell (Windows)**
```bash
.\run.ps1
```

**Option B: Direct Python**
```bash
python app.py
```

**Option C: Using Batch File (Windows)**
```bash
run.bat
```

The application will start on `http://127.0.0.1:5000`

## Usage

1. **Register** – Create a new account with email and credentials
2. **Login** – Authenticate with your username and password
3. **Enter Health Data** – Fill in cardiovascular parameters:
   - Age, Sex, Chest Pain Type
   - Blood Pressure, Cholesterol, Fasting Blood Sugar
   - ECG Results, Heart Rate, Exercise Indicators
   - ST Depression, Slope, Major Vessels, Thalassemia
4. **Get Prediction** – Model predicts abnormality risk
5. **Download Report** – Generate and save PDF report

## Input Parameters Guide

| Parameter | Range | Description |
|-----------|-------|-------------|
| Age | 29-77 | Patient age in years |
| Sex | 0/1 | 0=Female, 1=Male |
| Chest Pain | 1/2/3 | 1=Typical, 2=Asymptomatic, 3=Non-typical |
| Trestbps | 90-200 | Resting blood pressure (mm Hg) |
| Chol | 126-564 | Serum cholesterol (mg/dl) |
| FBS | 0/1 | Fasting blood sugar > 120 mg/dl |
| RestECG | 0/1/2 | ECG result type |
| Thalach | 71-202 | Maximum heart rate achieved |
| ExANG | 0/1 | Exercise induced angina |
| Old Peak | 0-6.2 | ST depression by exercise |
| Slope | 1/2/3 | Peak ST segment slope |
| Ca | 0-4 | Major vessels by fluoroscopy |
| Thal | 1/2/3 | Thalassemia type |

## Architecture

### Backend
- **Framework:** Flask (Python)
- **Database:** SQLite3
- **ML Model:** scikit-learn SVM classifier
- **Report Generation:** FPDF

### Frontend
- **HTML5** – Semantic structure
- **CSS3** – Responsive design with gradients and animations
- **Vanilla JavaScript** – Form validation and interactions

### Model Details
- **Algorithm:** Support Vector Machine (SVM)
- **Training Set:** 297 samples from Indian hospitals
- **Features:** 13 cardiovascular parameters
- **Accuracy:** 97.40%

## Database Schema

### Registration Table
```sql
CREATE TABLE registration (
    Fullname TEXT,
    address TEXT,
    username TEXT,
    Email TEXT,
    Phoneno TEXT,
    Gender TEXT,
    age TEXT,
    password TEXT
)
```

## API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/login` | GET, POST | User login |
| `/register` | GET, POST | User registration |
| `/predict` | GET, POST | Prediction form & results |
| `/download/<path>` | GET | Download PDF report |
| `/logout` | GET | User logout |

## Dependencies

See `Cardiovascular-Disease Prediction/requirements.txt`:
- Flask
- scikit-learn
- pandas
- numpy
- fpdf
- joblib

## Future Enhancements

- [ ] Docker containerization
- [ ] Mobile app (React Native/Flutter)
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] API endpoint for third-party integrations
- [ ] Email report delivery
- [ ] Real-time prediction statistics

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with:
- Clear commit messages
- Updated documentation
- Test coverage where applicable

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

## Author

**Chandan Kumar**  
GitHub: [@chandan123jha](https://github.com/chandan123jha)

---

**Last Updated:** April 2026


