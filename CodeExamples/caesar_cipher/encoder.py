from string import punctuation

file_name = 'encoder.txt'

with open(file_name, 'r') as file:
    contents = file.read()

class CodeWriter:

    def write_to_file(self, text, name='encoded.txt', prefix=''):
        with open(f'{prefix}{name}', 'w') as file:
            file.write(text)

class Encoder(CodeWriter):

    def encrypt(cipher, text):
        encrypted = ''
        for char in text:
            if char in punctuation or char == '\n' or char == ' ':
                encrypted += char
            else:
                encrypted += chr(ord(char)+3)
        return encrypted

class Decoder(CodeWriter):

    def decrypt(cipher, text):
        result_set = []
        for i in range(1, 27):
            decrypted = f'cipher=-{i}\n\n'
            for char in text: 
                if char in punctuation or char == '\n' or char == ' ':
                    decrypted += char
                else:
                    decrypted += chr(ord(char)-i)
            result_set.append(decrypted)
        return '\n--------------------------------\n'.join(result_set)

encoder = Encoder()

print(contents)
e_result = encoder.encrypt(contents)
encoder.write_to_file(text=e_result, name=file_name, prefix='encrypted_')
print(e_result)
print('\n\n########################################\n\n')
decoder = Decoder()
d_result = decoder.decrypt(e_result)
decoder.write_to_file(text=d_result, name=file_name, prefix='decrypted_')
print(d_result)