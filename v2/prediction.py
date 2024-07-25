import joblib
import pandas as pd

def predict_rating(name, year, genres):
    # Load the saved model
    model = joblib.load('movie_model.pkl')
    
    # Prepare the input data
    genres_str = ' '.join(sorted(genres))
    input_data = pd.DataFrame({
        'year': [year],
        'text_features': [f"{name} {genres_str}"]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    
    return prediction[0]

if __name__ == "__main__":
    # Example usage
    name = "The Avengers"
    year = 2023
    genres = ['Action', 'Sci-Fi']
    predicted_rating = predict_rating(name, year, genres)
    print(f"Predicted rating for '{name}' ({'/'.join(genres)}) from {year}: {predicted_rating}")