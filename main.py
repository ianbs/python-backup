import shutil
import pathlib
from datetime import date
#import logging

DATA_ATUAL = date.today()


def copia_pastas(pasta_origem: str, pasta_destino: str) -> bool:
    try:
        pasta_origem = pathlib.Path(pasta_origem).absolute()
        pasta_destino = pathlib.Path(
            pasta_destino + '-' + str(DATA_ATUAL)).absolute()
        shutil.copytree(pasta_origem, pasta_destino,
                        symlinks=True)
    except OSError:
        raise OSError.strerror


pasta_origem = str(
    input("Digite o caminho do diretorio de ORIGEM:"))
pasta_destino = str(input("Digite o caminho do diretorio de DESTINO:"))

if copia_pastas(pasta_origem, pasta_destino):
    print("Arquivos Copiados")
else:
    print("Erros")
