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
def quiz(attributes):
    df = _load_movies()

    if not isinstance(attributes,list) or len(attributes) == 0:
        raise ValueError("Attributes must be a non-empty list of strings")
    valid_attributes = {"director", "runtime", "year"}
    if not all(attr in valid_attributes for attr in attributes):
        raise ValueError("Invalid attributes in attributes list")

    # pick random movie
    movie = df.sample(1).iloc[0]
    movie_name = movie["name"]
    director = str(movie["directors"]).split(",")[0].strip()
    runtime = str(movie["run_time"]).strip()
    year = int(movie["year"])

    map = {
        "director": f"- Director: {director}",
        runtime: f"- Runtime: {runtime}",
        year: f"- Year: {year}"
    }


    #Ethan I am commenting out your code cuz it is not compiling yet. I will discuss this w u monday
    #clues = map[attr] for attr in attributes]

    #question = f"Guess the movie based on these clues:\n" + "\n".join(clues)


    return {
        #"question": question,
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



