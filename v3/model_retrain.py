import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import joblib

def fetch_data():
    conn = sqlite3.connect('movies.db')
    query = 'SELECT * FROM movies'
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def preprocess_data(df):
    df['genre'] = df['genre'].str.split(', ').apply(lambda x: ' '.join(sorted(x)))
    df['text_features'] = df['name'] + ' ' + df['description'] + ' ' + df['genre']
    X = df[['year', 'text_features']]
    y = df['rating']
    return X, y

def train_model():
    df = fetch_data()
    if len(df) < 10:  # Ensure there is enough data
        print("Not enough data to train the model.")
        return
    
    X, y = preprocess_data(df)
    
    # Create a preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', MinMaxScaler(), ['year']),
            ('text', TfidfVectorizer(stop_words='english'), 'text_features')
        ])
    
    # Create a pipeline
    model = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', MultinomialNB())
    ])
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Fit the model
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, 'movie_model.pkl')
    
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    train_model()