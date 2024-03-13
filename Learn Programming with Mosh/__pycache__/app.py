
#ບົດທີ 1  pirnt
#print("Hello word")
#print('o---')
#print('||||')
#print('*'*10)


##------ ບົດທີ 2 Variables -----##

#price = 10 #ເລກຈຳນວນເຕັມ
#price = 20
#print(price)

# price = 10
# rating = 4.9
# name = 'Mosh'
# is_published = False
# print(price)

# name = input ('What is your name? ')
# like = input ('what do you like color? ')
# print('Hello '+ name +(' like color ' + like))

# brit_year = input ('What is your Birth year? ')
# age = 2024 - int(brit_year)
# print(age)

# weight_lbs = input ('Weight (lbs) ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

##String array
# Text = ('Hello my name is Mr: Bounleuam')
# print(Text[0])
##print(Text[0:3])
##ເລິ່ມແຕ່ຂໍ້ຄວາມທຳອິດໄປ
#print(Text[0:])

# name = 'Jennifer'
# print(name[1:-1])

# course = 'Python for Beginners'
# print(len(course))

# course = 'Python for Beginners'
# print(course.upper()) # ຕົວອັກສອນໃຫຍ່
# print(course.lower()) # ຕົວອັກສອນນ້ອຍ
# print(course)

# course = 'Python for Beginners'
# print(course.find('f')) #ຫາເລກດັດສະນີຂອງ ອັກສອນ (ຫາຕຳແໜ່ງ)

#course = 'Python for Beginners'
#print(course.find('Beginners')) #ຜູູ້ເລີ່ມຕົ້ນເລີ່ມດ້ວຍດັດສະນີທີ່ 11

# course = 'Python for Beginners'
# print(course.replace('Beginners','Absolute Beginners')) # ວິທີການແທນທີ່ຕົວອັກສອນ ,ເປັນວິທີທີ່ຄືກັບວິທີການຄົ້ນຫາ

#course = 'Python for Beginners'
#print(course.replace('P','J')) # ແທນທີ່ຕົວອັກສອນຕົວດຽວໄດ້

# course = 'Python for Beginners'
# print('Python'in course) # ຄົ້ນຫາຄຳວ່າ Puthon ໃນ Course ມີຫຼືບໍ່? ໂດຍມັນຈະສະແດງຄຳຕອບອອກມາເປັນ Boolean
 
# course = 'Python for Beginners'
# print(course.title()) # ຫາຫົວຂໍ້

# print(10 // 3) #ຫາຈຳນວນເຕັມ

#print(10 % 3) #ຫາເສດເຫຼືອຈາກການຫານ

# print(10 ** 3) # ຍົກກຳລັງ

# x = 10
# x = x + 3
# x += 3 # ຂຽນໃຫ້ສັ້ນລົງ
# print(x) # ວິທີບວກກັນ

# x= 10 + 3 * 2 **2 # ດຳເນີນການກ່ອນ ແລະ ຫຼັງ
# print(x) 

# x = (2 + 3) * 10 - 3 #ລຽງລຳດັບຄວາມສຳຄັນ
# print(x)

# x = 2.9
# print(round(x)) # ຟັງເຊິ່ນໃນການປັດຈຸດ

# x = 2.9
# print(abs(-2.9)) #ຟັງເຊິ່ນປັັບໃຫ້ເປັນຄ່າສົມບູນ abs

# import math # ເປັນໂມດູລຄະນິດສາດ

# is_hot = False # ເງື່ອນໄຂ if
# is_could = False
# if is_hot:
#     print("It's a hot day") #ກົດຍະຫວ່າງ ມີຜົນສຳຫຼັບພາສາ Python
#     print("Drink plent of water")
# elif is_could:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day") # ສ່ວນໂຄ້ດນີ້ບໍ່ໄດ້ຢູ່ໃນເງື່ອນໄຂ

###  ກິດຈະກຳ
# price = 8000000
# has_good_credit = False
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

##ຕະກະ

