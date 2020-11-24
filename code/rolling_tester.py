import unittest
from rolling import *

class TestRollingMethods(unittest.TestCase):
    
#-------------------------------------------
#  BLACK BOX TEST CASES
#-------------------------------------------

    def test_roll_1(self):
        for i in range(1000):
            self.assertTrue(0 < roll() < 21)
            self.assertTrue(0 < roll(100) < 101)
    
    def test_roll_2(self):
        self.assertTrue(roll('x') == 'Slow your roll! We did not recognize the following parameters: [x].')
    
    def test_rollAdv_1(self):
        roll = rollAdv()[:-1]
        roll = roll.split()
        self.assertEqual(int(roll[5]), max(int(roll[1]), int(roll[3])))
   
    def test_rollAdv_2(self):
        roll = rollAdv(False)[:-1]
        roll = roll.split()
        self.assertEqual(int(roll[5]), min(int(roll[1]), int(roll[3])))

    def test_rollAdv_3(self):
        self.assertTrue(rollAdv('x') == 'Slow your roll! We did not recognize the following parameters: [x].')

    def test_multiRoll_BB_0_params(self):
        for i in range(1000):
            roll = multiroll()[:-1].split()
            self.assertTrue(int(roll[1]) == 1)
            self.assertTrue(int(roll[3]) == 20)
            self.assertTrue(int(roll[5][1:-1]) == 0)
            self.assertTrue(0 < int(roll[-1]) < 21)

    def test_multiRoll_BB_1_params(self):
        for i in range(1000):
            roll = multiroll(100)[:-1].split()
            self.assertTrue(int(roll[1]) == 1)
            self.assertTrue(int(roll[3]) == 100)
            self.assertTrue(int(roll[5][1:-1]) == 0)
            self.assertTrue(0 < int(roll[-1]) < 101)

    def test_multiRoll_BB_2_params(self):
        for i in range(1000):
            roll = multiroll(100, 10)[:-1].split()
            self.assertTrue(int(roll[1]) == 10)
            self.assertTrue(int(roll[3]) == 100)
            self.assertTrue(int(roll[5][1:-1]) == 0)
            self.assertTrue(0 < int(roll[-1]) < 1001)

    def test_multiRoll_BB_3_params(self):
        for i in range(1000):
            roll = multiroll(100, 10, 10)[:-1].split()
            self.assertTrue(int(roll[1]) == 10)
            self.assertTrue(int(roll[3]) == 100)
            self.assertTrue(int(roll[5][1:-1]) == 10)
            self.assertTrue(10 < int(roll[-1]) < 1011)

    def test_multiRoll_BB_fudge(self):
        for i in range(1000):
            roll = multiroll(100, 10, 10, 42)[:-1].split()
            self.assertTrue(int(roll[1]) == 10)
            self.assertTrue(int(roll[3]) == 100)
            self.assertTrue(int(roll[5][1:-1]) == 10)
            self.assertTrue(int(roll[-1]) == 42)

    def test_manualRoll(self):
        pass

    def test_addMacroBB(self):
        pass

    def test_delMacroBB(self):
        pass
    
#-------------------------------------------
#  WHITE BOX TEST CASES
#-------------------------------------------

    def test_multiRollWB(self):
        pass

    def test_addMacroWB(self):
        pass

    def test_delMacroWB(self):
        pass

    def test_inputError(self):
        pass

    def test_dbError(self):
        pass

if __name__ == '__main__':
    unittest.main()
    