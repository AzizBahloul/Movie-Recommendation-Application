import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit,
    QTextEdit, QCheckBox, QPushButton, QMessageBox, QTabWidget, QHBoxLayout
)
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

class MovieApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the application window
        self.setWindowTitle("Movie App")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(self.get_stylesheet())

        # Set up the layout
        self.layout = QVBoxLayout(self)

        # Create tab widget
        self.tabs = QTabWidget()
        self.add_tab = QWidget()
        self.predict_tab = QWidget()
        self.tabs.addTab(self.add_tab, "Add Movie")
        self.tabs.addTab(self.predict_tab, "Predict Rating")

        self.layout.addWidget(self.tabs)

        self.setup_add_movie_tab()
        self.setup_predict_rating_tab()

        # Animation example
        self.animate_widgets()

    def get_stylesheet(self):
        return """
            QWidget {
                background-color: #1e1e1e;  /* Dark blue */
                color: #e0e0e0;
                font-family: Arial, sans-serif;
            }
            QPushButton {
                background-color: #5a5a5a;
                border: none;
                color: #ffffff;
                padding: 10px;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #7a7a7a;
            }
            QTextEdit, QLineEdit {
                background-color: #2e2e2e;
                color: #e0e0e0;
                border: 1px solid #5a5a5a;
                border-radius: 5px;
            }
            QLabel {
                color: #e0e0e0;
                font-size: 16px;
            }
            QTabBar::tab {
                background-color: #3a3a3a;
                color: #e0e0e0;
                padding: 10px;
                border-radius: 5px;
            }
            QTabBar::tab:selected {
                background-color: #5a5a5a;
            }
        """

    def setup_add_movie_tab(self):
        layout = QFormLayout()

        self.name_entry = QLineEdit()
        self.year_entry = QLineEdit()
        self.year_entry.setPlaceholderText("e.g., 2023")
        self.rating_entry = QLineEdit()
        self.rating_entry.setPlaceholderText("e.g., 5/10")
        self.description_text = QTextEdit()
        self.description_text.setPlaceholderText("Enter description here...")

        self.genre_checkboxes = self.create_genre_checkboxes()

        layout.addRow(QLabel("Movie Name:"), self.name_entry)
        layout.addRow(QLabel("Year:"), self.year_entry)
        layout.addRow(QLabel("Rating (e.g., 5/10):"), self.rating_entry)
        layout.addRow(QLabel("Description:"), self.description_text)

        genre_widget = self.create_genre_widget(self.genre_checkboxes)
        layout.addRow(QLabel("Genres:"), genre_widget)

        self.add_button = QPushButton("Add Movie")
        self.add_button.clicked.connect(self.submit_add_movie)
        layout.addWidget(self.add_button)

        self.add_tab.setLayout(layout)

    def setup_predict_rating_tab(self):
        layout = QFormLayout()

        self.pred_name_entry = QLineEdit()
        self.pred_year_entry = QLineEdit()
        self.pred_year_entry.setPlaceholderText("e.g., 2023")
        self.pred_genre_checkboxes = self.create_genre_checkboxes()

        layout.addRow(QLabel("Movie Name:"), self.pred_name_entry)
        layout.addRow(QLabel("Year:"), self.pred_year_entry)

        genre_widget = self.create_genre_widget(self.pred_genre_checkboxes)
        layout.addRow(QLabel("Genres:"), genre_widget)

        self.predict_button = QPushButton("Predict Rating")
        self.predict_button.clicked.connect(self.submit_prediction)
        layout.addWidget(self.predict_button)

        self.predict_tab.setLayout(layout)

    def create_genre_checkboxes(self):
        genres = [
            'Science Fiction', 'Crime', 'Drama', 'Sci-Fi', 'Comedy', 'Romance', 
            'Action', 'Thriller', 'War', 'Musical', 'Adventure', 'History', 
            'Biography', 'Horror', 'Mystery', 'Film-Noir', 'Fantasy', 
            'Animation', 'Family', 'Western', 'Music', 'Sport', 'Documentary'
        ]
        return {genre: QCheckBox(genre) for genre in genres}

    def create_genre_widget(self, genre_checkboxes):
        genre_layout = QVBoxLayout()
        for checkbox in genre_checkboxes.values():
            genre_layout.addWidget(checkbox)
        
        genre_widget = QWidget()
        genre_widget.setLayout(genre_layout)
        return genre_widget

    def submit_add_movie(self):
        name = self.name_entry.text().strip()
        year = self.year_entry.text().strip()
        rating = self.rating_entry.text().strip()
        genres = [genre for genre in self.genre_checkboxes if self.genre_checkboxes[genre].isChecked()]
        description = self.description_text.toPlainText().strip()

        if not name or not year or not rating or not genres or not description:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        if not year.isdigit() or not (1900 <= int(year) <= 2100):
            QMessageBox.warning(self, "Input Error", "Please enter a valid year (1900-2100).")
            return

        if not self.is_valid_rating(rating):
            QMessageBox.warning(self, "Input Error", "Please enter a valid rating (e.g., 5/10).")
            return

        # Add watched movie logic here
        # add_watched_movie(name, int(year), rating, genres, description)
        # model_retrain.train_model()

        QMessageBox.information(self, "Success", "Movie added and model retrained successfully!")

    def is_valid_rating(self, rating):
        try:
            score, total = map(int, rating.split('/'))
            return 0 <= score <= total
        except ValueError:
            return False

    def submit_prediction(self):
        name = self.pred_name_entry.text().strip()
        year = self.pred_year_entry.text().strip()
        genres = [genre for genre in self.pred_genre_checkboxes if self.pred_genre_checkboxes[genre].isChecked()]

        if not name or not year or not genres:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields for prediction.")
            return

        if not year.isdigit() or not (1900 <= int(year) <= 2100):
            QMessageBox.warning(self, "Input Error", "Please enter a valid year (1900-2100).")
            return

        # Predict rating logic here
        # predicted_rating = predict_rating(name, int(year), genres)
        
        predicted_rating = "8/10"  # Example prediction result
        QMessageBox.information(self, "Prediction", f"Predicted rating for '{name}': {predicted_rating}")

    def animate_widgets(self):
        # Example animation: Fade in the window
        self.setWindowOpacity(0)
        animation = QPropertyAnimation(self, b"windowOpacity")
        animation.setDuration(1000)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec_())