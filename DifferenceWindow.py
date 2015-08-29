from Tkinter import *
import tkFont
import tkFileDialog
import tkMessageBox
import os
import pywsd.utils


class DifferenceWindow(Tk):

    answer = None
    words = None

    def __init__(self, words, original_answer, simple_answer, adapted_answer, cosine_answer):
        Tk.__init__(self)
        self.answer = answer
        self.words = words
        self.title(window_title)
        self.initialize_ui()
        return

    def initialize_ui(self):
        self.iconbitmap(default="PlaceholderIcon.ico")
        self.geometry("600x300")
        self.resizable(width=FALSE, height=FALSE)
        text = Text(self, height=17, width=70, wrap=WORD)
        text.place(x=15, y=10)

        for i in range(len(self.answer)):
            definition = self.words[i]
            definition += ": "
            print(self.answer[i])
            definition += self.answer[i].definition()
            definition += "\n\n"
            text.insert(END, definition)

        text.config(state="disabled")
        return

