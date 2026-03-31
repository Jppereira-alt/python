import os


print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

print('[1] Cadastrar restaurante')
print('[2] Listar restaurante')
print('[3] Ativar restaurante')
print('[4] Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('cls')
    print('finalizando app...\n')

if opcao_escolhida == 1:
    print('vamos iniciar o cadastro')
    nome = input('digite seu nome de usuário: ')
    senha = input('digite sua senha: ')
    if nome == 'joao' and senha == 1234:
        print("acesso permitido")
    else:
        print('acesso negado')

elif opcao_escolhida == 2:
    print('listar restaurantes')

elif opcao_escolhida == 3:
    print('ativar restaurantes')

else:
    finalizar_app()

    #usar bastante import OS