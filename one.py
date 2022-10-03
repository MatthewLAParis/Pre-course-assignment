# # 1 - Write a function to print "hello_USERNAME!" USERNAME 
# # is the input of the function
# # from re import X


def hello_name(user_name):
    return f"hello_{user_name.upper()}!"

print(hello_name('username'))

# # 2 - Write a python function, first_odds that prints out 
# # the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(1,100):
        if num % 2 != 0:
            print(num)
        else:
            pass 
first_odds()

# # 3 - Please write a Python function, max_num_in_list to return
# # the max number of a given list. 
# import numbers


def max_num_in_list(a_list):
    lgNum = a_list[0]
    for a in a_list:
        if a >= lgNum:
            lgNum = a
    return lgNum

print(f"\n{max_num_in_list([890, 290, 9, 900, 490])}\n")


# # 4 - Write a function to return if the given year is a leap year. 
# # A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 
# # 400. The return should be boolean Type (true/false). 
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

a_year = int(input("Please enter a year: "))
if (is_leap_year(a_year)):
    print(f"{a_year} is a Leap Year!")
else:
    print(f"{a_year} is not a Leap Year!")
print(type(is_leap_year(a_year)))

# 5 - Write a function to check to see if all numbers in list are
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
# numbers, but [1,2,4,5] are not consecutive numbers. The return
# should be boolean Type. 
def is_consecutive(a_list):
    a_list = [2,3,4,5,6]
    for a in a_list:
        if a == a + 1: 
            return True
        else:
            return False

print(f"\n{is_consecutive(a_list=[2,3,4,5,6])}\n")