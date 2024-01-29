import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')

import unittest
from src.Stack import Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        input = [1, 3, 4, 6, 8]
        new_stack = Stack()
        for num in input:
            new_stack.push(num)

        stack_output = new_stack.show_all()
        expected_output = input[::-1]
        self.assertEqual(stack_output, expected_output, 'PUSH didn\'t work')

if __name__ == '__main__':
    print("running the tests by directly calling the file and running the code below to run the test cases")
    unittest.main()