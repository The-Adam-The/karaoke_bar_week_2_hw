import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.plastic_love = Song("Plastic Love", "Mariya Takeuchi", "City Pop")

    def test_song_has_title(self):
        self.assertEqual("Plastic Love", self.plastic_love.title)

    def test_song_has_artist(self):
        self.assertEqual("Mariya Takeuchi", self.plastic_love.artist)

    def test_song_has_genre(self):
        self.assertEqual("City Pop", self.plastic_love.genre)

    
    
    
