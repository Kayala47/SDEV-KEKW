import unittest
import os
from rolling import *

class BlackBoxTests(unittest.TestCase):
    
#-------------------------------------------
#  BLACK BOX TEST CASES
#-------------------------------------------
    def test_inputError(self):
        message = \
        'Slow your roll! We did not recognize the following parameters: [x].'
        self.assertEqual(inputError(['x']), message)
    
    def test_dbError_False(self):
        message = \
        'test does not exist. Check your item name.'    
        self.assertEqual(dbError(False,'test'), message)
   
    def test_dbError_True(self):
        message = \
        'test already exists. Please remove item if attempting to add item of same name.'
        self.assertEqual(dbError(True, 'test'), message)

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

    #Note: Specs incorrectly identified the following test case:
    # Testing: multiroll(die ?= 20, q ?= 1, mod ?= 0, fudge ?= 0)
    # Testing Case 1: Assert that a 4th parameter (fudge) successfully overrides the roll
    #                 without providing any indication of doing so.
    # Justification: Fudge rolling is a valuable tool for a DM when discrete. We need
    #                to ensure that adding the 4th parameter changes the behavior of the
    #                function without showing the players.
    # Special Set-Up: None
    # Generation: Call multiroll with full parameter completeness AND a fudge > 0
    #             (ex. 1d20+4 24 will return 24 regardless of the roll)
    # Correctness: Correctly outputs formatted string with fudge substituted for calculation.
    # Clean-Up: None

    # This behavior is a black box test - as such it was included there instead

class WhiteBoxTests(unittest.TestCase):
    def setUp(self):
        with open('macroset.csv', mode='a+', newline='') as macro_file:
            macro_writer = csv.writer(macro_file, lineterminator='\r')
            item = ['sword of the divine', 2, 10, 6]
            macro_writer.writerow(item)
    
    def tearDown(self):
        if os.path.exists('macroset.csv'):
            os.remove('macroset.csv')

    def test_addMacro_no_collision(self):
        addMacro(1, 2, 3, 'spear of testing')
        with open('macroset.csv', 'r') as f:
            reader = csv.reader(f)
            items = [[row] for row in reader]
        for item in items:
            if item[0] == 'spear of testing':
                self.assertEqual(item[1], 1)
                self.assertEqual(item[2], 2)
                self.assertEqual(item[3], 3)
    
    def test_addMacro_collision(self):
        message = \
        'sword of the divine already exists. Please remove item if attempting to add item of same name.'
        self.assertEqual(addMacro(10, 10, 10, 'sword of the divine'), message)
    
    def test_delMacro_with_item(self):
        delMacro('sword of the divine')
        with open('macroset.csv', 'r') as f:
            reader = csv.reader(f)
            items = [[row] for row in reader]
        self.assertEqual(items, [])
    
    def test_delMacro_no_item(self):
        message = \
        'spear of testing does not exist. Check your item name.'
        self.assertEqual(delMacro('spear of testing'), message)

    #Note: Error toolkit does not necessitate white box testing, the components 
    #      calling the error methods did, so testing is done there instead

if __name__ == '__main__':
    unittest.main()
    