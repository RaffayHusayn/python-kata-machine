import unittest
import random
import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')
from src.TwoCrystalBalls import two_crystal_balls

class TwoCrystalBalls(unittest.TestCase):

    def test_two_crystal_balls_positive(self):
        len = 10000
        # index where it breaks
        idx = random.randrange(0,len)
        complete_array = []
        for i in range(0,10000):
            complete_array.append(False) if i < idx else complete_array.append(True)
        self.assertTrue(two_crystal_balls(complete_array))

    def test_two_crystal_balls_false(self):
        self.assertEqual(two_crystal_balls([False]*1000), -1)

if __name__ == '__main__':
    print("running the tests by directly calling the file and running the code below to run the test cases")
    unittest.main()



