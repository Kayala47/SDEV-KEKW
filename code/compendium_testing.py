import unittest
import timeit
import random
import requests
from PIL import Image
import os
# from compendium import *

# for use in testing


def get_date_taken(path):
    return Image.open(path).getexif()[36867]


# -------------------------------------
#   BLACK BOX TESTING
# -------------------------------------

class BlackBoxTesting(unittest.TestCase):

    def setUp(self):
        self.searches = ["class barbarian", "race dragonborn",
                         "feat great weapon master", "spell magic missile"]

    def tearDown(self):
        os.remove("screenshot.png")

    def test_time(self):
        arr = random.choice(self.searches)

        start = timeit.timeit()

        compendium.search(kwd)

        stop = timeit.time()

        self.assertTrue(stop - start < 0.20)

    def test_stepDist(self):
        self.assertEqual(stepDist("class", "cass"), 1)
        self.assertEqual(stepDist("race", "race"), 0)
        self.assertEqual(stepDist("sppelll", "spell"), 2)

    def test_api_search(self):
        phrases = "class barbarian".split(" ")

        self.assertEqual(requests.get(
            "https://www.dnd5eapi.co/api/classes/barbarian").text, compendium.api_search(phrases))

    def test_get_title(self):
        URL = "http://dnd5e.wikidot.com/gnome"

        self.assertEqual(compendium.get_title(URL), "Gnome")

    def test_search(self):
        first_shot = get_date_taken("screenshot.png")

        compendium.search(random.choice(self.searches).split(" "))

        second_shot = get_date_taken("screenshot.png")

        self.assertNotEqual(first_shot, second_shot)  # a new picture was taken

    def test_invalid_key_huge_difference(self):
        # if stepDist > 3, should not be accepted

        big_diff = ["difference", "magic-missile"]

        self.assertEqual(compendium.search(
            big_diff), "Woah! Our sending spell failed. That keyword isn't recognized.")

    def test_invalid_key_small_difference(self):

        small_diff = ["classs", "magic-missile"]

        self.assertEqual(compendium.search(
            small_diff, ["class", "magic-missile"]))

# -------------------------------------
#   WHITE BOX TESTING
# -------------------------------------


class WhiteBoxTesting(unittest.TestCase):

    def setUp(self):
        self.img_path = "screenshot.png"

    def test_strip_html(self):
        string_with_html = "<div class='main-content-wrap col-md-9'> <div class = 'main-content'> <div class='page-title page-header'> <span> Gnome </span> </div> </div> </div>"

        self.assertEqual(compendium.strip_html(string_with_html), "Gnome")

    def test_wrong_page_actually(self):
        bad_URL = "http://dnd5e.wikidot.com/gnomz"

        self.assertFalse(compendium.is_valid_url(
            bad_URL))

    def test_wrong_page_not(self):
        good_URL = "http://dnd5e.wikidot.com/gnome"

        self.assertTrue(compendium.is_valid_url(good_URL))


if __name__ == '__main__':
    unittest.main()
