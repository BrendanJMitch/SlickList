import os
import sqlite3
import unittest
import slicklist.db.manage_db
from slicklist.accessor.ingredient_accessor import IngredientAccessor
from slicklist.model.ingredient_model import Ingredient


class IngredientAccessorTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(this_class):
        # Run once for this class, before any tests are run
        dir_path = os.path.dirname(os.path.realpath(__file__))
        slicklist.db.manage_db.DB_PATH = os.path.join(dir_path, 'test_db.sqlite')

    def setUp(self):
        # Run before each test method is run
        slicklist.db.manage_db.clear_db()

    def test_insert(self):
        accessor = IngredientAccessor()
        ingredient = Ingredient(123, 456, "Honey", 1.45, True, "wm1", "honey.png", "A2")
        try:
            accessor.insert(ingredient)
        except Exception as e:
            self.fail(f"insert() raised an exception: {e}")

    def test_insert_duplicate(self):
        accessor = IngredientAccessor()
        ingredient = Ingredient(123, 456, "Honey", 1.45, True, "wm1", "honey.png", "A2")
        accessor.insert(ingredient)
        self.assertRaises(sqlite3.IntegrityError, accessor.insert, ingredient)
        
    def tearDown(self):
        # Run after each test method is run
        pass

    @classmethod
    def tearDownClass(this_class):
        # Run once for this class, after all test methods have finished
        pass