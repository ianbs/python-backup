from tkinter import Tk, Label, Entry, Button, PhotoImage, Frame
from tkinter.ttk import Progressbar
import time
from pystray import MenuItem as item
import os
import pystray
from PIL import Image

from events.backup import copia_pastas


def step(master, progresso_copia):
    for i in range(5):
        master.update_idletasks()
        progresso_copia["value"] += 5

        time.sleep(1)


def action():
    print("Teste")
    pass


class MainGui:
    def __init__(self, master):
        icon = PhotoImage(Image.open("./assets/icon.png"))
        self.master = master

        self.master.title("Backup")
        self.master.geometry("650x150")
        self.master.resizable(False, False)
        # master.iconphoto(False, icon)
        self.master.rowconfigure(4, minsize=300, weight=1)
        self.master.columnconfigure(3, minsize=500, weight=1)
        image = Image.open("assets/icon.ico")
        menu = (
            item("Restaurar janela", lambda: self.restaura_janela()),
            item("Quit", lambda: self.fecha_janela()),
        )
        self.icon_tray = pystray.Icon("name", image, "Backup de Arquivos", menu)
        self._create_frame()

    def _create_frame(self):
        self.frame = Frame(self.master)
        self.label_origem = Label(
            text="Digite o caminho de origem:",
            master=self.frame,
        )
        self.label_origem.grid(row=0, column=0, padx=5, pady=5)

        self.caminho_origem = Entry(width=70, master=self.frame)
        self.caminho_origem.grid(row=0, column=1, padx=5, pady=5)

        self.label_destino = Label(
            text="Digite o caminho de origem:",
            master=self.frame,
        )
        self.label_destino.grid(row=1, column=0, padx=5, pady=5)

        self.caminho_destino = Entry(width=70, master=self.frame)
        self.caminho_destino.grid(row=1, column=1, padx=5, pady=5)

        self.realizar_button = Button(
            self.frame,
            text="Realizar Copia de Arquivos",
            command=lambda: copia_pastas(
                self.caminho_origem.get(),
                self.caminho_destino.get(),
                step(self.master, self.progresso_copia),
            ),
            height=1,
            width=50,
        )
        self.realizar_button.grid(row=2, column=1, padx=5, pady=5)

        self.minimiza_bandeja = Button(
            self.frame,
            text="Minimizar para a bandeja",
            command=lambda: self.minimiza_bandeja_funcao(),
            height=1,
            width=20,
        )
        self.minimiza_bandeja.grid(row=2, column=0, padx=5, pady=5)

        self.progresso_copia = Progressbar(
            master=self.frame, orient="horizontal", length=300, mode="indeterminate"
        )
        self.progresso_copia.grid(row=3, column=1, padx=5, pady=5)

        self.frame.pack()
        return self.frame

    def minimiza_bandeja_funcao(self):
        self.master.withdraw()
        self.frame.destroy()
        self.icon_tray.run()

    def restaura_janela(self):
        self._create_frame()
        self.master.iconify()
        self.master.withdraw()
        self.master.update()

    def fecha_janela(self):
        self.master.deiconify()
        self.icon_tray.visible = False
        self.icon_tray.stop()
        self.master.destroy()


root = Tk()
gui = MainGui(root)
root.mainloop()
