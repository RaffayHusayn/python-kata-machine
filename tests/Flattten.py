import unittest
import sys 
sys.path.append('/Users/raffay/algo/python-kata-machine')

from src.Flatten import flatten 
class Flatten(unittest.TestCase):
    def test_flatten(self):
        test_list_1 = [1,2,3,[4,5,[6,7]], 8]
        expected_1= [1,2,3,4,5,6,7,8]
        test_list_2= [8]
        expected_2= [8]
        test_list_3= []
        expected_3= []
        self.assertEqual(expected_1, flatten(test_list_1))
        self.assertEqual(expected_2, flatten(test_list_2))
        self.assertEqual(expected_3, flatten(test_list_3))

if __name__=='__main__':
    print('calling the file directly not as a module')
    unittest.main()


