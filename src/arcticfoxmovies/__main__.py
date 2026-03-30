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
            print("  colloborators <colloborator1, colloborator2> - Find movies with collobrators")
            print("  quiz <director, runtime, year>")
            print("  movie night picker <actor, rating, runtime>")
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
                print("Provide atleast one atribute: runtime, rating, genre-to-avoid")
                return
            
            if len(sys.argv) == 3:
                movies.movie_night_picker(sys.argv[2])
            elif len(sys.argv) == 4:
                movies.movie_night_picker(sys.argv[2], sys.argv[3])
            else:
                movies.movie_night_picker(sys.argv[2], sys.argv[3], [sys.argv[4]])
        
        elif sys.argv[1] == "find-movie-by-director":
            if len(sys.argv) < 3:
                print("Give the director please")
                return 
        
            director = sys.argv[2]
            try:
                movies.find_movie_by_director(director)
            except ValueError as e:
                print(f"Error {e}")



if __name__ == "__main__":
    main()