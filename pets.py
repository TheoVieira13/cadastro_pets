import os

pets_cadastrados = []

def escolha():
    while True:
        n = input("""1. Cadastrar pet
2. Buscar dados do pet
3. Deletar pet
4. Listar pets
5. Listar pets por criterio
6. Sair
Escolha uma das opções: """)
        
        if n == '1':
            cadastrar_pet()
        elif n == '2':
            buscar_dados()
        elif n == '3':
            deletar_pet()
        elif n == '4':
            listar_pets()
        elif n == '5':
            listar_criterios()
        elif n == '6':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida! Tente novamente.')


def cadastrar_pet():
    os.system('cls')
    nome = input('Qual nome do pet: ')
    sobrenome = input('Qual o sobre nome do Pet: ')
    especie = input('Qual especie ? [G]ato / [C]achorro: ')
    sexo = input('Sexo: [M]acho / [F]emea: ')
    endereco = input('Endereço onde o animal foi encontrado: ')
    idade = input('Idade aproximada do animal: ')
    peso = input('Peso aproximado do animal em Kg: ')
    raca = input('Raça do animal: ')

    novo_pet = {
        'nome' : nome.capitalize(),
        'sobrenome' : sobrenome.capitalize(),
        'especie' : especie.capitalize(),
        'sexo' : sexo.capitalize(),
        'endereço' : endereco.capitalize(),
        'idade' : idade.capitalize(),
        'peso' : peso.capitalize(),
        'raça' : raca.capitalize() 
        } 

    pets_cadastrados.append(novo_pet)
    os.system('cls')
    print(f'Pet {nome} cadastrado com sucesso.')

def encontrar_pet(nome_pet):

    for pet in pets_cadastrados:
        if pet['nome'] == nome_pet.capitalize():
            return pet
    return None

def buscar_dados():
    os.system('cls')
    nome_pet = input('Digite o nome do pet: ').capitalize()
    pet_encontrado = encontrar_pet(nome_pet)

    if pet_encontrado:
        print(f'Dados do pet {nome_pet}: ')
        for chave, valor in pet_encontrado.items():
            print(f'{chave.capitalize()}: {valor}')
    else:
        print(f'O pet com o nome {nome_pet} não foi encontrado. ')

def deletar_pet():
    os.system('cls')
    nome_pet = input('Digite o nome do pet que deseja excluir: ').capitalize()
    pet_encontrado = encontrar_pet(nome_pet)

    if pet_encontrado:
        pets_cadastrados.remove(pet_encontrado)
        os.system('cls')
        print(f'Pet com o nome {nome_pet} foi deletado com seucesso!')
    else:
        print(f'O pet com o nome {nome_pet} não foi encontrado. ')

def listar_pets():
    os.system('cls')

    if not pets_cadastrados:
        print('Nenhum pet cadastrado.')
        return

    print('Lista de pets cadastrados:')
    for pet in pets_cadastrados:
        print(f'Nome: {pet['nome']} | Especie: {pet['especie']} | Sexo: {pet['sexo']}')

def listar_criterios():
    os.system('cls')

    if not pets_cadastrados:
        print('Nenhum pet cadastrado.')
        return

    print("""Listagem de pets por critério:
1. Todos os gatos
2. Todos os cachorros
3. Todos os machos
4. Todas as fêmeas""")
    
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        pets_filtrados = [pet for pet in pets_cadastrados if pet['especie'] == 'Gato']
    elif opcao == '2':
        pets_filtrados = [pet for pet in pets_cadastrados if pet['especie'] == 'Cachorro']
    elif opcao == '3':
        pets_filtrados = [pet for pet in pets_cadastrados if pet['sexo'] == 'Macho']
    elif opcao == '4':
        pets_filtrados = [pet for pet in pets_cadastrados if pet['sexo'] == 'Femea']
    else:
        print('Opção inválida!')
        return

    if pets_filtrados:
        print('Pets encontrados:')
        for pet in pets_filtrados:
            print(f"Nome: {pet['nome']} {pet['sobrenome']} | Sexo: {pet['sexo']} | Idade: {pet['idade']} | Peso: {pet['peso']}Kg | Raça: {pet['raça']} | Endereço: {pet['endereço']}")
    else:
        print('Nenhum pet encontrado com esse critério.')

escolha()
                