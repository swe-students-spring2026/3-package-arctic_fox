"""
Everyone's movie methods. Still waiting on 1 group member as of March 27th
"""
from pathlib import Path

import pandas as pd
import random

_DATA_CSV = Path(__file__).resolve().parents[2] / "data" / "IMDB Top 250 Movies.csv"

def _load_movies():
    return pd.read_csv(_DATA_CSV)

# Guess the movie based on clues - director, runtime, year.

def movie_night_picker(genres_to_avoid=None, runtime_max=150, minimum_rating=8.0):
    # params: genres_to_avoid=None, runtime_max=150, minimum_rating
    
    df = _load_movies()
    
    df['run_time'] = df['run_time'].astype(str).str.extract('(\d+)').astype(float) * 60

    # Filter by rating or runtime
    df = df[df['run_time'] <= runtime_max]
    df = df[df['rating'] >= minimum_rating]

    # Filter out genres to avoid 
    if genres_to_avoid:
        avoid = [g.lower() for g in genres_to_avoid]

        def is_safe(genre_str):
            return not any(g in genre_str.lower() for g in avoid)
        
        df = df[df['genre'].apply(is_safe)]

    if df.empty:
        return "No movies match your criteria!"
    
    winner = df.sample(1).iloc[0]

    return {
        "title": winner['name'],
        "year": winner['year'], 
        "rating": winner['rating'],
        "genre": winner['genre'],
        "run_time": winner['run_time']
    }

def quiz(attributes):
    df = _load_movies()

    if not isinstance(attributes, list) or len(attributes) == 0 or not all(attr in ["director", "runtime", "year"] for attr in attributes):
        raise ValueError("Attributes must be a non-empty list containing any of: 'director', 'runtime', 'year'")
        
    # pick random movie
    movie = df.sample(1).iloc[0]
    movie_name = movie["name"]
    director = str(movie["directors"]).split(",")[0].strip()
    runtime = str(movie["run_time"]).strip()
    year = int(movie["year"])

    map = {
        "director": f"- Director: {director}",
        "runtime": f"- Runtime: {runtime}",
        "year": f"- Year: {year}"
    }

    clues = [map[attr] for attr in attributes]

    question = f"Guess the movie based on these clues:\n" + "\n".join(clues)

    return {
        "question": question,
        "answer": movie_name,
        "director": director,
        "runtime": runtime,
        "year": year,
    }

#Actually play the quiz game 
def play_quiz(attributes):
    result = quiz(attributes)
    print(result["question"])
    guess =input("Your guess: ")

    #TODO Ethan you need to define answer here - I put in python if down below
    answer = "Hello"
    if guess.lower().strip == result[answer].lower().strip() if result.get(answer) else "random":
        print("Correct!")
    else:
        print(f"Wrong! The answer was: {result['answer']}")


def lead_actor(actor):
    # params: actor= 
    movies_df = _load_movies()
    if type(actor) != str:
        raise ValueError("Actor must be a string")
    movie_list = []
    for _, row in movies_df.iterrows():
        if row["casts"].split(",")[0] == actor:
            movie_list.append(row["name"])
    return movie_list

def find_collabs(person1: str, person2: str) -> list[str]:
    df = pd.read_csv(_DATA_CSV)

    if (not (person1 and person2)):
        raise ValueError("Make sure no None values in input")

    if type(person1) != str or type(person2) != str:
        raise ValueError("Both values need to be strings")

    #first make evrryone lower case + whitespace clear for normalization sake
    person1 = person1.lower().strip()
    person2 = person2.lower().strip()

    if person1 == person2:
        raise ValueError("People cannot colloborate with each other")

    collabs = []

    for _, row in df.iterrows():

        #look at my utility function - i confirmed that IMDB splits by comma
        #so, if multiple directors or writers per movie, we can "combine everyone" via commas
        full_cast = row["directors"].lower() + "," \
                     + row["writers"].lower() + "," \
                     + row["casts"].lower()
        members = set(full_cast.split(","))

        if person1 in members and person2 in members:
            collabs.append(row["name"])
    
    return collabs


def find_movie_by_director(director):
    # params: director
    movies_df = _load_movies()
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
    movies_df = _load_movies()
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


def find_shape_of_dataframe(path: str | None = None) -> None: 
    #Utility function for me to figure otu what I can work with after other trials

    if not path:
        path = _DATA_CSV

    df = pd.read_csv(path)
    print(df.head())
    print(df.tail())
    #print(df.rows())




