from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image
# root widget
win = Tk()
win.resizable(0, 0)
win.title("Nepali AI Anchor")
# Window size
appWidth = 852
appHeight = 480
font = "Times New Roman"

screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()

x = int((screenWidth / 2) - (appWidth / 2))
y = int((screenHeight / 2) - (appHeight / 2))

# window pops up on center of the screen
win.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

# label widget
myLabel1 = Label(win, text="Nepali AI Anchor",
                 font=("Calibri", 20), fg="Blue", anchor=N)  # Title
myLabel2 = Label(win, text="Modern Anchor Reimagined")  # Motto


# Print on Screen
myLabel1.grid(row=0, column=0, sticky="nsew")
myLabel2.grid(row=1, column=0, sticky="nsew", pady=(2, 8))

# myLabel1.pack()
# myLabel2.pack()

# Reading File


def import_file():
    file = askopenfile(mode='r', filetypes=[("Audio Files", ".wav .ogg")])
    if file is not None:
        content = file.read()
        print(content)


# Define Buttons
button_frame = Frame(win, highlightbackground="black",
                     highlightthickness=1)

button_import = Button(win, text="Import", padx=20,
                       pady=5, command=import_file, bg="#8cd9b3")

# photo = PhotoImage(file=r"E:\Nep_AIAnchor\mic.png")

originalImg = Image.open("mic.png")
resized = originalImg.resize((28, 28), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)
button_record = Button(win, padx=20, pady=5, command=import_file,
                       fg="Red", bg="#e6e6e6", image=img)

# button_import.pack(side=TOP, pady=10)
# button_record.pack(side=TOP,)
button_import.place(relx=0.1, rely=0.2)
button_record.place(relx=0.22, rely=0.2)

# Center the Content
win.columnconfigure(0, weight=1)
win.mainloop()
