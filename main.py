import shutil
import os
from datetime import date

data_atual = date.today()


def copia_pastas(pasta_origem, pasta_destino):
    pasta_origem = pasta_origem.replace("\\", "/")
    pasta_destino = pasta_destino.replace("\\", "/")+"-"+str(data_atual)
    shutil.copytree(pasta_origem, pasta_destino, symlinks=True)
    return True


pasta_origem = str(
    input("Digite o caminho do diretorio de ORIGEM:").replace("\\", "/"))
pasta_destino = str(pasta_origem.replace("\\", "/")+"-"+str(data_atual))

if copia_pastas(pasta_origem, pasta_destino):
    print("Arquivos Copiados")
else:
    print("Erros")
