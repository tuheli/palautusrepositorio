from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, Not, Or, PlaysIn

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.matcher = matcher

    def build(self):
        return self.matcher

    def plays_in(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))

    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
        query
        .plays_in("NYR")
        .has_at_least(10, "goals")
        .has_fewer_than(20, "goals")
        .build()
        )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
