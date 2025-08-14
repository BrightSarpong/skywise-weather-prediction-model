# Development Documentation

## 1. Development Environment Setup

### 1.1 Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git
- Web browser (Chrome/Firefox recommended)

### 1.2 Installation Steps

#### Clone the Repository
```bash
git clone https://github.com/yourusername/skycast.git
cd skycast
```

#### Create Virtual Environment (Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### 1.3 Running the Application
```bash
# Start the development server
python app.py
```

## 2. Project Structure

```
skycast/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   └── ...
├── models/                # Machine learning models
│   └── weather_model.joblib
├── docs/                  # Documentation
└── tests/                 # Test files
```

## 3. Core Components

### 3.1 Backend (Flask)

#### Main Application (app.py)
```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# API Endpoints
@app.route('/api/weather', methods=['GET'])
def get_weather():
    # Implementation here
    pass
```

### 3.2 Frontend

#### Main JavaScript (static/js/main.js)
```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    initializeApp();
    
    // Set up event listeners
    setupEventListeners();
});

function initializeApp() {
    // Initialize map, load saved locations, etc.
}
```

## 4. Feature Implementation

### 4.1 Location Detection
```javascript
function getCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const { latitude, longitude } = position.coords;
                updateWeatherForLocation(latitude, longitude);
            },
            error => {
                console.error("Error getting location:", error);
                showError("Unable to retrieve your location");
            }
        );
    } else {
        showError("Geolocation is not supported by your browser");
    }
}
```

### 4.2 Weather Prediction
```python
def predict_weather(latitude, longitude, date):
    """
    Predict weather for given location and date
    
    Args:
        latitude (float): Latitude coordinate
        longitude (float): Longitude coordinate
        date (str): Date in YYYY-MM-DD format
        
    Returns:
        dict: Weather prediction data
    """
    # Implementation details
    pass
```

## 5. Testing

### 5.1 Running Tests
```bash
python -m pytest tests/
```

### 5.2 Test Coverage
```bash
pytest --cov=.
```

## 6. Deployment

### 6.1 Production Dependencies
```bash
pip install gunicorn
```

### 6.2 Running with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 7. Version Control

### 7.1 Git Workflow
```bash
# Create a new branch
git checkout -b feature/new-feature

# Stage changes
git add .

# Commit changes
git commit -m "Add new feature"

# Push to remote
git push origin feature/new-feature
```

## 8. Troubleshooting

### 8.1 Common Issues

#### Module Not Found
```bash
pip install -r requirements.txt
```

#### Port Already in Use
```bash
# Find and kill the process
netstat -ano | findstr :5000
taskkill /PID [PID] /F
```

## 9. API Documentation

### 9.1 Weather Endpoints

#### GET /api/weather/current
- **Description**: Get current weather for a location
- **Parameters**:
  - `lat` (required): Latitude
  - `lon` (required): Longitude
- **Response**:
  ```json
  {
    "temperature": 28.5,
    "humidity": 75,
    "wind_speed": 5.2,
    "condition": "Sunny"
  }
  ```

## 10. Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
