#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import subprocess as sub
from tkinter.messagebox import showwarning
import webbrowser


# function to quick connect to nordvpn
def quick_connect():
    """
    Establishes a quick connection to the nearest server to you.
    :return:
    """
    os.system("nordvpn c")


def disconnect():
    """
    Interrupts the vpn connection. If no vpn connection, then nothing happens
    :return:
    """
    os.system("nordvpn disconnect")


def update_status():
    """
    This method takes the state of the connection from the terminal commands located separately
    in script.sh, and returns basic information about the vpn connection.
    :return:
    """
    # take the terminal command from the script, process it and save it in output/errors
    p = sub.Popen('./script.sh', stdout=sub.PIPE, stderr=sub.PIPE)
    output, errors = p.communicate()
    status.delete('1.0', END)  # delete any previous text for refreshing the content
    status.insert(END, output)  # insert the new status


def connect_to(country=None, event=None):
    """
    Depends on the input we give it in, establishes a connection to a server from the country we picked.
    :param country: This is for the quick connects from icons, so that i can pass directly the values
    :param  event: If we hit Keyboard-Enter, then we have the Event. Otherwise for the Button-Enter
    it is set to None.
    :return: None, just connect us to the country (& server if specified) we want.
    """
    if entry.get() is not None:
        country = entry.get()
        entry.delete(0, END)    # once we get the input, clear it out so that it doesn't interfere with the 'flags'
    os.system(f"nordvpn connect {country}")
    update_status()


def connect_to_flag(country):
    """
    Depends on the input we give it in, establishes a connection to a server from the country we picked.
    :param country: This is for the quick connects from icons, so that i can pass directly the values
    :return: None, just connect us to the country (& server if specified) we want.
    """
    os.system(f"nordvpn connect {country}")
    update_status()


def external_window(title, content):
    """
    This is just a pop-up window for the purpose of 'About this app'.
    """
    window = Toplevel(root)
    window.title(title)
    window.geometry("500x300")
    window.resizable(0, 0)
    text = Text(master=window, height=6, width=100)
    text.pack(side=LEFT, fill=Y)
    S = Scrollbar(window)
    S.pack(side=RIGHT, fill=Y)
    text.insert(END, content)
    text.config(yscrollcommand=S.set, state=DISABLED)


def get_github_dir():
    """
    Opens the project's website in github
    """
    url = 'https://github.com/takispig/nordvpn-linux-GUI'
    webbrowser.open(url)


def on_click(event):
    """
    On left-click (=event) the 'disabled' entry is free, and the placeholder deleted
    """
    entry.configure(state=NORMAL)
    entry.delete(0, END)
    # make the callback only work once
    entry.unbind('<Button-1>', click)


# Run the script order (status) at the startup and create the variables
p = sub.Popen('./script.sh', stdout=sub.PIPE, stderr=sub.PIPE)
output, errors = p.communicate()

# main:
root = Tk()
root.title("NordVPN (Unofficial Linux App)")
root.geometry("500x380")
root.resizable(0, 0)  # make the window-size static
# window.iconbitmap(bitmap="@nordvpn1.XBM")

# Create a basic toolbar to add some extras ---------------------------------------------
toolbar = Frame(bg='#333333')
toolbar.pack(fill=BOTH, expand=True)
# About
title_about = 'About this Application:'
content_about = 'This is an app developed by me in my free time, in a try to create a GUI version' \
                'of the NordVPN.\nThis is app has been tested under Ubuntu 20.04 and Raspberry Pi 4 with' \
                'raspbian booster. \nDeveloped with Python, it uses xterm for the internal Terminal.' \
                '\nIn no case this app is fully functionally and i know it is far from perfect, but i did' \
                'it for my everyday use and hoped that some of you may find it useful.'
b_about = Button(toolbar, text="About this app", command=lambda: external_window(title_about, content_about))
b_about.pack(side=LEFT, padx=5, pady=1)
b_about.config(padx=1, pady=1)

# Navigate to GitHub Project directory
b_git = Button(toolbar, text="GitHub Project's directory", command=lambda: get_github_dir())
b_git.pack(side=LEFT, padx=5, pady=3)
b_git.config(padx=1, pady=1)

