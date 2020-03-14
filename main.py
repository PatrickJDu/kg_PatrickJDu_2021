import sys


class Map:

    map_char = None

    def __init__(self):
        self.map_char = {}

    """
    One to One does not exist if the length of the strings are different. In order for one to one to
    """
    @staticmethod
    def initial_check(str1, str2):
        if len(str1) < len(str2) or len(str2) < len(str1):
            return False
        return True

    """
    This is the brute force method that compares the character of the first to see if there are unique characters.
    We only care about the uniqueness of the first string. O(n^2) time complexity O(1) space complexity
    """
    @staticmethod
    def brute_force(str1):
        for pos, value in enumerate(str1):
            for second_pos in range(pos+1, len(str1)):
                if value == str1[second_pos]:
                    return False
        return True

    """
    This uses a dictionary to map each character in the string to another character in another string.
    O(n) time complexity O(1) space complexity
    """
    def create_map(self, str1, str2):
        for pos, value in enumerate(str1):
            if value not in self.map_char:
                self.map_char[value] = str2[pos]
            else:
                return False
        return True

    """
    Start the one to one comparison
    """
    def run(self, str1, str2):
        if not self.initial_check(str1, str2):
            return False
        if not self.create_map(str1, str2):
            return False
        return True


string1 = sys.argv[1]
string2 = sys.argv[2]
m = Map()
print(m.run(string1, string2))
