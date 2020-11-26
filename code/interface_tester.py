
import unittest
import os
from testing_interface_functions import *

# This is the file with our unitesting. We are importing the testiing_interface_functions file which contains all of the logic from the 
# bot_interface file, but instead of sending messages to the chat of the discord bot, the file returns the value so we can do a check to see 
# if the functions are working correctly by using assert 

class BlackBoxTests(unittest.TestCase):
    def test_helpMe(self): 
        message = "SOME MESSAGE TO HELP: maybe a link to github"
        self.assertEqual(helpMe(), message)

    def test_roll_noInputs(self): 
        message = "You called default roll, rolling a d20"
        self.assertEqual(roll(""), message)

    def test_roll_twoInputs(self): 
        # going to call the roll function with the input of xdy. should return a list with x and y
        # Discord gives the argument to each function as a tuple of strings, we need to test it with tuples of string
        # The funcitons should work with any number of spacing
        result = ["x", "y"]
        self.assertEqual(roll(("xdy")), result)
        self.assertEqual(roll(("xd", "y")), result)
        self.assertEqual(roll(("x", "dy")), result)
        self.assertEqual(roll(("x", "d", "y")), result)
    
    def test_roll_threeInputs(self):
        # going to call the roll function with the input of xdy +m. should return a list with x, y and m
        # The funcitons should work with any number of spacing. As there are many different ways to space, we will test the edge cases and mostly used cases. For both + and - modifiers
        result = ["x", "y", "+m"]
        self.assertEqual(roll(("xdy+m")), result)
        self.assertEqual(roll(("xdy", "+m")), result)
        self.assertEqual(roll(("xdy", "+", "m")), result)
        self.assertEqual(roll(("xd", "y", "+m")), result)
        self.assertEqual(roll(("x", "dy", "+m")), result)
        self.assertEqual(roll(("x", "d", "y", "+", "m")), result)
        
        result2 = ["x", "y", "-m"]
        self.assertEqual(roll(("xdy-m")), result2)
        self.assertEqual(roll(("xdy", "-m")), result2)
        self.assertEqual(roll(("xdy", "-", "m")), result2)
        self.assertEqual(roll(("xd", "y", "-m")), result2)
        self.assertEqual(roll(("x", "dy", "-m")), result2)
        self.assertEqual(roll(("x", "d", "y", "-", "m")), result2)

    def test_roll_fourInputs(self):
        # going to call the roll function with the input of xdy +m fudgeroll. should return a list with x, y, m, and fudgeroll
        # The funcitons should work with any number of spacing. As there are many different ways to space, we will test the edge cases and mostly used cases. For both + and - modifiers
        result = ["x", "y", "+m", "f"]
        self.assertEqual(roll(("xdy+m", "f")), result)
        self.assertEqual(roll(("xdy", "+m", "f")), result)
        self.assertEqual(roll(("xdy", "+", "m", "f")), result)
        self.assertEqual(roll(("xd", "y", "+m", "f")), result)
        self.assertEqual(roll(("x", "dy", "+m", "f")), result)
        self.assertEqual(roll(("x", "d", "y", "+", "m", "f")), result)
       
        result2 = ["x", "y", "-m", "f"]
        self.assertEqual(roll(("xdy-m", "f")), result2)
        self.assertEqual(roll(("xdy", "-m", "f")), result2)
        self.assertEqual(roll(("xdy", "-", "m", "f")), result2)
        self.assertEqual(roll(("xd", "y", "-m", "f")), result2)
        self.assertEqual(roll(("x", "dy", "-m", "f")), result2)
        self.assertEqual(roll(("x", "d", "y", "-", "m", "f")), result2)

    def test_rollAdv(self):
        # the rollAdv takes in one input. If the user does not input anything we will send an error and if they do pass in an argument, we 
        # need to correctly parse it and return the input that they gave the user 
        errorResult = "You need a input for this command. Please input a bool as an input for this function. A true or false statement. Refer to helpMe command for more information :)"
        self.assertEqual(rollAdv(""), errorResult)
        # with the input "arg"
        msg = "Called rollAdv with input: arg"
        self.assertEqual(rollAdv("arg"), msg)

    def test_addMacro(self):
        msg1 = "You are missing all of the inputs needed for the addMacro function."
        msg2 = "Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        self.assertEqual(addMacro(""), result)

        msg1 = "You have too many inputs for the funciton addMacro."
        msg2 = "Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        self.assertEqual(addMacro(("d", "q", "m", "name", "extra")), result)

        self.assertEqual(addMacro(("d", "q", "m", "name")), ["d", "q", "m", "name"])

    def test_delMacro(self):
        self.assertEqual(delMacro(("")), "To delete a macro, you must input the name of the macro you wish to delete")
        self.assertEqual(delMacro(("name")), "name")
    
    def test_callMacro(self):
        self.assertEqual(callMacro(("")), "To call a macro, you must input the name of the macro you wish to call")
        self.assertEqual(callMacro(("name")), "name")

    def test_join(self):
        self.assertEqual(join(("name", "initRoll")), ["name", "initRoll"])
        self.assertEqual(join(""), "To join initiative, the input must be in the form: [name] [initiative roll].")
        self.assertEqual(join(("name", "lastName", "initRoll"), ["name lastName", "initRoll"])

if __name__ == '__main__':
    unittest.main()
