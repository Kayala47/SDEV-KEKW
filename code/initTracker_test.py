import unittest
import os
from initTracker import *

dummyJoin = [['@a', 'a', 20], ['@b', 'b', 15], ['@c', 'c', 10], ['@d', 'd', 5]]
tracker = InitTracker()

class initTracker_Tests(unittest.TestCase):

    def setUp(self):
        tracker.end()
    
    # Assert that the character is added to trackerInfo by checking that,
    # after join(username, name, initiative) is called, len(trackerInfo)
    # has increased by 1.
    def test_join_1(self):
        count = 0
        self.assertEqual(len(tracker.trackerInfo), 0)
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
            count = count + 1
            self.assertEqual(len(tracker.trackerInfo), count)
    
    # Assert that the username, name, and initiative value of the character
    # being added match.
    def test_join_2(self):
        count = 0
        self.assertEqual(tracker.trackerInfo, [])

        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
            count = count + 1
            
            if count == 1:
                self.assertEqual(tracker.trackerInfo[0], ['@a', 'a', 20])
            elif count == 2:
                self.assertEqual(tracker.trackerInfo[1], ['@b', 'b', 15])
            elif count == 3:
                self.assertEqual(tracker.trackerInfo[2], ['@c', 'c', 10])
            elif count == 4:
                self.assertEqual(tracker.trackerInfo[3], ['@d', 'd', 5])
            else:
                pass

    # Assert that initiative is an integer.
    def test_join_3(self):
        self.assertEqual(tracker.join('@a', 'a', 'string'), "Initiative must be an integer!")

    # Assert that when trackerInfo has less than two combatants, an error
    # message is returned.
    def test_begin_1(self):
        # Zero combatants
        error_str = "At least two combatants required!"
        self.assertEqual(tracker.begin(), error_str)

        # One combatant
        tracker.join(dummyJoin[0][0], dummyJoin[0][1], dummyJoin[0][2])
        self.assertEqual(tracker.begin(), error_str)

    # Assert that the full list of characters engaged in combat is returned
    # when begin() is called.
    def test_begin_2(self):
        count = 0
        error_str1 = "At least two combatants required!"
        error_str2 = "Combat has already begun! User !end to clear the initiative tracker."
        
        begin_str = "-----------------------------------\nCurrent Round: 1\n-----------------------------------"
        middle_str = ""
        end_str = "\n-----------------------------------"

        self.assertEqual(tracker.begin(), error_str1)
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
            count = count + 1
            if count == 1:
                middle_str = middle_str + "\n**" + str(data[2]) + ": " + data[1] + "**"
                self.assertEqual(tracker.begin(), error_str1)
            else:
                middle_str = middle_str + "\n" + str(data[2]) + ": " + data[1]
                self.assertEqual(tracker.begin(), begin_str + middle_str + end_str)
                self.assertEqual(tracker.begin(), error_str2)
                tracker.rounds = 0

    # Assert that the characters are in the correct sorted order when they
    #are printed.
    def test_sort(self):
        begin_str = "-----------------------------------\nCurrent Round: 1\n-----------------------------------"
        middle_str = ""
        end_str = "\n-----------------------------------"

        tracker.join('@b', 'b', 15)
        tracker.join('@a', 'a', 20)
        tracker.join('@d', 'd', 5)
        tracker.join('@c', 'c', 10)

        middle_str = "\n**20: a**\n15: b\n10: c\n5: d"

        self.assertEqual(tracker.begin(), begin_str + middle_str + end_str)

    # Assert that trackerInfo is cleared when end() is called.
    def test_end(self):
        self.assertEqual(tracker.trackerInfo, [])
        self.assertEqual(tracker.rounds, 0)
        self.assertEqual(tracker.currentPlayer, 0)

    # Assert that currentPlayer is increased by 1 if index isn't
    # len(trackerInfo) - 1.
    def test_next_1(self):
        self.assertEqual(tracker.currentPlayer, 0)
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
        
        tracker.begin()
        self.assertEqual(tracker.currentPlayer, 0)
        
        tracker.next()
        self.assertEqual(tracker.currentPlayer, 1)

        tracker.next()
        self.assertEqual(tracker.currentPlayer, 2)

        tracker.next()
        self.assertEqual(tracker.currentPlayer, 3)
    
    # Assert that currentPlayer is reset to 0 if index is len(trackerInfo)
    # - 1 when next() is called.
    def test_next_2(self):
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])

        tracker.begin()
        
        tracker.next()
        tracker.next()
        tracker.next()
        self.assertEqual(tracker.currentPlayer, 3)
        tracker.next()
        self.assertEqual(tracker.currentPlayer, 0)

    # Assert that an error is sent if begin() hasn't been called yet.
    def test_next_3(self):
        self.assertEqual(tracker.next(), "Combat hasn't begun yet! Use !begin to begin combat.")
        
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
        
        self.assertEqual(tracker.next(), "Combat hasn't begun yet! Use !begin to begin combat.")
        self.assertEqual(tracker.rounds, 0)
        self.assertEqual(tracker.currentPlayer, 0)
    
    # Assert that currentPlayer is decreased by 1 if index isn't 0.
    def test_prev_1(self):
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
        
        tracker.begin()
        tracker.currentPlayer = 3
        self.assertEqual(tracker.currentPlayer, 3)
        
        tracker.prev()
        self.assertEqual(tracker.currentPlayer, 2)

        tracker.prev()
        self.assertEqual(tracker.currentPlayer, 1)

        tracker.prev()
        self.assertEqual(tracker.currentPlayer, 0)

    # Assert that currentPlayer is reset to len(trackerInfo) - 1 if index is
    # 0 when prev() is called.
    def test_prev_2(self):
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
        
        tracker.begin()
        tracker.currentPlayer = 0
        tracker.rounds = 2
        self.assertEqual(tracker.currentPlayer, 0)

        tracker.prev()
        self.assertEqual(tracker.currentPlayer, 3)
    
    # Assert that an error is sent if begin() hasn't been called yet.
    def test_prev_3(self):
        self.assertEqual(tracker.next(), "Combat hasn't begun yet! Use !begin to begin combat.")

        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
        
        self.assertEqual(tracker.prev(), "Combat hasn't begun yet! Use !begin to begin combat.")
        self.assertEqual(tracker.rounds, 0)
        self.assertEqual(tracker.currentPlayer, 0)

    # Assert that the round has been incremented by 1.
    def test_inc(self):
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
        
        tracker.begin()
        tracker.next()
        tracker.next()
        tracker.next()
        self.assertEqual(tracker.currentPlayer, 3)
        self.assertEqual(tracker.rounds, 1)
        tracker.next()
        self.assertEqual(tracker.currentPlayer, 0)
        self.assertEqual(tracker.rounds, 2)

    # Assert that the round has been decremented by 1.
    def test_dec(self):
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
        
        tracker.begin()
        tracker.next()
        tracker.next()
        tracker.next()
        tracker.next()
        self.assertEqual(tracker.currentPlayer, 0)
        self.assertEqual(tracker.rounds, 2)
        tracker.prev()
        self.assertEqual(tracker.currentPlayer, 3)
        self.assertEqual(tracker.rounds, 1)


if __name__ == '__main__':
    unittest.main()
