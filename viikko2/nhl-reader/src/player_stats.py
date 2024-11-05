from player import Player
from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader: PlayerReader) -> None:
        self.players: list[Player] = reader.fetch_players()

    def top_scorers_by_nationality(self, nationality: str, max_count = 10) -> list[Player]:
        players = [player for player in self.players if nationality in player.nationality]
        players.sort(key=lambda player: player.assists + player.goals, reverse=True)
        return players[0:max_count - 1]