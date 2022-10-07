import os
import json


def realizar_login():
    user = input('Digite seu usuário: ')
    os.system('cls')
    print(f'Usuário: {user}')
    password = input('Digite sua senha: ')
    return {'user_name': user, 'password': password}


def autenticar_usuario(id):
    with open('resources/json/accounts.json') as my_json:
        accounts = json.load(my_json)

    if id['user_name'] in accounts:
        if id['user_name'] == accounts[id['user_name']]['user_name'] and id['password'] == accounts[id['user_name']]['password']:
            return (accounts[id['user_name']]['auth'], id['user_name'])
        else:
            print('Usuário e/ou senha incorretos')
            return (0, 0)
    else:
        print('Usuário e/ou senha incorretos')
        return (0, 0)
