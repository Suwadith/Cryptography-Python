import secrets
import string


def generate_cipher_text(message):
    input_message = message
    pad_message = ''.join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(len(input_message)))
    cipher_message = ''

    for x in range(len(input_message)):
        xor_current_chars = ord(input_message[x]) ^ ord(pad_message[x])
        cipher_current_char = chr(xor_current_chars)
        cipher_message += cipher_current_char

    output = [cipher_message, pad_message]

    return output


def decrypt_cipher_text(cipher, secret):
    cipher_message = cipher
    pad_message = secret
    original_message = ''

    for x in range(len(cipher_message)):
        xor_current_chars = ord(cipher_message[x]) ^ ord(pad_message[x])
        original_message_current_char = chr(xor_current_chars)
        original_message += original_message_current_char

    output = original_message

    return output

def write_to_file(filename, text):
    with open(filename+'.txt', "w+") as file:
        file.write(text)


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
    cipher = input("Enter your cipher message:")
    secret = input("Enter your secret key:")
    if (len(cipher) == len(secret)):
        print("Your decrypted text is: " + decrypt_cipher_text(cipher, secret))
    else:
        print("Both cipher and secret key should contain same number of characters")

else:
    print("Incorrect option")
