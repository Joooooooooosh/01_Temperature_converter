from tkinter import *

import random


class Converter:
    def __init__(self, parent):

        # Formatting varibles...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color)
        self.converter_frame.grid()

        # Temperature Conversion Heading (rov 0)
        self.temp_converter_label = Label (self.converter_frame, 
        text="Temperature Converter",font=("Arial", "16", "bold"),bg=background_color,padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (rov 1)
        # self.help_button = Button(self.converter_frame,)
    



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    Converter(root)
    root.mainloop()