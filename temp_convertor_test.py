import unittest
from tempConvertor import tempconvertor

class TempConvertorTest(unittest.TestCase):

    #get correct value
    #data type
    #exception for wrong datatype
    #check for null value and throw exception

    def test_celcius_is_converted_to_fareneit(self):
        """
        f= c*9/f +32
        """
        actual = tempconvertor(10)
        expected = 5
        self.assertEqual(actual, expected,'expect that with the actual equals expected')
