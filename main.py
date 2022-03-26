import argparse, re
import requests
from seleniumbase import BaseCase
from seleniumbase import __version__

# Wordle URL
URL = 'https://www.nytimes.com/games/wordle/index.html'

# Class for solving wordles offline
class WordleSolver():
    POSSIBLE_ANSWER_GIT = 'https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/28804271b5a226628d36ee831b0e36adef9cf449/wordle-answers-alphabetical.txt'

    def __init__(self):
        # Download the possible answer list
        self.answer_list = requests.get(WordleSolver.POSSIBLE_ANSWER_GIT).text.split('\n')

def main(args):
    # Validate arguments
    if args.run_type not in (valid_run_types := {'all', 'single'}):
        raise ValueError(f'Run type is not one of {valid_run_types}')
    elif args.run_type == 'single':
        if not args.answer: raise ValueError(f'single selected as run_type and no --answer argument was specified')
        if not re.match(r'([a-zA-Z]){5}', args.answer): raise ValueError(f'{args.answer} is an invalid wordle answer') # Fast validity check

    # Instantiate solver
    solver = WordleSolver()

    # Validate single word answer with real answer list
    if args.answer and args.answer.lower() not in solver.answer_list:
        raise ValueError(f'{args.answer} not in official answer list')

    # Based on run type, set up answer list
    answers = [args.answer] if args.run_type == 'single' else solver.answer_list

    # Solve wordles requested via our solver
    # for answer in answers:

if __name__ == '__main__':
    # Define parser
    parser = argparse.ArgumentParser(
        description='Wordle Solver, main.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Define arguments 
    parser.add_argument(
        '--run_type',
        default='all',
        help='One of [all, single], selects how to run the solver'
    )
    parser.add_argument(
        '--answer', 
        required=False,
        help='Correct answer to the wordle, if running in single mode'  
    )

    # Parse arguments
    args = parser.parse_args()

    # Solve
    main(args)