# has_high_income = False
# has_good_credit = True
# if has_high_income and has_good_credit: #ເປັນເທັດ
#     print("Eligible for loan")
#if has_high_income or has_good_credit: #ເປັນຈິງ
#     print("Eligible for loan")
# if has_high_income and not has_good_credit: #ເປັນເທັດ
    # print("Eligible for loan")

##ກິດຈະກຳ
# temperature = 30
# temperature = 100

# if temperature == 30: #
#   print("It's a hot day")
# if temperature < 30: #ແມ່ນ
#  print("It's a colde day")
# if temperature > 30: #ແມ່ນເປັນຈິງ
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

##ກິດຈະກຳ
# name = "jennifer"

# if len(name) < 3:
#     print("Name must be at least 3 character")
# elif len(name)> 50:
#     print("Name must be a maximum of 50 character")
# else:
#     print("Name look good!") 

##ກິດຈະກຳ
# weight = int(input('Weight:'))
# unit = input('(L)bs or (k)g:')
# if unit.upper() == "L" :
#     converted = weight * 0.45
#     print(f"You are {converted} kilos" )
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds") 

## While loops
# i=1
# while i <= 5:
#     print('*'*i)
#     i = i+1
# print("Done")


##ກິດຈະກຳ
# secret_number = 9
# guess_count = 0
# guss_limit = 3
# while guess_count < guss_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed!')

##ກິດຈຳກຳ
Command = ""
Started = False
while True:
      Command = input("> ").lower()
      if Command == "start":
          if Started:
            print("Car is already started!")
          else:
            Started = True
            print("Car sarted...")
      elif Command == "stop":
            if not Started:
               print("Car is already stopped!")
            else:
               Started = False
               print("Car Stopped...")
      elif Command == "help":
            print("""
start - to start the car
stop - to stop the car 
quit - to exit """)
      elif Command == "quit":
         break
      else:
          print("Sorry, I don't understand that")
      
    
## For loop

# for item in range(10): #for loop
#     print(item)

# for item in range(5, 10, 2): # ກ້າວໄປທາງໜ້າ 2 ກ້າວ
#     print(item)

## ກິດຈະກຳ

# prices = [10, 20, 30]

# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

## ລູປຊ້ອນລູປ
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y}')


## ກິດຈະກຳ
# numbers = [5, 2, 5, 2, 2]
# for numbers in numbers:
#     print('X'*numbers)

## ແບບທີ່ 2 ບໍ່ໃຊ້ ຟັງເຊິ່ນ

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'X'
#     print(output) 

## array

# names = ['John','Bob','Mosh','Sarhah','Jehn']
# print(names[2:4])
# names[0] = 'Jon' #ສາມາດແກ້ໄຂ ໄດ້
# print(names)

## ກິດຈຳກຳ ຫາຈຳນວນຫຼາຍທີ່ສຸດ

# jumnuan = [10,20,30,40,50]
# print(jumnuan[-1])
# print(max(jumnuan))

## ວິທີທີ 2

# numbers = [4,8,7,100,9]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# matrix = [
#     [1,  5,   8],
#     [4,  6,   7],
#     [9,  10, 11]
# ]
# matrix[0][1] = 20 # ປ່ຽນເລກ 5 ຢູ່ຖັນທີ 2 ແຖວ1 ໃຫ້ເປັນເລກ 20
# print(matrix[0][1])
# print(matrix [0][2])

## ລູປຊ້ອນລູປ ໃນArray 2 D

# matrix = [
#     [1,  5,   8],
#     [4,  6,   7],
#     [9,  10, 11]
# ]

# for row in matrix:
#     for item in row:
#       print(item)
        
