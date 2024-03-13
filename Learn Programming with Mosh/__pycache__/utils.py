# Original

# numbers = [10, 3, 6, 2]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

## Create modueles


# ທຳອິດກຳນົດຟັງເຊິ່ນ find max

# def find_max(numbers): # ເພີ່ມພາລາເມເຕີ ທີ່ເອີ້ນວ່າ number
# # Algorithm ໃນການຄົ້ນຫາ
#     maximum = numbers[0]
#     for number in numbers:
#         if number > maximum:
#             maximum = number
#     return maximum


## Module ສຸ່ມລູກເຕົ໋າ

import random

 # self ໃຊ້ ອ້າງອີງ Object ໃນMethod ຂອງ Class
class Dice: # ປະກາດຕົວປ່ຽນລູກເຕົ໋າ
    def roll(self): # ໃຊ້ວິທີການ  Tuples ຄືຈຳນວນລາຍການ ແຕ່ຈະບໍ່ສາມາດແປງຄ່າໃດໆ ໃນລາຍການ Tuples # ຈະສາມາດອ່ານໄດ້ຢ່າງດຽວ
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    

dice = Dice()
print(dice.roll())

