# ----------------------- LISTA -----------------------
lista = []

# 1. Adicionar aluno
def add_aluno():
    print("\n--- ADICIONAR ALUNO ---")
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    nota = float(input('Digite a nota do aluno: '))
    aluno = {'Nome': nome, 'Idade': idade, 'Nota': nota}
    lista.append(aluno)
    print('\nAluno adicionado com sucesso!\n')

# 2. Listar alunos
def listar_alunos():
    print('\n------ LISTA DE ALUNOS ------\n')
    if not lista:
        print('Nenhum aluno na lista!\n')
    else:
        for aluno in lista:
            print(f"Nome: {aluno['Nome']}\nIdade: {aluno['Idade']}\nNota: {aluno['Nota']}\n")

# 3. Remover aluno
def remover_aluno():
    print("\n--- REMOVER ALUNO ---")
    aluno_removido = input('Digite qual aluno quer remover da lista: ')
    for aluno in lista:
        if aluno['Nome'] == aluno_removido:
            lista.remove(aluno)
            print('\nAluno removido com sucesso!\n')
            return
    print('\nAluno não encontrado na lista!\n')

# 4. Mostrar média geral
def mostrar_media():
    print("\n--- MÉDIA GERAL DAS NOTAS ---")
    if not lista:
        print('\nNenhum aluno na lista!\n')
    else:
        soma = 0
        for aluno in lista:
            soma += aluno['Nota']
        media = soma / len(lista)
        print(f'\nO valor da média de todos os alunos é: {media:.2f}\n')


# 5. Atualizar aluno
def atualizar_aluno():
    print("\n--- ATUALIZAR ALUNO ---")
    nome_aluno = input("Digite o nome do aluno que deseja atualizar: ")
    
    for aluno in lista:
        if aluno['Nome'] == nome_aluno:
            print(f"\nAluno encontrado: Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Nota: {aluno['Nota']}")
            
            # Pergunta o que atualizar
            novo_nome = input("Digite o novo nome (ou pressione Enter para manter): ")
            if novo_nome.strip() != "":
                aluno['Nome'] = novo_nome
            
            nova_idade = input("Digite a nova idade (ou pressione Enter para manter): ")
            if nova_idade.strip() != "":
                aluno['Idade'] = int(nova_idade)
            
            nova_nota = input("Digite a nova nota (ou pressione Enter para manter): ")
            if nova_nota.strip() != "":
                aluno['Nota'] = float(nova_nota)
            
            print("\nAluno atualizado com sucesso!\n")
            return
    
    print("\nAluno não encontrado na lista!\n")

# ----------------------- MENU -----------------------
while True:
    print('\n---------- MENU ----------')
    print('1 - ADICIONAR ALUNO')
    print('2 - LISTAR ALUNOS')
    print('3 - REMOVER ALUNO')
    print('4 - MOSTRAR MÉDIA GERAL DAS NOTAS')
    print('5 - ATUALIZAR ALUNO')
    print('6 - SAIR')

    escolha = input('Escolha uma opção: ')

    match escolha:
        case '1':
            add_aluno()
        case '2':
            listar_alunos()
        case '3':
            remover_aluno()
        case '4':
            mostrar_media()
        case '5':
            atualizar_aluno()
        case 6:
            print('\nVocê saiu do programa!\n')
            break
        case _:
            print('\nOpção inválida!\n')
