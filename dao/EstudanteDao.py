import json
from random import random


filename = "data.json"


def loadFile() -> list:
    """Retorna uma lista de estudantes"""
    file = open(filename, "r", encoding='utf-8')
    data = file.read()
    return json.loads(data)


def saveFile(data: list):
    """Salva a lista de estudantes"""
    file = open(filename, "w+", encoding='utf-8')
    data = json.dumps(data)
    file.write(data)
    file.close()


def adicionar(estudante: dict) -> dict:
    data = loadFile()
    estudante['id'] = int(round(random() * 10000, 0))
    data.append(estudante)
    saveFile(data)

    return estudante


def editar(estudante: dict) -> None:
    data = loadFile()

    for e in data:
        if e['id'] == int(estudante['id']):
            data.remove(e)
            estudante['id'] = int(estudante['id'])
            data.append(estudante)
            break

    saveFile(data)


def deletar(id: int) -> None:
    data = loadFile()
    for e in data:
        if e['id'] == id:
            data.remove(e)
            break
    saveFile(data)


def selecionar(id: int) -> dict:
    data = loadFile()
    for e in data:
        if e['id'] == id:
            return e
    return None


def selecionarTodos() -> list:
    return loadFile()
