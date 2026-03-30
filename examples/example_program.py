"""Example program that demonstrates all public package features."""

from __future__ import annotations

import argparse
from pprint import pprint

from arcticfoxmovies.movies import (
    find_collabs,
    find_shape_of_dataframe,
    find_movie_by_director,
    genre_roulette,
    lead_actor,
    movie_night_picker,
    play_quiz,
    quiz,
)


def main(play_quiz_game: bool = False, show_dataframe_shape: bool = False) -> None:
    print("Arctic Fox Movies - Example Program")

    print("\n1) movie_night_picker")
    pick = movie_night_picker(
        genres_to_avoid=["Horror"],
        runtime_max=180,
        minimum_rating=8.0,
    )
    pprint(pick)

    print("\n2) quiz")
    quiz_result = quiz(["director", "runtime", "year"])
    print(quiz_result["question"])
    print("Sample answer:", quiz_result["answer"])

    print("\n3) lead_actor")
    lead_movies = lead_actor("Tom Hanks")
    print(lead_movies[:5])

    print("\n4) find_collabs")
    collabs = find_collabs("Morgan Freeman", "Tim Robbins")
    print(collabs)

    print("\n5) find_movie_by_director")
    directed = find_movie_by_director("Christopher Nolan")
    print(directed[:5])

    print("\n6) genre_roulette")
    roulette_pick = genre_roulette("Drama", avoid_year=1994)
    print(roulette_pick)

    print("\n7) play_quiz")
    if play_quiz_game:
        play_quiz(["director", "runtime", "year"])
    else:
        print("Skipped interactive quiz. Re-run with --play-quiz to enable it.")

    print("\n8) find_shape_of_dataframe")
    if show_dataframe_shape:
        find_shape_of_dataframe()
    else:
        print("Skipped dataframe preview. Re-run with --show-dataframe-shape to enable it.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Arctic Fox Movies examples")
    parser.add_argument(
        "--play-quiz",
        action="store_true",
        help="Enable the interactive play_quiz demo.",
    )
    parser.add_argument(
        "--show-dataframe-shape",
        action="store_true",
        help="Print dataframe head/tail preview using find_shape_of_dataframe.",
    )
    args = parser.parse_args()
    main(
        play_quiz_game=args.play_quiz,
        show_dataframe_shape=args.show_dataframe_shape,
    )
