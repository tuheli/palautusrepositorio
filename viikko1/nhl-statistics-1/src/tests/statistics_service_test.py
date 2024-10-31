import unittest
from player import Player
from statistics_service import SortBy, StatisticsService

initial_players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class PlayerReaderStub:
    def get_players(self):
        return initial_players
    
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self) -> None:
        self.stats = StatisticsService(PlayerReaderStub())

    def test_konstruktori_tallettaa_annetut_pelaajat(self):
        self.assertListEqual(self.stats._players, initial_players)

    def test_search_palauttaa_nimetyn_pelaajan(self):
        haluttu_pelaaja = initial_players[2] # Kurri
        hakusana = haluttu_pelaaja.name
        loydetty_pelaaja = self.stats.search(hakusana)
        
        self.assertEqual(haluttu_pelaaja, loydetty_pelaaja)

    def test_search_palauttaa_None_pelaajan_jos_nimea_ei_ole(self):
        hakusana = "Räikkönen"
        loydetty_pelaaja = self.stats.search(hakusana)

        self.assertEqual(loydetty_pelaaja, None)

    def test_team_palauttaa_tiimin_pelaajat_tiiminimella(self):
        halutut_pelaajat = [
            initial_players[0], # Semenko
            initial_players[2], # Kurri
            initial_players[4]  # Gretzky
            ]
        
        hakusana = "EDM"        
        loydetyt_pelaajat = self.stats.team(hakusana)

        print(loydetyt_pelaajat)

        self.assertListEqual(loydetyt_pelaajat, halutut_pelaajat)

    def test_top_palauttaa_pelaajat_jarjestyksessa_parhaat_pisteet_ensin(self):
        oikea_jarjestys = [
            Player("Gretzky", "EDM", 35, 89), # 124
            Player("Lemieux", "PIT", 45, 54), # 99
            Player("Yzerman", "DET", 42, 56), # 98
            Player("Kurri",   "EDM", 37, 53), # 90
            Player("Semenko", "EDM", 4, 12), # 16
        ]

        saatu_jarjestys = self.stats.top(5)

        self.assertSequenceEqual(saatu_jarjestys, oikea_jarjestys)
        
    def test_top_palauttaa_pelaajat_jarjestyksessa_parhaat_assistit_ensin(self):
        # Järjestys on goals, assists

        oikea_jarjestys = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Semenko", "EDM", 4, 12),
        ]

        saatu_jarjestys = self.stats.top(5, SortBy.ASSISTS)

        self.assertSequenceEqual(saatu_jarjestys, oikea_jarjestys)

    def test_top_palauttaa_pelaajat_jarjestyksessa_parhaat_goalit_ensin(self):
        # Järjestys on goals, assists

        oikea_jarjestys = [
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89),
            Player("Semenko", "EDM", 4, 12),
        ]

        saatu_jarjestys = self.stats.top(5, SortBy.GOALS)

        self.assertSequenceEqual(saatu_jarjestys, oikea_jarjestys)


        