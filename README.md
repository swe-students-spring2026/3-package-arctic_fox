[![Python package](https://github.com/swe-students-spring2026/3-package-arctic_fox/actions/workflows/python-package.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-arctic_fox/actions/workflows/python-package.yml)

# Arctic Fox Movies

Arctic Fox Movies is a lighthearted Python package for exploring the IMDB Top 250 dataset and discovering what to watch next.

It includes tools to:

- pick a movie based on your constraints,
- generate a movie quiz from random clues,
- search by lead actor,
- find collaboration movies between two people,
- list movies by a director, and
- spin a random pick by genre.

Dataset source: [IMDB Top 250 Movies (Kaggle)](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset)

## PyPI

- Package page: [https://pypi.org/project/arctic-fox-movies/](https://pypi.org/project/arctic-fox-movies/)
- Install command: `pip install arctic-fox-movies`

## Example Program

The project uses the package entry point in
`src/arcticfoxmovies/__main__.py`.

Run the program from the repository root:

```bash
pipenv run python -m arcticfoxmovies --help
```

## Function Reference

Import path:

```python
from arcticfoxmovies.movies import (
	movie_night_picker,
	quiz,
	play_quiz,
	lead_actor,
	find_collabs,
	find_movie_by_director,
	genre_roulette,
	find_shape_of_dataframe,
)
```

### `movie_night_picker(genres_to_avoid=None, runtime_max=150, minimum_rating=8.0)`

Returns either a movie dictionary or the fallback string `"No movies match your criteria!"`.

```python
movie = movie_night_picker(
	genres_to_avoid=["Horror", "War"],
	runtime_max=180,
	minimum_rating=8.3,
)
print(movie)
```

### `quiz(attributes)`

Builds a quiz question and returns quiz metadata.

Allowed values in `attributes` are `"director"`, `"runtime"`, and `"year"`.

```python
q = quiz(["director", "year"])
print(q["question"])
print("Answer:", q["answer"])
```

### `play_quiz(attributes)`

Interactive wrapper around `quiz(...)`.

```python
play_quiz(["director", "runtime", "year"])
```

### `lead_actor(actor)`

Returns movies where `actor` appears as the first listed cast member.

```python
tom_hanks_movies = lead_actor("Tom Hanks")
print(tom_hanks_movies[:5])
```

### `find_collabs(person1, person2)`

Returns movies where both people appear among directors, writers, or cast.

```python
shared = find_collabs("Morgan Freeman", "Tim Robbins")
print(shared)
```

### `find_movie_by_director(director)`

Returns all dataset movies directed by `director`.

```python
nolan_movies = find_movie_by_director("Christopher Nolan")
print(nolan_movies)
```

### `genre_roulette(genre, avoid_year=None)`

Returns one random movie title for `genre`, optionally skipping one year.

```python
pick = genre_roulette("Drama", avoid_year=1994)
print(pick)
```

## Developer Setup

### 1. Prerequisites

- Python 3.9+ (CI currently validates 3.9, 3.10, 3.11)
- `pip`
- `pipenv`

Install `pipenv` if needed:

```bash
python -m pip install --user pipenv
```

### 2. Clone and install dependencies

```bash
git clone https://github.com/swe-students-spring2026/3-package-arctic_fox.git
cd 3-package-arctic_fox
pipenv install --dev
pipenv run pip install -e .
```

### 3. Run tests

```bash
pipenv run pytest
```

### 4. Build package artifacts

```bash
pipenv run python -m build
```

Artifacts are produced in `dist/`.

### 5. Validate artifacts and upload to PyPI

```bash
pipenv run twine check dist/*
pipenv run twine upload dist/*
```

## Configuration and Data

- No local `.env` file is required to run this package.
- The dataset ships in the repository at `data/IMDB Top 250 Movies.csv`.
- No database setup or seed/import step is required.

## Teammates

- [ZhiHui Chen](https://github.com/zc3716)
-
-
-

## License

Licensed under the MIT License. See [LICENSE](LICENSE).

## Course Exercise

This repository is part of the package engineering exercise documented in [instructions.md](instructions.md).
