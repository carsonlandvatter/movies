# Overview

What I'm trying to accomplish as a software engineer to deepen my learning is understanding how to interact with and use a SQL Relational Database. 

The software that I wrote here is a command-line movie library. This integrates with a SQL Relational Database by performing specific CRUD operations to retrieve, update, delete, or view all of the movies. The way you use the program is you'll first start by initiating the application using python3 movies.py. Once you begin it, you'll see a menu of options that you can choose between. You can either see out list of movies, add a new movie, update and existing movie, change the rotten tomato rating of a movie, see the stats of all of the movies, delete a movie, or quit the application. 

The reason why I wrote this software is because I am first and foremost obsessed with going to the movie theater and watching all sorts of new movies. I thought it would be awesome to create and application where I could include all of my favorite movies to reference in the future.

Demo Video: https://youtu.be/zaorw6LQG8Q 

# Relational Database

I used a SQLite relational database. The database itself lives inside of movies.db in the repository.

The table I made for this relational database was a movies table that has 5 columns: id, title, director, rating, and length. Each row for the table would be a separate movie with each of these columns filled in. 

# Development Environment

The tools I used to develop the software was python and sqlite. Along with the journey, I was able to watch youtube videos that demonstrated how to use python and sqlite to create a software application. I also was able to read a lot of documentation that I will attach here down below. 

The programming language I chose to use was python and I used the sqlite3 library so that I would be able to interact with the relational database. 

# Useful Websites

{Make a list of websites that you found helpful in this project}

- How to Easily Create a SQLite Database https://www.youtube.com/watch?v=XSZE1iiKdSw 
- Python Getting Started - W3 Schools https://www.w3schools.com/python/python_getstarted.asp 

# Future Work

- Figure out a way to have it show hours and minutes in the stats for the total length of movies.
- Provide a way for the user to give their own rating of the movie.
- Allow users to update other items for each movie instead of just the movie rating. 