import sqlite3

def insert_fake_data():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    
    # Extended fake data with descriptions
    fake_data = [
        ('A Hidden Life', 2019, '5/10', 'Biography, Drama, Romance', 'The story of an Austrian farmer who refused to fight for the Nazis in World War II.'),
        ('The Matrix', 1999, '10/10', 'Action, Sci-Fi', 'A computer programmer discovers a dystopian world inside a simulation.'),
        ('Inception', 2010, '9/10', 'Action, Adventure, Sci-Fi', 'A thief with the ability to enter people\'s dreams takes on an impossible task.'),
        ('The Godfather', 1972, '10/10', 'Crime, Drama', 'The aging patriarch of an organized crime dynasty transfers control to his son.'),
        ('The Shawshank Redemption', 1994, '10/10', 'Drama', 'Two imprisoned men bond over a number of years, finding solace and redemption through acts of common decency.'),
        ('Interstellar', 2014, '9/10', 'Adventure, Drama, Sci-Fi', 'A team of explorers travels through a wormhole in space in an attempt to ensure humanity\'s survival.'),
        ('Pulp Fiction', 1994, '9/10', 'Crime, Drama', 'The lives of two mob hitmen, a boxer, a gangster\'s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'),
        ('The Dark Knight', 2008, '10/10', 'Action, Crime, Drama', 'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.'),
        ('Forrest Gump', 1994, '9/10', 'Drama, Romance', 'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate, and other historical events unfold from the perspective of an Alabamian man with an IQ of 75.'),
        ('Gladiator', 2000, '8/10', 'Action, Adventure, Drama', 'A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.'),
        ('The Lord of the Rings: The Fellowship of the Ring', 2001, '10/10', 'Adventure, Drama, Fantasy', 'A young hobbit, Frodo Baggins, embarks on a perilous journey to destroy a powerful ring sought by the dark lord Sauron.'),
        ('The Departed', 2006, '8/10', 'Crime, Drama, Thriller', 'An undercover cop and a mole in the police try to identify each other while infiltrating an Irish gang in Boston.'),
        ('Fight Club', 1999, '9/10', 'Drama', 'An insomniac office worker and a soap salesman build a global organization to help vent male aggression.'),
        ('The Silence of the Lambs', 1991, '9/10', 'Crime, Drama, Thriller', 'A young FBI cadet must confide in an incarcerated and manipulative killer to receive his help on catching another serial killer.'),
        ('Back to the Future', 1985, '8/10', 'Adventure, Comedy, Sci-Fi', 'A teenager is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend.'),
        ('Jurassic Park', 1993, '9/10', 'Action, Adventure, Sci-Fi', 'During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.'),
        ('The Revenant', 2015, '8/10', 'Action, Adventure, Drama', 'In the 1820s, a frontiersman on a quest for vengeance against those who left him for dead after a bear attack, battles for survival.'),
        ('Mad Max: Fury Road', 2015, '8/10', 'Action, Adventure, Sci-Fi', 'In a post-apocalyptic wasteland, a drifter teams up with a group of rebels to overthrow a tyrannical warlord.'),
    ]
    
    cursor.executemany('''
    INSERT INTO movies (name, year, rating, genre, description)
    VALUES (?, ?, ?, ?, ?)
    ''', fake_data)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_fake_data()
    print("Fake data inserted successfully!")
