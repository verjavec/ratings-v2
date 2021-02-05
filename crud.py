import datetime

""" CRUD operations """
from model import db, User, Movie, Rating, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """ Return all of the users """

    return User.query.all()

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """ Return all of the movies """

    return Movie.query.all()

def create_rating(user, movie, score):
    """ Create and return a new rating for a movie. """

    rating = Rating(user=user, movie=movie,score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movie_by_id(movie_id):
    """ Get a movie using movie_id and return the movie """

    return Movie.query.get(movie_id)

def get_user_by_id(user_id):
    """ Get a user using user_id and return the user """

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""
    
    return User.query.filter(User.email == email).first()


    

