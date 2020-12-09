## Generic Email Generator
- This simple command line project
- The result is a script that can be run from the command line and print out a generic email that can be copy/pasted

### Part 1  
#### Argparse  
- Open a python file and save as 'email_maker.py'
- In the file, import ArgumentParser from the argparse library
    > from argparse import ArgumentParser  
- Also import date from the datetime library
    > from datetime import date  
- The argparse library allows the writer to specify named arguments that can be entered from the command line
- To use it, first create an instance of the ArgumentParser class
    > parser = ArgumentParser()  
- Now that the parser has been created, it needs to know what arguments to parse
    - Add arguments for name and date
    > parser.add_argument('-name')
    > parser.add_argument('-date')

### Part 2  
#### Main function
- Define the main function
    - This time the function will take two parameters: name and date
        > def main (name=None, email_date=None):   
        - Assigning a default value ensures that the function will not fail if it is given no arguments
    - Check if the parameters are None using 'is'
        > if name is None:
        - Then assign a default value, such as 'friend'
    - If email_date is None, assign it a value using date.today()
        - This will assign the variable today's date
    - Create a variable called: template
        - This will be a skeleton for an email
        - It will contain generic information and placeholders for specific information like names and dates
    - The value of template will be an f-string
        - This is a special type of string introduced in Python 3 that allows the writer to put placeholders in the string itself that will be replace by variables
        - A placeholder in an f-string is denoted with curly braces
            > f'This is an f-string and a {placeholder}'
        - Example template:
            > f'Hello {name},\n\nI hope today finds you well.\nPlease make me a sandwich for this date: {email_date}.\n\n\nBest regards,\nA hungry guy'  
            - Note the placements of the newline character \n
            - Ensure that you place your function arguments in your template
    - Print template

### Part 3
#### if \__name__ == "\__main__"
- Convetion for running a script from command line is to create an if-statement that looks for the function name
    > if \__name__ == "\__main__":
    - If this statement evaluates to True then have parser parse the arguments into a variable
        > args = parser.parse_args()  
        - This object becomes a dictionary with attributes that were passed from the command line
    - Then use the parsed arguments to call the main function 
        > main(name=args.name, email_date=args.email_date)

- Run the application by calling the script using the command line
    - You will need to specify arguments as they were given to the ArgumentParser in the script
        > python email_maker.py -name MyName -email_date 12-20-2020


