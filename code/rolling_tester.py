import unittest
from rolling import *

class TestRollingMethods(unittest.TestCase):
    
#-------------------------------------------
#  BLACK BOX TEST CASES
#-------------------------------------------

    def test_roll1(self):
        for i in range(100):
            self.assertTrue(0<roll()<21)
        for i in range(100):
            self.assertTrue(0<roll(100)<101)
    
    def test_roll2(self):
        self.assertTrue(roll('x') == 'Slow your roll! We did not recognize the following parameters: [x], please be sure to use the following format: x d y + z.')
    
    def test_rollAdv1(self):
        roll = rollAdv()[:-1]
        roll = roll.split()
        self.assertEqual(int(roll[5]), max(int(roll[1]), int(roll[3])))
   
    def test_rollAdv1(self):
        roll = rollAdv(False)[:-1]
        roll = roll.split()
        self.assertEqual(int(roll[5]), min(int(roll[1]), int(roll[3])))

    def test_manualRoll(self):
        pass
    
    def test_multiRollBB(self):
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
    