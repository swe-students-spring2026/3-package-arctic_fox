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
