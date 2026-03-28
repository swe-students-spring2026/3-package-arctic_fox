import pytest
from arcticfoxmovies.movies import director_stats


# --- Happy path ---

def test_director_stats_returns_all_keys():
    result = director_stats("Christopher Nolan")
    assert set(result.keys()) == {"director", "num_movies", "avg_rating", "genres", "best_movie", "total_box_office"}


def test_director_stats_num_movies_positive_int():
    result = director_stats("Christopher Nolan")
    assert isinstance(result["num_movies"], int)
    assert result["num_movies"] > 0


def test_director_stats_avg_rating_in_range():
    result = director_stats("Christopher Nolan")
    assert isinstance(result["avg_rating"], float)
    assert 0.0 <= result["avg_rating"] <= 10.0


def test_director_stats_best_movie_is_string():
    result = director_stats("Christopher Nolan")
    assert isinstance(result["best_movie"], str)
    assert len(result["best_movie"]) > 0


def test_director_stats_genres_nonempty_list():
    result = director_stats("Christopher Nolan")
    assert isinstance(result["genres"], list)
    assert len(result["genres"]) > 0


def test_director_stats_total_box_office_nonnegative():
    result = director_stats("Christopher Nolan")
    assert isinstance(result["total_box_office"], (int, float))
    assert result["total_box_office"] >= 0


# --- Edge case: case-insensitive match ---

def test_director_stats_case_insensitive():
    result_lower = director_stats("christopher nolan")
    result_canonical = director_stats("Christopher Nolan")
    assert result_lower == result_canonical


def test_director_stats_canonical_name_returned():
    result = director_stats("christopher nolan")
    assert result["director"] == "Christopher Nolan"


# --- Invalid input ---

def test_director_stats_raises_type_error_on_int():
    with pytest.raises(TypeError):
        director_stats(123)


def test_director_stats_raises_type_error_on_none():
    with pytest.raises(TypeError):
        director_stats(None)


def test_director_stats_raises_value_error_on_unknown_director():
    with pytest.raises(ValueError):
        director_stats("Fake Director Who Does Not Exist")


def test_director_stats_raises_value_error_on_empty_string():
    with pytest.raises(ValueError):
        director_stats("")


def test_director_stats_raises_value_error_on_whitespace():
    with pytest.raises(ValueError):
        director_stats("   ")
