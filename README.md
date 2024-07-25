# Movie Recommendation Application

Welcome to the Movie Recommendation Application! This project allows users to enter movies they've watched and predict if they will like new movies based on AI models.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
    - [Clone the Repository](#clone-the-repository)
    - [Set Up the Virtual Environment](#set-up-the-virtual-environment)
    - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [Install the Dependencies](#install-the-dependencies)
3. [Usage](#usage)
    - [Run the Application](#run-the-application)
    - [Enter Movies](#enter-movies)
    - [Predict New Movies](#predict-new-movies)
4. [File Execution Order](#file-execution-order)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

This project is a Python application designed to recommend movies based on user preferences and ratings. It uses various AI models to make predictions about whether a user will like a new movie.

## Installation

Follow these steps to set up the project on your local machine:

### Clone the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/AzizBahloul/movie-recommendation.git
cd movie-recommendation
```
For creating a venv, you can use the following command:
```bash
python3 -m venv venv
```
Then, you can activate the venv using the following command:
```bash
source venv/bin/activate
```

After activating the venv, you can install the required packages using the following command:
```bash
pip install -r requirements.txt
```
### File Execution Order (for v3 and v2)
Follow this order to execute the files in your project:

1)createDB.py
2)insert_fake_data.py
3)model_retrain.py
4)GUI.py
gui.py: Contains the PyQt5 GUI code.


