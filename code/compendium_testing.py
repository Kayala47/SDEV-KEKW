import unittest
import timeit
import random
import requests
from PIL import Image
import os
from compendium import *

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

        search(random.choice(searches).split(" "))

        stop = timeit.time()

        self.assertTrue(stop - start < 0.20)

    def test_stepDist(self):
        self.assertEqual(editDistance("class", "cass"), 1)
        self.assertEqual(editDistance("race", "race"), 0)
        self.assertEqual(editDistance("sppelll", "spell"), 2)

    def test_api_search(self):
        phrases = "class barbarian".split(" ")

        self.assertEqual(requests.get(
            "https://www.dnd5eapi.co/api/classes/barbarian").text, api_search(phrases))

    def test_get_title(self):
        URL = "http://dnd5e.wikidot.com/gnome"

        self.assertEqual(getTitle(URL), "Gnome")

    def test_search(self):
        first_shot = get_date_taken("screenshot.png")

        search(random.choice(self.searches).split(" "))

        second_shot = get_date_taken("screenshot.png")

        self.assertNotEqual(first_shot, second_shot)  # a new picture was taken

    def test_invalid_key_huge_difference(self):
        # if stepDist > 3, should not be accepted

        big_diff = ["difference", "magic-missile"]

        self.assertEqual(search(
            big_diff), "Woah! Our sending spell failed. " + big_diff[0] + " isn't recognized.")

    def test_invalid_key_small_difference(self):

        small_diff = ["classs", "magic-missile"]

        self.assertEqual(search(
            small_diff, ["class", "magic-missile"]))

# -------------------------------------
#   WHITE BOX TESTING
# -------------------------------------


class WhiteBoxTesting(unittest.TestCase):

    def setUp(self):
        self.img_path = "screenshot.png"

    def test_strip_html(self):
        string_with_html = "<div class='main-content-wrap col-md-9'> <div class = 'main-content'> <div class='page-title page-header'> <span> Gnome </span> </div> </div> </div>"

        self.assertEqual(strip_html(string_with_html), "Gnome")

    def test_wrong_page_actually(self):
        bad_URL = "http://dnd5e.wikidot.com/gnomz"

        self.assertFalse(is_valid_url(
            bad_URL))

    def test_wrong_page_not(self):
        good_URL = "http://dnd5e.wikidot.com/gnome"

        self.assertTrue(is_valid_url(good_URL))

    def test_editHelper_bigDiff(self):
        word = "class"
        possibilities = ["lkajfd.sjfljfdlskj", "lskjdfsljfdl"]

        self.assertEqual(editHelper(word, possibilities), None)

    def test_editHelper_smallDiff(self):
        word = "class"
        possibilities = ["sldkjfsaldfjll", "class"]

        self.assertEqual(editHelper(
            word, possibilities), possibilities[1])

    def test_router_bad_url(self):
        bad_params = ["lkjsdfs", "magic-missile"]

        self.assertEqual(router(bad_params[0], bad_params[1]), None)

    def test_router_good_url(self):
        good_params = ["spell", "magic-missile"]

        self.assertEqual(router(
            good_params[0], good_params[1]), None)


if __name__ == '__main__':
    unittest.main()
