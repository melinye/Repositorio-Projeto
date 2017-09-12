import csv
import time
import os


'''listas variáveis'''
patente = []
Lista_nomes_femininos = []
Lista_nomes_masculinos = []
lista_coisas = []
lista_caracteristicas = []
descricao_cidade = []
nome_bandido = []  #escolher entre um nome masculino e feminino para ser o nome do bandido
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
lugar1 = []
lugar2 = []
lugar3 = []
save = []
cidade_atual = []


Dificuldade_atual = 0
chances = 5
nome_jogador = ''
cidades_visitadas = 0
bandidos_capturados = 0
patente_atual = ''
tempo_total = 0



'''---------------------------------COMANDOS CSV-----------------------------------------------------------------'''

'''comando para abrir arquivos csv '''

''' csv nomes femininos '''
with open('arquivo CSV/nomesfemininos.csv', 'r',  encoding='ISO-8859-1') as nomes_f:
    nomes_f_dois= csv.reader(nomes_f)
    for linha in nomes_f_dois:
        try:
            Lista_nomes_femininos.append(linha[0])
        except IndexError:
            continue

'''csv nomes masculinos'''
with open('arquivo CSV/nomesmasculinos.csv', 'r',  encoding='ISO-8859-1') as nomes_m:
    nomes_m_dois = csv.reader(nomes_m)
    for linha in nomes_m_dois:
        try:
            Lista_nomes_masculinos.append(linha[0])
        except IndexError:
            continue


'''csv caracteristicas do bandido'''
with open('arquivo CSV/caracteristicas.csv', 'r',  encoding='ISO-8859-1') as carac_te:
    caracte_2 = csv.reader(carac_te)
    for linha in caracte_2:
        try:
            lista_caracteristicas.append(linha[0])
        except IndexError:
            continue


'''csv lugares'''
with open('arquivo CSV/lugares.csv', 'r', encoding='ISO-8859-1') as lugares_1:
    lugares_2 = csv.reader(lugares_1)
    for linha in lugares_2:
        try:
            lista_visita.append(linha[0])
        except IndexError:
            continue

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
    os.system('cls')
    return resposta

def Abrir_Menu_Inicio():
    A = Menu()
    if A == 1:
        print('-------------NOVO JOGO----------')
        Nome_jogador_Função()
        Nova_fase(Tempo) #chama a funçao de nova fase
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
    print('Digite o seu NOME: ', end=" ")
    nome = input()
    nome_jogador = nome
    os.system('cls')

def Nova_fase(T):
    '''função para iniciar uma fase'''
    '''primeiro vem a introdução ao objetivo'''
    #T = tempo
    print('Sua Patente:', patente)
    print('Seu Objetivo: Encontrar e capturar o bandido', nome_bandido)
    print('O que foi roubado:', item_roubado)
    print('Cidade onde ocorreu o crime: ', cidade_inicial)
    print()
    print('Voce tem', chances,'chances e', T,'horas')
    print()
    print('Digite 1 para Continuar, 2 para voltar ao MENU e 3 para SAIR')
    print('Resposta: ', end="") #colorir
    A = int(input())
    if A == 1:
        print('a')
    elif A == 2:
        os.system('cls')
        Menu()
    elif A == 3:
        Sair_jogo()
    else:
        print('Numero incorreto, tente novamente.')
        A = int(input())

def dificuldade_fase():
    '''dificuldade de cada "fase" '''
    global  caracteristicas_necessarias, de_lugar_a_lugar, nome_bandido, sexo_bandido

    if dificuldade == 0:
        de_lugar_a_lugar = 2
        caracteristicas_necessarias = 3
        return de_lugar_a_lugar, caracteristicas_necessarias
    elif dificuldade == 1:
        de_lugar_a_lugar = 3
        caracteristicas_necessarias = 3
        return de_lugar_a_lugar, caracteristicas_necessarias
    elif dificuldade == 2:
        de_lugar_a_lugar = 4
        caracteristicas_necessarias = 4
        return de_lugar_a_lugar, caracteristicas_necessarias
    elif dificuldade == 3:
        de_lugar_a_lugar = 4
        caracteristicas_necessarias = 4
        return de_lugar_a_lugar, caracteristicas_necessarias
    elif dificuldade == 4:
        de_lugar_a_lugar = 5
        caracteristicas_necessarias = 4
        return de_lugar_a_lugar, caracteristicas_necessarias
    elif dificuldade == 5:
        de_lugar_a_lugar = 4
        caracteristicas_necessarias = 5
        return de_lugar_a_lugar, caracteristicas_necessarias
    if dificuldade_fase() == 6:
        de_lugar_a_lugar = 5
        caracteristicas_necessarias = 5
        sexo_bandido = 'Feminino'
        nome_bandido = "Carmen Sandiego"
        return de_lugar_a_lugar, caracteristicas_necessarias, sexo_bandido, nome_bandido


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
        os.system('cls')
        Menu()
    elif resposta == 2:
        variavel = '' #variavel pra inserir o retorno
        return variavel


def Fase_Atual(tempo, dificuldade):
    #função para exibir as informações da fase em que vc está
    print('Cidade: ', cidade_inicial)
    print()
    print(descricao_cidade)
    print()
    print('Lugares visitáveis:', lugar1, '       ', lugar2, '       ', lugar3)
    print('Para visitar o', lugar1, 'digite 1', '   ', 'Para  visitar o', lugar2, 'digite 2', '   ', 'Para visitar o', lugar3, 'digite 3')
    print()
    print('Para acessar o mandado, Digite X')
    print('Você tem', tempo, 'horas')
    print('Voce tem', chances, 'chances')
    print('Resposta: ', end= '')
    lugar = int(input())
    de_lugar_a_lugar = 0
    if dificuldade == 0:
        de_lugar_a_lugar = 2
    elif dificuldade == 1:
        de_lugar_a_lugar = 3
    elif dificuldade == 2:
        de_lugar_a_lugar = 4
    elif dificuldade == 3:
        de_lugar_a_lugar = 4
    elif dificuldade == 4:
        de_lugar_a_lugar = 5
    elif dificuldade == 5:
        de_lugar_a_lugar = 4
    if dificuldade_fase() == 6:
        de_lugar_a_lugar = 5
    if lugar == 1:
        tempo = tempo - de_lugar_a_lugar
        print(dica_1)
        print('Para voltar digite X')
        voltar = input()
        if voltar == 'X' or voltar == 'x':
            os.system('cls')
            Fase_Atual(tempo, dificuldade)
    elif lugar == 2:
        tempo = tempo - de_lugar_a_lugar
        print(dica_2)
        print('Para voltar digite X')
        voltar = input()
        if voltar == 'X' or voltar == 'x':
            os.system('cls')
            Fase_Atual(tempo, dificuldade)
    elif lugar == 3:
        tempo = tempo - de_lugar_a_lugar
        print(dica_3)
        print('Para voltar digite X')
        voltar = input()
        if voltar == 'X' or voltar == 'x':
            os.system('cls')
            Fase_Atual(tempo, dificuldade)
    elif lugar == 'X' or lugar == 'x':
        os.system('cls')
        mandado()
    else:
        print('Numero Invalido, Digite Y para Retornar')
        voltar = input()
        if voltar == 'y' or voltar == 'Y':
            os.system('cls')
            Fase_Atual(tempo, dificuldade)









