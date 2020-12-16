## Generic Email Generator
- This simple command line script
- The result is a script that can be run from the command line to send a prewritten email from a dummy account.
- A more detailed explanation of this exercise can be found [here at Real Python](https://realpython.com/python-send-email/)

### Part 1  
#### Dummy account
- Create a dummy email account through Gmail
- In your dummy account settings, switch 'Allow less secure apps' to 'On'
    - Very important because Gmail is smart enough to reject logins from third-party applications
- Write the password and email address into a JSON file
    - You can save it as 'email_credentials.json'
    > {
    >    "email_address":"your_email@gmail.com",
    >    "password":"your_email_password"
    > }  
    - Remember that by placing your email password in a separate document, you keep it safe if you should wish to share your code with others
##### Keep in mind that if you send emails often enough through this account, there is a chance that it will be identified as spam and blocked.

### Part 2
#### Email server
- Create a variable called 'message' and assign a string to it that will be the body of your email
    > message = 'Hi. This is an email. Bye'
- Create a variable called 'context' and assign the value of ssl's create_default_context()
    > context = ssl.create_default_context()  
    - This creates a fresh secure socket layer with default settings
- The next block is a 'with' statement that will create a server temporarily on your machine
    - From here, you will log in to your dummy account and trigger it to send an email using your predefined message
    - It uses a default setup through Gmail
    > with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:  
    >   server.login(email_address, password)  
    >   server.sendmail(email_address, receiver, message=message)
- The script is now ready to run, but you may find it useful to include print statements at several points in the code to make sure that your script is running correctly.
    - Otherwise there is no other output from this script apart from the mail that may or may not have been received.

- Save the script and run it from command line