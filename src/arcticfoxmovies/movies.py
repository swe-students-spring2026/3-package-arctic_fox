"""
Create your movie methods here
"""
from pathlib import Path

import pandas as pd
import random

_DATA_CSV = Path(__file__).resolve().parents[2] / "data" / "IMDB Top 250 Movies.csv"

def _load_movies():
    return pd.read_csv(_DATA_CSV)


def movie_night_picker():
    # params: genres_to_avoid=None, runtime_max=150, minimum_rating
    pass


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
    guess = input("Your guess: ")
    if guess.lower().strip() == result["answer"].lower().strip():
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


def find_similar():
    # params: movie_name=, attributes=["Director", "Runtime", etc]
    pass


def _parse_runtime(runtime_str: str) -> int:
    """Parse '2h 22m', '1h 45m', '142m' etc. into total minutes."""
    import re
    hours = re.search(r'(\d+)h', str(runtime_str))
    minutes = re.search(r'(\d+)m', str(runtime_str))
    total = 0
    if hours:
        total += int(hours.group(1)) * 60
    if minutes:
        total += int(minutes.group(1))
    return total


def genre_stats(genre_name: str) -> dict:
    if not isinstance(genre_name, str):
        raise TypeError("genre_name must be a string")
    if not genre_name.strip():
        raise ValueError("genre_name must not be empty or whitespace")

    df = _load_movies()
    query = genre_name.strip().lower()

    matched_rows = []
    canonical_name = None

    for _, row in df.iterrows():
        genres = [g.strip() for g in str(row["genre"]).split(",")]
        for g in genres:
            if g.lower() == query:
                if canonical_name is None:
                    canonical_name = g
                matched_rows.append(row)
                break

    if not matched_rows:
        raise ValueError(f"No genre found matching '{genre_name}'")

    ratings = [float(row["rating"]) for row in matched_rows]
    avg_rating = round(sum(ratings) / len(ratings), 2)
    best_movie = max(matched_rows, key=lambda r: float(r["rating"]))["name"]
    worst_movie = min(matched_rows, key=lambda r: float(r["rating"]))["name"]

    runtimes = [_parse_runtime(row["run_time"]) for row in matched_rows]
    runtimes = [r for r in runtimes if r > 0]
    avg_runtime_minutes = round(sum(runtimes) / len(runtimes)) if runtimes else 0

    from collections import Counter
    actor_counts = Counter()
    for row in matched_rows:
        lead = str(row["casts"]).split(",")[0].strip()
        if lead:
            actor_counts[lead] += 1
    top_actors = [actor for actor, _ in actor_counts.most_common(3)]

    return {
        "genre": canonical_name,
        "num_movies": len(matched_rows),
        "avg_rating": avg_rating,
        "best_movie": best_movie,
        "worst_movie": worst_movie,
        "avg_runtime_minutes": avg_runtime_minutes,
        "top_actors": top_actors,
    }
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
