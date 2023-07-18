import sys
import os
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(root_path)
import unittest
from accessor.ingredient_accessor_test import IngredientAccessorTestCase


if __name__ == '__main__':
    unittest.main()


# -=-=-=-=-=-=-=-=-=-=- Example Test Case -=-=-=-=-=-=-=-=-=-=- #
"""

import unittest


class ExampleTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(this_class):
        # Run once for this class, before any tests are run
        pass

    def setUp(self):
        # Run before each test method is run
        pass

    def test_math(self):
        pass

    def tearDown(self):
        # Run after each test method is run
        pass

    @classmethod
    def tearDownClass(this_class):
        # Run once for this class, after all test methods have finished
        pass

"""
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #