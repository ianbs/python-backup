from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Progressbar
import time

from events.backup import copia_pastas


def step(master, progresso_copia):
    for i in range(5):
        master.update_idletasks()
        progresso_copia["value"] += 20

        time.sleep(1)


class MainGui:
    def __init__(self, master):
        self.master = master
        master.title("Backup")
        master.geometry("650x150")
        master.rowconfigure(4, minsize=300, weight=1)
        master.columnconfigure(3, minsize=500, weight=1)

        self.label_origem = Label(
            text="Digite o caminho de origem:",
            master=master,
        )
        self.label_origem.grid(row=0, column=0, padx=5, pady=5)

        self.caminho_origem = Entry(width=70)
        self.caminho_origem.grid(row=0, column=1, padx=5, pady=5)

        self.label_destino = Label(
            text="Digite o caminho de origem:",
            master=master,
        )
        self.label_destino.grid(row=1, column=0, padx=5, pady=5)

        self.caminho_destino = Entry(width=70)
        self.caminho_destino.grid(row=1, column=1, padx=5, pady=5)

        self.realizar_button = Button(
            master,
            text="Realizar Copia de Arquivos",
            command=lambda: copia_pastas(
                self.caminho_origem.get(),
                self.caminho_destino.get(),
                step(master, self.progresso_copia),
            ),
            height=1,
            width=50,
        )
        self.realizar_button.grid(row=2, column=1, padx=5, pady=5)

        self.progresso_copia = Progressbar(
            master=master, orient="horizontal", length=300, mode="indeterminate"
        )
        self.progresso_copia.grid(row=3, column=1, padx=5, pady=5)


root = Tk()
gui = MainGui(root)
root.mainloop()
