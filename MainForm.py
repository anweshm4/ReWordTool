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
from StopwordDictionary import StopWordDictionary
from DifferenceWindow import DifferenceWindow


class MainForm(Tk):

    # Declaration of controls
    radio_button = radio_enter_text = radio_select_file = text_input = label_file = None
    entry_file_location = button_file_location = label_frame = None
    check_original_var = check_simple_var = check_adapted_var = check_cosine_var = None
    check_original = check_simple = check_adapted = check_cosine = None
    button_proceed = button_cancel = None
    stop_word_dictionary = None

    def __init__(self):
        Tk.__init__(self)  # Initialize parent class.
        self.initialize_form()  # Initialize controls.
        return

    def initialize_form(self):
        # global radio_button, radio_enter_text, radio_select_file, text_input, label_file
        # global entry_file_location, button_file_location, label_frame
        # global check_original_var, check_simple_var, check_adapted_var, check_cosine_var
        # global check_original, check_simple, check_adapted, check_cosine
        # global button_proceed, button_cancel
        self.stop_word_dictionary = StopWordDictionary()

        print("Reword tool UI")

        x_pos = 15  # Markers that we will manipulate to position items
        y_pos = 15
        self.geometry("900x450")  # Set size
        self.resizable(width=FALSE, height=FALSE)  # Make window of fixed size
        self.title("ReWord Tool")  # Set title
        # self.iconbitmap(default="PlaceholderIcon.ico") # Maybe jpeg will work? Will test.
        # Breaks platform independence as it is now.
        self.center()  # Place window in the center of the form. NOT an inbuilt method.

        self.radio_button = IntVar()  # See http://effbot.org/tkinterbook/variable.htm
        self.radio_enter_text = Radiobutton(self, variable=self.radio_button,  # variable indicates which radio button was pressed
                                            value=1,  # this button, when pressed will hold a value of 1
                                            text="Enter text",
                                            command=self.radio_check_changed
                                            )
        self.radio_enter_text.place(x=x_pos, y=y_pos)

        y_pos += 35
        self.text_input = Text(self, height=10, width=108, wrap=WORD)
        self.text_input.place(x=x_pos, y=y_pos)

        y_pos += 180
        self.radio_select_file = Radiobutton(self,
                                             variable=self.radio_button,
                                             value=2,  # when pressed this button will hold a value of 2
                                             text="Select file",
                                             command=self.radio_check_changed
                                             )
        self.radio_select_file.place(x=x_pos, y=y_pos)

        y_pos += 35
        self.label_file = Label(self, text="File Location: ")
        self.label_file.place(x=x_pos, y=y_pos)

        x_pos += 90
        self.entry_file_location = Entry(self, width=60)
        self.entry_file_location.config(state="disabled", bg='grey')
        self.entry_file_location.place(x=x_pos, y=y_pos)

        x_pos += 500
        y_pos -= 5
        self.button_file_location = Button(self, text="Browse", command=self.select_file, width=25)
        self.button_file_location.config(state="disabled")
        self.button_file_location.place(x=x_pos, y=y_pos)
        y_pos += 5

        x_pos = 15
        y_pos += 35
        self.label_frame = LabelFrame(self, text="Select algorithm(s): ")
        self.label_frame.place(x=x_pos, y=y_pos, width=600, height=60)

        y_pos += 20
        x_pos += 10
        self.check_original_var = IntVar()
        self.check_original = Checkbutton(self,
                                          variable=self.check_original_var,
                                          onvalue=1,
                                          offvalue=0,
                                          text="Original Lesk"
                                          )
        self.check_original.place(x=x_pos, y=y_pos)
        self.check_original.config(state="disabled")

        x_pos += 150
        self.check_simple_var = IntVar()
        self.check_simple = Checkbutton(self,
                                        variable=self.check_simple_var,
                                        onvalue=1,
                                        offvalue=0,
                                        text="Simple Lesk"
                                        )
        self.check_simple.place(x=x_pos, y=y_pos)

        x_pos += 150
        self.check_adapted_var = IntVar()
        self.check_adapted = Checkbutton(self,
                                         variable=self.check_adapted_var,
                                         onvalue=1,
                                         offvalue=0,
                                         text="Adapted Lesk"
                                        )
        self.check_adapted.place(x=x_pos, y=y_pos)

        x_pos += 150
        self.check_cosine_var = IntVar()
        self.check_cosine = Checkbutton(self,
                                        variable=self.check_cosine_var,
                                        onvalue=1,
                                        offvalue=0,
                                        text="Cosine Lesk"
                                        )
        self.check_cosine.place(x=x_pos, y=y_pos)

        x_pos = 15
        y_pos += 65
        font_big = tkFont.Font(size=14)
        self.button_proceed = Button(self, text="Proceed", font=font_big, command=self.proceed_pressed)
        self.button_proceed.place(x=x_pos, y=y_pos, height=50, width=400)

        x_pos += 460
        self.button_cancel = Button(self, text="Cancel", font=font_big, command=self.cancel_pressed)
        self.button_cancel.place(x=x_pos, y=y_pos, height=50, width=400)

        self.radio_select_file.deselect()
        self.radio_enter_text.select()
        self.text_input.delete(INSERT, END)
        print "UI Initiation complete."
        self.mainloop()
        print "Exiting..."
        exit(0)

        return

    def center(self):
        """
        centers a tkinter window
        :param self: the root or Toplevel window to center
        """
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()
        return

    def radio_check_changed(self):
        # global radio_button, button_file_location, entry_file_location, text_input

        if self.radio_button.get() == 1:
            print "Enter text mode:"
            self.button_file_location.config(state="disabled")
            self.text_input.config(state="normal")
            self.entry_file_location.config(state="disabled")
        else:
            print "Open file mode:"
            self.button_file_location.config(state="normal")
            self.text_input.config(state="disabled")
            self.entry_file_location.config(state="normal")
        return

    def select_file(self):
        # global entry_file_location
        print "File open dialog box."

        options = {'defaultextension': '.txt',
                   'filetypes': [('Text files', '.txt'), ('All files', '.*')],
                   'title': 'Select file'}
        file_name = tkFileDialog.askopenfilename(**options)

        print("File selected: " + file_name)
        if file_name != '':
            self.entry_file_location.delete(0, END)
            self.entry_file_location.insert(0, file_name)
        return

    def validate(self):
        print "Validating form"
        # global radio_button, button_file_location, entry_file_location, text_input
        # global check_original_var, check_simple_var, check_adapted_var, check_cosine_var

        if self.radio_button.get() == 1:
            print("INFO: Checking input text.")
            text = self.text_input.get("1.0", END)

            if text == '' or text == '\n':
                print("ERROR: Text absent.")
                tkMessageBox.showerror("Error", "Input text cannot be empty.")
                return False
            else:
                print("OK: Text present.")
        else:
            print("INFO: Checking input file.")
            text = self.entry_file_location.get()

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
                    input_file = open(text, "r")
                    text = input_file.read()
                    input_file.close()

        print(text)

        if MainForm.correct_spelling(text):
            print("OK: No spelling errors.")
        else:
            print("ERROR: Text has spelling errors or unknown words.")
            tkMessageBox.showerror("Error", "Text has spelling errors or unknown words.")
            return False

        if self.check_original_var.get() or self.check_simple_var.get() or self.check_adapted_var.get() or self.check_cosine_var.get():
            print "OK: At least one algorithm selected"
        else:
            print "ERROR: No algorithm selected"
            tkMessageBox.showerror("Error", "No algorithm selected.")
            return False

        return True

    def proceed_pressed(self):
        # global radio_button, text_input, entry_file_location
        # global check_original_var, check_simple_var, check_adapted_var, check_cosine_var

        if self.validate():
            if self.radio_button.get() == 1:
                input_string = self.text_input.get("1.0", END)
            else:
                location = self.entry_file_location.get()
                file_object = open(location, "r")
                input_string = file_object.read()
                file_object.close()
                print("INPUT: " + location)

            pe = ParaphrasingEngine(input_string, self.stop_word_dictionary)
            print "Words: "
            print pe.words

            original_result = simple_result = adapted_result = cosine_result = None

            if self.check_original_var.get():
                original_result = pe.disambiguate_original_lesk()
                ResultWindow("Original Lesk", pe.words, original_result)

            if self.check_simple_var.get():
                simple_result = pe.disambiguate_simple_lesk()
                ResultWindow("Simple Lesk", pe.words, simple_result)

            if self.check_adapted_var.get():
                adapted_result = pe.disambiguate_adapted_lesk()
                ResultWindow("Adapted Lesk", pe.words, adapted_result)

            if self.check_cosine_var.get():
                cosine_result = pe.disambiguate_cosine_lesk()
                ResultWindow("Cosine Lesk", pe.words, cosine_result)

            DifferenceWindow(input_string, simple_result, adapted_result, cosine_result)

            # print "#######################################################"
            # print original_result
            #
            # print "#######################################################"
            # print simple_result
            #
            # print "#######################################################"
            # print adapted_result
            #
            # print "#######################################################"
            # print cosine_result
        return

    @staticmethod
    def cancel_pressed():
        if tkMessageBox.askquestion("Confirm exit", "Are you sure you want to exit?", icon="question") == 'yes':
            print("Exiting...")
            exit(0)
        return

    @staticmethod
    def correct_spelling(input_text):
        words = nltk.word_tokenize(str(input_text).translate(None, string.punctuation))
        dict_en_us = enchant.Dict("en_US")
        dict_en_uk = enchant.Dict("en_UK")

        correct = True

        for each_word in words:
            if not each_word[0].isupper():
                # If doesn't start with a upper case
                if (not dict_en_us.check(each_word)) and (not dict_en_uk.check(each_word)):
                    # if not present in US and UK dictionaries
                    correct = False
                    break
        return correct

MainForm()
