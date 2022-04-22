import unittest
import game

class TestCombination(unittest.TestCase):
    def test_combination_ones_everything(self):
        self.assertAlmostEqual(game.find_by_combination((1,1,1,1,1), 1), 5)
    def test_combination_ones_some(self):
        self.assertAlmostEqual(game.find_by_combination((1,2,1,4,5), 1), 2)
    def test_combination_ones_nothing(self):
        self.assertAlmostEqual(game.find_by_combination((6,2,6,4,5), 1), 0)
    def test_combination_twos_everything(self):
        self.assertAlmostEqual(game.find_by_combination((2,2,2,2,2), 2), 10)
    def test_combination_twos_some(self):
        self.assertAlmostEqual(game.find_by_combination((1,2,2,4,5), 2), 4)
    def test_combination_twos_nothing(self):
        self.assertAlmostEqual(game.find_by_combination((6,1,6,4,5), 2), 0)
    def test_combination_threes_everything(self):
        self.assertAlmostEqual(game.find_by_combination((3,3,3,3,3), 3), 15)
    def test_combination_threes_some(self):
        self.assertAlmostEqual(game.find_by_combination((1,2,3,4,3), 3), 6)
    def test_combination_threes_nothing(self):
        self.assertAlmostEqual(game.find_by_combination((6,1,6,4,5), 3), 0)
    def test_combination_fours_everything(self):
        self.assertAlmostEqual(game.find_by_combination((4,4,4,4,4), 4), 20)
    def test_combination_fours_some(self):
        self.assertAlmostEqual(game.find_by_combination((1,2,3,4,4), 4), 8)
    def test_combination_fours_nothing(self):
        self.assertAlmostEqual(game.find_by_combination((6,1,6,3,5), 4), 0)
    def test_combination_fives_everything(self):
        self.assertAlmostEqual(game.find_by_combination((5,5,5,5,5), 5), 25)
    def test_combination_fives_some(self):
        self.assertAlmostEqual(game.find_by_combination((5,2,3,4,5), 5), 10)
    def test_combination_fives_nothing(self):
        self.assertAlmostEqual(game.find_by_combination((6,1,6,4,4), 5), 0)
    def test_combination_sixes_everything(self):
        self.assertAlmostEqual(game.find_by_combination((6,6,6,6,6), 6), 30)
    def test_combination_sixes_some(self):
        self.assertAlmostEqual(game.find_by_combination((1,6,3,4,6), 6), 12)
    def test_combination_sixes_nothing(self):
        self.assertAlmostEqual(game.find_by_combination((2,1,1,4,5), 6), 0)


if __name__ == '__main__':
    unittest.main()