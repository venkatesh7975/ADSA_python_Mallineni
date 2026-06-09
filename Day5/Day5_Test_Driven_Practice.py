import unittest

def sum_all_numbers(nums):
    return sum(nums)

def product_all_numbers(nums):
    if not nums: return 0
    res = 1
    for n in nums: res *= n
    return res

def count_frequencies(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return freq

class TestDay5Methods(unittest.TestCase):

    def test_sum_all_numbers(self):
        self.assertEqual(sum_all_numbers([1, 2, 3]), 6)
        self.assertEqual(sum_all_numbers([10, -10, 5]), 5)

    def test_product_all_numbers(self):
        self.assertEqual(product_all_numbers([1, 2, 3, 4]), 24)
        self.assertEqual(product_all_numbers([]), 0)
        self.assertEqual(product_all_numbers([5, 0, 2]), 0)

    def test_count_frequencies(self):
        self.assertEqual(count_frequencies([1, 1, 2]), {1: 2, 2: 1})
        self.assertEqual(count_frequencies(["a", "b", "a"]), {"a": 2, "b": 1})

if __name__ == '__main__':
    unittest.main()
