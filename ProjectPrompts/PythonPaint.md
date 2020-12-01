## Python Paint
- This project is a GUI application started through the command line
- It is fairly simple but allows for expansion 

### Part 1
#### Creating a GUI
- Open a python file and save as 'python_paint.py'
- Use 'from' to import * from tkinter
    > from tkinter import *
- Use 'from' to import askcolor from tkinter.colorchooser
    > from tkinter.colorchooser import askcolor
    
- Create the following global variables:
    > default_color = 'black'   
    > default_size = '2.0'      
    > b1 = 'up'   
    > x_old = None   
    > y_old = None   

- Define the main function
    - It takes no parameters but will be used to access the OS's GUI generator
    - Create a variable called window and assign it to Tk()
        - window will be the variable name for the GUI
        > window = Tk()
    - Give the window a title by calling the title function of window
        > window.title('The title goes here')
    - Create a variable called canvas and assign it to Canvas()
        - This will implement Tkinter's Canvas class
        - It can take a lot of parameters, but we will give it 4 values: a place to be displayed, a background color, width, and height
        > canvas = Canvas(window, bg='white', width=500, height=400) 
    - Specify its location in window's grid by calling its grid function
        > canvas.grid(row=1, columnspan=5)  
        - This will span the window, but will leave some room above for more functionalities
    - Call the mainloop function of window to keep the GUI listening to user input
        > window.mainloop()   

- Call the main function 

- Run the application by calling the script using the command line
    - It will open up a new window and you can see your title and a big white rectangle


### Part 2
#### Mouse Events
- Define a function called b1down
    - This function will trigger when the left mouse button is clicked
    - It will take one parameter called: event
    - The only action taken in this function is to change the value of a global parameter
    - Reference the global variable b1 and reassign it to 'down'
        > global b1   
        > b1 = 'down'   
        - NOTE: be sure to use the global keyword

- Define a function called b1up
    - This function will trigger when the left mouse button is released
    - It will take one parameter called: event
    - Reference the global variables: b1, x_old, y_old
    - The purpose of this function is to reassign the values of global variables
        > global b1, x_old, y_old  
        > b1 = 'up'  
        > x_old = None  
        > y_old = None  

- Define a function called motion
    - This function will be used when the left mouse button is clicked and the mouse is moving
    - This function will update x_old and y_old as the mouse moves and create a line on the canvas
    - It will take one parameter called: event
    - Everything in this function is dependent on b1 == 'down', so if b1 does not equal 'down', the function will do nothing
        > if b1 == 'down':
    - Reference the global variables: x_old and y_old
    - Write an if-statement that is conditional on x_old and y_old not being None
        > if x_old is not None and y_old is not None:
    - If the statement evaluates to True
        - Call the create_line function of event's widget attribute
            > event.widget.create_line(x_old, y_old, event.x, event.y, smooth=True, fill=default_color, width=default_size)  
            - This will use the global default color and size for the brush
        - Reassign x_old and y_old to event's x and y values
            > x_old, y_old = event.x, event.y  
        
- Make adjustments to the main function
    - Canvas needs to be linked to the functions that you just wrote
    - Call canvas's bind function to link specific mouse events
    - Place the following lines of code after the canvas declaration and above window.mainloop()
        > canvas.bind('<Motion>', motion)
        > canvas.bind('<ButtonPress-1>', b1down)
        > canvas.bind('<ButtonRelease-1>', b1up)


### Part 3
#### Choosing a color
- Define a function called choose_color
    - Reference the global variable default_color
    - Create a variable called color and assign it to the askcolor function that was imported 
        - askcolor returns a list of values for each selection
        - Use list index notation to select the 2nd element in the list
        > color = askcolor()[1]
    - Write an if-statement to check if color's value is not None
        - Checks to see that askcolor worked correctly
        > if color != None:
    - If color's value is not None reassign default_color to color
    - Else return None

- Make adjustments to the main function
    - Create a button in window by implementing Tk's button class
        - It can take many variables, but we will give it 3 values: a place to be displayed, a text to display, and a function to be executed when clicked
        > color_button = Button(window, text='color', command=choose_color)
    - Place the button on window's grid at row 0 and column 2
        > color_button.grid(row=0, column=2)




### ENHANCEMENTS: 

> Implement a 'clear' button that will delete all lines on the canvas   
> Implement an 'eraser' button that will erase whatever is under the mouse cursor  
> Implement a button which will change the size of the brush   


