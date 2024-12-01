import joblib
import pandas as pd
from robot.api import logger

def load_model_and_predict(input_file='output.txt'):
    # Load the saved model
    model = joblib.load('car_price_predictor_model.pkl')
    
    # Read the input data from the file
    with open(input_file, 'r') as f:
        car_data = f.readline().strip()
    
    # Split the data based on semicolons (you may adjust if it's different)
    data_parts = car_data.split(';')
    
    # Check if the data has all the required parts
    if len(data_parts) != 6:
        print("Error: Input data is incomplete.")
        return

    # Extract individual values from the input data
    brand = data_parts[0]
    transmission = data_parts[1]
    make_year = data_parts[2]
    fuel_type = data_parts[3]
    km_driven = data_parts[4]

    # Preprocess: Map 'Schaltgetriebe' to 'Manual' and 'Benzin' to 'Petrol'
    transmission_mapping = {
        'Schaltgetriebe': 'Manual',  # Map Schaltgetriebe to Manual
        'Automatik': 'Automatic',  # Assuming the input can contain 'Automatik' for automatic transmission
    }
    
    fuel_type_mapping = {
        'Benzin': 'Petrol',  # Map Benzin to Petrol
        'Diesel': 'Diesel',  # Keep Diesel as Diesel
    }
    
    # Apply the mappings
    transmission = transmission_mapping.get(transmission, transmission)  # Default to original if no mapping
    fuel_type = fuel_type_mapping.get(fuel_type, fuel_type)  # Default to original if no mapping

    # Clean and preprocess the data
    # Extract only the brand name (first word from the brand string)
    brand = brand.split(' ')[0].strip()  # Get the first word (brand name)

    # Clean the other values
    make_year = make_year.split('/')[1]
    km_driven = km_driven.replace(' km', '').replace('.', '').strip()
    
    # Convert km_driven to integer and make_year to integer
    km_driven = int(km_driven.replace(' ', ''))
    make_year = int(make_year.strip().split('/')[0])  # Extract just the year

    # Prepare the input data in the same format as the training data
    example = pd.DataFrame([{
        'brand': brand,
        'transmission': transmission,
        'make_year': make_year,
        'fuel_type': fuel_type,
        'km_driven': km_driven
    }])

    # Make the prediction
    predicted_price = model.predict(example)

    # Print the predicted price
    print(f"Predicted Price for the car: {predicted_price[0]:.2f} Euros")

    return predicted_price[0]
