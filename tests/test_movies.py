import pytest
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

