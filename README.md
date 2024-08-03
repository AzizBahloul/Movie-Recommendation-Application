

# Movie Recommendation Application

Welcome to the Movie Recommendation Application! This Python project allows users to input movies they’ve watched and predicts if they will like new movies based on AI models. The application utilizes various AI techniques to offer personalized movie recommendations.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up the Virtual Environment](#set-up-the-virtual-environment)
  - [Activate the Virtual Environment](#activate-the-virtual-environment)
  - [Install the Dependencies](#install-the-dependencies)
- [Usage](#usage)
  - [Run the Application](#run-the-application)
  - [Enter Movies](#enter-movies)
  - [Predict New Movies](#predict-new-movies)
- [File Execution Order](#file-execution-order)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a Python application designed to recommend movies based on user preferences and ratings. By analyzing user input and historical data, the application predicts the likelihood of users enjoying new movies. It features a graphical user interface built with PyQt5 and leverages AI models for making recommendations.

## Installation

### Clone the Repository

Start by cloning the repository from GitHub:
```sh
git clone https://github.com/AzizBahloul/movie-recommendation.git
cd movie-recommendation
```

### Set Up the Virtual Environment

Create a virtual environment using the following command:
```sh
python3 -m venv venv
```

### Activate the Virtual Environment

Activate the virtual environment:
- **On Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

### Install the Dependencies

Install the required Python packages:
```sh
pip install -r requirements.txt
```

## Usage

### Run the Application

To start the application, follow these steps:

#### File Execution Order for v2 and v3

For versions `v2` and `v3`, ensure you follow this execution order:

1. **Create the Database:**
   ```sh
   python createDB.py
   ```

2. **Insert Fake Data (for testing purposes):**
   ```sh
   python insert_fake_data.py
   ```

3. **Retrain the Model:**
   ```sh
   python model_retrain.py
   ```

4. **Launch the GUI:**
   ```sh
   python GUI.py
   ```

### Enter Movies

Use the GUI to enter movies you have watched. The application will use this information to tailor its recommendations.

### Predict New Movies

Once movies have been entered, use the application to predict if you will like new movies based on your preferences and the AI models.

## Specific Structure

For the `v2` and `v3` versions, the project structure includes the following key files:

- **`createDB.py`**: Script to set up the database.
- **`insert_fake_data.py`**: Script to insert sample data into the database.
- **`model_retrain.py`**: Script to retrain the recommendation model.
- **`GUI.py`**: Script to launch the graphical user interface.
- **`prediction.py`**: Script for making predictions (included in both `v2` and `v3`).

## Contributing

Contributions are welcome. Please follow standard open-source guidelines for contributing to the project. Ensure to review the code and test thoroughly before submitting a pull request.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

