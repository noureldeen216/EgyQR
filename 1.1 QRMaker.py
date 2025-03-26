# copyrights goes for nour_eldeen Ahmed 2024_2025
# for the source code of QR_Code generator Tool 
# NOTE!: this tool is NOT open source project. 

# Version 1.1

import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Function to generate QR code
def generator_qr():
    user_input = entry.get()  # Get the user input from the entry field
    if user_input.strip():  # Ensure input is not empty or whitespace
        try:
            img = qrcode.make(user_input)  # Generate the QR code
            
            # Prompt the user to choose a save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")],
                title="Save QR Code As",
                initialfile="Rename.png"
            )
            
            # Save the QR code image to the selected location or default location
            if file_path:
                img.save(file_path)
                label.config(text=f"QR code has been saved at: {file_path}")
            else:
                img.save("QR_Code.png")  # Default save if no location is selected
                label.config(text="QR code has been saved as 'QR_Code.png'!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        label.config(text="Please enter some text to generate a QR code.")

# Main GUI setup
myframe = tk.Tk()
myframe.title("QR Code Generator")
# use x as small for the size and not captail
myframe.geometry("300x200")
# resizable It makes me can lock the window frame like i can size it 
myframe.resizable(False, False)

# window icon
icon = Image.openicon = icon = Image.open("D:/Python/projects/exe builds of apps & programs/programs/builds of QRCode/1.1/img/icon.png")
icon = ImageTk.PhotoImage(icon)
myframe.iconphoto(True, icon)

# Input field (Entry widget)
entry = tk.Entry(myframe, width=40)
entry.pack(pady=10)

# Button to generate QR code
mybutton = tk.Button(myframe, text="Click here to generate QR", command=generator_qr, fg="Blue")
mybutton.pack(pady=10)

# Buttons
def show_credit():
    messagebox.showinfo("Credits", "Created By EGYCODE")

credit_button = tk.Button(myframe, text="Show Credits", command=show_credit, fg="blue")
credit_button.pack(side="bottom")

# Label to show success or error messages
label = tk.Label(myframe, text="", fg="blue")
label.pack(pady=10)

# Context Menu Functions
def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def cut():
    entry.event_generate("<<Cut>>")

def copy():
    entry.event_generate("<<Copy>>")

def paste():
    entry.event_generate("<<Paste>>")

# Create Context Menu
context_menu = Menu(myframe, tearoff=0)
context_menu.add_command(label="Cut / قص", command=cut)
context_menu.add_command(label="Copy / نسخ", command=copy)
context_menu.add_command(label="Paste / لصق", command=paste)

# Bind right-click to show context menu
entry.bind("<Button-3>", show_context_menu)

myframe.mainloop()