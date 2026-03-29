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


def test_quiz_happy():
    #Assertion 1: Valid input returns a dict with expected keys
    result = quiz()
    assert isinstance(result, dict)
    assert "question" in result
    assert "answer" in result
    assert "director" in result
    assert "runtime" in result
    assert "year" in result

def test_quiz_edge():
    #Assertion 2: For movies with multiple directors
    result = quiz()
    assert "," not in result["director"]
    assert result["director"] in result["question"]

def test_quiz_invalid():
    #Assertion 3: Invalid quiz data raises an error
    result = quiz(attributes=123) 
    #Should still return the question as attributes is not used in the quiz function 
    assert isinstance(result, dict)
    assert "question" in result