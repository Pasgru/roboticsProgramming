import pandas as pd

# Load the CSV file
file_path = 'pre-owned-cars.csv'  # Replace with your file's path
df = pd.read_csv(file_path)

# Data Cleaning Function
def clean_data(df):
    # Select the desired columns
    columns_to_keep = ['brand', 'transmission', 'make_year', 'fuel_type', 'km_driven', 'price']
    df = df[columns_to_keep]

    # Drop rows with missing values
    df = df.dropna()

    # Convert price from INR to Euros
    df['price'] = df['price'] * 0.011

    return df

# Clean the data
cleaned_df = clean_data(df)

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = 'cleaned_data.csv'
cleaned_df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned file saved to {cleaned_file_path}")
