# To Do List App - Projeto Extensionista III

def exibir_menu():
    print("=== MENU DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("Função de adicionar tarefa em desenvolvimento...")
        elif opcao == "2":
            print("Função de ver tarefas em desenvolvimento...")
        elif opcao == "3":
            print("Encerrando o aplicativo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()