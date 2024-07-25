import sqlite3

def create_database():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    # Create table with description field
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        rating TEXT CHECK(rating LIKE '%/10') NOT NULL,
        genre TEXT NOT NULL,
        description TEXT
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")