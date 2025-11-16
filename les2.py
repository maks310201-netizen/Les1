#print ('Hello World')


#a = iter(range(5))

#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#print(next(a))
#try:
 #   print(next(a))
#except:
 #   print('Error!')

#class Counter:
 #   def __init__(self):
  #      self.a = 0

   # def __iter__(self):
    #    self.a = 0
     #   return self

    #def __next__(self):
     #   self.a *= 4
      #  return self.a


#c = iter(Counter())

#for i in range(50):
 #   print(next(c))


#def gen(number):
    #b = number
    #i = 0
    #while True:
   #     i += 1
  #      b += i
 #       yield b
#g = gen(5)
#print(next(g))
#print(next(g))
#print(next(g))


from colorama import init, Fore, Style

init()

print(Fore.red + 'Це червоний текст')
print('Це звичайний текст')
print(Fore.yellow + 'Це жовтий текст')
