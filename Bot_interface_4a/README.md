The read me file for bot_interface.py 

Note: There are three "code" files made for this interface. The bot_interface.py is the actual initial executable code that 
will make the bot be able to respond to users once it is invited to your discord channel. The testing_interface_functions 
was a file that was made, the logic same to that of bot_interface.py, for testing purposes. To make the testing process 
autonomous, we used return statements in testing_interface_functions so we could use assert in the testing file. The 
interface_tester.py is simply the testing file for the component and uses testing_interface_functions.py in it for the testing. 

SETUP FOR USING THE BOT_INTERFACE IN DISCORD:

This is the main file that is used to make the bot online on discord. If you follow these steps you can get the bot to run 
and also invite it to a server where it can perform actions. 

-Ensure that bot_interface.py, rolling.py, initTracker.py and compendium.py are all in the direcotry 

-Before trying to run bot_interface.py, make sure that you have to download some packages: 

    - pip install -U discord.py
	
    - pip intall selenium 
	
    - pip install webdriver-manager
	
    - pip install requests
	
    - pip install bs4
	
    - pip install numpy
	
    - Alternatively we should have a requirements.txt file that you can call using pip install -r requirements.txt 
    
- The token field in the python file is empty, you will have to pull that from the discord bot developer website and paste that in place of the empty ""
    - Tokens are unique for each bot, if you want to see the bot in action in the discord channel, make sure you have the correct token for the bot 
- After you have followed those steps, you can run the bot interface function as you would normally run a 
    python program 

To invite to a specific server in your discord, paste this link into your web browser: 
https://discord.com/api/oauth2/authorize?client_id=759194112640811028&permissions=1476917360&scope=bot
    
SETUP FOR USING    TESTING_INTERFACE_FUNCTIONS:

This was the file I had used for testing. This file contains all of the same functions as the bot_interface.py file but instead of sending 
messages to a server, the functions in this module just return either a string or an array, which we used for testing purposes. 

There is no special setup for this except ensuring that testing_interface_funcitons.py and interface_tester.py are in the same 
location in your directory. 

TESTING:   
simply run interface_tester.py in the same directory   
as testing_interface_functions.py in your python interpreter.   
If you run with just the command "python interface_tester.py" you will not get a specific message including all the different testcases passed 
use python -m unittest -v interface_tester.py to get the detailed message, like the one seen in the output_4a.txt file. 

USING COMPONENT:   
The testing_interface_functions.py was meant to just be used for testing purposes, but if you would like to test/ call specific funcitons, you can make a main 
function and call any of the functions you would like in the main function. You can also just call individual functions inside of the terminal. 

Note that for any of the parameterized functions, valid arguments   
will be required, details for which can be found in specs and/or design. 
In most cases, the funcitons in the testing_interface_functions.py will take an 
input of a tuple of strings. 
