
# global_var is a string variable with global scope
# that means that anything that wants access to it, has access to it
global_var = 'This is a global variable'

def test_scope():
    # When you define a variable within a function, it has local scope
    # That means that only things that begin inside the function have access to the variable

    # Even though this variable has the same name as the variable with global scope, it is a separate entity
    # Anything that we do to this variable does not affect the variable at global scope
    global_var = 'a local copy'
    
    print('global_var at local scope: ', global_var)

    global_var = 23

    print('global_var as a number: ', global_var)

    # The function ends here

# This prints 'global_var' to the screen with its original value
print('global_var at global scope: ', global_var)

# Within this function, a local variable called 'global_var' is also created
# It changes value several times, but the variable at global scope remains unchanged
test_scope()

# Printing it again shows that the variable was unchanged
print('global_var at global scope: ', global_var)


def test_scope2():
    # Using the global keyword tells the function to look for a variable called 'global_var' at the global scope
    global global_var

    # This will change the value of 'global_var' at the global scope
    global_var = 'a local copy'
    
    print('global_var at local scope: ', global_var)

    global_var = 23

    print('global_var as a number: ', global_var)

# Print global scope var
print(global_var)

# Call the new function and modify the global variable
test_scope2()

# Check the value of the global variable
print(global_var)