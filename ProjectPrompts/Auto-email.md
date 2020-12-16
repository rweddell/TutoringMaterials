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
##### NOTE: Keep in mind that if you send emails often enough through this account, there is a chance that it will be identified as spam and blocked.

### Part 2
#### Email server
- Open a python file and save as 'email_sender.py'
- Import three libraries:
    > import smtplib, ssl, json  
    - Smtplib is the library that will manage emails
    - SSL will allow you to create secure connections
    - JSON will allow you to access your email credentials in a separate file
- Create a variable called 'reciever' and assign the value of the address where you want to send a message
    > reciever = 'some_email@email.com'
- Create a variable called 'port' and assign the value of 465 (int)
    > port = 465  
    - A port is a physical location on your machine that other processes (or other machines) can point to in order to recieve information
- Open your credentials file and read the information into variables
    > with open('your_file_path.json', 'r') as credentials:
    >   creds = json.loads(credentials.read())
    >   password = creds['password']
    >   email_address = creds['email_address']
- To use it, first create an instance of the ArgumentParser class
    > parser = ArgumentParser()  
- Now that the parser has been created, it needs to know what arguments to parse
    - Add arguments for name and date
    > parser.add_argument('-name')
    > parser.add_argument('-date')
- Print email_address to make sure that

### Part 3
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

### Enhancements
- Combine this project with the email generator project to create a command-line program that intakes parameters and sends an auto-generated email