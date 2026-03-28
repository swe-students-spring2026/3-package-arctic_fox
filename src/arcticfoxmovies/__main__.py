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
            return
            
        if sys.argv[1] == "lead_actor":
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


if __name__ == "__main__":
    main()