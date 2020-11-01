# Concepts for working with APIs

## What is an API?
    - Application Programming Interface
    - Series of functions that are exposed to the internet
        - Sometimes requires authentication
            - username/password
            - key
            - token
    - Allows interaction with a service without requiring knowledge of the back-end
    - Uses RESTful state architecture
        - REpresentational State Tansfer
        - Communication protocol that uses predefined requests

## What is a request?
    - Message transfer protocol that uses a keyword as a header to describe the type of message being sent
        - These types are universal
    - Most frequently used headers:
        - DELETE
            - Delete an instance of information in the receiver's environment
        - GET
            - A request for information
                - JSON, HTML, XML
            - A browser makes a GET request to see a web page
        - PATCH
            - Update the state of the receiver's environment
        - POST
            - Create an instance of new information in the receiver's environment
        - PUT
            - Replaces an instance of information 

## What is JSON?
    - JavaScript Object Notation
        - JavaScript was the first language designed specifically for use with the internet
        - The notation was based on a subset of Javascript
        - Now is language independent
    - Object structure 
        - Defined with curly braces {}
        - Made up of key value pairs and array structures (python lists)
        - Function similarly to python dictionaries
    - Commonly used in as the notation for responses to requests

## Status codes
    - Part of the response from a request
    - Informs the sender how their request was received
    - Comes in the form of a 3 digit integer
        - 200s
            - Received without errors
        - 300s
            - Received, but redirected
        - 400s
            - Bad requests/not received/not accepted
        - 500s
            - Server-side error while parsing request
            - Can attempt resend
    