import random


# computer randomly selects a three-digit number
def pick_number():
    number = random.randint(100, 999)
    return str(number)


# player enters a three-digit number
def get_player_number():
    pl_number = input(f'Enter a three-digit number: ')
    # check if player entered a valid number
    while len(pl_number) != 3 or not pl_number.isdecimal():
        pl_number = input('Please, enter a three-digit number: ')
    return str(pl_number)


'''def find(number, pl_number):
    return [i for i, dgt in enumerate(number) if dgt == pl_number]'''


# comparison of computer's and player's numbers
def compare(number, pl_number):
    clues = []

    for i in range(0, 3):
        # a correct digit is in a correct place
        if pl_number[i] == number[i]:
            clues.append('fermi')
        # a correct digit is in a wrong place
        elif pl_number[i] in number:
            clues.append('pico')
        # a digit is not in the number
        else:
            clues.append('bagel')

    # sort clues, so it's not obvious
    # which digit is in which place
    clues.sort()
    return ' '.join(clues)


def main():
    # main game loop
    while True:
        number = pick_number()
        won = False

        # 10 turns
        for i in range(0, 10):
            if i > 6:
                print(f'You have {10-i} turns left.')

            pl_number = get_player_number()

            if pl_number == number:
                print('You won!')
                won = True
                break

            clues = compare(number, pl_number)
            print(clues)

        if not won:
            print('You lost.')

        play_again = input('Do you wanna play again? (yes/no): ')
        if not play_again.lower().startswith('y'):
            break


if __name__ == "__main__":
    main()
