from bowling_game import Game
import unittest

class GameTests(unittest.TestCase):

    game = Game()

    def setUp(self):
        self.game = Game()

    def test_game_not_null(self):
        self.assertIsNotNone(self.game)

    def test_can_bowl_gutter_game(self):
        self.rollMany(20, 0)
        self.assertEqual(self.game.score(), 0)

    def test_can_bowl_all_ones(self):
        self.rollMany(20, 1)
        self.assertEqual(self.game.score(), 20)

    def test_can_bowl_spare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(2)
        self.game.roll(2)
        self.rollMany(16, 0)
        self.assertEqual(self.game.score(), 16)

    def test_can_bowl_strike(self):
        self.game.roll(10)
        self.game.roll(5)
        self.game.roll(2)
        self.game.roll(2)
        self.rollMany(15, 0)
        self.assertEqual(self.game.score(), 26)

    def test_can_bowl_perfect_game(self):
        self.rollMany(12, 10)
        self.assertEqual(self.game.score(), 300)

    def rollMany(self, times, pins):
        for roll in range (0, times):
            self.game.roll(pins)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