# ການໃຊ້ List Method 
# numbers = [7, 8, 4, 10, 20]
# numbers.append(30) # ເປັນຟັງເຊິ່ນເພິ່ມ ລາຍການໃໝ່່
# numbers.insert(0,9) # ເປັນຟັງເຊິ່ນເພິ່ມ ລາຍການໃສ່ສ່ວນກາງ ຫຼື ສ່ວນທ້າຍຂອງຕິວເລກໄດ້
# numbers.remove(20) # ເປັນຟັງເຊິ່ນເອົາລາຍການອອກ
# numbers.clear() # ເປັນຟັງເຊິ່ນລ້າງລາຍການທັງໝົດ
# numbers.pop() # ເປັນຟັງເຊິ່ນລົບລາຍການສ່ວນທ້າຍ
# print(numbers)

## ກວດສອບລາຍການ
# numbers = [7, 8, 4, 10, 20]
# print(numbers.index(30)) # ເປັນຟັງເຊິ່ນກວດສອບລາຍການທີ່ມີຢູ່ໃນດັດສະນີວ່າເປັນ ດັດສະນີໃດ?
# print(30 in numbers) # ເປັນອີກວິທີໜຶ່ງໃນການກວດສອບລາຍການ ໂດຍໃຊ້ ໂອເປີເຣເຕີ ກັບສະຕິງ.

## ການກວດລາຍການຊ້ຳ
# numbers = [7, 10, 8, 4, 10, 20]
# print(numbers.count(10)) # ຟັງເຊິ່ນນັບຈຳນວນຄັ້ງຂອງລາຍການ ມີຈັກລາຍການທີ່ຊ້ຳກັນ

## ລຽງລຳດັບລາຍການ
# numbers = [7, 10, 8, 4, 10, 20]
# numbers.sort() # ລຽງລຳດັບໃຫ້ກັບລາຍການແຕ່ນ້ອຍຫາໃຫຍ່
# print(numbers)
# numbers.sort() # ລຽງລຳດັບໃຫ້ກັບລາຍການແຕ່ນ້ອຍຫາໃຫຍ່
# numbers.reverse() # ຍ້ອນກັບລາຍການ ຫຼຶ ຍ້າຍສ່ວນທ້າຍຂອງລາຍການປ່ຽນຕຳແໜ່ງໄປໄວ້ສ່ວນຫົວ ເປັນການລຽງຈາກໃຫຍ່ໄປຫານ້ອຍ
# print(numbers)


## ການ Coppy ເມື່ອມີການລົບຈະມີສົ່ງຜົນກະທົບຕໍ່ລາຍການທີ່ 2 (ຕົວປ່ຽນ)
# numbers = [7, 10, 8, 4, 10, 20]
# number2 = numbers.copy() # ເປັນການ Coppy ເມື່ອມີການປ່ຽນແປງຈະບໍ່ສົ່ງຜົນກະທົບຕໍ່ ລາຍການຕົ້ນສະບັບ
# numbers.append(50)
# print(number2)


# numbers = [5, 8, 8, 2, 1] 
# uniques = [] # ຕ້ອງການເຮັດຊ້ຳ
# for number in numbers: # ກວດສອບເບິ່ງວ່າ ມີ number ຢຸ່ໃນ numbers ເລິຍໃຊ້ in
#     if number not in uniques: # ຖ້າບໍ່ມີຕົວເລກໃນໜ່ວຍ
#        uniques.append(number) # ເລີ່ມລົບຈຳນວນທີ່ຊ້ຳກັນອອກແລ້ວລຽງໃໝ່
# print(uniques)


## Tuple
# number = (1, 2, 3)
# print(number[0])

# coordinates = [1, 2, 3]
# x, y, z = coordinates
# print(z)


## Dictionaries
# customer = {
#     "name": "Jonth smith",
#     "age": 30,
#     "is_yerifie":True
# }
# print(customer["name"])
# print(customer.get["nam"]) #ໃຊ້ຟັງເຊິ່ນ get ເພື່ອແກ້ໄຂຂໍ້ຜິດພາດ ມັນຈະສົ່ງກັບມາເປັນຄ່າ Boolean
# customer["name"] = "jack Smith2" 
# print(customer["name"])

# customer["brithdate"] ="Jan 1 1980" # ສາມາດຕັ້ງຄ່າຄີໃໝ່ໄດ້
# print(customer["brithdate"])


