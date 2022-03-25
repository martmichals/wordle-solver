import argparse, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Wordle URL
URL = 'https://www.nytimes.com/games/wordle/index.html'

# Path to chromium driver
CHROMIUM_PATH = 'C:\Program Files\Chromium\chromedriver.exe'

# Helper function for getting all letters in the wordle matrix
def get_letters(browser):
    # Get all of the letter squares
    letter_divs = browser.find_elements(by=By.CLASS_NAME, value='tile')
    print(letter_divs)
    print(f'Length: {len(letter_divs)}')

# Naive solver
def naive_solver(browser):
    # Get and validate the initial board state
    wordle_matrix = get_letters(browser)

    return

# Solving strategies
STRATEGIES = {
    'naive': naive_solver
}

# Solve function launcher
def main(args):
    # Launch selenium, opening the daily wordle
    print('Launching selenium browser...')
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s)
    browser.get(URL)

    # Wait until the webpage loads
    print('Waiting for the page to load...')
    try:
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="game"]/game-modal//div/div/div/game-icon//svg'))).click()
    except TimeoutException:
        print('Page load failure.')
    time.sleep(50000)

    # Launch the selected solver
    if args.strategy not in STRATEGIES:
        raise ValueError(f'{args.strategy} is not one of ({", ".join(STRATEGIES)})')
    STRATEGIES[args.strategy](browser)
    
if __name__ == '__main__':
    # Define parser
    parser = argparse.ArgumentParser(
        description='Wordle Solver, main.py',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Define arguments 
    parser.add_argument(
        '--strategy',
        default='naive'
    )

    # Parse arguments
    args = parser.parse_args()

    # Solve
    main(args)


