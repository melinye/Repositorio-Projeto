import csv
import time
import os


'''listas variáveis'''
patente = []
Lista_nomes_femininos = []
Lista_nomes_masculinos = []
lista_coisas = []
lista_caracteristicas = []
descricao_da_cidade = []
sexo_bandido = []
item_roubado = []
cidade_inicial = []
destino_1 = []
destino_2 = []
destino_3 = []
distancia_tempo_1 = []
distancia_tempo_2 = []
distancia_tempo_3 = []
dica_1 = []
dica_2 = []
dica_3 = []
lugar_1 = []
lugar_2 = []
lugar_3 = []
save = []


Dificuldade_atual = 0
chances = 5
nome_jogador = ''
cidades_visitadas = 0
bandidos_capturados = 0
patente_atual = ''
tempo_total = 0
caracteristicas_necessárias = 0
num_caract_atual = 0
de_lugar_a_lugar = 0
sexo_mandado = ''
hobby_mandado = ''
caracteristica_mandado = ''
automóvel_mandado = ''
cabelo_mandado = ''
tesouro = ''
cidade_atual = ''
descricao_cidade = ''
lugar1 = ''
lugar2 = ''
lugar3 = ''
nome_bandido = ''
'''---------------------------------- FUNÇÕES ----------------------------------------------------------------'''

'''--------------------------------------------------------------------------------------------------'''

def Menu():
    ''' função para abrir a introdução ao jogo'''
    print('              Nome do Jogo: "Onde no mundo está Carmen Sandiego?"') #colorir
    print()
    print('Deseja começar um NOVO JOGO? - R: 1')
    print('Deseja CONTINUAR um jogo? - R: 2')
    print('Deseja ver o RANKING? - R: 3')
    print('Deseja ver as INSTRUÇÕES? - R: 4')
    print('Resposta: ', end="") #colorir
    resposta = int(input())
    os.system('clear')
    return resposta

def Abrir_Menu_Inicio():
    A = Menu()
    if A == 1:
        print('-------------NOVO JOGO----------')
        Nome_jogador_Função()
        Nova_fase() #chama a funçao de nova fase
    elif A == 2:
        print('continuar')
    elif A == 3:
        print('ranking')
    elif A == 4:
        print('O objetivo do jogo é encontrar bandidos da gangue de Carmen Sandiego que cometem crimes por todo o mundo.')
    else:
        print('valor inválido')

def Nome_jogador_Função():
    '''por o nome do jogador e salvar'''
    print('Bem vindo!')
    print('Digite o seu NOME: ', end=" ")
    nome = input()
    nome_jogador = nome
    os.system('clear')

def Nova_fase():
    '''função para iniciar uma fase'''
    '''primeiro vem a introdução ao objetivo'''
    #T = tempo
    print('Sua Patente:', patente_atual)
    print('Seu Objetivo: Encontrar e capturar o bandido', nome_bandido)
    print('O que foi roubado:', tesouro)
    print('Cidade onde ocorreu o crime: ', cidade_atual)
    print()
    print('Voce tem', chances,'chances e', tempo_total,'horas')
    print()
    print('Digite 1 para Continuar, 2 para voltar ao MENU e 3 para SAIR')
    print('Resposta: ', end="") #colorir
    A = int(input())
    if A == 1:
        os.system('clear')
        dificuldade_fase()
        Fase_Atual()
    elif A == 2:
        os.system('cls')
        Menu()
    elif A == 3:
        Sair_jogo()
    else:
        print('Numero incorreto, tente novamente.')
        A = int(input())


def dificuldade_fase():

    if patente_atual == 'Cadete':
        Dificuldade_atual = 1
        carateristicas_necessarias = 3
        de_lugar_a_lugar = 2
        tempo_total = 78
    elif patente_atual == 'Guarda Local':
        Dificuldade_atual = 2
        caracteristicas_necessárias = 3
        de_lugar_a_lugar = 3
        tempo_total = 72
    elif patente_atual == 'Detetive':
        Dificuldade_atual = 3
        caracteristicas_necessárias = 4
        de_lugar_a_lugar = 3
        tempo_total = 65
    elif patente_atual == 'Policial Federal':
        Dificuldade_atual = 4
        caracteristicas_necessárias = 4
        de_lugar_a_lugar = 4
        tempo_total = 60
    elif patente_atual == 'Agente Secreto':
        Dificuldade_atual = 5
        caracteristicas_necessárias = 4
        de_lugar_a_lugar = 4
        tempo_total = 55
    elif patente_atual == 'Inspetor':
        Dificuldade_atual = 6
        caracteristicas_necessárias = 5
        de_lugar_a_lugar = 5
        tempo_total = 50
    elif patente_atual == 'Chefe de Policia':
        Dificuldade_atual = 7
        caracteristicas_necessárias = 5
        sexo_bandido = 'Feminino'
        nome_bandido = 'Carmen Sandiego'
        de_lugar_a_lugar = 5
        tempo_total = 48


