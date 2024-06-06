import random
import math

def help():
    print("\t===HELP===")
    print("Enter a lower and upper limit for the numbers. The game will generate a random number between that range.")
    print("You have a fixed amount of tries to guess the correct number.")
    print("You win if you can guess the number within the given number of tries. Good Luck!")

def take_limits():
    limit_check = False
    while limit_check is False:
        try:
            lower = int(input(">>Lower Limit: "))
            upper = int(input(">>Upper Limit: "))
        except(ValueError):
            print("ERR_CODE(0):NUMBER_INVALID")
            continue
        if (lower < upper):
            limit_check = True
        else:
            print("ERR_CODE(1):RANGE_INVALID")
    return lower, upper

def try_number_calculator(lower, upper):
    try_num = round(math.log(upper - lower + 1, 2))
    return try_num

def random_number(lower, upper):
    rand_num = random.randint(lower, upper)
    return rand_num

