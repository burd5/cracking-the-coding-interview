"""
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?

"""

import unittest
import time
from collections import defaultdict

# Using set - one liner

def unique_char_set(str):
    return len(set(str)) == len(str)

# With data structures - Set

def unique_characters(str):
    # create list to hold values
    values = set()
    # iterate through str and add values to list, return false if value already exists
    for x in str:
        if x in values:
            return False
        values.add(x)
    return True

# using dictionary

def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True

# O(NlogN)
def is_unique_chars_sorting(string: str) -> bool:
    sorted_string = sorted(string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True

# Sorting without extra variable. TC: O(NlogN) SC: O(1) Con: Modifies input string
def is_unique_chars_sort(string: str) -> bool:
    string = sorted(string)
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True

# Without data structure

def uniq_without_struc(str):
    # iterate through str to see if current val is in substring of values before it
    for i in range(1, len(str)):
        if str[i] in str[:i]:
            return False
    return True

def is_unique_bit_vector(string):
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        unique_char_set,
        uniq_without_struc,
        unique_characters,
        is_unique_bit_vector,
        is_unique_chars_sort,
        is_unique_chars_sorting,
        is_unique_chars_using_dictionary
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()