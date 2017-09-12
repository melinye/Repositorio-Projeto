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


sair = ''
Dificuldade_atual = 0
chances = 5
nome_jogador = ''
cidades_visitadas = 1
bandidos_capturados = 0
patente_atual = ''
tempo_total = 0
caracteristicas_necessárias = 0
num_caract_atual = 0 #numero de caracteristicas corretas do mandado
de_lugar_a_lugar = 0 #tempo para se deslocar dentro da cidade
sexo_mandado = '' #os _mandado, vao receber o que for digitado no mandado
hobby_mandado = ''
caracteristica_mandado = ''
automóvel_mandado = ''
cabelo_mandado = ''
tesouro = '' #o que foi roubado do csv
cidade_atual = '' #recebe a cidade do csv ou a cidade de escolha
descricao_cidade = '' #recebe a descrição da cidade pelo csv
lugar1 = '' #lugares que se pode visitar na cidade recebido randomicaemente da lista
lugar2 = ''
lugar3 = ''
nome_bandido ='' #nome recebido randomicamente da lista
destino1 = '' #locais para onde se vai viajar
destino2 = ''
destino3 = ''
distancia1 = 0 #tempo da viagem
distancia2 = 0
distancia3 = 0
sexo_real = '' #recebe o sexo do csv
auto_real = '' #recebe o automovel do csv
caracter_real = '' #recebe a característica do csv
hobby_real = '' #recebe o hobby do csv
cabelo_real = '' #recebe o cabelo do csv



'''---------------------------------COMANDOS CSV-----------------------------------------------------------------'''

'''comando para abrir arquivos csv '''

''' csv nomes femininos '''
with open('nomesfemininos.csv', 'r',  encoding='ISO-8859-1') as nomes_f:
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
    if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4:
        return resposta
    else:
        print('Valor inválido, tente novamente')
        os.system('cls')
        Menu()


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
    os.system('cls')

def Nova_fase():
    global patente_atual, nome_bandido, tesouro, cidade_atual, chances, tempo_total
    #função para iniciar uma fase
    #primeiro vem a introdução ao objetivo
    dificuldade_fase()
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
        os.system('cls')
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
    global patente_atual, tempo_total, de_lugar_a_lugar, Dificuldade_atual, caracteristicas_necessárias
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
    quit()

def Sair_jogo():
    global sair
    print('Você já vai sair? :( Tem certeza? Você vai perder seu progresso da busca atual!')
    print('Para SAIR digite 1. Para FICAR digite 2.')
    print('Resposta: ', end='') #colorir
    resposta = int(input())
    if resposta == 1:
        sair = 'sim'
        Salvar_Jogo()
    elif resposta == 2:
        variavel = '' #variavel pra inserir o retorno
        return variavel


def Fase_Atual():
    #função para exibir as informações da fase em que vc está
    global tempo_total, Dificuldade_atual, cidade_atual, destino1, destino2, destino3, distancia1, distancia2, distancia3, descricao_cidade, cidades_visitadas
    print('Cidade: ', cidade_atual)
    print()
    print(descricao_cidade)
    print()
    print('Para INVESTIGAR os lugares, digite 2')
    print('Para VIAJAR, digite 1')
    print('Para acessar o MANDATO, Digite 3')
    print('Você tem', tempo_total, 'horas')
    print('Voce tem', chances, 'chances')
    print('Resposta: ', end= '')
    resposta = input()
    if resposta == 1:
        print('Cidades para qual pode viajar: ')
        print(destino1, '   ,digite 1')
        print(destino2, '   ,digite 2')
        print(destino3, '   ,digite 3')
        print('Para VOLTAR, digite 4')
        print()
        print('Resposta: ', end= '')
        answer = int(input())
        cont = 0
        while cont == 0:
            if answer == 1:
                cidades_visitadas += 1
                cidade_atual = destino1
                tempo_total = tempo_total - distancia1
                descricao_cidade = descricao_da_cidade[0]
                cont += 1
                os.system('cls')
                Fase_Atual()
            elif answer == 2:
                cidades_visitadas += 1
                cidade_atual = destino2
                tempo_total = tempo_total - distancia2
                descricao_cidade = descricao_da_cidade[0]
                os.system('cls')
                cont += 1
                Fase_Atual()
            elif answer == 1:
                cidades_visitadas += 1
                cidade_atual = destino3
                tempo_total = tempo_total - distancia3
                descricao_cidade = descricao_da_cidade[0]
                cont += 1
                os.system('cls')
                Fase_Atual()
            elif answer == 4:
                os.system('cls')
                cont +=1
                Fase_Atual()
            else:
                print('Número incorreto, tente novamente!')
                print('Resposta: ', end='')
                answer = int(input())
    if resposta == 2:
        print('Lugares visitáveis: ', lugar1, '       ', lugar2, '       ', lugar3)
        print('Para visitar o', lugar1, 'digite 1', '   ', 'Para  visitar o', lugar2, 'digite 2', '   ', 'Para visitar o', lugar3, 'digite 3')
        lugar = int(input())
        dificuldade = Dificuldade_atual
        cont = 0
        while cont == 0:
            if lugar == 1:
                cont += 1
                tempo_total = tempo_total - de_lugar_a_lugar
                print(dica_1)
                print('Para voltar digite X')
                voltar = input()
                if voltar == 'X' or voltar == 'x':
                    os.system('cls')
                    Fase_Atual()
            elif lugar == 2:
                cont += 1
                tempo_total = tempo_total - de_lugar_a_lugar
                print(dica_2)
                print('Para voltar digite X')
                voltar = input()
                if voltar == 'X' or voltar == 'x':
                    os.system('cls')
                    Fase_Atual()
            elif lugar == 3:
                cont += 1
                tempo_total = tempo_total - de_lugar_a_lugar
                print(dica_3)
                print('Para voltar digite X')
                voltar = input()
                if voltar == 'X' or voltar == 'x':
                    os.system('cls')
                    Fase_Atual()
            else:
                print('Numero Invalido, Tente novamente!')
                print('Resposta: ', end= '')
                lugar = input()
    elif resposta == 3:
        os.system('cls')
        mandado()
    else:
        print('Número Inválido, tente novamente!')
        os.system('cls')
        Fase_Atual()

