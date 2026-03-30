import pytest
from arcticfoxmovies.movies import (
    quiz, 
    find_movie_by_director, 
    genre_roulette,
    find_collabs
)


def test_colloborators():

    #happy path
    assert isinstance(find_collabs("tweedledee", "tweedledoo"), list)

    assert "The Shawshank Redemption" in find_collabs("Morgan Freeman", "Tim Robbins")

    assert "The Shawshank Redemption" in find_collabs("Tim Robbins", "Morgan Freeman")

    assert len(find_collabs("blah", "crah")) == 0

    #Invalid input cases cases -

    with pytest.raises(TypeError):
        find_collabs(1, "hello", "three")

    with pytest.raises(ValueError):
        find_collabs("hello", None)
    
    with pytest.raises(TypeError):
        find_collabs(1)
    
    with pytest.raises(TypeError):
        find_collabs()
    

    #Edge cases - same colloborators
    with pytest.raises(ValueError):
        find_collabs("Hello", "Hello")
    
    #Partial name match

    results = find_collabs("Robins", "Morgan Freeman")

    assert len(results) == 0

    #Lowercase Upper Case

    assert "The Shawshank Redemption" in find_collabs("MorGan Freeman", "Tim RObbins")

    #Trailing Whitespace

    assert "The Shawshank Redemption" in find_collabs("  MorGan Freeman   ", "  Tim RObbins ")
    






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
    result = quiz(["director", "runtime", "year"])
    assert isinstance(result, dict)
    assert "question" in result
    assert "answer" in result
    assert "director" in result
    assert "runtime" in result
    assert "year" in result

def test_quiz_edge():
    #Assertion 2: For movies with multiple directors
    result = quiz(["director", "runtime", "year"])
    assert "," not in result["director"]
    #year should be an int, not string
    assert isinstance(result["year"], int)
    #runtime and answer should be non empty strings
    assert isinstance(result["runtime"], str) and len(result["runtime"]) > 0
    assert isinstance(result["answer"], str) and len(result["answer"]) > 0

def test_quiz_invalid():
    #not a list
    with pytest.raises(ValueError):
        quiz(123)
    #empty list
    with pytest.raises(ValueError):
        quiz([])
    #invalid attribute
    with pytest.raises(ValueError):
        quiz(["invalid_attribute"])
