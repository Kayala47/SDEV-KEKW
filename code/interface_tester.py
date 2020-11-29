
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
        result = ["x", "y", "+0"]
        self.assertEqual(roll(("xdy",)), result)
        self.assertEqual(roll(("xd", "y")), result)
        self.assertEqual(roll(("x", "dy")), result)
        self.assertEqual(roll(("x", "d", "y")), result)
    
    def test_roll_threeInputs(self):
        # going to call the roll function with the input of xdy +m. should return a list with x, y and m
        # The funcitons should work with any number of spacing. As there are many different ways to space, we will test the edge cases and mostly used cases. For both + and - modifiers
        result = ["x", "y", "+m"]
        self.assertEqual(roll(("xdy+m",)), result)
        self.assertEqual(roll(("xdy", "+m")), result)
        self.assertEqual(roll(("xdy", "+", "m")), result)
        self.assertEqual(roll(("xd", "y", "+m")), result)
        self.assertEqual(roll(("x", "dy", "+m")), result)
        self.assertEqual(roll(("x", "d", "y", "+", "m")), result)
        
        result2 = ["x", "y", "-m"]
        self.assertEqual(roll("xdy-m",), result2)
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

    def test_mRoll_fourInputs(self):
        # going to call the roll function with the input of xdy +m fudgeroll. should return a list with x, y, m, and fudgeroll
        # The funcitons should work with any number of spacing. As there are many different ways to space, we will test the edge cases and mostly used cases. For both + and - modifiers
        result = ["x", "y", "+m", "f"]
        self.assertEqual(mRoll(("xdy+m", "f")), result)
        self.assertEqual(mRoll(("xdy", "+m", "f")), result)
        self.assertEqual(mRoll(("xdy", "+", "m", "f")), result)
        self.assertEqual(mRoll(("xd", "y", "+m", "f")), result)
        self.assertEqual(mRoll(("x", "dy", "+m", "f")), result)
        self.assertEqual(mRoll(("x", "d", "y", "+", "m", "f")), result)
       
        result2 = ["x", "y", "-m", "f"]
        self.assertEqual(mRoll(("xdy-m", "f")), result2)
        self.assertEqual(mRoll(("xdy", "-m", "f")), result2)
        self.assertEqual(mRoll(("xdy", "-", "m", "f")), result2)
        self.assertEqual(mRoll(("xd", "y", "-m", "f")), result2)
        self.assertEqual(mRoll(("x", "dy", "-m", "f")), result2)
        self.assertEqual(mRoll(("x", "d", "y", "-", "m", "f")), result2)

    def test_rollAdv(self):
        # the rollAdv takes in one input. If the user does not input anything we will send an error and if they do pass in an argument, we 
        # need to correctly parse it and return the input that they gave the user 
        errorResult = "You need a input for this command. Please input a bool as an input for this function. A true or false statement. Refer to helpMe command for more information :)"
        self.assertEqual(rollAdv(""), errorResult)
        # with the input "arg"
        msg = "Called rollAdv with input: arg"
        self.assertEqual(rollAdv("arg"), msg)

    def test_addMacro(self):
        msg1 = "You are missing some inputs needed for the addMacro function."
        msg2 = "Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        self.assertEqual(addMacro(""), result)

        self.assertEqual(addMacro(("d", "q", "m", "name")), ["d", "q", "m", "name"])

    def test_delMacro(self):
        self.assertEqual(delMacro(("")), "To delete a macro, you must input the name of the macro you wish to delete")
        self.assertEqual(delMacro(("name")), "name")
    
    def test_callMacro(self):
        self.assertEqual(callMacro(("")), "To call a macro, you must input the name of the macro you wish to call")
        self.assertEqual(callMacro(("name")), "name")

    def test_viewMacro(self):
        self.assertEqual(viewMacro(), "Called the View Macro Function.")
    
    def test_deleteMacros(self):
        self.assertEqual(deleteMacros(), "Called the Delete Macro File Function.")

    def test_join(self):
        self.assertEqual(join(("name", "initRoll")), ["name", "initRoll"])
        self.assertEqual(join(""), "To join initiative, the input must be in the form: [name] [initiative roll].")
        self.assertEqual(join(("name", "lastName", "initRoll")), ["name lastName", "initRoll"])

    def test_begin(self):
        msg = "Begin function called"
        self.assertEqual(begin(), msg)

    def test_end(self):
        msg = "End function called"
        self.assertEqual(end(), msg)
      
    def test_next(self):
        msg = "Next function called"
        self.assertEqual(next(), msg)

    def test_prev(self):
        msg = "Previous function called"
        self.assertEqual(prev(), msg)

    def test_showTracker(self):
        msg = "Show function called"
        self.assertEqual(showTracker(), msg)

    def test_search(self):
        msg1 = "You are missing some inputs needed for the search function."
        msg2 = "Make sure that you are inputing at least two key words to search. Refer to helpMe command for more information"
        result = msg1 + " " + msg2
        self.assertEqual(search(("",)), result)
        self.assertEqual(search(("keyword",)), result)

        inputs = ["keyword1", "word2"]
        self.assertEqual(search(("keyword1","word2")), inputs)

        inputs = ["keyword1", "word2", "word3"]
        self.assertEqual(search(("keyword1","word2", "word3")), inputs)