## ກິດຈະກຳ 1

# phone = input("Phone: ")
# digits_mapping = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four"
# }
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + ""
# print(output)  

## ກິດຈຳກຳ 2 Emoji Converter

# message = input(">")
# words = message.split(' ') ## ຊ່ອງວ່າງນີ້ຈະໃຊ້ເປັນຂອບເຂດ
# emojis = {
#     ":)": "😊",
#     ":(": "😔"
# }
# output = ""
# for word in words:
#     output += emojis.get (word, word) + " "
# print(output)

## ແປງໃຫ້ສັ້ນລົງ ໂດຍສ້າງເປັນຟັງເຊິ່ນ

# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard')


#     ##ຕ້ອງຫ່າງກັນ 2 ບັນທັດ ເມື່ອສ້າງ ຟັງເຊິ່ນທຸກຄັ້ງ
# print("Start")
# greet_user()
# print("Finish")


## Parameters

# def greet_user (first_name, last_name):
#     print(f'Hi {first_name} {last_name}! ')
#     print('Welcom aboard')


# print("Start")
# greet_user("John", "Smith")
# print("Finish")

## Keyword Arguments 

# def greet_user (first_name, last_name):
#     print(f'Hi {first_name} {last_name}! ')
#     print('Welcom aboard')


# print("Start")
# greet_user("John", last_name="Smith") # ໃໍຊ້ Arguments ໃຫ້ກົງກັບຕຳແໜ່ງທີ່ກຳນົດໄວ້
## greet_user(first_name="John", "Smith") # ໃໍຊ້ Arguments ແບບນີ້ຈະເກີດຂໍ້ໂຕ້ແຍ່ງທັນທີ່
### calc_cost(tolal=50, shipping = 5, discount = 0.1) #ຕົວຢ່າງ ຖ້າມີຟັງເຊິ່ນອື່ນເຂົ້າມາ ຈຳສາມາດກຳນົດຕົວແປໃຫ້ມັນໄດ້
# print("Finish")

## Return Statement

# def square(number): # ຄຳນວນຕົວເລກ
#     return number * number #ສົ່ງຄ່າຄືນ
    # print(number * number)  # ຖ້າບໍ່ມີຄຳສັ່ງ return ມັນຈະບໍ່ສາມາດສົ່ງຄ່າໃດໆຄືນກັບໄດ້ ເຊັ່ນຈະສົ່ງຄືນເປັນ "None" ບໍ່ມີຫຍັງ


# result = square(3) # ເອິ້ນໃຊ້ຟັງເຊິ່ນ ພ້ອມປະກາດຕົວແປ
# print(result)
# print(square(3)) # ສາມາດລົດ ຕົວແປອອກ result = square(3) ແລ້ວເອີ້ນໃຊ້ໄດ້ ເຮັດໃຫ້ໂຄ້ດສັ້ນລົງ


## Creating a Reusable Function 

# def emoji_converter(message): # ຊື່ຂອງຟັ່ງເຊິ່ນຕ້ອງລະບຸໃຫ້ຊັດເຈນ ວ່າແມ່ນຫຍັງ? # ຕົວແປງ ອິໂມຈິຟັງເຊິ່ນນີ້ຮັບ parameter ເອືີ້ນວ່າ ຂໍ້ຄວາມມ
#     # ຟັງເຊິ້ນຕ້ອງຮັບແຕ່ວຽກດຽວເທົ່ານັ້ນ
#     words = message.split(' ') ## ຊ່ອງວ່າງນີ້ຈະໃຊ້ເປັນຂອບເຂດ
#     emojis = {
#     ":)": "😊",
#     ":(": "😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get (word, word) + " "
#     return output


# message = input(">")
# print(emoji_converter(message))


## Exceptions