# Log message box -----------------------------------------------------------------------
log_frame = Frame(relief=RAISED)
log_frame.pack(fill=BOTH, expand=True)
log_frame.configure(background='#4da6ff')
# update_status(status, window)
status = Text(master=log_frame, height=8)
status.pack()
status.insert(END, output)
# status.config(state=DISABLED)   # prevents output text from being editable
status.update_idletasks()

# Add Terminal for further accessibility ------------------------------------------------
xterm_frame = Frame(relief=RAISED, height=120, width=50, borderwidth=1)
xterm_frame.pack(fill=BOTH, expand=True, side=TOP)
xterm_frame_id = xterm_frame.winfo_id()
try:
    sub.Popen(
        ["xterm", "-into", str(xterm_frame_id), "-geometry", "100x30"],
        stdin=sub.PIPE, stdout=sub.PIPE)
except FileNotFoundError:
    showwarning("Error", "xterm is not installed")
    raise SystemExit

# Create frame for the quick-connect options --------------------------------------------
frame_qc = Frame(padx=3)
frame_qc.pack(fill=BOTH)
# quick-connect text
text_quick = Text(frame_qc, height=1, width=17)
text_quick.pack(side=LEFT)
text_quick.insert(END, "Quick connect to: ")
text_quick.config(state=DISABLED, bg='#F0F0F0')
# quick-connect to greece
greece = PhotoImage(file="images/greece-flag-3d-icon-32.png")
roundedbutton_gr = Button(frame_qc, image=greece, command=lambda: [connect_to_flag('gr'), update_status()])
roundedbutton_gr["bg"] = "white"
roundedbutton_gr["border"] = "0"
roundedbutton_gr.pack(side=LEFT)
# quick-connect to germany
germany = PhotoImage(file="images/germany-flag-3d-icon-32.png")
roundedbutton_ger = Button(frame_qc, image=germany, command=lambda: [connect_to_flag('de'), update_status()])
roundedbutton_ger["bg"] = "white"
roundedbutton_ger["border"] = "0"
roundedbutton_ger.pack(side=LEFT)
# quick-connect to uk
uk = PhotoImage(file="images/england-flag-3d-icon-32.png")
roundedbutton_uk = Button(frame_qc, image=uk, command=lambda: [connect_to_flag('uk'), update_status()])
roundedbutton_uk["bg"] = "white"
roundedbutton_uk["border"] = "0"
roundedbutton_uk.pack(side=LEFT)
# quick-connect to greece
usa = PhotoImage(file="images/united-states-of-america-flag-3d-icon-32.png")
roundedbutton_usa = Button(frame_qc, image=usa, command=lambda: [connect_to_flag('us'), update_status()])
roundedbutton_usa["bg"] = "white"
roundedbutton_usa["border"] = "0"
roundedbutton_usa.pack(side=LEFT)

# adding manual input for user, to select a country if it is not listed in the default 4 countries
entry = Entry(frame_qc, justify='center', width=23)
entry.pack()
entry.insert(0, 'Country (i.e. US or Sweden)')  # set example placeholder
entry.configure(state=DISABLED)  # make text seem blocked unless user clicks
click = entry.bind("<Button-1>", on_click)
entry.bind("<Return>", connect_to)
# add an ENTER button, if user can't/won't press the enter button
submit = Button(frame_qc, text='Enter', justify='center', height=1, width=2, command=connect_to)
submit.pack()

# Add buttons to navigate through options -------------------------------------------------------------
frame_buttons = Frame()
frame_buttons.pack(fill=BOTH)
button1 = Button(frame_buttons, text="Quick Connect", command=lambda: [quick_connect(), update_status()], bg='#00cc00')
button1.pack(side=LEFT, padx=5, pady=5)
button2 = Button(frame_buttons, text="Update Status", command=update_status)
button2.pack(side=LEFT, padx=5, pady=5)
button3 = Button(frame_buttons, text="Disconnect", command=lambda: [disconnect(), update_status()], bg='#ff4d4d')
button3.pack(side=RIGHT, padx=5, pady=5)

# run the main loop
root.mainloop()
