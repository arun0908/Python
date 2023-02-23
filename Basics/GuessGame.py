# Small game to guess numbers to utilize import, error handling and other concepts.

import sys
import random


def generate_random():
    rand_number = random.randint(int(sys.argv[1]), int(sys.argv[2]))
    while True:
        try:
            user_input = int(input(
                f'Please enter your guess from your specified range : '))
            if 0 < user_input < 11:
                if user_input == rand_number:
                    print('Great, you guessed the number right')
                    break
                else:
                    print('Oops, you got it wrong, kindly try again')
            else:
                print('Kindly enter a number from your specified range')
        except ValueError:
            print('Kindly try again with proper inputs')
            continue


generate_random()
