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

        #set the frame for whole background appearance 
        whole_frame= Frame(self.root, width=398, height=375, relief=GROOVE, borderwidth=5, bg="#1c1c1c")
        whole_frame.place(x=0, y=0)

        #create text boxes for the input of message and key
        self.message_box = Text(whole_frame, relief=GROOVE, borderwidth=0, font = ("verdana", 13), fg="white", bg="black")
        self.message_box.place(x=15, y=50, width=355, height=100)        
        self.key_box = Text(whole_frame, borderwidth=0, font = ("verdana", 15), fg="white", bg="black")
        self.key_box.place(x=15, y=200,  width=355, height=50)

        #add the labels for user input guidance
        message_label = Label(self.root, text="Enter a message to encrypt", font = ("Helvetica 12 bold"), fg="gray", bg="#1c1c1c")
        message_label.place(x=15, y=20)
        key_label = Label(self.root, text="Enter a key for encryption", font = ("Helvetica 12 bold"), fg="gray", bg="#1c1c1c")
        key_label.place(x=15, y=170)

        self.root.mainloop()



Interface()