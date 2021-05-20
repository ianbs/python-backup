import shutil
import pathlib
import time
import os
import logging
from datetime import date
from tkinter.messagebox import showerror

DATA_ATUAL = date.today()


def _copiar_com_log(src, dst):
    logging.info("Working in %s" % src)
    logging.info("Working in %s" % dst)
    print(f"Copiando: {src} to {dst}")
    shutil.copy2(src, dst)


def copia_pastas(pasta_origem: str, pasta_destino: str, step) -> bool:
    try:
        if not pasta_origem and not pasta_destino:
            return showerror(
                "Falta informação",
                "Preencha os campos do diretorio de origem e de destino.",
            )
        pasta_origem = pathlib.Path(pasta_origem).absolute()
        pasta_destino = pathlib.Path(pasta_destino + "-" + str(DATA_ATUAL)).absolute()
        step
        shutil.copytree(
            pasta_origem, pasta_destino, symlinks=True, copy_function=_copiar_com_log
        )
    except OSError as error:
        showerror(error, error)
        raise OSError.strerror
