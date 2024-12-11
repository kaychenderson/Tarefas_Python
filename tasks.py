class Tarefa:
    def __init__(self, descricao, status="Pendente"):
        self.descricao = descricao
        self.status = status

    def marcar_concluida(self):
        self.status = "Concluída"

    def editar_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    def __str__(self):
        return f"[{'X' if self.status == 'Concluída' else ' '}] {self.descricao}"


def carregar_tarefas(nome_arquivo):
    tarefas = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                if "|" in linha:
                    descricao, status = linha.strip().split("|", maxsplit=1)
                    tarefas.append(Tarefa(descricao, status))
    except FileNotFoundError:
        pass  # Se o arquivo não existir, retornamos uma lista vazia.
    return tarefas


def salvar_tarefas(nome_arquivo, tarefas):
    with open(nome_arquivo, "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa.descricao}|{tarefa.status}\n")


def exibir_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa disponível.")
        return False
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")
    return True


def adicionar_tarefa(tarefas, nome_arquivo):
    descricao = input("Digite a descrição da tarefa: ").strip()
    tarefas.append(Tarefa(descricao))
    salvar_tarefas(nome_arquivo, tarefas)
    print("Tarefa adicionada com sucesso!")


def editar_tarefa(tarefas, nome_arquivo):
    if exibir_tarefas(tarefas):
        try:
            indice = int(input("Digite o número da tarefa que deseja editar: ")) - 1
            if 0 <= indice < len(tarefas):
                nova_descricao = input("Digite a nova descrição: ").strip()
                tarefas[indice].editar_descricao(nova_descricao)
                salvar_tarefas(nome_arquivo, tarefas)
                print("Tarefa editada com sucesso!")
            else:
                print("Tarefa inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")


def concluir_tarefa(tarefas, nome_arquivo):
    if exibir_tarefas(tarefas):
        try:
            indice = int(input("Digite o número da tarefa que deseja marcar como concluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice].marcar_concluida()
                salvar_tarefas(nome_arquivo, tarefas)
                print("Tarefa marcada como concluída!")
            else:
                print("Tarefa inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")


def excluir_tarefa(tarefas, nome_arquivo):
    if exibir_tarefas(tarefas):
        try:
            indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                salvar_tarefas(nome_arquivo, tarefas)
                print("Tarefa excluída com sucesso!")
            else:
                print("Tarefa inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")


def menu():
    nome_arquivo = "tarefas.txt"
    tarefas = carregar_tarefas(nome_arquivo)

    while True:
        print("\n--- Sistema de Gestão de Tarefas ---")
        print("1. Exibir tarefas")
        print("2. Adicionar tarefa")
        print("3. Editar tarefa")
        print("4. Concluir tarefa")
        print("5. Excluir tarefa")
        print("6. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas, nome_arquivo)
        elif opcao == "3":
            editar_tarefa(tarefas, nome_arquivo)
        elif opcao == "4":
            concluir_tarefa(tarefas, nome_arquivo)
        elif opcao == "5":
            excluir_tarefa(tarefas, nome_arquivo)
        elif opcao == "6":
            salvar_tarefas(nome_arquivo, tarefas)
            print("Tarefas salvas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