def mandado():
    global sexo_mandado, cabelo_mandado, hobby_mandado, automóvel_mandado, caracteristica_mandado, num_caract_atual
    print('Mandado:')
    print()
    print('São necessárias', caracteristicas_necessárias, 'características corretas para emitir o mandado.')
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
        print('Para voltar digite Y.')
        print('Resposta: ', end='')
        sexo = input()
        if sexo == 'y' or sexo == 'Y':
            os.system('cls')
            mandado()
        else:
            sexo_mandado = sexo
            num_caract_atual += 1
            os.system('cls')
            mandado()
    elif resposta == 'C' or resposta == 'c':
        print('Qual a cor do cabelo do bandido? ', end='')
        print('Para voltar digite Y.')
        print('Resposta: ', end='')
        cabelo = input()
        if cabelo == 'y' or cabelo == 'Y':
            os.system('cls')
            mandado()
        else:
            cabelo_mandado = cabelo
            num_caract_atual += 1
            os.system('cls')
            mandado()
    elif resposta == 'H' or resposta == 'h':
        print('Qual o hobby do bandido?' , end='')
        print('Para voltar digite Y.')
        print('Resposta: ', end='')
        hobby = input()
        if hobby == 'y' or hobby == 'Y':
            os.system('cls')
            mandado()
        else:
            hobby_mandado = hobby
            num_caract_atual += 1
            os.system('cls')
            mandado()
    elif resposta == 'A' or resposta == 'a':
        print('Qual o automóvel do bandido?', end='')
        print('Para voltar digite Y.')
        print('Resposta: ', end='')
        auto = input()
        if auto == 'y' or auto == 'Y':
            os.system('cls')
            mandado()
        else:
            automóvel_mandado = auto
            num_caract_atual += 1
            os.system('cls')
            mandado()
    elif resposta == 'W' or resposta == 'w':
        print('Qual a característica do bandido?', end='')
        print('Para voltar digite Y.')
        print('Resposta: ', end='')
        caract = input()
        if caract == 'y' or caract == 'Y':
            os.system('cls')
            mandado()
        else:
            caracteristica_mandado = caract
            num_caract_atual += 1
            os.system('cls')
            mandado()
    elif resposta == 'Y' or resposta == 'y':
        os.system('cls')
        Fase_Atual()
    else:
        print('Letra invalida, tente novamente!')
        os.system('cls')
        mandado()
    verificar_mandado()

def verificar_mandado():
    global sexo_mandado, num_caract_atual, sexo_real, cabelo_real, caracter_real, hobby_real, auto_real
    num_caract_atual = 0
    if sexo_mandado == sexo_real:
        num_caract_atual += 1
    elif cabelo_mandado == cabelo_real:
        num_caract_atual += 1
    elif caracteristica_mandado == caracter_real:
        num_caract_atual += 1
    elif hobby_mandado == hobby_real:
        num_caract_atual += 1
    elif automóvel_mandado == auto_real:
        num_caract_atual += 1

