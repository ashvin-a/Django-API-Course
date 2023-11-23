'''
Sample test
'''

from django.test import SimpleTestCase
from app import calcu

class CalcTest(SimpleTestCase):
    '''Test the calc module'''


    def test_add(self) :
        res = calcu.add(1, 2)

        self.assertEqual(res, 3)

    def test_sub(self):
        res = calcu.subtract(2, 1)

        self.assertEqual(res, 1)