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


def find_similar():
    # params: movie_name=, attributes=["Director", "Runtime", etc]
    pass


def director_stats(director_name: str) -> dict:
    if not isinstance(director_name, str):
        raise TypeError("director_name must be a string")
    if not director_name.strip():
        raise ValueError("director_name must not be empty or whitespace")

    df = _load_movies()
    query = director_name.strip().lower()

    matched_rows = []
    canonical_name = None

    for _, row in df.iterrows():
        directors = [d.strip() for d in str(row["directors"]).split(",")]
        for d in directors:
            if d.lower() == query:
                if canonical_name is None:
                    canonical_name = d
                matched_rows.append(row)
                break

    if not matched_rows:
        raise ValueError(f"No director found matching '{director_name}'")

    genres = set()
    for row in matched_rows:
        for g in str(row["genre"]).split(","):
            genres.add(g.strip())

    ratings = [float(row["rating"]) for row in matched_rows]
    avg_rating = round(sum(ratings) / len(ratings), 2)

    best_movie = max(matched_rows, key=lambda r: float(r["rating"]))["name"]

    total_box_office = 0
    for row in matched_rows:
        try:
            total_box_office += int(row["box_office"])
        except (ValueError, TypeError):
            pass

    return {
        "director": canonical_name,
        "num_movies": len(matched_rows),
        "avg_rating": avg_rating,
        "genres": sorted(genres),
        "best_movie": best_movie,
        "total_box_office": total_box_office,
    }
