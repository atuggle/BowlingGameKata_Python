from bowling_game import Game
import unittest

class GameTests(unittest.TestCase):

    game = Game()

    def test_game_not_null(self):
        self.assertIsNotNone(self.game)

    def test_can_bowl_gutter_game(self):
        self.rollMany(20, 0)
        self.assertEqual(self.game.score(), 0)

    def rollMany(self, times, pins):
        for roll in range (0, times):
            self.game.roll(pins)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
