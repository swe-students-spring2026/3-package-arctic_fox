import sys
import arcticfoxmovies.movies as movies


def main():
    """Main entry point for the package."""
    print("🎬 Arctic Fox Movies 🎬")
    print("=" * 40)

    if len(sys.argv) >= 2:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("Usage: python -m arcticfoxmovies <command> <args>")
            print("Commands:")
            print("  lead_actor <actor_name> - Find movies with a specific lead actor")
            print("  colloborators <colloborator1> <colloborator2> - Find movies with collobrators")
            print("  quiz <director, runtime, year>")
            print("  movie-night-picker <runtime_max> <minimum_rating> <genres_to_avoid>")
            print("  find-movie-by-director <director_name>")
            print("  genre-roulette <genre>")
            return

        elif sys.argv[1] == "lead_actor":
            actor_name = sys.argv[2]
            if not actor_name:
                print("Error: Actor name is required")
                return
            print(f"\nSearching for movies with: {actor_name}")
            result = movies.lead_actor(actor_name)
            if result:
                print(f"Found: {result}")
            else:
                print("No movies found")
        
        elif sys.argv[1] == "colloborators":
            if len(sys.argv) < 4:
                print("Error: provide two colloborators")
                return
            
            colloborator_name_1 = sys.argv[2]
            colloborator_name_2 = sys.argv[3]
            if not colloborator_name_1 or not colloborator_name_2:
                print("Error: Colloborator name is required")
                return
            print(f"\nSearching for movies with: {colloborator_name_1} and {colloborator_name_2}")
            result = movies.find_collabs(colloborator_name_1, colloborator_name_2)
            if result:
                print(f"Found: {result}")
            else:
                print("No movies found")

        elif sys.argv[1] == "quiz":
            if len(sys.argv) < 3:
                print("Error: Provide at least one attribute: director, runtime, year")
                return
            attributes = sys.argv[2:]
            try:
                movies.play_quiz(attributes)
            except ValueError as e:
                print(f"Error: {e}")

        elif sys.argv[1] == "movie-night-picker":
            if len(sys.argv) < 3:
                print("Provide at least runtime_max (e.g., 150)")
                return

            try:
                runtime_max = int(sys.argv[2])
                minimum_rating = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
                genres_to_avoid = sys.argv[4].split(",") if len(sys.argv) > 4 else None
            except ValueError:
                print("Error: runtime_max must be int and minimum_rating must be float")
                return

            result = movies.movie_night_picker(
                genres_to_avoid=genres_to_avoid,
                runtime_max=runtime_max,
                minimum_rating=minimum_rating,
            )
            print(f"Result: {result}")
        
        elif sys.argv[1] == "find-movie-by-director":
            if len(sys.argv) < 3:
                print("Give the director please")
                return

            director = sys.argv[2]
            try:
                result = movies.find_movie_by_director(director)
                print(f"Found: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif sys.argv[1] == "genre-roulette":
            if len(sys.argv) < 3:
                print("Error: Provide a genre")
                return

            genre = sys.argv[2]

            try:
                avoid_year = int(sys.argv[3]) if len(sys.argv) > 3 else None
            except ValueError:
                print("Error: year-to-avoid must be an integer")
                return

            try:
                result = movies.genre_roulette(genre, avoid_year=avoid_year)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()