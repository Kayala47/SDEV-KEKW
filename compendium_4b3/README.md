Building and executing this component is extremely easy.

FIRST SETUP:   
Simply ensure that both compendium.py and compendium_testing.py are   
in the same location and that you have installed all dependencies in 
the requirements.txt file located under the code folder.   

TESTING:   
Simply run compendium_testing.py in the same directory   
as compendium.py in your Python interpreter.   

USING COMPONENT:   
Normally, only search can be called form the bot interface. If you'd like to call
any of the individual functions, the easiest way is to call them using the main 
function of comepndium_testing.py   

AVAILABLE FUNCTIONS

search() - takes as input an array of strings
screenshot() - takes as input a url as a string
getTitle() - takes a string url as input
editHelper() - takes two inputs: a string and a list of 
    strings to compare it to
editDistance() - takes two strings as inputs, which it 
    compares to each other using the editDistance algorithm
