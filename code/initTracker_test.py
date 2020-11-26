import unittest
import os
from initTracker import *

dummyJoin = [['@a', 'a', 20], ['@b', 'b', 15], ['@c', 'c', 10], ['@d', 'd', 5]]
tracker = InitTracker()

#-------------------------------------------
#  BLACK BOX TEST CASES
#-------------------------------------------

class initTracker_BlackBoxTests(unittest.TestCase):

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
        self.assertEqual(tracker.join('@a', 'a', 2.5), "Initiative must be an integer!")

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
        error_str2 = "Combat has already begun!"
        
        begin_str = "-----------------------------------\nCurrent Initiative: 1\n-----------------------------------"
        middle_str = ""
        end_str = "\n-----------------------------------"

        self.assertEqual(tracker.begin(), error_str1)
        for data in dummyJoin:
            tracker.join(data[0], data[1], data[2])
            count = count + 1
            # self.assertEqual(, )
    
if __name__ == '__main__':
    unittest.main()
