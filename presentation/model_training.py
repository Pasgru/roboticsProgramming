import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
file_path = 'cleaned_data.csv'  # Replace with your file's path
df = pd.read_csv(file_path)

# Split features and target
X = df.drop(columns=['price'])
y = df['price']

# Identify categorical and numerical columns
categorical_cols = ['brand', 'transmission', 'fuel_type']
numerical_cols = ['make_year', 'km_driven']

# Preprocessing: OneHotEncoding for categorical, StandardScaler for numerical
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(), categorical_cols)
    ])

# Create a pipeline with a Random Forest Regressor
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(random_state=42))
])

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:\nMAE: {mae:.2f}\nMSE: {mse:.2f}\nR² Score: {r2:.2f}")

# Save the entire model and preprocessor pipeline to a file
joblib.dump(model, 'car_price_predictor_model.pkl')  # Save model pipeline
print("Model saved to 'car_price_predictor_model.pkl'")

# Save the OneHotEncoders separately for categorical columns
# You can extract the encoder from the pipeline and save it
onehot_encoder = model.named_steps['preprocessor'].transformers_[1][1]
joblib.dump(onehot_encoder, 'onehot_encoder.pkl')  # Save OneHotEncoder for categorical features
print("OneHotEncoder saved to 'onehot_encoder.pkl'")

# Example prediction
example = pd.DataFrame([{
    'brand': 'Ford',
    'transmission': 'Manual',
    'make_year': 2021.0,
    'fuel_type': 'Diesel',
    'engine_capacity(CC)': 1498.0,
    'km_driven': 23480.0
}])

predicted_price = model.predict(example)
print(f"Predicted Price for example: {predicted_price[0]:.2f}")
