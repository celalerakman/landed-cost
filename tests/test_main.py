import unittest
import main as m

class Behavior(unittest.TestCase):
    def test_behavior(self):
        self.assertEqual(m.landed_cost(80,'12.5',90,100),1340)
        with self.assertRaises(ValueError): m.landed_cost(-1,2,3)
