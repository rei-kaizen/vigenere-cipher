from tkinter import *

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#define a class which represents vigenere cipher
class VigenereCipher:
    def __init__(self):
        """Initialize a new VigenereCipher object."""
        self.key = ''
        self.message = ''
        self.ciphertext = ''

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
        self.message_box = Entry(whole_frame, relief=GROOVE, borderwidth=0, font = ("verdana", 13), fg="white", bg="black")
        self.message_box.place(x=15, y=50, width=355, height=100)        
        self.key_box = Entry(whole_frame, borderwidth=0, font = ("verdana", 15), fg="white", bg="black")
        self.key_box.place(x=15, y=200,  width=355, height=50)

        #add the labels for user input guidance
        message_label = Label(self.root, text="Enter a message to encrypt", font = ("Helvetica 12 bold"), fg="gray", bg="#1c1c1c")
        message_label.place(x=15, y=20)
        key_label = Label(self.root, text="Enter a key for encryption", font = ("Helvetica 12 bold"), fg="gray", bg="#1c1c1c")
        key_label.place(x=15, y=170)

        #embed buttons for encrypt, paste and reset methods
        encrypt_button = Button(whole_frame, text="ENCRYPT", width=17, height=2, borderwidth=0, font = ("verdana 10 bold"), bg="red", fg="white", command=self.encrypt)
        encrypt_button.place(x=20, y=260)
        self.paste_button = Button(whole_frame, text="PASTE", width=17, height=2, borderwidth=0, font = ("verdana 10 bold"), bg="green", fg="white", command=self.paste)
        self.paste_button.place(x=200, y=260)
        reset_button = Button(whole_frame, text="RESET", width=37, height=2, borderwidth=0, font = ("verdana 10 bold"), bg="blue", fg="white", command=self.reset)
        reset_button.place(x=20, y=310)

        #hold the ciphertext output and update the corresponding widget
        self.ciphertext_display_var = StringVar()

        self.root.mainloop()

    def encrypt(self):
        """Encrypts the message using the key and updates the GUI with the ciphertext."""
        message = self.message_box.get().upper().replace(' ', '')
        key = self.key_box.get().upper()

        #set vigenere cipher's key and message attributes
        cipher = VigenereCipher()
        cipher.key = key
        cipher.message = message

        #encrypt the message and update GUI ciphertext display
        cipher.encrypt()
        ciphertext = cipher.ciphertext
        self.ciphertext_display_var.set(ciphertext)

        root1 = Toplevel(self.root)
        root1.geometry("400x200")
        root1.title("Encrypted Message")
        root1.configure(bg="black")

        Label(root1, text="CIPHERTEXT", font = ("Helvetica 12 bold"), fg="gray", bg="#1c1c1c").place(x=10, y=10)
        self.ciphertext = Text(root1, relief=GROOVE, borderwidth=0, font = ("verdana", 13), fg="white", bg="black")
        self.ciphertext.place(x=10, y=40, width=380, height=150) 
        self.ciphertext.insert(END, ciphertext)

    
Interface()