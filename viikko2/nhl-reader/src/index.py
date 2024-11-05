import requests
from player import Player
from rich.console import Console
from rich.table import Table


season_options = [
    "2023-24",
    "2024-25",
]

nationalty_options = [
    "FIN",
    "SWE",
    "USA",
]

class PlayerReader:
    def __init__(self, url: str) -> None:
        self.url = url

    def fetch_players(self) -> list[Player]:
        response = requests.get(self.url).json()
        players: list[Player] = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players

        
class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.players: list[Player] = reader.fetch_players()

    def top_scorers_by_nationality(self, nationality: str, max_count = 10) -> list[Player]:
        players = [player for player in self.players if nationality in player.nationality]
        players.sort(key=lambda player: player.assists + player.goals, reverse=True)
        return players[0:max_count - 1]


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