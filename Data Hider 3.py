from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from tkinter import messagebox

def genData(data):
    return [format(ord(i), '08b') for i in data]

def modPix(pix, data):
    datalist = genData(data)
    imdata = iter(pix)
    for i in range(len(datalist)):
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]
        for j in range(8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if pix[j] != 0:
                    pix[j] -= 1
                else:
                    pix[j] += 1
        if i == len(datalist) - 1:
            if pix[-1] % 2 == 0:
                if pix[-1] != 0:
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
        else:
            if pix[-1] % 2 != 0:
                pix[-1] -= 1
        yield tuple(pix[:3])
        yield tuple(pix[3:6])
        yield tuple(pix[6:9])

def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
    for pixel in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1
    return newimg

def decode(img):
    data = ''
    imgdata = iter(img.getdata())
    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]
        binstr = ''.join(['0' if i % 2 == 0 else '1' for i in pixels[:8]])
        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            return data

# GUI Code
root = Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("900x600+200+100")  # Enlarged window size
root.resizable(False, False)
root.configure(bg="#2f4155")

# Global variables
filename = None
secret = None

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetype=(("PNG file", "*.png"),
                                                    ("JPG File", "*.jpg"), ("All files", "*.*")))
    if filename:
        img = Image.open(filename)
        
        # Resize the image to fit within the 300x300 box while maintaining aspect ratio
        img = img.resize((300, 300), Image.LANCZOS)        
        # Convert the resized image to a PhotoImage object
        img = ImageTk.PhotoImage(img)
        
        lbl.configure(image=img, width=300, height=300)
        lbl.image = img
        lbl.config(text="")

def Hide():
    global secret
    message = text1.get(1.0, END).strip()
    if filename and message:
        img = Image.open(filename)
        secret = encode_enc(img.copy(), message)
        lbl.config(text="Data hidden in image!")
def Show():
    if filename:
        img = Image.open(filename)
        clear_message = decode(img)
        text2.delete(1.0, END)  # Clear any existing decoded text in text2
        text2.insert(END, clear_message)  # Insert decoded text

def show_alert():
    messagebox.showinfo("Alert", "Image Saved Successfully")

def clearData():
    text1.delete(1.0, END)
    text2.delete(1.0, END)
    lbl.config(image='', text="No Image Selected")

def save():
    if secret:
        secret.save("hidden.png")
        lbl.config(text="Image saved as hidden.png")
        show_alert()
        clearData()

# UI Elements
Label(root, text="STEGANOGRAPHY", bg="#2d4255", fg="white", font="arial 25 bold").place(x=350, y=20)

# Image Frame
f = Frame(root, bd=3, bg="black", width=350, height=320, relief=GROOVE)
f.place(x=30, y=80)

lbl = Label(f, bg="black", text="No Image Selected", font="Arial 15 bold", fg="white")
lbl.place(x=30, y=10)

# Encoded Text Frame
frame2 = Frame(root, bd=3, width=450, height=150, bg="white", relief=GROOVE)
frame2.place(x=400, y=80)

text1 = Text(frame2, font="Roboto 15", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=35, width=430, height=110)

lbl3 = Label(frame2, bg="white", text="Encoded Text", font="Arial 15 bold", fg="black")
lbl3.place(x=150, y=5)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=430, y=0, height=135)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Decoded Text Frame
frame5 = Frame(root, bd=3, width=450, height=150, bg="white", relief=GROOVE)
frame5.place(x=400, y=260)

lbl2 = Label(frame5, bg="white", text="Decoded Text", font="Arial 15 bold", fg="black")
lbl2.place(x=150, y=5)

text2 = Text(frame5, font="Roboto 15", bg="white", fg="black", relief=GROOVE, wrap=WORD, height=4, width=28)
text2.place(x=0, y=35, width=430, height=110)

scrollbar2 = Scrollbar(frame5)
scrollbar2.place(x=430, y=0, height=135)
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Control Buttons
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=150, relief=GROOVE)
frame3.place(x=30, y=420)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=10, y=15)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=170, y=15)
Button(frame3, text="Clear All", width=10, height=2, font="arial 14 bold", command=clearData).place(x=90, y=80)

frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=400, y=420)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)

root.mainloop()