class WhiteBoxTests(unittest.TestCase):
    def test_multiroll(self):
        error_str1 = "Please input a value for the number of dice. Roll should be in format xdy+m where x is number of dice you want to roll. Please use help for more information"
        error_str2 = "Please input a value for the side of dice. Roll should be in format xdy +m where y is the number of sides of the die you want to roll. Please use help for more information"
        error_str3 = "Input Error: Make sure that your input for roll is in the format xdy + m"
        error_str4 = "Too many inputs for the roll function"

        # Missing numDie
        self.assertEqual(roll(('dy',)), error_str1)
        self.assertEqual(roll(('d', 'y')), error_str1)
        self.assertEqual(roll(('dy', '+m')), error_str1)
        self.assertEqual(roll(('d', 'y', '+m')), error_str1)
        self.assertEqual(roll(('d', 'y', '+', 'm')), error_str1)
        self.assertEqual(roll(('dy', '-m')), error_str1)
        self.assertEqual(roll(('d', 'y', '-m')), error_str1)
        self.assertEqual(roll(('d', 'y', '-', 'm')), error_str1)

        # Missing sideDie
        self.assertEqual(roll(('xd',)), error_str2)
        self.assertEqual(roll(('x', 'd')), error_str2)
        self.assertEqual(roll(('xd', '+m')), error_str2)
        self.assertEqual(roll(('x', 'd', '+m')), error_str2)
        self.assertEqual(roll(('x', 'd', '+', 'm')), error_str2)
        self.assertEqual(roll(('xd', '-m')), error_str2)
        self.assertEqual(roll(('x', 'd', '-m')), error_str2)
        self.assertEqual(roll(('x', 'd', '-', 'm')), error_str2)

        # Missing d
        self.assertEqual(roll(('xy',)), error_str3)
        self.assertEqual(roll(('x', 'y')), error_str3)
        self.assertEqual(roll(('xy', '+m')), error_str3)
        self.assertEqual(roll(('x', 'y', '+m')), error_str3)
        self.assertEqual(roll(('x', 'y', '+', 'm')), error_str3)
        self.assertEqual(roll(('xy', '-m')), error_str3)
        self.assertEqual(roll(('x', 'y', '-m')), error_str3)
        self.assertEqual(roll(('x', 'y', '-', 'm')), error_str3)

        # Too many inputs
        self.assertEqual(roll(('x', 'd', 'y', '+', 'm', 'f', 'extra')), error_str4)

    def test_manualRoll(self):
        error_str1 = "Please input a value for the number of dice. Roll should be in format xdy+m rollResult where x is number of dice you want to roll. Please use help for more information"
        error_str2 = "Please input a value for the side of dice. Roll should be in format xdy +m rollResult where y is the number of sides of the die you want to roll. Please use help for more information"
        error_str3 = "Input Error: Make sure that your input for roll is in the format xdy + m rollResult"
        error_str4 = "You cannot call manual roll with no inputs. Put in form xdy + m rollResult"
        error_str5 = "Too many inputs for the manual roll function"

        # Missing numDie
        self.assertEqual(mRoll(('dy',)), error_str1)
        self.assertEqual(mRoll(('d', 'y')), error_str1)
        self.assertEqual(mRoll(('dy', '+m')), error_str1)
        self.assertEqual(mRoll(('d', 'y', '+m')), error_str1)
        self.assertEqual(mRoll(('d', 'y', '+', 'm')), error_str1)
        self.assertEqual(mRoll(('dy', '-m')), error_str1)
        self.assertEqual(mRoll(('d', 'y', '-m')), error_str1)
        self.assertEqual(mRoll(('d', 'y', '-', 'm')), error_str1)

        # Missing sideDie
        self.assertEqual(mRoll(('xd',)), error_str2)
        self.assertEqual(mRoll(('x', 'd')), error_str2)
        self.assertEqual(mRoll(('xd', '+m')), error_str2)
        self.assertEqual(mRoll(('x', 'd', '+m')), error_str2)
        self.assertEqual(mRoll(('x', 'd', '+', 'm')), error_str2)
        self.assertEqual(mRoll(('xd', '-m')), error_str2)
        self.assertEqual(mRoll(('x', 'd', '-m')), error_str2)
        self.assertEqual(mRoll(('x', 'd', '-', 'm')), error_str2)

        # Missing d
        self.assertEqual(mRoll(('xy',)), error_str3)
        self.assertEqual(mRoll(('x', 'y')), error_str3)
        self.assertEqual(mRoll(('xy', '+m')), error_str3)
        self.assertEqual(mRoll(('x', 'y', '+m')), error_str3)
        self.assertEqual(mRoll(('x', 'y', '+', 'm')), error_str3)
        self.assertEqual(mRoll(('xy', '-m')), error_str3)
        self.assertEqual(mRoll(('x', 'y', '-m')), error_str3)
        self.assertEqual(mRoll(('x', 'y', '-', 'm')), error_str3)

        # Missing all
        self.assertEqual(mRoll(('',)), error_str4)

        # Too many inputs
        self.assertEqual(mRoll(('x', 'd', 'y', '+', 'm', 'f', 'extra')), error_str5)
    
    def test_addMacro(self):
        msg1 = "You are missing some inputs needed for the addMacro function."
        msg_end = "Make sure that your inputs are in the form: die q mod name. Refer to helpMe command for more information"
        result1 = msg1 + " " + msg_end

        self.assertEqual(addMacro(('d',)), result1)
        self.assertEqual(addMacro(('d', 'q')), result1)
        self.assertEqual(addMacro(('d', 'q', 'mod')), result1)

        result2 = ["d", "q", "mod", "name", "extra"]
        self.assertEqual(addMacro(('d', 'q', 'mod', 'name', 'extra')), result2)

    def test_join(self):
        error_msg = "To join initiative, the input must be in the form: [name] [initiative roll]."

        self.assertEqual(join(('',)), error_msg)
        self.assertEqual(join(('name',)), error_msg)
    
    def test_search(self):
        msg1 = "You are missing some inputs needed for the search function."
        msg2 = "Make sure that you are inputing at least two key words to search. Refer to helpMe command for more information"
        result = msg1 + " " + msg2

        self.assertEqual(search(('',)), result)
        self.assertEqual(search(('kw1',)), result)
    
    # testing the helper functions for parsing 

    def test_getSideDie(self):
        result = "y"
        self.assertEqual(getSideDie("xdy"), result)
        self.assertEqual(getSideDie("xd y"), result)
        self.assertEqual(getSideDie("x dy"), result)
        self.assertEqual(getSideDie("x d y"), result)

        self.assertEqual(getSideDie("xdy+m"), result)
        self.assertEqual(getSideDie("x dy+m"), result)
        self.assertEqual(getSideDie("x d y+m"), result)
        self.assertEqual(getSideDie("xdy + m"), result)
        self.assertEqual(getSideDie("xd y+m"), result)

        self.assertEqual(getSideDie("xdy-m"), result)
        self.assertEqual(getSideDie("x dy-m"), result)
        self.assertEqual(getSideDie("x d y-m"), result)
        self.assertEqual(getSideDie("xdy - m"), result)
        self.assertEqual(getSideDie("xd y-m"), result)
 

    def test_getModifier(self):
        # no modifier input should default to +0 
        result = "+0"
        # We are manually setting the has Fudge Value as getModifierWIthFudge gets called if hasFudge is True 
        self.assertEqual(getModifier("xdy", False), result)
        self.assertEqual(getModifier("x dy", False), result)
        self.assertEqual(getModifier("xd y", False), result)
        self.assertEqual(getModifier("x d y", False), result)
        
        # with a positive modifier 
        result = "+m"
        self.assertEqual(getModifier("xdy+m", False), result)
        self.assertEqual(getModifier("x dy+m", False), result)
        self.assertEqual(getModifier("xd y+m", False), result)
        self.assertEqual(getModifier("xdy + m", False), result)
        self.assertEqual(getModifier("x dy +m", False), result)
        self.assertEqual(getModifier("xd y+ m", False), result)

        # with negative modifier 
        result = "-m"
        self.assertEqual(getModifier("xdy-m", False), result)
        self.assertEqual(getModifier("x dy-m", False), result)
        self.assertEqual(getModifier("xd y-m", False), result)
        self.assertEqual(getModifier("xdy - m", False), result)
        self.assertEqual(getModifier("x dy -m", False), result)
        self.assertEqual(getModifier("xd y- m", False), result)
    
    def test_getModifierWithFudge(self):
        # this function does not get called unless there is a modifier present 

        #positive modifier 
        result = "+m"
        self.assertEqual(getModifierWithFudge("xdy+m f"), result)
        self.assertEqual(getModifierWithFudge("xdy +m f"), result)
        self.assertEqual(getModifierWithFudge("x dy+m f"), result)
        self.assertEqual(getModifierWithFudge("xdy +m f"), result)
        self.assertEqual(getModifierWithFudge("x d y + m f"), result)

        #negative modifier 
        result = "-m"
        self.assertEqual(getModifierWithFudge("xdy-m f"), result)
        self.assertEqual(getModifierWithFudge("xdy -m f"), result)
        self.assertEqual(getModifierWithFudge("x dy-m f"), result)
        self.assertEqual(getModifierWithFudge("xdy -m f"), result)
        self.assertEqual(getModifierWithFudge("x d y - m f"), result)

    def test_hasFudge(self):
        #if there is a fudge roll, returns true, else returns false 
        # true cases 
        result = True
        self.assertEqual(hasFudge("xdy+m f"), result)
        self.assertEqual(hasFudge("xdy +m f"), result)
        self.assertEqual(hasFudge("x dy+m f"), result)
        self.assertEqual(hasFudge("xdy +m f"), result)
        self.assertEqual(hasFudge("x d y + m f"), result)

        self.assertEqual(hasFudge("xdy-m f"), result)
        self.assertEqual(hasFudge("xdy -m f"), result)
        self.assertEqual(hasFudge("x dy-m f"), result)
        self.assertEqual(hasFudge("xdy -m f"), result)
        self.assertEqual(hasFudge("x d y - m f"), result)

        #false cases 
        result = False
        self.assertEqual(hasFudge("xdy"), result)
        self.assertEqual(hasFudge("xd y"), result)
        self.assertEqual(hasFudge("x dy"), result)
        self.assertEqual(hasFudge("x d y"), result)
        self.assertEqual(hasFudge("xdy+m"), result)
        self.assertEqual(hasFudge("x dy+m"), result)
        self.assertEqual(hasFudge("x d y+m"), result)
        self.assertEqual(hasFudge("xdy + m"), result)
        self.assertEqual(hasFudge("xd y+m"), result)

        self.assertEqual(hasFudge("xdy-m"), result)
        self.assertEqual(hasFudge("x dy-m"), result)
        self.assertEqual(hasFudge("x d y-m"), result)
        self.assertEqual(hasFudge("xdy - m"), result)
        self.assertEqual(hasFudge("xd y-m"), result)

    def test_getFudgeValue(self):
        
        result = "f"
        self.assertEqual(getFudgeValue("xdy+m f"), result)
        self.assertEqual(getFudgeValue("xdy +m f"), result)
        self.assertEqual(getFudgeValue("x dy+m f"), result)
        self.assertEqual(getFudgeValue("xdy +m f"), result)
        self.assertEqual(getFudgeValue("x d y + m f"), result)

        self.assertEqual(getFudgeValue("xdy-m f"), result)
        self.assertEqual(getFudgeValue("xdy -m f"), result)
        self.assertEqual(getFudgeValue("x dy-m f"), result)
        self.assertEqual(getFudgeValue("xdy -m f"), result)
        self.assertEqual(getFudgeValue("x d y - m f"), result)

if __name__ == '__main__':
    unittest.main()
