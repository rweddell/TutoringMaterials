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
    
- Create a while loop that will continually ask for user input
    1. Prompt the user to press any key to continue or type 'exit' to quit
        - Use input() to wait for the user to input a keypress
        - If the user does not want to create a character
            - Break the loop
    2. Clear the screen again
        > os.system('cls' if os.name == 'nt' else 'clear')
    3. Select a fantasy race
        - Use choice() from the random library to select a fantasy race
    4. Generate a name
        - Use the randint() function to generate a random integer
            - This will be the number of syllables selected from the syllable collection to generate a name
        - For the range generated in the previous step, select a syllable from the collection and store in a variable
            - Either as a list or concatenated into a string
        - This can be done twice (or more) for every name that you want to generate
    5. Select an occupation
        - Use choice() to select an occupation from the collection
    6. Generate a location
        - Use the randint() function to generate a random integer
            - This will be the number of syllables selected from the syllable collection to generate a name
        - For the range generated in the previous step, select a syllable from the collection and store in a variable
            - Either as a list or concatenated into a string
        - Consider appending a suffix that would indicate that this is the name of a location
            - burg, ton, _city, etc
    7. Print the generated character
        - For each attribute:
            print('{0:<10} {1:<30}'.format(<name_of_attribute>, <value_of_attribute>))
            
- When the loop ends
    - Thank the user for using the program
       - Use the art library to beautify the text
                
                

>EHANCEMENTS: 
    1. Generate an age attribute based on the race of the character
    2. Ask the user if they want a randomly generated character, or if they want to choose the character's fantasy race and generate attributes unique to that race
        Names of characters and locations as well as an age based on the race