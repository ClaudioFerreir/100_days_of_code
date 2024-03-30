import unittest

from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
  def test_bubble_sort(self):
    self.assertEqual(bubble_sort([5, 3, 8, 6, 7, 2]), [2, 3, 5, 6, 7, 8])
    self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
  unittest.main()