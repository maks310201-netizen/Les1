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







# 1.
users_age_groups = {
    "Данічка": "Молодий карлік",
    "Вадім": "Дорослий",
    "Олена": "Пенсія",
    "Дмитро": "Малолітка",
    "Віктор": "дорослий"
}
user_name = input("Введіть ім'я користувача для перевірки вікової групи: ")

if user_name in users_age_groups:
    age_group = users_age_groups[user_name]
    print("Вікова група користувача '{user_name}' — {age_group}.")
else:
    print("Користувача з ім'ям '{user_name}' не знайдено.")




#2
def safe_integer_conversion():

    user_input = input("Будь ласка, введіть число: ").strip()

    try:

        converted_number = int(user_input)

        print(f"{user_input}{converted_number}")

    except ValueError:

        print(f"Введене значення '{user_input}' не можна конвертувати у ціле число.")
        print("Будь ласка, переконайтеся, що ви вводите лише цілі числа (наприклад, 123 або -45).")


safe_integer_conversion()





#3
def read_and_display_file():

    file_path = input("Введіть повний шлях до файлу (наприклад, file.txt): ").strip()

    if not file_path:
        print("Шлях до файлу не може бути порожнім.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        print("Будь ласка, перевірте ім'я файлу.")

read_and_display_file()

