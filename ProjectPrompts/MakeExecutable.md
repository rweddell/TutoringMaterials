## Creating Executables with Python
- This is a more complex project involving the creation of an executable in the form of a GUI application
- The project will create a single application file that will open a window with a small amount of available user interaction


### Part 1  
#### Virtual environments  
- A virtual environment allows a programmer to specify what and which versions of libraries and dependencies are included in an executable
- Create an empty directory called 'exedemo'
    - This will allow the programmer to keep a tidy working environment
- CD into that directory
- From a terminal, install the virtual env library in python if needed
    - Mac/Linux:
        > python3 -m pip install --user virtualenv  
    - Windows:
        > pip install virtualenv
- Navigate to your chosen directory where you will be writing your scripts
- Create a virtual environment named 'env'
    - Mac/Linx:
        > python3 -m venv env  
    - Windows:
        > python -m venv env  
- You environment should now exist in your folder structure, but it is not yet activated
- Activate the environment to begin creating code
    - Mac/Linux:
        > source env/bin/activate  
    - Windows:
        > .\env\Scripts\activate  
- You can confirm that the environment has been activated by typing the following command and the result should be the location of the environment in the file system
    - Mac/Linux:
        > which python  
    - Windows:
        > where python  

> NOTE:
    Make sure to turn off your environment when you are not using it
    Mac/Linux/Windows:
>> deactivate  

### Part 2
#### Application code
- Now we need to develop the code of the application
    - You don't need to have your virtualenv activated to do the coding, but test it from your virtualenv before you build your executable
> NOTE:  
    There are many potential dependencies that you can add to the structure of the project, but this guide is only focused on the bare-bones approach of creating a single script that will encompass the application.
- Within the directory that was created in the previous step, create a python script called hello_application.py
- Import the tkinter library
- Initialize an instance of the Tk() class from tkinter and name it 'window'
- Create a Canvas() from tkinter and pass in window as an argument and name it 'canvas'
- Give canvas a place in the window by calling it's pack() method
    > canvas.pack()  
- Define a function called hello():
    - Initialize an instance of tkinter.Label() and name it 'label' and pass in window as an argument
        - It also needs text to display and a foreground color
        > label = tkinter.Label(window, text='Hello World', fg='black')  
        > label.pack()  
    - Call canvas's create_window() and pass in values: 150, 200, and label
        > canvas.create_window(150, 200, window=label)  
    - Initialize an instance of Button() from tkinter and name it 'button'
        - Pass in window as an argument
        - All buttons need a command, so pass in hello()
    - Call canvas's create_window() and pass in values for height and width as well as the label object that was just created
        > canvas.create_window(150, 200, window=label)
- Outside of the function, initialize an instance of Tk's Button() and name it 'button'
    - It needs text to display, a command to trigger, and foreground/background colors if desired
    > button =  tkinter.Button(text='Click me', command = hello)  
- Call canvas's create_window() and pass in button
    > canvas.create_window(150, 150, window=button)  
- Call window's mainloop() to begin the program
    > window.mainloop()  



### Part 3
#### Build the application
- 

### Enhancements
- Include functionality to randomly change the color of the displayed text when the button is clicked
    - You will need to include the random library for this