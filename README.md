# Arctic Fox Movies

## About this project

**Arctic Fox Movies** is a Python package built around the [IMDB Top 250 movies](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset) dataset from Kaggle. The movies in that list are the usual suspects—classics and fan favorites—with details like title, year, genre, cast, directors, and runtime.

The package is meant to be something you can import in your own scripts or run from the command line to get movie ideas, play a quick game, or look up facts without building a full application.

## What you can do with it

The package exposes several functions that work together around the same CSV data:

- **Pick a movie for tonight** — Filter by things you care about (for example genres to skip, how long you’re willing to sit, or a minimum rating) and get a suggestion.
- **Play a quiz** — The computer picks a movie from the list and gives you clues (such as director, runtime, and year). You try to guess the title from those hints.
- **Look up an actor** — Find which movies in the dataset feature a given actor in a leading role, especially once the dataset is enriched with clearer billing information.
- **Find similar movies** — Start from a title you like and ask for other films that match on chosen details (director, runtime, and so on).
- **See simple stats** — For a director (and optional details like time period), get a small summary of genre or career-oriented patterns in the data.


## Tests and course work

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.
