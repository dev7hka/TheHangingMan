import random, time

"""
19.09.2020 - Hangman Project - Day 1

Rules of the game:
    - It is a word guessing game
    - In every tour, you pick a letter; if true, letter(s) are placed. Otherwise, the hanging man will be drawn more.
    - You have limited number of guess
    - It may be more than one word
    - Your point will be calculated according to the guess left
    - Example of hanging man
    |----------|
    |          |
    |         ---
    |        |   |
    |         ---
    |          |
    |          |
    |       -------
    |      |   |   |
    |      |   |   |
    |      |   |   |
    |          |
    |          |
    |         / \
    |        /   \
    |       /     \
    |
    |
    |
Tasks(functions):
    - Man drawer
    - letter picker
    - letter checker
    - point calculator
    - word viewer
    - man printer
    
"""

class HangingMan():
    __wordsDatabase: list = ["BATMAN", "SUPERMAN", "SPIDERMAN", "IRONMAN","ITISALOOONGWORDYOUKNOW"]
    __word: list = None
    __guessWord: list = None
    __guessLeft: int = None
    __lettersAvailable = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                          "T", "U", "V", "W", "X", "Y", "Z"]
    __wholeMan = [
        "|----------|",
        "|          |",
        "|         ---",
        "|        |   |",
        "|         ---",
        "|          |",
        "|          |",
        "|       -------",
        "|      |   |   |",
        "|      |   |   |",
        "|      |   |   |",
        "|          |",
        "|          |",
        "|         / \\",
        "|        /   \\",
        "|       /     \\",
        "|",
        "|",
        "|"]
    __hangingManCounter: int = None

    def __init__(self):
        index = random.randint(0, len(self.__wordsDatabase) - 1)
        self.__word = [x for x in self.__wordsDatabase[index]]
        self.__guessLeft = 10
        self.__guessWord = ["_" for i in range(len(self.__word))]
        self.__hangingManCounter = 0

    def letterPicker(self):

        self.wordViewer()
        self.letterViewer()
        print("Your Guess:", end="")
        guess = input()
        index = -1 if self.__lettersAvailable.count(guess) == 0 else self.__lettersAvailable.index(guess)
        if index < 0 or index >= len(self.__lettersAvailable):
            return -1
        else:
            letter = self.__lettersAvailable.pop(index)
            return letter

    def letterChecker(self, letter):

        self.__guessLeft -= 1
        if letter == -1 or self.__word.count(letter) == 0:
            self.__hangingManCounter += 1
            return -1
        for i in range(len(self.__word)):
            if self.__word[i] == letter:
                self.__guessWord[i] = letter
        return self.__word.count(letter)

    def pointViewer(self):

        print("Point:",len(self.__word) - self.__guessWord.count("_"))

    def wordViewer(self):

        print("Your Guess: ", "".join(self.__guessWord), end="\n")

    def letterViewer(self):

        print("Letters: ", "-".join(self.__lettersAvailable), end="\n")

    def manPrinter(self):

        end = self.__hangingManCounter * int(18 / len(self.__word))
        if len(self.__word) > 18:
            end = self.__hangingManCounter
        if self.__guessLeft == 0 or end >= len(self.__word):
            print("\n".join(self.__wholeMan), end="\n\n")
            self.pointViewer()
            exit()
        print("\n".join(self.__wholeMan[0:end]), end="\n\n")
        self.pointViewer()
        if self.__word == self.__guessWord:
            print("Congratulations !!!")
            exit()
hangingManGame = HangingMan()
while True:
    letter = hangingManGame.letterPicker()
    hangingManGame.letterChecker(letter)
    hangingManGame.manPrinter()
