import sys


class Map:
    map_set = None

    def __init__(self):
        self.map_set = set()

    @staticmethod
    def initial_check(str1, str2):
        """
        One to One does not exist if the length of the strings are different. In order for one to one to
        :param str1: Initial string 1 passed from command line
        :param str2: Initial string 2 passed from command line
        :return: True or False
        """
        if len(str1) < len(str2) or len(str2) < len(str1):
            return False
        return True

    def create_set(self, str1, str2):
        """
        This replaces the need for if/else statements like the dictionary to store. Again we only care about the
        uniqueness of string1. For example if string1 = foo and string2 = bar it would false because foo has 2 o's.
        A set would catch if string1 has multiple of the same characters
        O(n) time complexity and O(n) space complexity
        :param str1: Initial string 1 passed from command line
        :param str2 Initial string 2 passed from command line
        :return: True or False
        """
        self.map_set = {char for char in str1}
        return True if len(self.map_set) == len(str2) else False

    def run(self, str1, str2):
        """
        Start the one to one comparison
        :param str1: Initial string 1 passed from command line
        :param str2: Initial string 2 passed from command line
        :return: String version of True or False
        """
        if not self.initial_check(str1, str2):
            return "false"
        if not self.create_set(str1, str2):
            return "false"
        return "true"


def main():
    string1 = sys.argv[1]
    string2 = sys.argv[2]
    m = Map()
    print(m.run(string1, string2))


main()
