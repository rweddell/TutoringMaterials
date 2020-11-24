## Fantasy Factory
- This project is a command-line program in the form of a Python script
- The concept is to pseudo-randomly generate characters for role-playing games based on parameters set by user-input

### Outline
- Open a python file and save as 'fantasyfactory.py'
- Import the following libraries:
    - random
    - os
    - art
    
- Create list variables to store components that will make up a character
    - Fantasy races
    - Syllables 
        - These can be concatenated to make pseudo-random names for locations and people
    - Occupations
    
- Clear the screen using the following code:
    > os.system('cls' if os.name == 'nt' else 'clear')
    
    - This changes what command is called depending on the operating system 
        - 'clear' -> iOS, Linux
        - 'cls' -> Windows
            
- Print a welcome message to the screen
    - This will be the first thing that users see when they start up the program
    - Use tprint() from the art library to make your text more interesting
    - Prompt the user to press any key to continue
        - Use input() to wait for the user to input a keypress
    
- Create a while loop that will continually ask for user input
    - Within this loop we need to:
        1. Clear the screen again
        2. Select a fantasy race
        3. Generate a name
        4. Select an occupation
        5. Generate a location
    - The break condition will be when the user enters 'exit'
    - Ask the user if they would like to create a new character
        > - EHANCEMENT: 
            - How could we ask the user if they want a randomly generated character, or if they want to choose the character's fantasy race?
    - If the user would like to generate a new character:
        - Create a variable and assign it to the value of a random entry in the list of fantasy races
            - Or, if the user chooses to select a race, use that
        - Create a variable and assign it to a random choice of syllables
            - Use randint() from the random library to generate a random integer - N
                - This will be the number of syllables that are selected from the collection of syllables
            - Use a for loop to select N number of syllables 
            > - ENHANCEMENT:
                - How could we customize the syllable selection to be semi-unique depending on the character's fantasy race?
                