from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup


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


def editDistance(str1, str2):
    return editDistanceHelper(str1, str2, len(str1), len(str2))


def editDistanceHelper(str1, str2, m, n) -> int:
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

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1] == str2[n-1]:
        return editDistanceHelper(str1, str2, m-1, n-1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistanceHelper(str1, str2, m, n-1),    # Insert
                   editDistanceHelper(str1, str2, m-1, n),    # Remove
                   editDistanceHelper(str1, str2, m-1, n-1)    # Replace
                   )


if __name__ == '__main__':
    getTitle("http://dnd5e.wikidot.com/feat:great-weapon-maste")
