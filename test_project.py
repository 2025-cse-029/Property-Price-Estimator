import unittest
from estimator import estimate_price


class PropertyEstimatorTests(unittest.TestCase):
    def test_small_normal_property(self):
        self.assertEqual(estimate_price(5, 2, "normal", "average"), 5400000)

    def test_central_good_property(self):
        self.assertEqual(estimate_price(10, 4, "central", "good"), 14000000)

    def test_outer_poor_property(self):
        self.assertEqual(estimate_price(3, 1, "outer", "poor"), 2495000)

    def test_normal_good_property(self):
        self.assertEqual(estimate_price(7, 3, "normal", "good"), 8300000)

    def test_invalid_area(self):
        self.assertIsNone(estimate_price(-2, 2, "normal", "average"))

    def test_invalid_location_or_condition(self):
        self.assertIsNone(estimate_price(5, 2, "unknown", "average"))
        self.assertIsNone(estimate_price(5, 2, "normal", "unknown"))

if __name__ == "__main__":
    unittest.main()
