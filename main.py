import generator
import game

if __name__ == '__main__':
    print("\tNUMBER GUESSING GAME")
    generator.help()
    lower, upper = generator.take_limits()
    rand_num = generator.random_number(lower, upper)
    try_num = generator.try_number_calculator(lower, upper)
    game.guess_check(try_num, rand_num)











