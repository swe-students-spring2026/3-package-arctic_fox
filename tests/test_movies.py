import pytest
<<<<<<< HEAD
from arcticfoxmovies.movies import genre_stats


# --- Happy path ---

def test_genre_stats_returns_all_keys():
    result = genre_stats("Drama")
    assert set(result.keys()) == {"genre", "num_movies", "avg_rating", "best_movie", "worst_movie", "avg_runtime_minutes", "top_actors"}


def test_genre_stats_num_movies_positive_int():
    result = genre_stats("Drama")
    assert isinstance(result["num_movies"], int)
    assert result["num_movies"] > 0


def test_genre_stats_avg_rating_in_range():
    result = genre_stats("Drama")
    assert isinstance(result["avg_rating"], float)
    assert 0.0 <= result["avg_rating"] <= 10.0


def test_genre_stats_best_movie_is_string():
    result = genre_stats("Drama")
    assert isinstance(result["best_movie"], str)
    assert len(result["best_movie"]) > 0


def test_genre_stats_worst_movie_is_string():
    result = genre_stats("Drama")
    assert isinstance(result["worst_movie"], str)
    assert len(result["worst_movie"]) > 0


def test_genre_stats_avg_runtime_positive():
    result = genre_stats("Drama")
    assert isinstance(result["avg_runtime_minutes"], int)
    assert result["avg_runtime_minutes"] > 0


def test_genre_stats_top_actors_list():
    result = genre_stats("Drama")
    assert isinstance(result["top_actors"], list)
    assert 1 <= len(result["top_actors"]) <= 3


# --- Case-insensitive ---

def test_genre_stats_case_insensitive():
    assert genre_stats("drama") == genre_stats("Drama")


def test_genre_stats_canonical_name_returned():
    result = genre_stats("drama")
    assert result["genre"] == "Drama"


# --- Invalid input ---

def test_genre_stats_raises_type_error_on_int():
    with pytest.raises(TypeError):
        genre_stats(123)


def test_genre_stats_raises_type_error_on_none():
    with pytest.raises(TypeError):
        genre_stats(None)


def test_genre_stats_raises_value_error_on_unknown():
    with pytest.raises(ValueError):
        genre_stats("FakeGenreThatDoesNotExist")


def test_genre_stats_raises_value_error_on_empty():
    with pytest.raises(ValueError):
        genre_stats("")


def test_genre_stats_raises_value_error_on_whitespace():
    with pytest.raises(ValueError):
        genre_stats("   ")
=======
from arcticfoxmovies.movies import (
    movie_night_picker, 
    quiz, 
    lead_actor, 
    find_movie_by_director, 
    genre_roulette
)



def test_find_movie_by_director():
    # Assertion 1: Valid input returns a list
    assert isinstance(find_movie_by_director("Christopher Nolan"), list)
    
    # Assertion 2: Bad type raises ValueError
    with pytest.raises(ValueError):
        find_movie_by_director(["Christopher Nolan"])
        
    # Assertion 3: Empty string raises ValueError
    with pytest.raises(ValueError):
        find_movie_by_director("")


def test_genre_roulette():
    # Assertion 1: Bad genre type raises ValueError
    with pytest.raises(ValueError):
        genre_roulette(123)
        
    # Assertion 2: Bad avoid_year type raises ValueError
    with pytest.raises(ValueError):
        genre_roulette("Action", avoid_year="2020")
        
    # Assertion 3: Bizarre genre returns the fallback string
    result = genre_roulette("Underwater Basket Weaving")
    assert isinstance(result, str)
    assert "No Underwater Basket Weaving movies found" in result


def test_quiz():
    # Assertion 1: Valid call returns a dict with the expected keys
    result = quiz()
    assert isinstance(result, dict)
    assert "question" in result
    assert "answer" in result
    assert "director" in result
    assert "runtime" in result
    assert "year" in result

    # Assertion 2: Answer and year look like usable movie data
    assert isinstance(result["answer"], str)
    assert len(result["answer"]) > 0
    assert isinstance(result["year"], int)

    # Assertion 3: Question text includes the clues shown in the dict
    assert "Guess the movie:" in result["question"]
    assert result["director"] in result["question"]
    assert result["runtime"] in result["question"]
    assert str(result["year"]) in result["question"]

>>>>>>> c2a315538a4d2c94042867df1b4a62f91c341df8
