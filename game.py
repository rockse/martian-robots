# import evaluate_guess from engine
import random

class Game():
    """Game class"""

    def __init__(self, length):
        self.pattern = []
        self.length = length
        self.__generate_pattern()
        self.guess = []

    def __generate_pattern(self):
        self.pattern = random.sample(range(0, 9), self.length)

    def get_pattern(self):
        return self.pattern

    def ask_user_guess(self):
        self.guess = []
        for i in range(0, self.length):
            ele = int(input("Enter value of {} element: ".format(i+1)))
            self.guess.append(ele) # adding the element
        print("User input: ", self.guess)
        self.__evaluate_guess()

    def __evaluate_guess(self):
        right_matches = 0
        wrong_matches = 0

        temp_pattern = []
        temp_guess = []

        for index, (a, b) in enumerate(zip(self.pattern, self.guess)):
            if a == b:
                right_matches += 1
                print("Correct guess for {} element and number is {}".format(index+1, a))
            else:
                temp_pattern.append(a)
                temp_guess.append(b)


        for a in temp_guess:
            if a in temp_pattern:
                wrong_matches += 1
                print("Wrong guess but correct number {}".format(a))
                temp_pattern.remove(a)

        if right_matches == self.length:
            print("You won!!")
        else:
            print("Try again! or Press Ctrl + C to end the game")
            self.ask_user_guess()

if __name__ == '__main__':
    l = int(input("Enter the length of elements you want to guess: "))
    game = Game(l)
    # This is added to see the pattern generated by computer
    # Please comment it to hide the computer generated pattern
    print("Computer Pattern is: ", game.get_pattern())
    game.ask_user_guess()