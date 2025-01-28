from Pilha import Pilha
import random

qtde_pilhas = int(input("Quantos números diferentes serão distribuídos entre as pilhas? Escolha de 1 a 7: "))
lista_base = []
pilhas_jogo = []

def cria_embaralha_pilha(qtde_pilhas: int) -> list:
    for i in range(1, qtde_pilhas + 1):
        lista_base.append(i)
        lista_base.append(i)
        lista_base.append(i)
        lista_base.append(i)
    random.shuffle(lista_base)
    num_pilhas = qtde_pilhas + 2
    for i in range(1, num_pilhas +1):
        pilhas_jogo.append(Pilha(4))
    for j in pilhas_jogo:
        for k in range(4):
            if len(lista_base) != 0: 
                num = lista_base.pop()
                j.Empilha(num)
    return pilhas_jogo

p_origem = input("")
p_destino = input("")

p_origem -= 1
p_destino -= 1

def validade_entradas(p_origem: int, p_destino: int) -> bool:
    num_pilhas = qtde_pilhas + 2
    r = True
    s = True
    if p_origem < 0 or p_origem > num_pilhas:
        r = False
    if p_destino < 0 or p_destino > num_pilhas:
        s = False
    return r, s

def condicoes_troca(pilhas_jogo, p_origem, p_destino):
    answer = True
    if pilhas_jogo[p_origem].PilhaVazia:
        answer = False
    elif pilhas_jogo[p_destino].PilhaCheia:
        answer = False
    elif pilhas_jogo[p_origem].ElementoDoTopo() == pilhas_jogo[p_destino].ElementoDoTopo():
        if not pilhas_jogo[p_destino].PilhaVazia and not pilhas_jogo[p_destino].PilhaCheia:
            answer = True
        else:
            answer = False   
    return answer

def VerificaFimDeJogo:


#-------------------------------------------------------------------------------------------
def main():

    exit = False
    while not exit:
        qtde_pilhas = int(input("Quantos números diferentes serão distribuídos entre as pilhas? Escolha de 1 a 7: "))
        if qtde_pilhas <1 or qtde_pilhas >7:
            print('Número Inválido')
        else:
            exit = True
    
    pilhas_jogo = cria_embaralha_pilha(qtde_pilhas)

    for i, pilha in enumerate(pilhas_jogo):
        print(f"Pilha {i + 1}: {pilha.mostrar_elementos()}")

if __name__ == '__main__':
    main()
