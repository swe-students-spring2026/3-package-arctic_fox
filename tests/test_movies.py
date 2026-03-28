import pytest
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