# try: # ເປັນການແກ້ໄຂຂໍ້ຍົກເວັ້ນ (Exceptions)
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')# ສ້າງ except ອີກຄັ້ງເພື່ອແກ້ໄຂຂໍ້ຍົກເວັ້ນ
# except ValueError: # ຖ້າໂປຣແກຣມ Error ໃຫ້ຄືນຄ່າ
#     print('Invalid value')
# Exceptions ເທົ່າ 0 ໝາຍຄວາມວ່າ  ຄືເກີດຂໍ້ຍົກເວັ້ນ

## Class 

# class Point:
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")


# point1 = Point ()
# point1.x = 10 # attribute
# point1.y = 20
# print(point1.x)
# point1.move()

# point2 = Point()
# point2.x = 1
# print(point2.x)

##  Constructors ຄືຟັງເຊິ່ນທີ່ຖືກເອີ້ນ

# class Point:
#     def __init__(self, x, y): # ສ້າງຟັງເຊິ່ນໃໝ່ ໂດຍໃຊ້ ຂີດລຸ່ມຄູ່ 
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")


# Point = Point(10, 20)
# Point.x = 11
# print(Point.x)

## ກິດຈະກຳ

# class Person: # ມີພຽງກໍລິນີ ນີ້ເທົ່ານັ້ນທີ່ຕັ້ງຊື່ພິມໃຫຍ່ໄດ້
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi I am {self.name}")


# john = Person("John Smith") # ສາມາດສ້າງວັດຖຸໄດ້
# john.talk()

# bob = Person("Bob Smith")
# bob.talk()


## Inheritance

# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal): # ຈະສືບທອດວິທີທັງໝົດທີ່ກຳນົດໃນ Class Mammal
#     def bark(self):
#         print("bark")

# class Cat(Mammal):
#     def be_annoying(self):
#         print("annoying")          


# # dog1 = Dog()
# # dog1.walk()

# ## ເອີ້ນໃຊ້ໄດ້ 2 ວິທີ
# dog1 = Dog()
# dog1.bark()


## Packages ເປັຍໂຄງສ້າງທີ່ໃຊ້ໃນການຈັດການ ແລະ ຈັດລະບຽບໃຫ້ກັບ Modules

# package Ecommerce

# ວິທີ 1

# import ecommerce.shipping #ການຈັດສົ່ງ ເຮົາພິມ Ecommerce ນຳເຂົ້າ
# ecommerce.shipping.calc_shipping() # ເຂົ້າເຖິງການຄຳນວນ calc_shipping()

# ວິທີ 2

# from ecommerce.shipping import calc_shipping

# calc_shipping()
# calc_shipping()
# calc_shipping()
# calc_shipping()


## Generating Random Values

## packages ທີ່ມາກັບເຄື່ອງ

# import random

# for i in range(3): # ສາມາດລັນ ໄດ້3ຄັ້ງ
#     # print(random.random())
#     print(random.randint(10, 20)) ## ລະຫວ່າງ 10-20  # ໂດຍໃໍຊ້ randint


## ກິດຈຳກຳ ສຸ່ມເລືອກໃຜເປັນຫົວໜ້າ

# import random # ກຳນົດຊື່ສະມາຊິກໃນທີມ

# members = ['john', 'Mary', 'Bob', 'Mosh']
# leader = random.choice(members) # ສົ່ງຕໍ່ລາຍຊື່
# print(leader)

## ກິດຈະກຳ ສຸ່ມລູກເຕົ໋າ
# import random

#  # self ໃຊ້ ອ້າງອີງ Object ໃນMethod ຂອງ Class
# class Dice: # ປະກາດຕົວປ່ຽນລູກເຕົ໋າ
#     def roll(self): # ໃຊ້ວິທີການ  Tuples ຄືຈຳນວນລາຍການ ແຕ່ຈະບໍ່ສາມາດແປງຄ່າໃດໆ ໃນລາຍການ Tuples # ຈະສາມາດອ່ານໄດ້ຢ່າງດຽວ
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
    

# dice = Dice()
# print(dice.roll())


