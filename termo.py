import random

lista_palavras = ["agil", "bolo", "cabra", "dente", "escar", "fusca", "girar", "haste", "igreja", "janela", "lapis", "musica", "nivel", "oculos", "paz", "quero", "risco", "saldo", "tenis", "uva", "vapor", "waffle", "xerox", "yogur", "zangar", "porta", "gamer", "lasco","parca","lindo","lindas","ilhas","pais","lugar","carne","copo","agua","poste","musgos","latir","guiar","iscas","opera","lenda","manga","ele","porra","osasco","linha","azul","haste","local"]

tentativas = 7# numeros totais de tentativas

amarelo = '\033[33m'
limpo = '\033[m'
verde = '\033[32m'
vermelho = '\033[31m'


palavra_secreta_indice = random.randint(0,len(lista_palavras))
palavra_secreta = lista_palavras[palavra_secreta_indice]
len_palavra_secreta = len(palavra_secreta)

print(f"A palavra possuí {len_palavra_secreta} letras ")


while True:
    certo = []
    errado = []
    posicao_errada = []

    palavra_digitada = input("\n").upper()

    if len(palavra_digitada) > len_palavra_secreta:
        print(f'\nVocê só pode digitar uma palavra com {len_palavra_secreta}')
        continue 
    if (palavra_digitada).upper() == (palavra_secreta.upper()):
        print(f"\nVocê acertou! A palavra era {palavra_secreta}")
        exit()

    lista_digitada = list(palavra_digitada)
    lista_secreta = list(palavra_secreta.upper())

    for i in range(0,len(lista_digitada)):
        for j in range(0, len(lista_secreta)):
            if (lista_digitada[i] == lista_secreta[i]) and (lista_digitada[i] not in posicao_errada) and (lista_digitada[i] not in errado):
                certo.append(lista_digitada[i])
                print( f"{verde}{lista_digitada[i]}{limpo}", end=" ")
                break
            elif (lista_digitada[i] in lista_secreta) and (lista_digitada[i] not in certo)  and (lista_digitada[i] not in errado):
                posicao_errada.append(lista_digitada[i])
                print( f"{amarelo}{lista_digitada[i]}{limpo}", end=" ")
                break
            elif (lista_digitada[i] not in certo) and (lista_digitada[i] not in posicao_errada):
                errado.append(lista_digitada[i])
                print( f"{vermelho}{lista_digitada[i]}{limpo}", end=" ")
                break     
    tentativas -= 1

    if tentativas == 0:
        print(f"\nVocê perdeu :C A palavra era {palavra_secreta}")
        exit()
        
            
                
    