# Weather Prediction Website

A simple web application that uses a trained machine learning model to predict weather conditions based on location input.

## Features

- **Location Input**: Enter any city, state, or country name
- **Geocoding**: Automatically converts location names to coordinates
- **Weather Prediction**: Uses a trained joblib model to predict weather conditions
- **Modern UI**: Clean, responsive design with real-time feedback
- **Error Handling**: Comprehensive error handling for invalid locations and server issues

## Files Structure

```
My weather/
├── app.py                           # Flask backend application
├── templates/
│   └── index.html                   # Frontend HTML template
├── combined_weather_models_geo.joblib # The trained ML model
├── requirements.txt                 # Python dependencies
└── README.md                       # This file
```

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter a location in the input field (e.g., "New York", "London", "Tokyo")
2. Click "Predict Weather" button
3. View the prediction results including:
   - Location name
   - Coordinates (latitude, longitude)
   - Predicted weather condition

## API Endpoints

- `GET /` - Main page with the web interface
- `POST /predict` - Weather prediction endpoint
- `GET /health` - Health check endpoint

## Model Requirements

The application expects your model (`combined_weather_models_geo.joblib`) to:
- Accept input features as [latitude, longitude]
- Return a weather condition prediction

If your model requires different input features, you may need to modify the `input_features` preparation in `app.py`.

## Troubleshooting

- **Model not loading**: Ensure `combined_weather_models_geo.joblib` is in the same directory as `app.py`
- **Location not found**: Try using more specific location names or major cities
- **Dependencies issues**: Make sure all packages in `requirements.txt` are installed

## Customization

You can customize the application by:
- Modifying the CSS in `templates/index.html` for different styling
- Adjusting the input features in `app.py` based on your model's requirements
- Adding more sophisticated error handling or logging
