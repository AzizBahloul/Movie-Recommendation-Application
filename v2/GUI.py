import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
import sqlite3
import joblib
import pandas as pd
import model_retrain
from prediction import predict_rating

def add_watched_movie(name, year, rating, genres, description):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO movies (name, year, rating, genre, description)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, year, rating, ', '.join(genres), description))
    
    conn.commit()
    conn.close()
    
    # Retrain model after adding new movie
    model_retrain.train_model()

def submit_add_movie():
    name = name_entry.get()
    year = year_entry.get()
    rating = rating_entry.get()
    genres = [genre for genre in genre_vars if genre_vars[genre].get()]
    description = description_text.get("1.0", tk.END).strip()
    
    if not name or not year or not rating or not genres or not description:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
        return
    
    add_watched_movie(name, int(year), rating, genres, description)
    messagebox.showinfo("Success", "Movie added and model retrained successfully!")

def submit_prediction():
    name = pred_name_entry.get()
    year = pred_year_entry.get()
    genres = [genre for genre in pred_genre_vars if pred_genre_vars[genre].get()]
    
    if not name or not year or not genres:
        messagebox.showwarning("Input Error", "Please fill in all fields for prediction.")
        return
    
    predicted_rating = predict_rating(name, int(year), genres)
    messagebox.showinfo("Prediction", f"Predicted rating for '{name}': {predicted_rating}")

app = tk.Tk()
app.title("Movie App")

# Create notebook (tabs)
notebook = ttk.Notebook(app)
add_tab = tk.Frame(notebook)
predict_tab = tk.Frame(notebook)
notebook.add(add_tab, text="Add Movie")
notebook.add(predict_tab, text="Predict Rating")
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# Add Movie Tab
tk.Label(add_tab, text="Movie Name:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
name_entry = tk.Entry(add_tab, width=40)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(add_tab, text="Year:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
year_entry = tk.Entry(add_tab, width=40)
year_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(add_tab, text="Rating (e.g., 5/10):").grid(row=2, column=0, sticky='e', padx=5, pady=5)
rating_entry = tk.Entry(add_tab, width=40)
rating_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(add_tab, text="Description:").grid(row=3, column=0, sticky='ne', padx=5, pady=5)
description_text = scrolledtext.ScrolledText(add_tab, width=40, height=5)
description_text.grid(row=3, column=1, padx=5, pady=5)

tk.Label(add_tab, text="Genres:").grid(row=4, column=0, sticky='ne', padx=5, pady=5)
genre_vars = {genre: tk.BooleanVar() for genre in [
    'Science Fiction', 'Crime', 'Drama', 'Sci-Fi', 'Comedy', 'Romance', 'Action', 
    'Thriller', 'War', 'Musical', 'Adventure', 'History', 'Biography', 'Horror', 
    'Mystery', 'Film-Noir', 'Fantasy', 'Animation', 'Family', 'Western', 'Music', 
    'Sport', 'Documentary'
]}

for i, genre in enumerate(genre_vars):
    tk.Checkbutton(add_tab, text=genre, variable=genre_vars[genre]).grid(row=4 + (i // 3) + 1, column=i % 3, sticky='w', padx=5, pady=2)

tk.Button(add_tab, text="Add Movie", command=submit_add_movie).grid(row=4 + (len(genre_vars) // 3) + 1, column=1, pady=10)

# Predict Rating Tab
tk.Label(predict_tab, text="Movie Name:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
pred_name_entry = tk.Entry(predict_tab, width=40)
pred_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(predict_tab, text="Year:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
pred_year_entry = tk.Entry(predict_tab, width=40)
pred_year_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(predict_tab, text="Genres:").grid(row=2, column=0, sticky='ne', padx=5, pady=5)
pred_genre_vars = {genre: tk.BooleanVar() for genre in [
    'Science Fiction', 'Crime', 'Drama', 'Sci-Fi', 'Comedy', 'Romance', 'Action', 
    'Thriller', 'War', 'Musical', 'Adventure', 'History', 'Biography', 'Horror', 
    'Mystery', 'Film-Noir', 'Fantasy', 'Animation', 'Family', 'Western', 'Music', 
    'Sport', 'Documentary'
]}

for i, genre in enumerate(pred_genre_vars):
    tk.Checkbutton(predict_tab, text=genre, variable=pred_genre_vars[genre]).grid(row=2 + (i // 3) + 1, column=i % 3, sticky='w', padx=5, pady=2)

tk.Button(predict_tab, text="Predict Rating", command=submit_prediction).grid(row=2 + (len(pred_genre_vars) // 3) + 1, column=1, pady=10)

if __name__ == "__main__":
    app.mainloop()
