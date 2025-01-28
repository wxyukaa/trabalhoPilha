from ClassePilha import Pilha
import random

def cria_embaralha_pilha(qtde_pilhas: int) -> list:
    pilhas_jogo = []
    lista_base = []

    '''
    Coloca os números que serão utilizados nas pilhas
    na *lista_base* e embaralha essa lista para gerar
    aleatoriedade no jogo.
    '''
    for i in range(1, qtde_pilhas + 1):
        lista_base.append(i)
        lista_base.append(i)
        lista_base.append(i)
        lista_base.append(i)
    random.shuffle(lista_base)

    '''
    Cria as pilhas Empilhando em cada uma os números da lista base
    as pilhas criadas estão guardadas na lista de pilhas *pilha_jogo*
    '''
    num_pilhas = qtde_pilhas + 2
    for i in range(1, num_pilhas +1): #A pilha é criada com espaços vazios
        pilhas_jogo.append(Pilha(4)) 
    for j in pilhas_jogo:
        for k in range(4): #A pilha é preenchida com os números de *lista_base*
            if len(lista_base) != 0: 
                num = lista_base.pop()
                j.Empilha(num)
    return pilhas_jogo

def validade_entradas(p_origem: int, p_destino: int, qtde_pilhas) -> bool:
    num_pilhas = qtde_pilhas + 2
    r = True
    s = True
    f = bool
    if p_origem < 0 or p_origem > num_pilhas:
        r = False
    if p_destino < 0 or p_destino > num_pilhas:
        s = False
    if r and s:
        f = True
    else: 
        f = False
    return f

def condicoes_troca(pilhas_jogo, p_origem, p_destino) -> bool:
    answer = True
    if pilhas_jogo[p_origem - 1].PilhaVazia():
        answer = False
    elif pilhas_jogo[p_destino - 1].PilhaCheia():
        answer = False
    elif pilhas_jogo[p_origem - 1].ElementoDoTopo() == pilhas_jogo[p_destino - 1].ElementoDoTopo():
        if not pilhas_jogo[p_destino - 1].PilhaVazia() and not pilhas_jogo[p_destino - 1].PilhaCheia():
            answer = True
        else:
            answer = False   
    return answer

def ValidaVitória(pilhas_jogo) -> bool:
    for p in pilhas_jogo:
        vitoria = False
        if not p.PilhaVazia():
            for i in range(0,4):
                i_prox = i+1
                if i == i_prox:
                    vitoria = True
    return vitoria

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

    win = False
    while not win:
        for i, pilha in enumerate(pilhas_jogo):
            print(f"Pilha {i + 1}: {pilha.mostrar_elementos()}")

        win = ValidaVitória(pilhas_jogo)
        pilha_origem = int(input('De qual pilha você quer tirar? Digite: '))
        pilha_destino = int(input('Em qual pilha você quer colocar? Digite: '))
        if validade_entradas(pilha_origem,pilha_destino,qtde_pilhas):
            if condicoes_troca(pilhas_jogo,pilha_origem,pilha_destino):
                po = pilhas_jogo[pilha_origem - 1].Desempilha()
                pilhas_jogo[pilha_destino - 1].Empilha(po)
            else:  
                print('Troca Inválida.Selecione novamente: ')           
        else:
            print('Troca Inválida.Selecione novamente: ')

if __name__ == '__main__':
    main()