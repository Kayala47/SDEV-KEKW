import unittest
import timeit
import random
#from ourfile import search, stepDIst


class BlackBoxTesting(unittest.TestCase):

    testClasses = ["class barbarian", "class paladin",
                   "class rogue", "class wizard"]
    testRaces = ["race dragonborn", "race human", "race elf"]
    testFeats = ["feat greate weapon master", "feat shield master"]
    testSpells = ["spell magic missile",
                  "spell fireball", "spell eldritch blast"]

    # now we'll try some misspellings
    testClasses_misp = ["clas barbarian", "cass paladin",
                        "lass rogue", "classs wizard"]
    testRaces_misp = ["racer dragonborn", "rac human", "race elf"]
    testFeats_misp = ["feet greate weapon master", "feat shield master"]
    testSpells_misp = ["spelll magic missile",
                       "spel fireball", "sdpell eldritch blast"]

    container = [testClasses, testRaces, testFeats, testSpells,
                 testClasses_misp, testRaces_misp, testFeats_misp, testSpells_misp]

    def test_time(self):

        arr = random.choice(self.container)
        keywd = random.choice(arr)
        start = timeit.timeit()

        search(keywd)

        stop = timeit.timeit()

        self.assertTrue(stop - start < 0.20)

    def test_typos(self):
        for i in range(4, len(self.container)):
            for phrase in i:
                self.assertIsNot(search(phrase), "Invalid Argument")

    def test_stepDist(self):
        # arr = random.choice(self.container)
        # arr_index_1 = self.container.index(arr)
        # arr_index_2 = arr_index_1 + 4 if arr_index_1 < 4 else arr_index_1 - 4

        # phrase = random.choice(arr)
        # p_index = arr.index(phrase)
        self.assertEqual(stepDist("hello", "hell"), 1)  # subtraction
        self.assertEqual(stepDist("dragonborn", "dragonbourne"), 1)  # addition
        self.assertEqual(stepDist("rogue", "rouge"), 1)  # swap

    def test_overload(self):

        try:
            count = 0
            max = 1000  # let's say that's the max number we can let a user have in backlog
            while count < max:

            for l in self.container:
                for phrase in l:
                    search(phrase)

        except:
            traceback.print_exec()


if __name__ == '__main__':
    unittest.main()
