import unittest
import game

class TestCombinationOnes(unittest.TestCase):
    def test_combination_ones_everything(self):
        self.assertAlmostEqual(game.ones((1,1,1,1,1)), 5)
    def test_combination_ones_some(self):
        self.assertAlmostEqual(game.ones((1,2,1,4,5)), 2)
    def test_combination_ones_nothing(self):
        self.assertAlmostEqual(game.ones((6,2,6,4,5)), 0)