from tkinter import *

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#define a class which represents vigenere cipher
class VigenereCipher:
    def __init__(self):
        """Initialize a new VigenereCipher object."""
        self.key = ''
        self.message = ''
        self.ciphertext = ''

        #to set the ciphertext attribute
        self.encrypt()

    def encrypt(self):
        """Encrypts the message using the vigenere cipher algorithm and sets the 
        ciphertext attribute with the uses the key and message attribute of the object."""
        #iterate each symbol in the message, applying the vigenere cipher
        #adding the corresponding letters in the message and key
        #then finding the letter in LETTERS that corresponds to the sum (% len(LETTERS))
        #if the symbol is not in LETTERS, leave it unchanged 
        self.ciphertext = ''.join(LETTERS[(LETTERS.find(symbol.upper()) + 
            LETTERS.find(self.key[key_index % len(self.key)].upper())) % len(LETTERS)]
            if symbol.upper() in LETTERS else symbol
            for key_index, symbol in enumerate(self.message)
        )


# #ask the user for the key and message
# key = input('Enter the key: ')
# message = input('Enter the message: ')

# #set vigenere cipher's key and message attributes
# cipher = VigenereCipher()
# cipher.key = key
# cipher.message = message

# #encrypt the message and print the ciphertext
# cipher.encrypt()
# print('Ciphertext:', cipher.ciphertext)

#build a GUI for the Vigenere Cipher
class Interface:
    def __init__(self):
        """Initializes the interface window and runs the main loop."""
        self.root = Tk()
        self.root.geometry("375x398")
        self.root.title('Vigenere Cipher')
        
        #add logo
        logo = PhotoImage(file="assets/vc-logo.png")
        self.root.iconphoto(False, logo)

        self.root.mainloop()

Interface()