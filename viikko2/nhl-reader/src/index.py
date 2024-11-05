import requests
from player import Player


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

    def top_scorers_by_nationality(self, nationality: str) -> list[Player]:
        players = [player for player in self.players if nationality in player.nationality]

        players.sort(key=lambda player: player.assists + player.goals, reverse=True)
        
        return players


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN:")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()