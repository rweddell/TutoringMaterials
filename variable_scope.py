
# value is a string variable with global scope
# that means that anything that wants access to it, has access to it
value = 'global'

def test_scope():
    # When you define a variable within a function, it has local scope
    # That means that only things that begin inside the function have access to the variable

    # Even though this variable has the same name as the variable with global scope, it is a separate entity
    # Anything that we do to this variable does not affect the variable at global scope
    value = 'local'
    
    print('value at local scope: ', value)

    value = 23

    print('value as a number: ', value)

    # The function ends here
print()
# This prints 'value' to the screen with its original value
print('value at global scope: ', value)

# Within this function, a local variable called 'value' is also created
# It changes value several times, but the variable at global scope remains unchanged
test_scope()

# Printing it again shows that the variable was unchanged
print('value at global scope: ', value)

print('\n')


def modify_global_variable():
    # Using the global keyword tells the function to look for a variable called 'value' at the global scope
    global value

    # This will change the value of 'value' at the global scope
    value = 'modified'
    
    print('value at local scope: ', value)

    value = 23

    print('value as a number: ', value)


# This prints 'value' to the screen with its original value
print('value at global scope: ', value)

# Within this function, we invoke the 'global' keyword
# This allows us to reference and modify a global variable 
modify_global_variable()

# Printing it again shows that the variable has changed
print('value at global scope: ', value)
print()