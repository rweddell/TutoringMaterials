# Encoder/Decoder  

# Caesar Encoding  
- Caesar encoding is an old form of encryption where each letter is replaced by  another letter by a set number of characters in the alphabet  
- For example with a caesar encoding of +3, 'apple' becomes 'dttoh'  
    - a + 3 = d  
    - p + 3 = t  
    - l + 3 = o  
    - e + 3 = d  
- We'll use this for our encryption here  


## Part 1  

- Create a text file in a location that is accessible to a python script  
    - If you're having trouble finding a text file, save this text to a new file:
        ```
        ANAIS NIN “RISK”
        And then the day came,
        when the risk
        to remain tight
        in a bud
        was more painful
        than the risk
        it took
        to blossom.
        ```
- Open a new python file and read the text file  
    - Use the context definer 'with'  
        ```python
        with open('file_name.txt') as file:  
        ```
- Create a class called 'Encoder'  
    - It should have two functions:  
        - encrypt(cipher, text)  
            - 'cipher' is the offset for the encryption
                - '3' is the cipher in the example above
            - 'text' is the object to be encoded
            - encrypts 'text' using 'cipher'
            - Ignore punctuation
        - write_file()
            - writes the encrypted text to a new file with 'encrypted_' prepended to the file_name  
            - EX: file_name.txt => encrypted_file_name.txt  


## Part 2  
- Create a class called 'Decoder'
- Decoder should have two functions:
    - decrypt(text, cipher=None)
        - text is the object to decrypt
            - alternatively, this could just be a file and could be read in the function
        - If cipher is None, brute force the encryption and hold all results in memory
            - Attempt every possible key to decryption
                - Hint: there are only 26 unique characters in the english alphabet
        - If cipher is not None
            - decrypt the text using cipher
        - Return the results
    - write_file()
        - writes the decrypted text to a new file with 'decrypted_' prepended to the file_name
        - EX: file_name.txt => decrypted_file_name.txt