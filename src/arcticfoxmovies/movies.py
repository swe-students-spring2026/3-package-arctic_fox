"""
Create your movie methods here
"""
import pandas as pd
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


def find_similar():
    # params: movie_name=, attributes=["Director", "Runtime", etc]
    pass
