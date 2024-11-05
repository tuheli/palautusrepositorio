from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

season_options = [
    "2023-24",
    "2024-25",
]

nationalty_options = [
    "FIN",
    "SWE",
    "USA",
]

def main():
    console = Console()
    console.print("\nNHL statistics by nationality")
    
    user_input_season = console.input(f"\nSelect season {season_options}: ")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{user_input_season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        user_input_nationality = console.input(f"\nSelect nationality {nationalty_options} ('exit' to quit): ")

        if user_input_nationality == "exit":
            break

        players = stats.top_scorers_by_nationality(user_input_nationality)

        console.print(f"\nTop 10 scorers of {user_input_nationality} season {user_input_season}:\n")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name")
        table.add_column("Team")
        table.add_column("Goals")
        table.add_column("Assists")
        table.add_column("Points")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                f"{player.goals}",
                f"{player.assists}",
                f"{player.assists + player.goals}",
            )

        console.print(table)

if __name__ == "__main__":
    main()