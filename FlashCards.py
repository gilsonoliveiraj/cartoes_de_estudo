import csv
import random
import os

# Função que lê um arquivo CSV e retorna uma lista com as informações contidas nele
def read_csv(file_name):
    # Abre o arquivo CSV com a codificação 'utf-8' e armazena o conteúdo em uma variável
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]  # Pula a primeira linha (cabeçalho) e armazena o restante em uma lista
        reader = csv.reader(lines)  # Instância um objeto reader para ler o conteúdo das linhas
        return list(reader)  # Transforma o objeto reader em uma lista e retorna

# Função que limpa a tela do terminal
def limpar_tela(): 
    # Verifica o sistema operacional em uso e executa o comando de limpeza de tela adequado
    os.system('clear' if os.name == 'posix' else 'cls')

# Função que apresenta ao usuário as categorias disponíveis e retorna a categoria selecionada
def menu_inicio(category_dict):
    limpar_tela()  # Limpa a tela do terminal
    print("Bem-vindo estudante!\nEsse é o nosso Programa de perguntas e respostas para fixar seu conhecimento")
    print("Temos essas Categorias de Estudo disponíveis:")
    # Loop para exibir as categorias disponíveis
    for i, category in category_dict.items():
        print(f"{i}: {category}")
    user_input = input("Escolha uma categoria pelo número: ")  # Recebe a categoria selecionada pelo usuário
    selected_category = category_dict.get(int(user_input))  # Obtém a categoria pelo número selecionado

    # Verifica se a categoria selecionada existe na lista de categorias disponíveis
    if selected_category is None:
        print("Categoria inválida. Tente novamente.")
        return  # Retorna None para indicar que a categoria não é válida

    return selected_category  # Retorna a categoria selecionada

def question_loop(selected_category, questions_answers):
    # Inicializa uma variável de controle 'running' para determinar se o loop de perguntas deve continuar ou não.
    running = True
    # Enquanto a variável 'running' for verdadeira, o loop de perguntas continuará.
    while running:
        # Seleciona uma pergunta aleatória da categoria selecionada.
        question = random.choice([qa for qa in questions_answers if qa[2] == selected_category])
        # Limpa a tela.
        limpar_tela()
        # Exibe a categoria e a pergunta.
        print("Categoria:",selected_category,"\n\nResponda: ",question[0])
        # Aguarda o usuário pressionar qualquer tecla para ver a resposta.
        input("Pressione qualquer tecla para ver a resposta")
        # Exibe a resposta.
        print("Resposta: " + question[1])
        # Pergunta ao usuário se deseja ver outra pergunta aleatória.
        user_input = input("Deseja ver outra pergunta aleatória? (s/n) ")
        # Se a resposta for 'n', a variável 'running' é definida como falsa e o loop de perguntas é encerrado.
        if user_input.lower() == 'n':
            running = False

def main():
    # Carrega as perguntas e respostas a partir de um arquivo CSV
    questions_answers = read_csv('perguntas_respostas.csv')

    # Cria uma lista de categorias únicas a partir das perguntas e respostas carregadas
    categories = set(qa[2] for qa in questions_answers)

    # Cria um dicionário que associa um número inteiro a cada categoria
    category_dict = {i+1: category for i, category in enumerate(categories)}

    # Loop principal do programa
    running = True
    while running:
        # Limpa a tela antes de exibir o menu inicial
        os.system('clear' if os.name == 'posix' else 'cls')

        # Exibe o menu inicial e obtém a categoria selecionada pelo usuário
        selected_category = menu_inicio(category_dict)

        # Se o usuário selecionou uma categoria, entra no loop de perguntas e respostas
        if selected_category is not None:
            question_loop(selected_category, questions_answers)

        # Pergunta ao usuário se ele deseja escolher outra categoria
        user_input = input("Deseja escolher outra categoria? (s/n) ")
        if user_input.lower() == 'n':
            # Se o usuário não deseja escolher outra categoria, sai do loop principal
            running = False

    

if __name__ == '__main__':
    main()
