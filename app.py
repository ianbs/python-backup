from tkinter import Tk, Label, Button

# from events.backup import copia_pastas


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.geometry("500x300")

        # self.label_index = 0
        # self.label_text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        # self.label = Label(master, textvariable=self.label_text)
        # self.label.bind("<Button-1>", self.cycle_label_text)
        # self.label.pack()

        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self):
        print("Greetings!")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
