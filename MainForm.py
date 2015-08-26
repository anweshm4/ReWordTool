from Tkinter import *
import tkFont
import tkFileDialog
import tkMessageBox
import os
import enchant
import string
import nltk
from ParaphrasingEngine import ParaphrasingEngine
from ResultWindow import ResultWindow


class MainForm(Tk):

    radio_button = radio_enter_text = radio_select_file = text_input = label_file = None
    entry_file_location = button_file_location = label_frame = None
    check_original_var = check_simple_var = check_adapted_var = check_cosine_var = None
    check_original = check_simple = check_adapted = check_cosine = None
    button_proceed = button_cancel = None

    def __init__(self):
        Tk.__init__(self)
        self.initialize_form()
        ResultWindow("TEST", None)
        return

    def initialize_form(self):
        global radio_button, radio_enter_text, radio_select_file, text_input, label_file
        global entry_file_location, button_file_location, label_frame
        global check_original_var, check_simple_var, check_adapted_var, check_cosine_var
        global check_original, check_simple, check_adapted, check_cosine
        global button_proceed, button_cancel

        print("Reword tool UI")

        x_pos = 15
        y_pos = 15
        self.geometry("900x450")
        self.resizable(width=FALSE, height=FALSE)
        self.title("ReWord Tool")
        #self.iconbitmap(default="PlaceholderIcon.ico")
        self.center(self)

        radio_button = IntVar()
        radio_enter_text = Radiobutton(self,
                                       variable=radio_button,
                                       value=1,
                                       text="Enter text",
                                       command=self.radio_check_changed
                                       )
        radio_enter_text.place(x=x_pos, y=y_pos)

        y_pos += 35
        text_input = Text(self, height=10, width=108, wrap=WORD)
        text_input.place(x=x_pos, y=y_pos)

        y_pos += 180
        radio_select_file = Radiobutton(self,
                                        variable=radio_button,
                                        value=2,
                                        text="Select file",
                                        command=self.radio_check_changed
                                        )
        radio_select_file.place(x=x_pos, y=y_pos)

        y_pos += 35
        label_file = Label(self, text="File Location: ")
        label_file.place(x=x_pos, y=y_pos)

        x_pos += 90
        entry_file_location = Entry(self, width=90)
        entry_file_location.config(state="disabled", bg='grey')
        entry_file_location.place(x=x_pos, y=y_pos)

        x_pos += 555
        y_pos -= 5
        button_file_location = Button(self, text="Browse", command=self.select_file, width=30)
        button_file_location.config(state="disabled")
        button_file_location.place(x=x_pos, y=y_pos)
        y_pos += 5

        x_pos = 15
        y_pos += 35
        label_frame = LabelFrame(self, text="Select algorithm(s): ")
        label_frame.place(x=x_pos, y=y_pos, width=420, height=60)

        y_pos += 20
        x_pos += 10
        check_original_var = IntVar()
        check_original = Checkbutton(self,
                                     variable=check_original_var,
                                     onvalue=1,
                                     offvalue=0,
                                     text="Original Lesk"
                                     )
        check_original.place(x=x_pos, y=y_pos)
        check_original.config(state="disabled")

        x_pos += 100
        check_simple_var = IntVar()
        check_simple = Checkbutton(self,
                                   variable=check_simple_var,
                                   onvalue=1,
                                   offvalue=0,
                                   text="Simple Lesk"
                                   )
        check_simple.place(x=x_pos, y=y_pos)

        x_pos += 100
        check_adapted_var = IntVar()
        check_adapted = Checkbutton(self,
                                    variable=check_adapted_var,
                                    onvalue=1,
                                    offvalue=0,
                                    text="Adapted Lesk"
                                    )
        check_adapted.place(x=x_pos, y=y_pos)

        x_pos += 100
        check_cosine_var = IntVar()
        check_cosine = Checkbutton(self,
                                   variable=check_cosine_var,
                                   onvalue=1,
                                   offvalue=0,
                                   text="Cosine Lesk"
                                   )
        check_cosine.place(x=x_pos, y=y_pos)

        x_pos = 15
        y_pos += 65
        font_big = tkFont.Font(size=14)
        button_proceed = Button(self, text="Proceed", font=font_big, command=self.proceed_pressed)
        button_proceed.place(x=x_pos, y=y_pos, height=50, width=400)

        x_pos += 460
        button_cancel = Button(self, text="Cancel", font=font_big, command=self.cancel_pressed)
        button_cancel.place(x=x_pos, y=y_pos, height=50, width=400)

        radio_select_file.deselect()
        radio_enter_text.select()
        text_input.delete(INSERT, END)
        print "UI Initiation complete."
        self.mainloop()
        print "Exiting..."
        exit(0)

        return

    @staticmethod
    def center(win):
        """
        centers a tkinter window
        :param win: the root or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()
        return

    @staticmethod
    def radio_check_changed():
        global radio_button, button_file_location, entry_file_location, text_input

        if radio_button.get() == 1:
            print "Enter text mode:"
            button_file_location.config(state="disabled")
            text_input.config(state="normal")
            entry_file_location.config(state="disabled")
        else:
            print "Open file mode:"
            button_file_location.config(state="normal")
            text_input.config(state="disabled")
            entry_file_location.config(state="normal")
        return

    @staticmethod
    def select_file():
        global entry_file_location
        print "File open dialog box."

        options = {'defaultextension': '.txt',
                   'filetypes': [('Text files', '.txt'), ('All files', '.*')],
                   'title': 'Select file'}
        file_name = tkFileDialog.askopenfilename(**options)

        print("File selected: " + file_name)
        if file_name != '':
            entry_file_location.delete(0, END)
            entry_file_location.insert(0, file_name)
        return

    # TODO: Write method
    @staticmethod
    def validate():
        print "Validating form"
        global radio_button, button_file_location, entry_file_location, text_input
        global check_original_var, check_simple_var, check_adapted_var, check_cosine_var

        if radio_button.get() == 1:

            print("INFO: Checking input text.")
            text = text_input.get("1.0", END)

            if text == '' or text == '\n':
                print("ERROR: Text absent.")
                tkMessageBox.showerror("Error", "Input text cannot be empty.")
                return False
            else:
                print("OK: Text present.")
        else:
            print("INFO: Checking input file.")
            text = entry_file_location.get()

            if text == '':
                print("ERROR: No file name given.")
                tkMessageBox.showerror("Error", "No file name given.")
                return False
            else:
                print("INFO: Checking file stats.")

                if os.path.isfile(text):
                    print("OK: File exists.")
                else:
                    print("ERROR: File doesn't exist.")
                    tkMessageBox.showerror("Error", "File doesn't exist.")
                    return False

                if os.path.getsize(text) == 0:
                    print("ERROR: File is empty.")
                    tkMessageBox.showerror("Error", "File is empty.")
                    return False
                else:
                    print("OK: File isn't empty.")

        if MainForm.correct_spelling(text):
            print("OK: No spelling errors.")
        else:
            print("ERROR: Text has spelling errors or unknown words.")
            tkMessageBox.showerror("Error", "Text has spelling errors or unknown words.")
            return False

        if check_original_var.get() or check_simple_var.get() or check_adapted_var.get() or check_cosine_var.get():
            print "OK: At least one algorithm selected"
        else:
            print "ERROR: No algorithm selected"
            tkMessageBox.showerror("Error", "No algorithm selected.")
            return False

        return True

    @staticmethod
    def correct_spelling(input_text):
        words = nltk.word_tokenize(str(input_text).translate(None, string.punctuation))
        dict_en_us = enchant.Dict("en_US")

        correct = True

        for each_word in words:
            if not dict_en_us.check(each_word):
                correct = False
        return correct

    # TODO: Write method
    def proceed_pressed(self):
        global radio_button, text_input
        global check_original_var, check_simple_var, check_adapted_var, check_cosine_var

        if self.validate():
            if radio_button.get():
                input_string = text_input.get("1.0", END)
            else:
                input_string = None

            pe = ParaphrasingEngine(input_string)
            print "Words: "
            print pe.words

            original_result = simple_result = adapted_result = cosine_result = None

            if check_original_var.get():
                original_result = pe.disambiguate_original_lesk()
                ResultWindow("Original Lesk",pe.words, original_result)

            if check_simple_var.get():
                simple_result = pe.disambiguate_simple_lesk()
                ResultWindow("Simple Lesk", pe.words, simple_result)

            if check_adapted_var.get():
                adapted_result = pe.disambiguate_adapted_lesk()
                ResultWindow("Adapted Lesk", pe.words, adapted_result)

            if check_cosine_var.get():
                cosine_result = pe.disambiguate_cosine_lesk()
                ResultWindow("Cosine Lesk", pe.words, cosine_result)

            print "#######################################################"
            print original_result

            print "#######################################################"
            print simple_result

            print "#######################################################"
            print adapted_result

            print "#######################################################"
            print cosine_result

        return

    # TODO: Write method
    @staticmethod
    def cancel_pressed():
        if tkMessageBox.askquestion("Confirm exit", "Are you sure you want to exit?", icon="question") == 'yes':
            print("Exiting...")
            exit(0)
        return

MainForm()
