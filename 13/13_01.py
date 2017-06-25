# 1. Name and Address
# Write a GUI program that displays your name and address when a button is clicked.
# The program’s  window  should  appear  as  the  sketch  on  the  left  side  of
# Figure  13-26  when  it runs. When the user clicks the Show Info button, the program
# should display your name and address, as shown in the sketch on the right of the
# figure.

import tkinter

class ShowInfo:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        name = "bnoden"
        street = "555 Circuit Blvd"
        city = "Computer City, RX 65536"

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="{0}\n{1}\n{2}"
                                          .format(name, street, city))

sinfo = ShowInfo()
