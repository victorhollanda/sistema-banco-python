import os
import json
from time import sleep


def linha(n=40):
    return ('-'*n)


def seInt(text):
    while True:
        n = (input(text))
        if n.isnumeric():
            return int(n)
            break
        else:
            print('Digite apenas numeros!')


def menu(name, list):
    l = (40-(len(name)))/2-1
    print(linha(int(l)), name, linha(int(l)))
    c = 1
    for item in list:
        print(f'[{c}] {item}')
        c += 1
    print(linha())


def open_menu(name):
    os.system('cls')
    with open('resources/json/menus.json') as my_json:
        menus = json.load(my_json)
    menu(name, menus[name])


def menu_saque(user):
    n = seInt('Digite sua opção: ')
    while True:
        if 1 <= n < 3:
            if n == 1:
                conta = 'corrente'
            if n == 2:
                conta = 'poupanca'
            break
        else:
            print('Escolha um numero disponivel!')
            n = seInt('Digite sua opção: ')
    os.system('cls')
    val = seInt('Digite o valor que deseja sacar: ')
    print(f'Sacando R$:{val},00 da conta {conta}...')
    sleep(3)
    print('Saque realizado com sucesso!')
    sleep(3)


def menu_saldo(user):
    n = seInt('Digite sua opção: ')
    while True:
        if 1 <= n < 3:
            if n == 1:
                conta = 'corrente'
            if n == 2:
                conta = 'poupanca'
            break
        else:
            print('Escolha um numero disponivel!')
            n = seInt('Digite sua opção: ')
    os.system('cls')
    with open('resources/json/accounts.json') as my_json:
        account = json.load(my_json)
    saldo = account[user][conta]
    print(f'Seu saldo é de R$:{saldo},00')
    sleep(3)


def menu_principal(user):
    n = seInt('Digite sua opção: ')
    while True:
        if 1 <= n < 5:
            if n == 1:
                open_menu('Saldo')
                menu_saldo(user)
            if n == 2:
                open_menu('Saque')
                menu_saque(user)
            if n == 3:
                open_menu('Deposito')
            if n == 4:
                open_menu('Transferencia')
            break
        else:
            print('Escolha um numero disponivel!')
            n = seInt('Digite sua opção: ')
    retornar(user)


def retornar(user):
    open_menu('retornar')
    r = seInt('Deseja realizar outra consulta?')
    while True:
        if 1 <= r < 3:
            if r == 1:
                open_menu("Menu_Principal")
                menu_principal(user)
            if r == 2:
                print('Obrigado por usar o caixa 24h!')
                sleep(3)
                os.system('cls')
            break
        else:
            print('Escolha um numero disponivel!')
            r = seInt('Digite sua opção: ')
