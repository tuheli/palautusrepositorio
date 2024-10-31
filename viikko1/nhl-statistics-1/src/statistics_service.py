from player_reader import PlayerReader
from player import Player
from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService:
    def __init__(self, reader: PlayerReader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by = SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points
        
        def sort_by_goals(player: Player):
            return player.goals
        
        def sort_by_assists(player: Player):
            return player.assists
        
        if sort_by == SortBy.POINTS:
            key_to_use = sort_by_points

        if sort_by == SortBy.ASSISTS:
            key_to_use = sort_by_assists
        
        if sort_by == SortBy.GOALS:
            key_to_use = sort_by_goals

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=key_to_use
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
