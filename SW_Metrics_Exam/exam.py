"""Program check if numbers are devisible"""
import unittest
import math

REM = "Numbers divided with remainder"
NOR = "Divisible"
INV = "Ivalid input"


def results(x,y):
    """Function returns the remainder of x divided by y if exists"""
    new_rem = ""
    print(x, y)
    result = ""
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float):
        dev = math.fmod(float(x),float(y))
        new_rem = str(dev)
        if dev == 0:
            result = NOR
        else:
            result = REM
    else:
        result = INV
        new_rem="Invalid input"
    print(result)
    print("Reminder: "+ new_rem)
    return result


class TestDevisionResults(unittest.TestCase):
    """Test inputs"""
    def test_no_reminder(self):
        """Test for numbers that are divisible"""
        self.assertEqual(results(25,5), NOR)

    def test_invalid(self):
        """Test for invalid input"""
        self.assertEqual(results(4, "a"), INV)

    def test_with_reminder(self):
        """Test for numbers that are not divisible"""
        self.assertEqual(results(12, 7), REM)


if __name__ == '__main__':
    unittest.main()
