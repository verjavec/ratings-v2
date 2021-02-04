"""Script to seed database.

seed_database.py is one of the few files that you’ll write as a script. 
What this means for you is that you won’t have to define functions! 
Sounds scary, we know, but this file will only be used to re-create your database.

"""

import os
import json
# choice is a function that takes in a list and returns a random element in the list. 
# randint will return a random number within a certain range. 
# You’ll use both to generate fake users and ratings.
from random import choice, randint
from datetime import datetime 

import crud
import model
import server

# The first thing you do when re-creating a database is run dropdb and createdb. 
# You can get Python to run those commands for you using os.system.
os.system('dropdb ratings')
os.system('createdb ratings')

# If we had written from model import db, we’d be able to access db. 
# However, since it’s just import model, 
# you have to go through model before you can access db.
model.connect_to_db(server.app)
model.db.create_all()

# Then, load data from data/movies.json and save it to a variable:
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Now, movie_data will be a list of dictionaries that look like this:
# [{'overview': 'The near future, [...] search of the unknown.',
#   'poster_path': 'https://image.tmdb.org/t/p/original//xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg',
#   'release_date': '2019-09-20',
#   'title': 'Ad Astra'}
#   ...
#   ]

# Loop over each dictionary in movie_data and use it to supply arguments to crud.create_movie.

# Here’s how datetime.strptime works:
# datetime.strptime(date_string, format)
# Return a datetime corresponding to date_string, parsed according to format.

# In other words, it takes in two arguments:
# date_string — a string with a date in it (the data that you want to turn into a datetime object)
# format — a string that tells Python how the date is formatted. 

# Time format codes start with a percent sign followed by another character. 
# You can view all the different format codes here: https://strftime.org/

# Create movies, store them in list so we can use them
# to create fake ratings later


movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
    db_movie=crud.create_movie(title, overview, release_date, poster_path)

    movies_in_db.append(db_movie)


for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user=crud.create_user(email, password)
    
    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)
        crud.create_rating(user, random_movie, score)

