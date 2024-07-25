# Movie App

## Overview

The Movie App is a Python application with a graphical user interface (GUI) built using PyQt5. It allows users to:
- Add movies to a database with details such as name, year, rating, genres, and description.
- Predict ratings for movies based on user input.
- Automatically retrain machine learning models when new movies are added.

## Features

- **Add Movie**: Enter movie details, including name, year, rating, genres, and description. The data is stored in an SQLite database.
- **Predict Rating**: Predict the rating of a movie based on its name, year, and genres using a machine learning model.
- **Dark Blue and Purple Theme**: A modern and stylish GUI with a dark blue and purple theme.
- **Animations**: Smooth fade-in animation for a polished user experience.

## Requirements

Ensure you have Python 3.7 or later installed. You can install the required packages using the `requirements.txt` file.

### `requirements.txt`

```plaintext
PyQt5==5.15.9
pandas==2.0.3
scikit-learn==1.2.2
joblib==1.3.2
numpy==1.24.3
