from Tkinter import *

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
        # self.iconbitmap(default="PlaceholderIcon.ico")
        # Breaks portability. Can't use this. Will look for workaround.
        self.geometry("600x300")
        self.resizable(width=FALSE, height=FALSE)
        text = Text(self, height=17, width=70, wrap=WORD)
        text.place(x=15, y=10)

        for i in range(len(self.answer)):
            definition = self.words[i]
            definition += ": "
            print(self.answer[i])
            try:
                definition += self.answer[i].definition()
            except AttributeError:   # TODO: This is redundant.We already provide definitions for stopwords and such.
                definition += self.answer[i]
            definition += "\n\n"
            text.insert(END, definition)

        text.config(state="disabled")
        return
