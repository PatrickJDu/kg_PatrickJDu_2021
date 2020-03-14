import sys


class Map:
    map_char = None

    def __init__(self):
        self.map_char = {}

    @staticmethod
    def initial_check(str1, str2):
        """
        One to One does not exist if the length of the strings are different. In order for one to one to
        exist the lengths of the two strings must be the same
        :param str1: Initial string1 passed from command line
        :param str2: Initial string2 passed from command line
        :return: True or False
        """
        if len(str1) < len(str2) or len(str2) < len(str1):
            return False
        return True

    def create_map(self, str1, str2):
        """
        Dictionary contains instances where string1 is foo and string2 is baa. While o cannot have multiple values
        attached to it, it can have a singular repeating one.
        :param str1: Initial string1 passed from command line
        :param str2: Initial string2 passed from command line
        :return: True or False
        """
        for pos, value in enumerate(str1):
            if value not in self.map_char:
                self.map_char[value] = str2[pos]
            else:
                if self.map_char[value] == str2[pos]:
                    continue
                return False
        return True

    def run(self, str1, str2):
        """
        Start the one to one comparison
        :param str1: Initial string1 passed from command line
        :param str2: Initial string2 passed from command line
        :return: String version of True or False
        """
        if not (self.initial_check(str1, str2) and self.create_map(str1, str2)):
            return "false"
        return "true"


def main():
    try:
        string1 = sys.argv[1]
        string2 = sys.argv[2]
    except IndexError:
        print("You entered one argument when there should be two arguments! Exiting...")
        exit(1)
    m = Map()
    print(m.run(string1, string2))


main()
