import tkinter as tk
from tkinter import ttk
from cavendish import main


running = True
exiting = False

#=======================================
# Basic tkinter window settings
#=======================================
root = tk.Tk()
root.title('Cavendish Launcher')
root.geometry('528x350')
root.resizable(False, False)
root.iconbitmap('./assets/favicon.ico')

def __on_destroy(*_) -> None:
    global exiting
    exiting = True

root.bind('<Destroy>', __on_destroy)

#=======================================
# Launcher logo and description
#=======================================
canvas = tk.Canvas(width=528, height=124)
canvas.pack()

logo = tk.PhotoImage(file='./assets/logo.png')
canvas.create_image(0, 0, anchor=tk.NW, image=logo)

description = tk.Label(text='Yet another gravitational physics simulator', font=("Times New Roman", 16, "bold", "italic"))
description.pack()

ttk.Separator(orient="horizontal").pack(fill="x", pady=20)

#=======================================
# Launcher components
#=======================================
language = ttk.Combobox(
    state="readonly",
    values=["English", "Español"],
    font=("Times New Roman", 14)
)
language.set('English')
language.pack()

ttk.Style().configure('Font.TCheckbutton', font=("Times New Roman", 14))
show_gui = tk.BooleanVar(value=True)
gui = ttk.Checkbutton(
    text='Display settings panel',
    variable=show_gui,
    style='Font.TCheckbutton'
)
gui.pack(pady=20)

def __on_launch_button_click(*_) -> None:
    global running
    running = False

ttk.Style().configure('Font.TButton', font=("Times New Roman", 14))
launch_button = ttk.Button(text="Launch!", style="Font.TButton", command=__on_launch_button_click)
launch_button.pack()

if __name__ == '__main__':
    while running:
        if exiting:
            exit(0)
        root.update()
    lang, gui = language.get(), show_gui.get()
    root.destroy()
    main(lang, gui)