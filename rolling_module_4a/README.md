Building and executing this component is extremely easy.

FIRST SETUP:   
Simply ensure that both rolling.py and rolling_tester are   
in the same location that you want your macros to be stored.   

TESTING:   
simply run rolling_tester.py in the same directory   
as rolling.py in your python interpreter.   

USING COMPONENT:   
Normally, methods will be called by the bot in bot_interface.py.    
However, if you want to test individual components, in main(), add    
any of the following user-facing methods to be executed and printed:    

multiRoll(die, q, mod)  
manualRoll(die, q, mod, roll)   
rollAdv(adv)  
addMacro(q, die, mod, name)  
viewMacros() 
callMacro(name)    
delMacro(name)   
deleteMacroFile()   

Note that for any of the parameterized functions, valid arguments   
will be required, details for which can be found in specs and/or design.
