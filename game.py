import generator
def user_input():
    limit_check = False
    while limit_check is False:
        try:
            input_num = int(input(">>Guess: "))
            limit_check = True
        except(ValueError):
            print("ERROR_CODE(0):NUMBER_INVALID")
            continue
    return input_num

def guess_check(try_num, rand_num):
    for tries in range(try_num):
        input = user_input()
        if input == rand_num:
            print("\tCONGRATULATIONS, YOU WIN!")
            print(f"You got the correct answer on try {tries + 1} of {try_num}!")
            break
        else:
            print("\tWRONG GUESS, TRY AGAIN!")
            print(f"Tries Left: {try_num - (tries + 1)} / {try_num}")
            if (tries + 1) == try_num:
                print("\tYOU LOSE! BETTER LUCK NEXT TIME!")
                print(f"RANDOM NUMBER: {rand_num}")
                break