## Working with Directories  ## ນິຍາມ Directory ເປັນໂຄງສ້າງໂຟເດີ ຫຼື ໂຟເດີລະບົບ ເປັນການຈັດການລະບຽບຂໍ້ມູນ ແລະ ເຮັດໃຫ້ເຂົ້າເຖິງທີ່ຈັດເກັບໄຟລ໌ໄດ້ງ່າຍ

# from pathlib import Path

# path = Path("__pycache__")
# print(path.exists())

## ເພິ່ມ Directory ໃໝ່
# path = Path("Emails")
# # print(path.mkdir())  # ເພິ່ມ Directory ໂດຍໃຊ້ mkdir
# print(path.rmdir())  # ລົບ Directory ໂດຍໃຊ້ rmdir

# path = Path("__pycache__")
# print(path.glob('*.*')) # ຄົ້ນຫາ Directory ທັງໝົດ ໂດຍໃຊ້  glonb '*.*'
# print(path.glob('*.py')) # ຄົ້ນຫາ ໄຟລ໌ py ທັງໝົດ ໂດຍໃຊ້ glonb '*.p'
# print(path.glob('*.xls')) # ຄົ້ນຫາ ໄຟລ໌ xcel ທັງໝົດ ໂດຍໃຊ້ glonb '*.xls'


## ຫາໄຟລ໌ py
# path = Path()
# for file in path.glob('*.py'):
#     print(file)

## ຫາໄຟລ໌ ປັດຈຸບັນ

# path = Path()
# for file in path.glob('*'):
#     print(file)

## Pypi and Pip
##pip install openpyxl Package ກ່ຽວກັບ xcel

# ## Project 1: Automation with Python

# import openpyxl as xl 
# from openpyxl.chart import BarChart, Reference # ນຳ Modules BarChart ຫຼື ເອີ້ນອີກຢ່າງວ່າ ເປັນແທ່ງກຣາຟ
# file_path = r'D:\ບົດຮຽນ\Python\__pycache__\transaction.xlsx'
# wb = xl.load_workbook(file_path)
# sheet = wb['Sheet1']
# cell = sheet['a1']
# cell = sheet.cell(1, 1) #column 1
# # print(cell.value)
# # print(sheet.max_row)# ກວດມີຈັກແຖວ

# for row in range(2, sheet.max_row + 1): #range ສ້າງຊ່ອງຕົວເລກ ເພື່ອບວກໄປຈົນຄົບ ແຸຖວ
#     # print(row) # ສະແກງແຖວ
#     cell = sheet.cell( row, 3) # ໃໍຊ້sheet ເພື່ອໃຫ້ເຂົ້າເຖິງ cell # column ຄວນເປັນ 3
#     # print(cell.value) # ສະແດງ colum value 3 
#     corrected_price = cell.value * 0.9 # ຄູນດ້ວຍ 0.9
#     corrected_price_cell = sheet.cell(row, 4) # ສ້າງ column ໃໝ່ເພື່ອມາຮັບຄ່າ corrected_price 
#     corrected_price_cell.value = corrected_price

# valuse = Reference(sheet, 
#           min_row = 2, 
#           max_row = sheet.max_row,
#           min_col = 4,
#           max_col = 4)

# chart = BarChart() # ເກັບຄ່າໄວ້ນ Chart
# chart.add_data(valuse) # ເອີ້ນໃຊ້ chart.add_data # ຜ່ານ valuse 
# sheet.add_chart(chart, 'e2')

# wb.save('transaction2.xlsx') # ເປັນການ Save ເພື່ອຈົບ For loop # workbook # ໂດຍຈະ Save ໃສ່ໄຟລ໌ transaction2.xlsx ກັນເພື່ອບໍ່ໃຫ້ມັນທັບກັບຕົ້ນສະບັບ ຫຼຽກຫຼ່ຽງຄວາມຜິດພາດ
#  # ເພີ່ມ  Chart ລົງໃນ Sheet ປັດຈຸບັດ



## ແກ້ໄຂໂຄ້ດໃຫ້ເປັນລະບຽບ
## Project 1: Automation with Python

