import unittest
from percentage import percentage

class PercentageTests(unittest.TestCase):
    def test_examples(self):
        for value, percent, expected in [(200, 10, 20), (80, 12.5, 10), (100, 0, 0), (200, -10, -20)]:
            with self.subTest(value=value, percent=percent):
                self.assertEqual(percentage(value, percent), expected)

if __name__ == '__main__':
    unittest.main()
