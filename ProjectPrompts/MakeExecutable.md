## Creating Executables with Python
- This is a more complex project involving the creation of an executable in the form of a GUI application
- The project will create a single application file that will open a window.
    - The window will have an text input box where a user can enter a series of names
    - Once all of the names have been entered, the user can press a button to pull a name at random until the list is empty


### Part 1  
#### Virtual environments  
- A virtual environment allows a programmer to specify which versions of libraries and dependencies are used in an executable
- Open a terminal
- Install the virtual env library in python if needed
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

#### NOTE:
- You can turn off the virtual environment by typing. You should do this every time that you are finished programming for that environment
    - Mac/Linux/Windows:
        > env deactivate

### Part 2
#### 
- Now we need to develop the code of the application
##### NOTE:
    There are many potential dependencies that you can add to the structure of the project, but the guide is only focused on the bare-bones approach of creating a single script that will encompass the application.
- Create an empty directory called 'exedemo'
- cd into the directory and create a python script called 


### Part 2
#### 

### Part 3
#### 

### Enhancements
- Combine this project with the email generator project to create a command-line program that intakes parameters and sends an auto-generated email