# MainForm.py
# Author: Amlanjyoti Saikia
# PartOf: Project ReWord
# Date: 31/July/2015

from Tkinter import *
import tkFont
import tkFileDialog
import tkMessageBox
import os
import pywsd.utils


class ResultWindow(Tk):

    answer = None
    words = None

    def __init__(self, window_title, words, answer):
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
            try:
                definition += self.answer[i].definition()  # TODO: Throws exception if there is no definition
            except AttributeError:
                definition += self.answer[i]
            definition += "\n\n"
            text.insert(END, definition)

        text.config(state="disabled")
        return
