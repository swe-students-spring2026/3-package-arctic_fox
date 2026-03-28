"""
Create your movie methods here
"""
import pandas as pd
import random
movies_df = pd.read_csv("data/IMDB Top 250 Movies.csv")

def movie_night_picker():
    # params: genres_to_avoid=None, runtime_max=150, minimum_rating
    pass


def quiz():
    # params: attributes=["Director", "Runtime", "Year", etc]
    pass


def lead_actor(actor):
    # params: actor= 
    if type(actor) != str:
        raise ValueError("Actor must be a string")
    movie_list = []
    for _, row in movies_df.iterrows():
        if row["casts"].split(",")[0] == actor:
            movie_list.append(row["name"])
    return movie_list


def find_movie_by_director(director):
    # params: director
    if type(director) != str:
        raise ValueError("Director must be a string")

    director = director.strip()
    if not director:
        raise ValueError("Director cannot be empty")

    movie_list = []
    for _, row in movies_df.iterrows():
        directors = [name.strip() for name in str(row["directors"]).split(",")]
        if director in directors:
            movie_list.append(row["name"])

    return movie_list

def genre_roulette(genre, avoid_year=None):
    # params: genre, avoid_year
    if type(genre) != str:
        raise ValueError("Genre must be a string")

    genre = genre.strip()
    if not genre:
        raise ValueError("Genre cannot be empty")

    if avoid_year is not None and type(avoid_year) != int:
        raise ValueError("avoid_year must be an integer or None")

    candidates = []
    for _, row in movies_df.iterrows():
        genres = [item.strip() for item in str(row["genre"]).split(",")]
        if genre in genres:
            if avoid_year is None or int(row["year"]) != avoid_year:
                candidates.append(row["name"])

    if not candidates:
        return f"No {genre} movies found. Try another genre!"

    return random.choice(candidates)
