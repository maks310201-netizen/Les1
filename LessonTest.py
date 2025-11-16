
#def dec(f1):
   # def f2():
   #     result = f1()
  #      return f"Result: {result}"

 #   return f2

#@dec
#def test():
 #   return "Test"

#print(test())

#import logging

#с = 12

#logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='w', format='We have next logging message:%(asctime)s:%(levelname)s:%(message)s')
#logging.info(с)
#logging.info("Watermelon")

#assert 2+2==5

#"""
#>>> 2+2
#5
#"""

#if __name__ == "__main__":
 #   import doctest
  #  doctest.testmod()


import unittest
from main import *

def f1(a, b):
    if b > 0:
        return a / b
    else:
        return a * b


class MyTest(unittest.TestCase):

    def test_negative(self):
        for i in range(5):
            self.assertEqual(f1(i, -6), i * (-4))

    def test_zero(self):
        for i in range(5):

            with self.assertRaises(ZeroDivisionError):
                f1(i, 0)
            pass

    def test_positive(self):
        for i in range(5):

            self.assertEqual(f1(i, 2), i * 2)


