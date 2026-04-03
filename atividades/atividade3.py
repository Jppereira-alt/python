import os

restaurantes = []
ativados = []
desativados = []

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def tabela(): 
    print('[1] Cadastrar restaurante ')
    print('[2] Listar restaurante ')
    print('[3] Ativar restaurante ')
    print('[4] Desativar restaurantes')
    print('[5] Remover restaurante ')
    print('[6] Sair\n')

def finalizar_app(): #caso para limpar o terminal
    os.system('cls')
    print('finalizando app...\n')

def opcao_invalida(): #funçao que entrega a opçao invalida
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal: ') 
    main()

def cadastrar_restaurante(): #cadastro do restaurante
    os.system('cls')
    print('vamos iniciar o cadastro')
    nome_restaurante = input('digite seu nome do Restaurante: ').lower()

    restaurantes.append(nome_restaurante)
    print (f'RESTAURANTE {nome_restaurante} FOI CADASTRADO COM SUCESSO!')

    input('Digite uma tecla para voltar ao Menu: ')
    main()

def listar_restaurantes():
    print (f"""esses são todos os restaurantes listados\n""")
    for item in restaurantes:
        print('-' + item)
    
    input('Digite uma tecla para voltar ao Menu: ')
    main()

def remover_restaurante():
    nome = input("Qual remover? ").lower()

    if nome in restaurantes:
        restaurantes.remove(nome)
        print("Removido!")
    else:
        print("Não encontrado!")

    input('Digite uma tecla para voltar ao Menu: ')
    main()

def ativar_restaurante():
    os.system("cls")
    print('Esses são os restaurantes para ativar: \n')
    for item in ativados:
        print('-' + item)
    nome = input('\nQual Restaurante voce deseja ativar?\n')
    
    if nome in ativados:
        print('restaurante ativado')
    else:
        print('não encontrado')
    input('Digite uma tecla para voltar ao Menu: ')
    main()

def desativar_restaurantes():
    os.system("cls")
    print('Esses são os restaurantes ativados: \n')
    for item in ativados:
        print('-' + item)
    nome = input('\nQual Restaurante voce deseja ativar?\n')
    
    if nome in ativados:
        print('restaurante ativado')
    else:
        print('não encontrado')
    input('Digite uma tecla para voltar ao Menu: ')
    main()

def escolher_opção():
    try: # usado como "tente(try) isso, se nao der certo use opçao invalida" (except), entendeu?
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:  
            ativar_restaurante()
            
        elif opcao_escolhida == 4:
            desativar_restaurantes()

        elif opcao_escolhida == 5:
            remover_restaurante()
             #caso em que o app finaliza
        elif  opcao_escolhida == 6:
            finalizar_app() 
        else:
            opcao_invalida #caso em que nao for um dos 4 numeros ele entrega opçao invalida
    except:
        opcao_invalida() # caso em que ele escreve uma letra ele entrega opçao invalida
        
def main(): #funçao principal que é entregue tudo
    os.system('cls')
    exibir_nome_do_programa()
    print ('Cadastre o restaurantes antes de ativa-lo ou desativa-lo \n')
    tabela()
    escolher_opção()

if __name__ == '__main__':
    main() #nao entendi muito bem essa parte

    #usar bastante import OS