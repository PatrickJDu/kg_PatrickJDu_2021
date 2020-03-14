import sys


class Map:

    """
    This is the brute force method that compares the character of the first to see if there are unique characters.
    We only care about the uniqueness of the first string.
    """
    @staticmethod
    def brute_force(str1):
        for pos, value in enumerate(str1):
            for second_pos in range(pos+1, len(str1)):
                print("Before if ", value, " ", str1[second_pos])
                if value == str1[second_pos]:
                    print(pos, " ", str1[second_pos])
                    return False
        return True


string1 = sys.argv[1]
string2 = sys.argv[2]

print(Map.brute_force(string1))
