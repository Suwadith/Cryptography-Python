# Cryptography-Python

A simple Python-based implementation which demonstrates a variation of the one-time pad encryption/decryption logic.

**Execution Command** – python3 main.py

**Options Given** – “encrypt” or “decrypt”

After the completion of the encryption process, 3 files will be created inside the same 
directory.

1. **original.txt** – Stores the initial phrase that the user provided.
2. **cipher.txt** – Stores the encrypted/cipher phrase.
3. **secret.txt** – Stores the secret key/one-time pad key which was generated.

- When the user selects the option to decrypt the data stored in both the cipher.txt and 
the secret.txt files will be used to decrypt and reveal the original phrase in the 
terminal.

- The usage of file reading and writing was introduced mainly due to the inability of the 
terminal to display some of the ASCII characters properly, hence making it hard for 
the user to copy and paste during the decryption process.

> Note: This program was developed as part of an assessment given by the Middlesex University
