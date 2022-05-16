from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import base64
import os

def closeW():
   screen3.destroy()

def closeMainW():
    screen.destroy()

def decrypt():
    password = code.get()

    if password == "290120": 
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii") 

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10,y=0)
        text2 = Text(screen2, font="Robote 10", bg= "white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("Decryption","Input Password")

    elif password != "290120":
        messagebox.showerror("Decryption","Invalid Password")

def nWin():
    global text3
    global screen3
    password = code.get()

    if password == "290120": 
        screen3 = Toplevel(screen)
        screen3.title("Decryption")
        screen3.geometry("400x200")        
        Label(screen3, text="Enter New File Name With Extension:", font="arial", fg="black").place(x=10,y=10)
        text3 = StringVar()
        Entry(screen3, textvariable=text3, font="Robote 20", bg="white", bd=0).place(x=10,y=50, width=300,height=40)
        b1 = Button(screen3, text="Select", height="2",width=15, bg="#00bd56", fg="white",bd=0, command=decryptF)
        b1.place(x=30,y=100)
        b2 = Button(screen3, text = "Exit",height="2",width=15, bg="#ED3833", fg="white",bd=0, command = closeW)
        b2.place(x=170,y=100)

    elif password == "":
        messagebox.showerror("Encryption","Input Password")

    elif password != "290120":
        messagebox.showerror("Encryption","Invalid Password")

def decryptF():

    m = text3.get()


    screen1 = Toplevel(screen)
    screen1.title("Decryption")
    screen1.geometry("250x30")
    screen1.configure(bg="#ed3833")

    i = label_file_explorer.cget("text")
    data = open(i, 'rb')
    byte = data.read()
    data.close()
        
    fh= open(m, 'wb')
    fh.write(base64.b64decode(byte))

    Label(screen1, text="DECRYPTED FILE CREATED", font="arial", fg="white", bg="#ed3833").place(x=10,y=0)

def encryptF():
    password = code.get()

    if password == "290120": 
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("800x400")
        screen1.configure(bg="#ed3833")

        i = label_file_explorer.cget("text")
        with open(i, 'rb') as file:
            e = base64.b64encode(file.read())

        Label(screen1, text="ENCRYPTED FILE CREATED", font="arial", fg="white", bg="#ed3833").place(x=10,y=0)
        text2 = Text(screen1, font="Robote 10", bg= "white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=780, height=350)

        text2.insert(END, e)

        lab = open('out.txt', 'wb')
        lab.write(e)
        lab.close()
    elif password == "":
        messagebox.showerror("Encryption","Input Password")

    elif password != "290120":
        messagebox.showerror("Encryption","Invalid Password")



def encrypt():
    password = code.get()

    if password == "290120": 
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")


        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10,y=0)
        text2 = Text(screen1, font="Robote 10", bg= "white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("Encryption","Input Password")

    elif password != "290120":
        messagebox.showerror("Encryption","Invalid Password")


def main_screen():

    global screen
    global code
    global text1
    global label_file_explorer

    screen = Tk()
    screen.geometry("375x448")
    screen.title("EncryptApp")

    def reset():
        code.set("")
        text1.delete(1.0,END)
        label_file_explorer.config(text="")

    Label(text = "Enter The Message", fg= "black", font=("calbri",13)).place(x=10,y=10)
    text1= Text(font="Robote 20", bg="white", relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=200,height=100) 

    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("all files", "*.*"), ("Text files", "*.txt*")))
        label_file_explorer.configure(text=filename)

    Label(text = "Select The File", fg= "black", font=("calbri",13)).place(x=225,y=10) 
    label_file_explorer = Label(font=("Robote 20", 10), bg="white", fg="black", wraplength=140)
    label_file_explorer.place(x=225, y=50, width=145, height=55)
    Button(text = "Browse Files",height="2",width=23, bg="#00bd56", fg="white",bd=0, command = browseFiles).place(x=250,y=112, width=90)


    Label(text = "Enter Password", fg= "black", font=("calbri",13)).place(x=10,y=170)
    code  = StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25), show="*").place(x=10,y=200)
    Button(text="ENCRYPT  TEXT", height="2",width=23, bg="#00bd56", fg="white",bd=0, command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT  TEXT", height="2",width=23, bg="#00bd56", fg="white",bd=0, command=decrypt).place(x=200,y=250)
    Button(text="ENCRYPT  FILE", height="2",width=23, bg="#00bd56", fg="white",bd=0, command=encryptF).place(x=10,y=300)
    Button(text="DECRYPT  FILE", height="2",width=23, bg="#00bd56", fg="white",bd=0, command=nWin).place(x=200,y=300)
    Button(text="RESET", height="2",width=50, bg="#ED3833", fg="white",bd=0,command=reset).place(x=10,y=350)
    Button( text = "Exit",height="2",width=50, bg="#ED3833", fg="white",bd=0, command = closeMainW).place(x=10,y=400)
    screen.mainloop()

main_screen()