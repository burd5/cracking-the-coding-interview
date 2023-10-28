# Given two strings, write a method to decide if one is a permutation of the other

import unittest
from collections import Counter

def is_permutation(str1, str2):
    if len(str1) != len(str2): return False
    return sorted(str1) == sorted(str2)



class Test_Permutation(unittest.TestCase):
    def test_is_permutation(self):
        self.assertTrue(is_permutation('west', 'stew'))
        self.assertFalse(is_permutation('pig', 'dad'))
        self.assertFalse(is_permutation('123jsj', 'hello'))
        self.assertTrue(is_permutation('1uw34ns', 'ns34w1u'))

if __name__ == '__main__':
    unittest.main()


# Other solutions

def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True


def check_permutation_pythonic(str1, str2):
    # short-circuit to avoid instantiating a Counter which for big strings
    # may be an expensive operation
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)