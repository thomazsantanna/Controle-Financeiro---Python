# caixa.py

def adicionar_movimentacao(lista, tipo, descricao, valor):
    movimentacao = {
        "Tipo": tipo,
        "Descrição": descricao,
        "Valor": valor
    }

    lista.append(movimentacao)


def calcular_saldo(lista):
    saldo = 0

    for mov in lista:
        if mov["Tipo"] == "Entrada":
            saldo += mov["Valor"]
        else:
            saldo -= mov["Valor"]

    return saldo