#!/usr/bin/env python3
"""
Test script to diagnose model loading issues
"""
import joblib
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_model_loading():
    """Test loading and using the weather prediction model"""
    try:
        print("=== Testing Model Loading ===")
        
        # Load the model
        model_data = joblib.load('combined_weather_models_geo.joblib')
        print(f"✓ Model loaded successfully. Type: {type(model_data)}")
        
        # Check if it's a dictionary
        if isinstance(model_data, dict):
            print(f"✓ Model is a dictionary with keys: {list(model_data.keys())}")
            
            # Check each model in the dictionary
            weather_models = {}
            for key, value in model_data.items():
                print(f"  - {key}: {type(value)}")
                if hasattr(value, 'predict'):
                    weather_models[key] = value
                    print(f"    ✓ Has predict method")
                else:
                    print(f"    ✗ No predict method")
            
            if weather_models:
                print(f"✓ Found {len(weather_models)} valid models: {list(weather_models.keys())}")
                
                # Test prediction with sample data
                print("\n=== Testing Predictions ===")
                
                # Create sample input (12 features as expected by the model)
                sample_input = np.array([[
                    5.6,      # latitude (Accra)
                    -0.2,     # longitude (Accra)
                    28.0,     # temperature
                    75.0,     # humidity
                    1013.25,  # pressure
                    5.0,      # wind speed
                    10.0,     # rainfall likelihood
                    8,        # month
                    223,      # day of year
                    33.0,     # max temp
                    23.0,     # min temp
                    15        # day of month
                ]])
                
                print(f"Sample input shape: {sample_input.shape}")
                print(f"Sample input: {sample_input[0]}")
                
                # Test each model
                for weather_type, weather_model in weather_models.items():
                    try:
                        prediction = weather_model.predict(sample_input)
                        print(f"✓ {weather_type}: {prediction}")
                    except Exception as e:
                        print(f"✗ {weather_type} failed: {e}")
                        
            else:
                print("✗ No valid models found!")
                
        else:
            print(f"✓ Model is not a dictionary, type: {type(model_data)}")
            if hasattr(model_data, 'predict'):
                print("✓ Model has predict method")
                
                # Test with sample data
                sample_input = np.array([[5.6, -0.2, 28.0, 75.0, 1013.25, 5.0, 10.0, 8, 223, 33.0, 23.0, 15]])
                prediction = model_data.predict(sample_input)
                print(f"✓ Prediction: {prediction}")
            else:
                print("✗ Model has no predict method")
        
    except Exception as e:
        print(f"✗ Error loading model: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_model_loading()
