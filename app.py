from time import sleep
import resources.scripts.auth as at
import resources.scripts.tools as tool
import os

os.system('cls')  # Limpar terminal
while True:
    print('-- Bem vindo ao banco 24h --')
    id = at.realizar_login()    # Digitar usuario e senha
    auth = at.autenticar_usuario(id)    # Autenticar usuário
    if auth[0] != 0:  # Login bem sucedido
        user = id['user_name']
        tool.open_menu("Menu_Principal")
        tool.menu_principal(user)

    else:   # Login mal sucedido
        print('Tente novamente..')
        sleep(4)
        os.system('cls')
