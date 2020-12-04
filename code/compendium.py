from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup
import numpy as np


# Component Implementation - Compendium Search

'''
Team: Discord Dragons
    Members: Dana, Kevin, Max, Swamik
    Project: 4B.3 - Test Driven Development
    Primary Author: Kevin
    Slip Days: 0

PURPOSE: 

The purpose of this module is to get information to our users
about rulesets that pertain to them. Specifically, we want to 
do this for free, which is a huge departure from the existing 
programs that do this. Furthermore, in the true spirit of D&D, 
we do it using the great wealth of information cultivated by 
players of the game in the form of the D&D wiki at
http://dnd5e.wikidot.com/
'''

# ------------------------------------------------------------
#   ERROR TOOLKIT
# ------------------------------------------------------------


def invalidKeyError(kwd: str) -> str:
    return "Woah! Our sending spell failed. " + kwd + " isn't recognized."


def wrongPageError(params: str) -> str:
    return "Darn. Someone cast Shatter on that page. You sure this is the right spelling? \n " + " ".join(params.split("-"))


def noScreenshotError() -> str:
    return "Oops. Looks like our screenshot misty-stepped away! It's probably a timeout, try again?"

# ------------------------------------------------------------
#   SEARCH TOOLKIT
# ------------------------------------------------------------


POSSIBLE_KEYWORDS = ["class", "feat", "background", "spell"]


def search(params: list) -> (bool, str):
    '''
    Searches the wiki for relevant results and takes a screenshot
    if successful.
    Inputs:
        params[0] | the keyword for the search. One of: "class", 
            "feat", "spell", "background"
        params[1:] | all other strings passed in are an individual 
            search parameter. Ex: [..., "magic", "missile"]

    Outputs:
        bool | True if a webpage was found and screenshot taken. 
            False if any errors occured.
        str | the message the bot will send. 
    '''

    # let's unpack the array we're given
    kwd = params[0]
    search = "-".join(params[1:])

    retString = ""  # we'll add some messages to this later

    # first check if the keyword is valid
    url = router(kwd, search, True)

    if not url:
        return (False, invalidKeyError(kwd))

    # now we check if the rest of the search is good, by just
    # making sure it finds a working webpage
    title = getTitle(url)

    if title == "The page does not (yet) exist.":
        return (False, wrongPageError(search))
    else:
        retString += title + ": \n"

    if not screenshot(url):
        return (False, noScreenshotError())

    retString += url

    return (True, retString)


def screenshot(url: str) -> bool:
    '''
    Takes a screenshot of the given url and saves locally. 
    Inputs:
        url | the url to be visited
    Output: 
        bool | True if screenshot taken, False if not
    '''
    try:
        # these can be adjusted to take a good screenshot
        options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        options.headless = True  # wont' open a browser window to do this

        # this is what will scrape the web
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        driver.get(url)  # opens the page

        # quick function to grab the scroll values for height and width
        def S(X): return driver.execute_script(
            'return document.body.parentNode.scroll'+X)
        # that tells us the size of our img
        driver.set_window_size(S('Width') * .8, min(S('Height') * .80, 700))
        #S('Height') * .88

        # takes screenshot and saves as "screenshot.png"
        driver.find_element_by_tag_name('body').screenshot('screenshot.png')
        # driver.get_screenshot_as_file("screenshot.png")

        driver.quit()  # closes the page

        return True
    except:   
        return False


def router(kwd: str, srch: str, first_rnd: bool) -> str:
    '''
    Routes the search to the correct url based on the keyword. Applies
    editDistance in case there was a close typo.
    Inputs:
        kwd | keyword for the search, used to route to correct url. 
        srch | the rest of the url parameters. Words are split by a 
            hyphen 
    Output: 
        str | the resultant URL
    '''

    # they all start with this
    base_url = "http://dnd5e.wikidot.com/"

    # no switch statements in Python :/

    if kwd == "race":
        return base_url + srch
    elif kwd == "spell":
        return base_url + "spell:" + srch
    elif kwd == "background":
        return base_url + "background:" + srch
    elif kwd == "feat":
        return base_url + "feat:" + srch
    elif kwd == "class":
        return base_url + srch
    else:
        # if none of them fit, we try to fix it /ONCE/
        if first_rnd:
            kwd = editHelper(kwd, POSSIBLE_KEYWORDS)
            return router(kwd, srch, False)
            # fixd_typo = True
        else:
            return None


def getTitle(url: str) -> str:
    '''
    Checks the specified URL and (using Requests and Beautiful Soup), 
    determines whether this page is valid. 
    Inputs:
        url | the url to be validated 
    Output: 
        str | the text of this page's title
    '''

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')  # tanslates results

    # finds the correct div
    results = soup.body.find('div', attrs={'class': 'page-title'})

    # inside of the div, this span contains the title
    title = results.find('span').text

    return title


def editHelper(kwd: str, possibilies: list) -> str:
    '''
    Compares kwd to the list of possible str's, returning
    one of those is the str is within 3 edits of that word and
    if that word has the least edit distance. 

    Inputs:
        kwd | the keyword, probably containing a typo
        possibilities | list of possible strings
    Output: 
        str | the keyword corrected for typos
    '''

    min = np.inf
    ret = possibilies[0]
    for p in possibilies:
        dist = editDistance(kwd, p)

        if dist < min:
            ret = p
            min = dist

    if min <= 3 and ret[0] == kwd[0]:
        return ret
    else:
        return None


def editDistance(s1, s2):
    '''
    Compares two strings to see how many steps there are to turn 
    str1 into str2
    Inputs:
        str1 | first string compared
        str2 | second string compared
        m    | length of first string
        n    | length of second string
    Output: 
        int | the min number of addditions, deletions, or 
            substitutions needed to make str1 into str2 or 
            vice versa
    '''
    if not s1:
        return 1000
    elif not s2:
        return 1000

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


if __name__ == '__main__':
    print(screenshot("http://dnd5e.wikidot.com/barbarian"))