def Salvar_Jogo():
    '''função para arquivar as informações de save'''
    save.append(nome_jogador)
    save.append(patente_atual)
    save.append(bandidos_capturados)
    save.append(cidades_visitadas)
    save.append(chances)
    #acrescentar a lista no csv
    print('Jogo salvo! Volte em breve! ^-^')

def Sair_jogo():
    print('Você já vai sair? :( Tem certeza? Você vai perder seu progresso da busca atual!')
    print('Para SAIR digite 1. Para FICAR digite 2.')
    print('Resposta: ', end='') #colorir
    resposta = int(input())
    if resposta == 1:
        Salvar_Jogo()
        #acrescentar um tempo antes de limpar a tela
        os.system('clear')
        Menu()
    elif resposta == 2:
        variavel = '' #variavel pra inserir o retorno
        return variavel


def Fase_Atual():
    #função para exibir as informações da fase em que vc está
    global  tempo_total
    print('Cidade: ', cidade_inicial)
    print()
    print(descricao_cidade)
    print()
    print('Lugares visitáveis:', lugar1, '       ', lugar2, '       ', lugar3)
    print('Para visitar o', lugar1, 'digite 1', '   ', 'Para  visitar o', lugar2, 'digite 2', '   ', 'Para visitar o', lugar3, 'digite 3')
    print()
    print('Para acessar o mandado, Digite 4')
    print('Você tem', tempo_total, 'horas')
    print('Voce tem', chances, 'chances')
    print('Resposta: ', end= '')
    lugar = int(input())
    dificuldade = Dificuldade_atual
    if lugar == 1:
        tempo_total = tempo_total - de_lugar_a_lugar
        print(dica_1)
        print('Para voltar digite X')
        voltar = input()
        if voltar == 'X' or voltar == 'x':
            os.system('clear')
            Fase_Atual()
    elif lugar == 2:
        tempo_total = tempo_total - de_lugar_a_lugar
        print(dica_2)
        print('Para voltar digite X')
        voltar = input()
        if voltar == 'X' or voltar == 'x':
            os.system('clear')
            Fase_Atual()
    elif lugar == 3:
        tempo_total = tempo_total - de_lugar_a_lugar
        print(dica_3)
        print('Para voltar digite X')
        voltar = input()
        if voltar == 'X' or voltar == 'x':
            os.system('clear')
            Fase_Atual()
    elif lugar == 4:
        os.system('clear')
        mandado()
    else:
        print('Numero Invalido, Digite Y para Retornar: ', end='')
        voltar = input()
        if voltar == 'y' or voltar == 'Y':
            os.system('clear')
            Fase_Atual()

def mandado():
    global sexo_mandado, cabelo_mandado, hobby_mandado, automóvel_mandado, caracteristica_mandado
    print('Mandado:')
    print()
    print('Nome do Bandido:', nome_bandido)
    print('Sexo:', sexo_mandado)
    print('Cabelo:', cabelo_mandado)
    print('Hobby:', hobby_mandado)
    print('Automóvel:', automóvel_mandado)
    print('Característica:', caracteristica_mandado)
    print('Para SEXO, digite S. Para CABELO digite C. Para HOBBY digite H.')
    print('Para AUTOMÓVEL, digite A. Para CARACTERÍSTICAS digite W.')
    print()
    print('Para voltar digite Y')
    print('Resposta:', end='')
    resposta = input()
    if resposta == 'S' or resposta == 's':
        print('Qual o sexo do bandido?', end='')
        sexo = input()
        sexo_mandado = sexo
        os.system('clear')
        mandado()
    elif resposta == 'C' or resposta == 'c':
        print('Qual a cor do cabelo do bandido?', end='')
        cabelo = input()
        cabelo_mandado = cabelo
        os.system('clear')
        mandado()
    elif resposta == 'H' or resposta == 'h':
        print('Qual o hobby do bandido?', end='')
        hobby = input()
        hobby_mandado = hobby
        os.system('clear')
        mandado()
    elif resposta == 'A' or resposta == 'a':
        print('Qual o automóvel do bandido?', end='')
        automovel = input()
        automóvel_mandado = automovel
        os.system('clear')
        mandado()
    elif resposta == 'W' or resposta == 'w':
        print('Qual a característica do bandido?', end='')
        caract= input()
        caracteristica_mandado = caract
        os.system('clear')
        mandado()
    elif resposta == 'Y' or resposta == 'y':
        os.system('clear')
        Fase_Atual()
    else:
        print('Letra invalida, tente novamente!')
        os.system('clear')
        mandado()






Abrir_Menu_Inicio()




