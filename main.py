import secrets
import string


# method to generate the cipher text
def generate_cipher_text(message):
    input_message = message
    # creates a secret key/one time pad using the secrets library with the combination of upper and lowercase english
    # letters and matches with the same length of the original message.
    pad_message = ''.join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(len(input_message)))
    cipher_message = ''

    for x in range(len(input_message)):
        # perform xor operation on characters from both the one time pad and the original message
        xor_current_chars = ord(input_message[x]) ^ ord(pad_message[x])
        # convert it back to characters from ASCII values
        cipher_current_char = chr(xor_current_chars)
        # append the characters together to form the cipher message
        cipher_message += cipher_current_char

    output = [cipher_message, pad_message]

    return output


def decrypt_cipher_text(cipher, secret):
    cipher_message = cipher
    pad_message = secret
    original_message = ''

    for x in range(len(cipher_message)):
        # perform xor operation on characters from both the one time pad and the cipher message
        xor_current_chars = ord(cipher_message[x]) ^ ord(pad_message[x])
        # convert it back to characters from ASCII values
        original_message_current_char = chr(xor_current_chars)
        # append the characters together to form the original message
        original_message += original_message_current_char

    output = original_message

    return output


# method to write the values on to a file
def write_to_file(filename, text):
    with open(filename + '.txt', "w+") as file:
        file.write(text)


# method to read contents from a given file
def read_from_file(filename):
    with open(filename + '.txt') as f:
        file_data = f.read()
        return file_data


option = input("Do you wish to encrypt or decrypt?")

if option == "encrypt":
    message = input("Enter your message:")
    output = generate_cipher_text(message)

    write_to_file('original', message)
    write_to_file('cipher', output[0])
    write_to_file('secret', output[1])

    print("Original message has been stored as original.txt")
    print("Cipher message has been stored as cipher.txt")
    print("Secret key/one time pad key has been stored as secret.txt")

elif option == "decrypt":
    cipher = read_from_file('cipher')
    secret = read_from_file('secret')
    # condition to make sure that the cipher and the secret key has the same amount of characters
    if len(cipher) == len(secret):
        print("Your decrypted text is: " + decrypt_cipher_text(cipher, secret))
    else:
        print("Both cipher and secret key should contain same number of characters")

else:
    print("Incorrect option")
