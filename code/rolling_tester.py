import unittest
import os
from rolling import *

class TestRollingMethods(unittest.TestCase):
    
#-------------------------------------------
#  BLACK BOX TEST CASES
#-------------------------------------------

    def test_roll(self):
        for test in range(1000):
            self.assertTrue(0 < roll() < 21)
            self.assertTrue(0 < roll(100) < 101)
    
    def test_roll_param_eror(self):
        self.assertEqual(roll('x'), 'Slow your roll! We did not recognize the following parameters: [x].')

    def test_roll_param_error2(self):
        self.assertEqual(roll(0), negativeError())

    def test_rollAdv_True(self):
        roll = rollAdv()[:-1]
        roll = roll.split()
        self.assertEqual(int(roll[5]), max(int(roll[1]), int(roll[3])))
   
    def test_rollAdv_False(self):
        roll = rollAdv(False)[:-1]
        roll = roll.split()
        self.assertEqual(int(roll[5]), min(int(roll[1]), int(roll[3])))

    def test_rollAdv_param_error(self):
        self.assertEqual(rollAdv('x'), 'Slow your roll! We did not recognize the following parameters: [x].')

    def test_multiRoll_0_params(self):
        for test in range(1000):
            roll = multiroll()[:-1].split()
            self.assertEqual(int(roll[1]), 1)
            self.assertEqual(int(roll[3]), 20)
            self.assertEqual(int(roll[5][1:-1]),  0)
            self.assertTrue(0 < int(roll[-1]) < 21)

    def test_multiRoll_1_params(self):
        for test in range(1000):
            roll = multiroll(100)[:-1].split()
            self.assertEqual(int(roll[1]), 1)
            self.assertEqual(int(roll[3]), 100)
            self.assertEqual(int(roll[5][1:-1]),  0)
            self.assertTrue(0 < int(roll[-1]) < 101)

    def test_multiRoll_2_params(self):
        for test in range(1000):
            roll = multiroll(100, 10)[:-1].split()
            self.assertEqual(int(roll[1]), 10)
            self.assertEqual(int(roll[3]), 100)
            self.assertEqual(int(roll[5][1:-1]),  0)
            self.assertTrue(0 < int(roll[-1]) < 1001)

    def test_multiRoll_3_params(self):
        for test in range(1000):
            roll = multiroll(100, 10, 10)[:-1].split()
            self.assertEqual(int(roll[1]), 10)
            self.assertEqual(int(roll[3]), 100)
            self.assertEqual(int(roll[5][1:-1]),  10)
            self.assertTrue(10 < int(roll[-1]) < 1011)

    def test_multiRoll_fudge(self):
        for test in range(1000):
            roll = multiroll(100, 10, 10, 42)[:-1].split()
            self.assertEqual(int(roll[1]), 10)
            self.assertEqual(int(roll[3]), 100)
            self.assertEqual(int(roll[5][1:-1]),  10)
            self.assertEqual(int(roll[-1]), 42)

    def test_multiRoll_param_error(self):
        error_str = 'Slow your roll! We did not recognize the following parameters: [x'
        self.assertEqual(multiroll('x'), error_str + '].' )
        self.assertEqual(multiroll('x', 'x'), error_str + ', x].')
        self.assertEqual(multiroll('x', 'x', 'x'), error_str + ', x, x].')
        self.assertEqual(multiroll('x', 'x', 'x', 'x'), error_str + ', x, x, x].')
    
    def test_multiRoll_param_error2(self):
        self.assertEqual(multiroll(0), negativeError())
        
    def test_manualRoll_combined_params(self):
        roll = manualRoll(20)[:-1].split()
        self.assertEqual(int(roll[1]), 1)
        self.assertEqual(int(roll[3]), 20)      
        self.assertEqual(int(roll[5][1:-1]), 0)          
        self.assertEqual(int(roll[-1]), 20)

    def test_addMacro_param_error(self):
        error = 'Slow your roll! We did not recognize the following parameters: [x].'
        self.assertEqual(addMacro('x', 2, 3, 'x'), error)
        self.assertEqual(addMacro(1, 'x', 3, 'x'), error)
        self.assertEqual(addMacro(1, 2, 'x', 'x'), error)

    #Note: Specs incorrectly identified the following test case:
    # Testing: delMacro(itemname)
    # Testing Case 1: Assert that delMacro() successfully flags an input error if 
    #                 itemname is an int.
    # Justification: We cant look for a key in the database if the key can't exist.
    # Special Set-Up: None
    # Generation: When delMacro() is called where itemname is not a string.
    # Correctness: We expect the anticipated error message (see specs) along with 
    #              an indicator that any specific parameter is invalid.
    # Clean-Up: None

    # I have determined this behavior is actually fine, players may identify items by 
    # integers and store lore details elsewhere, for instance.

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
    