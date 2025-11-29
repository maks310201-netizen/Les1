
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


#import unittest
#from main import *

#def f1(a, b):
 #   if b > 0:
  #      return a / b
   # else:
    #    return a * b


#class MyTest(unittest.TestCase):

 #   def test_negative(self):
  #      for i in range(5):
   #         self.assertEqual(f1(i, -6), i * (-4))

    #def test_zero(self):
     #   for i in range(5):

      #      with self.assertRaises(ZeroDivisionError):
       #         f1(i, 0)
        #    pass

    #def test_positive(self):
     #   for i in range(5):

      #      self.assertEqual(f1(i, 2), i * 2)









import cv2

image_path = 'cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)

print(cat_face)
cv2.imshow("Cat", image)
cv2.waitKey()




#Дз
class WordLengthIterator:
    def __init__(self, words):
        self._words = words
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._words):
            length = len(self._words[self._index])
            self._index += 1
            return length
        else:
            raise StopIteration

my_words = ["Об’єктно", "орієнтоване", "та", "функціональне", "програмування", "Python"]
word_iterator = WordLengthIterator(my_words)

print("Довжини слів:")
for length in word_iterator:
    print(length)



#Дз
import random
import string


def random_letter_generator():

    lytter = string.ascii_lowercase

    while True:
        random_char = random.choice(lytter)
        yield random_char

letter_gen = random_letter_generator()
for _ in range(5):
    letter = next(letter_gen)
    print(letter, end=' ')
