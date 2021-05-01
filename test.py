import unittest
from main import Puzzle

""""Puzzle(size, turn, debug)"""
""""process(players, depth)"""

class TestCases(unittest.TestCase):
    
    def test_1(self):
        puz = Puzzle(1,1,False)
        self.assertEqual(puz.process(0,10), 'Player 2 wins!')

    def test_2(self):
        puz = Puzzle(2,1,False)
        self.assertEqual(puz.process(0,10), 'Player 1 wins!')
    
    def test_3(self):
        puz = Puzzle(3,1,False)
        self.assertEqual(puz.process(0,10), 'Player 1 wins!')
    
    def test_4(self):
        puz = Puzzle(4,1,False)
        self.assertEqual(puz.process(0,10), 'Player 2 wins!')
    
    def test_5(self):
        puz = Puzzle(5,1,False)
        self.assertEqual(puz.process(0,10), 'Player 1 wins!')
    
    def test_6(self):
        puz = Puzzle(6,1,False)
        self.assertEqual(puz.process(0,10), 'Player 1 wins!')
    
    def test_7(self):
        puz = Puzzle(7,1,False)
        self.assertEqual(puz.process(0,10), 'Player 2 wins!')
    
    def test_8(self):
        puz = Puzzle(8,1,False)
        self.assertEqual(puz.process(0,10), 'Player 1 wins!')
    
    def test_9(self):
        puz = Puzzle(9,1,False)
        self.assertEqual(puz.process(0,10), 'Player 2 wins!')
    
    def test_10(self):
        puz = Puzzle(10,1,False)
        self.assertEqual(puz.process(0,10), 'Player 1 wins!')
    
    def test_100(self):
        puz = Puzzle(8,1,False)
        self.assertEqual(puz.process(0,10), 'Player 1 wins!')

if __name__ == '__main__':
    unittest.main()