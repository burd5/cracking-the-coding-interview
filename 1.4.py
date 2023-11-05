"""
Write a method to replace all spaces in a string with '%20%'. You may assume that
the string has sufficient space at the end of the string to hold the additional
characters, and that you are given the "true" length of the string.

Ex.)

Input: "Mr  John Smith    "
Output: "Mr%20John%20Smith"

"""

import unittest


def urlify_algo(string, length):
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])


def urlify_pythonic(text, length):
    return text[:length].replace(" ", "%20")



class Test_add_20(unittest.TestCase):
    def test_add_20_func(self):
        self.assertEqual(urlify_algo("Mr John Smith       ", 13), "Mr%20John%20Smith")
        self.assertEqual(urlify_pythonic("Mr John Smith       ", 13), "Mr%20John%20Smith")



if __name__ == '__main__':
    unittest.main()