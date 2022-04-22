import unittest
import game

class TestCombinationOnes(unittest.TestCase):
    def test_combination_ones_everything(self):
        self.assertAlmostEqual(game.ones((1,1,1,1,1)), 5)
    def test_combination_ones_some(self):
        self.assertAlmostEqual(game.ones((1,2,1,4,5)), 2)
    def test_combination_ones_nothing(self):
        self.assertAlmostEqual(game.ones((6,2,6,4,5)), 0)

class TestCombinationTwos(unittest.TestCase):
    def test_combination_twos_everything(self):
        self.assertAlmostEqual(game.twos((2,2,2,2,2)), 10)
    def test_combination_twos_some(self):
        self.assertAlmostEqual(game.twos((1,2,2,4,5)), 4)
    def test_combination_twos_nothing(self):
        self.assertAlmostEqual(game.twos((6,1,6,4,5)), 0)

class TestCombinationThrees(unittest.TestCase):
    def test_combination_threes_everything(self):
        self.assertAlmostEqual(game.threes((3,3,3,3,3)), 15)
    def test_combination_threes_some(self):
        self.assertAlmostEqual(game.threes((1,2,3,4,3)), 6)
    def test_combination_threes_nothing(self):
        self.assertAlmostEqual(game.threes((6,1,6,4,5)), 0)

if __name__ == '__main__':
    unittest.main()