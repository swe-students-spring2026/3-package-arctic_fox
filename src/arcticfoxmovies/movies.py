"""
Create your movie methods here
"""
from pathlib import Path

import pandas as pd

_DATA_CSV = Path(__file__).resolve().parents[2] / "data" / "IMDB Top 250 Movies.csv"

def _load_movies():
    return pd.read_csv(_DATA_CSV)


def movie_night_picker():
    # params: genres_to_avoid=None, runtime_max=150, minimum_rating
    pass


# Guess the movie based on clues - director, runtime, year.
def quiz(attributes=None):
    df = _load_movies()

    # pick random movie
    movie = df.sample(1).iloc[0]

    movie_name = movie["name"]
    director = str(movie["directors"]).split(",")[0].strip()
    runtime = str(movie["run_time"]).strip()
    year = int(movie["year"])

    question = (
        f"Guess the movie:\n"
        f"- Director: {director}\n"
        f"- Runtime: {runtime}\n"
        f"- Year: {year}"
    )

    print(question)

    return {
        "question": question,
        "answer": movie_name,
        "director": director,
        "runtime": runtime,
        "year": year,
    }


def lead_actor():
    # params: actor=
    pass


def find_similar():
    # params: movie_name=, attributes=["Director", "Runtime", etc]
    pass