# import openpyxl as xl
# from openpyxl.chart import BarChart, Reference # ນຳ Modules BarChart ຫຼື ເອີ້ນອີກຢ່າງວ່າ ເປັນແທ່ງກຣາຟ

# def process_workbook(filename): # ສ້າງ ຟັງເຊິ່ນ ແລະ ຍ້າຍໂຄ້ດທັ້ງໝົດໄວ້ໃນ ຟັງເຊິ່ນ


#     file_path = r'D:\ບົດຮຽນ\Python\__pycache__\transaction.xlsx'
#     wb = xl.load_workbook(filename) #ປ່ຽນ file_path ມາເປັນ
#     sheet = wb['Sheet1']

#     # print(cell.value)
#     # print(sheet.max_row)# ກວດມີຈັກແຖວ

#     for row in range(2, sheet.max_row + 1): #range ສ້າງຊ່ອງຕົວເລກ ເພື່ອບວກໄປຈົນຄົບ ແຸຖວ
#         # print(row) # ສະແກງແຖວ
#         cell = sheet.cell( row, 3) # ໃໍຊ້sheet ເພື່ອໃຫ້ເຂົ້າເຖິງ cell # column ຄວນເປັນ 3
#         # print(cell.value) # ສະແດງ colum value 3
#         corrected_price = cell.value * 0.9 # ຄູນດ້ວຍ 0.9
#         corrected_price_cell = sheet.cell(row, 4) # ສ້າງ column ໃໝ່ເພື່ອມາຮັບຄ່າ corrected_price
#         corrected_price_cell.value = corrected_price

#     valuse = Reference(sheet,
#             min_row = 2,
#             max_row = sheet.max_row,
#             min_col = 4,
#             max_col = 4)

#     chart = BarChart() # ເກັບຄ່າໄວ້ນ Chart
#     chart.add_data(valuse) # ເອີ້ນໃຊ້ chart.add_data # ຜ່ານ valuse
#     sheet.add_chart(chart, 'e2')

#     wb.save(filename) # ເປັນການ Save ເພື່ອຈົບ For loop # workbook # ໂດຍຈະ Save ໃສ່ໄຟລ໌ transaction2.xlsx ກັນເພື່ອບໍ່ໃຫ້ມັນທັບກັບຕົ້ນສະບັບ ຫຼຽກຫຼ່ຽງຄວາມຜິດພາດ
    # ເພີ່ມ  Chart ລົງໃນ Sheet ປັດຈຸບັດ


##  Project 2: Machine Learning with Python 

##Algorithm ທີ່ໃຊ້ແມ່ນ Side Kick Learn

## step1: import the Data
## step2: Clean the Data
## step3: Split the Data into Training (ແບ່ງຂໍ້ມູນອອກເປັນຊຸດສຳຫຼັບການຝືກອົບຮົມ) / Test Sets (ແບ່ງຊູດຂໍ້ມຼນສຳຫຼັບທົດສອບທົດສອບວ່າໂມເດລຂອງເຮົາໃຫ້ຜົນໄດ້ຮັບທີ່ຖືກຕ່້ອງ)
## step4: Create a Model
## step5: Train the Model (ຝຶກໂມເດລ)
## step6: Make Predictions (ຄາດເດົາ)
## step7: Evaluate and Improve (ປະເມີນຄ່າການຄາດການ ແລະ ວັັດຄວາມຈະແຈ້ງ)

## Libraries 
   ## numpy ຈັດກຽມ ອາເຣຫຼາຍມິຕິ
   ## Pandas ວິເຄາະຂໍ້ມູນ # Data frame
   ## MatPSlotLib ການລົງຈຸດສອງມິຕິສຳຫຼັບສ້າງ Garph plot
   ## Scikit-Learn ເປັນ Algorithmນິຍົມໃນການເຮັດ Machine Learning ເຊັ່ນ ແຜນຜັງ, ການຕັດສິນໃຈ

## Project 3: Building a Website with Django