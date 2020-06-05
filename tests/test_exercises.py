import unittest
from mathdrills.exercises import qty_discrimination

class ExercisesTest(unittest.TestCase):
    def test_qty_discrimination_success(self):
        qty_discrimination(list(range(100)))
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
