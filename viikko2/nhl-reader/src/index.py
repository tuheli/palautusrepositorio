import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players: list[Player] = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")

    finnish_players = [player for player in players if "FIN" in player.nationality]

    finnish_players.sort(key=lambda player: player.assists + player.goals, reverse=True)

    for player in finnish_players:
        print(player)


if __name__ == "__main__":
    main()