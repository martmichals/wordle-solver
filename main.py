import argparse, time
from seleniumbase import BaseCase
from seleniumbase import __version__

# Wordle URL
URL = 'https://www.nytimes.com/games/wordle/index.html'

# Class for interacting with the wordle webpage
class WordleSolver(BaseCase):
    # Function taken from:
    #       https://github.com/seleniumbase/SeleniumBase/blob/master/examples/wordle_test.py
    def skip_if_incorrect_env(self):
        if self.headless:
            message = "This test doesn't run in headless mode!"
            print(message)
            self.skip(message)
        version = [int(i) for i in __version__.split(".") if i.isdigit()]
        if version < [2, 4, 4]:
            message = "This test requires SeleniumBase 2.4.4 or newer!"
            print(message)
            self.skip(message)

    def load_wordle(self):
        # Check environment, open the wordle url
        self.skip_if_incorrect_env()
        self.open(URL)

        # Delete the pop up with game instructions
        self.click('game-app::shadow game-modal::shadow game-icon')

    # @property
    # def letters(self):
        

    def test_wordle_solver(self):
        print('Loading the wordle webpage')
        self.load_wordle()
