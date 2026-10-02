#import pythons sqlite library
import sqlite3

#connect to the database
connection = sqlite3.connect("movies.db")

#get everything that actually runs SQL. Every query will go through cursor
cursor = connection.cursor()

#create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY, 
        title TEXT,
        director TEXT,
        rating INTEGER,
        length INTEGER
    )
""")

#function that allows you to add a movie
def add_movie():
    title = input("\nTitle: ")
    director = input("Director: ")
    rating = int(input("Rotten Tomatoes Rating (1-100): "))
    length = int(input("Minutes Long: "))

    cursor.execute(
        #insert the input values into the parameters
        "INSERT INTO movies (title, director, rating, length) VALUES (?, ?, ?, ?)",
        (title, director, rating, length)
    )
    connection.commit()
    print("\nMovie added.")

#function that lists all of the movies
def list_movies():
    #execute the sql query
    cursor.execute("SELECT id, title, director, rating, length FROM movies")
    #fetch the query
    movies = cursor.fetchall()

    #loop over each item that comes back from the query that was fetched
    if movies:
        for movie in movies: 
            print(f"{movie[0]}. {movie[1]} by {movie[2]} - {movie[3]}% Rotten Tomatoes, {movie[4]} minutes")
    else: 
        print("\nNo movies to display.")

#function that updates each movie's rating
def update_rating():
    #first, let's list all of the movies.
    list_movies()
    #then, based off of the movie id, the user can decide which movie they want to update
    movie_id = int(input("\nID of movie to update: "))
    new_rating = int(input("New rotten tomatoes rating (1-100): "))

    cursor.execute(
        "UPDATE movies SET rating = ? WHERE id = ?",
        (new_rating, movie_id)
    )
    connection.commit()
    print("\nRating updated.")

#function that deletes a movie
def delete_movie():
    list_movies()
    movie_id = int(input("\nID of movie to delete: "))

    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    connection.commit()
    print("\nMovie deleted.")

def show_stats():
    cursor.execute("SELECT ROUND(AVG(rating), 1), SUM(length) FROM movies")
    stats = cursor.fetchone()

    print(f"\nAverage rating: {stats[0]}")
    print(f"Total minutes: {stats[1]}")

#create a menu where each user can decide what they want to do with the movies
while True:
    print("\n1. Add a movie")
    print("2. List movies")
    print("3. Update rating")
    print("4. Delete a movie")
    print("5. Show stats")
    print("6. Quit")

    decision = input("\nSelect an option: ")

    if decision == "1":
        add_movie()
    elif decision == "2":
        list_movies()
    elif decision == "3":
        update_rating()
    elif decision == "4":
        delete_movie()
    elif decision == "5":
        show_stats()
    elif decision == "6":
        break

connection.close()