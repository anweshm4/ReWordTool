from Tkinter import *
import tkMessageBox


class DifferenceWindow(Tk):

    simple_answer = adapted_answer = cosine_answer = words = None
    text_pane_1 = text_pane_2 = text_pane_3 = None
    has_difference = False
    sense_1 = sense_2 = sense_3 = None

    def __init__(self, words, simple_answer, adapted_answer, cosine_answer):
        Tk.__init__(self)
        self.words = words
        self.simple_answer = simple_answer
        self.adapted_answer = adapted_answer
        self.cosine_answer = cosine_answer
        self.setup_panes()

        if self.has_difference:
            self.show_differences()
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

    def setup_three_panes(self):
        self.has_difference = True
        self.geometry("980x650")
        self.resizable(width=FALSE, height=FALSE)
        self.center()

        scrollbar_1 = Scrollbar(self)
        self.text_pane_1 = Text(self, height=45, width=33, wrap=WORD, yscrollcommand=scrollbar_1.set)
        self.text_pane_1.pack(padx=10, pady=5, side=LEFT)
        scrollbar_1.pack(side=LEFT, fill=Y)
        scrollbar_1.config(command=self.text_pane_1.yview)

        scrollbar_2 = Scrollbar(self)
        self.text_pane_2 = Text(self, height=45, width=33, wrap=WORD, yscrollcommand=scrollbar_2.set)
        self.text_pane_2.pack(padx=25, pady=5, side=LEFT)
        scrollbar_2.pack(padx=0, side=LEFT, fill=Y)
        scrollbar_2.config(command=self.text_pane_2.yview)

        scrollbar_3 = Scrollbar(self)
        self.text_pane_3 = Text(self, height=45, width=33, wrap=WORD, yscrollcommand=scrollbar_3.set)
        self.text_pane_3.pack(padx=25, pady=5, side=LEFT)
        scrollbar_3.pack(padx=0, side=LEFT, fill=Y)
        scrollbar_3.config(command=self.text_pane_3.yview)
        return

    def setup_two_panes(self):
        self.has_difference = True
        self.geometry("1000x650")
        self.resizable(width=FALSE, height=FALSE)
        self.center()

        scrollbar_1 = Scrollbar(self)
        self.text_pane_1 = Text(self, height=45, width=55, wrap=WORD, yscrollcommand=scrollbar_1.set)
        self.text_pane_1.pack(padx=10, pady=10, side=LEFT)
        scrollbar_1.pack(side=LEFT, fill=Y)
        scrollbar_1.config(command=self.text_pane_1.yview)

        scrollbar_2 = Scrollbar(self)
        self.text_pane_2 = Text(self, height=45, width=55, wrap=WORD, yscrollcommand=scrollbar_2.set)
        self.text_pane_2.pack(padx=25, pady=10, side=LEFT)
        scrollbar_2.pack(padx=0, side=LEFT, fill=Y)
        scrollbar_2.config(command=self.text_pane_2.yview)
        return

    def setup_no_panes(self):
        self.has_difference = False
        self.geometry("0x0")
        self.resizable(width=FALSE, height=FALSE)
        self.center()
        tkMessageBox.showinfo("Information", "There aren't any differences to show.")
        self.destroy()
        return

    def setup_panes(self):
        if self.has_three_sense_sets():
            if DifferenceWindow.same_senses_three(self.simple_answer, self.adapted_answer, self.cosine_answer):
                self.setup_no_panes()
            else:
                self.sense_1 = self.simple_answer
                self.sense_2 = self.adapted_answer
                self.sense_3 = self.cosine_answer
                self.title("Comparison - Simple Lesk, Adapted Lesk and Cosine Lesk")
                self.setup_three_panes()
        elif self.has_two_sense_sets():
            if self.has_simple_sense() and self.has_adapted_sense():
                if DifferenceWindow.same_senses_two(self.simple_answer, self.adapted_answer):
                    self.setup_no_panes()
                else:
                    self.sense_1 = self.simple_answer
                    self.sense_2 = self.adapted_answer
                    self.title("Comparison - Simple Lesk and Adapted Lesk")
                    self.setup_two_panes()
            if self.has_simple_sense() and self.has_cosine_sense():
                if DifferenceWindow.same_senses_two(self.simple_answer, self.cosine_answer):
                    self.setup_no_panes()
                else:
                    self.sense_1 = self.simple_answer
                    self.sense_2 = self.cosine_answer
                    self.title("Comparison - Simple Lesk and Cosine Lesk")
                    self.setup_two_panes()

            if self.has_adapted_sense() and self.has_cosine_sense():
                if DifferenceWindow.same_senses_two(self.adapted_answer, self.cosine_answer):
                    self.setup_no_panes()
                else:
                    self.sense_1 = self.adapted_answer
                    self.sense_2 = self.cosine_answer
                    self.title("Comparison - Adapted Lesk and Cosine Lesk")
                    self.setup_two_panes()
        else:
            self.setup_no_panes()
        return

    def has_two_sense_sets(self):
        if (self.has_simple_sense() and self.has_adapted_sense()) or (self.has_simple_sense() and self.has_cosine_sense()) or (self.has_adapted_sense() and self.has_cosine_sense()):
                return True
        else:
            return False

    def has_three_sense_sets(self):  # Do we need three panes or two?
        if self.has_simple_sense() and self.has_adapted_sense() and self.has_cosine_sense():
            return True
        else:
            return False

    def has_simple_sense(self):
        try:
            if len(self.simple_answer) > 0:
                return True
            else:
                return False
        except TypeError:
            return False

    def has_adapted_sense(self):
        try:
            if len(self.adapted_answer) > 0:
                return True
            else:
                return False
        except TypeError:
            return False

    def has_cosine_sense(self):
        try:
            if len(self.cosine_answer) > 0:
                return True
            else:
                return False
        except TypeError:
            return False

    # * Get all three sense-sets - simple, adapted and cosine.
    # * Make sure at least two of them have 0+ senses.
    #  (If not, then no need to compare)
    # * Compare all senses.
    #    If they are all equal
    #        show "No differences"
    #    else
    #        show the differences.
    # SA AA, SA CA, AA CA

    def show_differences(self):
        if self.has_three_sense_sets():
            for i in range(len(self.sense_1)):
                definition_1 = self.words[i]
                definition_2 = self.words[i]
                definition_3 = self.words[i]
                definition_1 += ": "
                definition_2 += ": "
                definition_3 += ": "

                try:
                    definition_1 += self.sense_1[i].definition()
                    definition_2 += self.sense_2[i].definition()
                    definition_3 += self.sense_3[i].definition()
                except AttributeError:
                    definition_1 += self.sense_1[i]
                    definition_2 += self.sense_2[i]
                    definition_3 += self.sense_3[i]

                definition_1 += "\n\n"
                definition_2 += "\n\n"
                definition_3 += "\n\n"

                if not definition_1 == definition_2 == definition_3:
                    self.text_pane_1.insert(END, definition_1)
                    self.text_pane_2.insert(END, definition_2)
                    self.text_pane_3.insert(END, definition_3)

            self.text_pane_3.config(state="disabled")
        else:
            for i in range(len(self.sense_1)):
                definition_1 = self.words[i]
                definition_2 = self.words[i]
                definition_1 += ": "
                definition_2 += ": "

                try:
                    definition_1 += self.sense_1[i].definition()
                    definition_2 += self.sense_2[i].definition()
                except AttributeError:
                    definition_1 += self.sense_1[i]
                    definition_2 += self.sense_2[i]

                definition_1 += "\n\n"
                definition_2 += "\n\n"

                if not definition_1 == definition_2:
                    self.text_pane_1.insert(END, definition_1)
                    self.text_pane_2.insert(END, definition_2)

        self.text_pane_1.config(state="disabled")
        self.text_pane_2.config(state="disabled")
        return

    @staticmethod
    def same_senses_two(sense_1, sense_2):
        all_same = True
        for i in range(len(sense_1)):
            if not (sense_1[i] == sense_2[i]):
                all_same = False
        return all_same

    @staticmethod
    def same_senses_three(sense_1, sense_2, sense_3):
        all_same = True
        for i in range(len(sense_1)):
            if not (sense_1[i] == sense_2[i] == sense_3[i]):
                all_same = False
        return all_same
