Building and executing this component is extremely easy.

FIRST SETUP:   
Simply ensure that both initTracker.py and initTracker_test.py are   
in the same location.   

TESTING:   
Simply run initTracker_test.py in the same directory   
as initTracker.py in your Python interpreter.   

USING COMPONENT:   
Normally, methods will be called by the bot in bot_interface.py.    
However, if you want to test individual components, in your Python    
interpreter, create an initiative tracker object: tracker = InitTracker().
Then, add any of the following methods to be executed and printed:    

printTracker()
join(username, name, initiative)
   username: a string representing a Discord user's username
   name: a string representing the name of the combatant
   initiative: a string that can be interpreted as an int
               or an int representing the initiative roll
begin()
end()
next()
prev()
inc_round()
dec_round()
