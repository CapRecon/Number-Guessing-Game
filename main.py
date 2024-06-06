import functions

if __name__ == '__main__':
    print("\tNUMBER GUESSING GAME")
    functions.help()
    lower, upper = functions.take_limits()
    rand_num = functions.random_number(lower, upper)
    print("Random number generated : ",rand_num)











