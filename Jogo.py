from Pilha import Pilha
import random
import os

def cria_embaralha_pilha(qtde_pilhas: int) -> list:
    '''
    é criado uma lista (lista_base) na qual será inserido a quantidade exata de números necessários para a execução do jogo e as embaralha utilizando a função pronta random.shuffle
    em seguida é criado a quantidade de pilhas necessárias de aconto com o número escolhido pelo usuário. Então os elementos da lista_base são distribuídos para as pilhas, que possuem
    tamanho fixo de 4 unidades de alocação. Ao mesmo tempo, no momento em que o elemento é alocação na pilha, esse mesmo termo é removido da lista_base, que não será mais utilizada.
    '''
    pilhas_jogo = []
    lista_base = []

    for i in range(1, qtde_pilhas + 1):
        lista_base.append(i)
        lista_base.append(i)
        lista_base.append(i)
        lista_base.append(i)

    random.shuffle(lista_base)
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
    '''
    verifica se os números de orientação das pilhas que o jogador quer fazer a mudança dos elementos está dentro dos limites possíveis de troca de posição.
    sendo assim, o número válido deve estar entre o intervalo de 1 até o número máximo de pilhas geradas (de acordo com o número já escolhido pelo jogador inicialmente).
    '''
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
    '''
    é feito uma verificação se a troca é valida de acordo com as condições/regras do jogo.
    regras: quando o elemento do topo da pilha de origem é igual ao elemento do topo da pilha de destino; quando o a pilha de origem não está vazia;
            quando a pilha de destino não está cheia; o movimento também é válido quando a pilha de destino não está nem cheia nem vazia. 
    '''
    answer = True
    if pilhas_jogo[p_origem - 1].ElementoDoTopo() == pilhas_jogo[p_destino - 1].ElementoDoTopo() or pilhas_jogo[p_destino - 1].ElementoDoTopo() == None:
        if pilhas_jogo[p_origem - 1].PilhaVazia():
            answer = False
            if pilhas_jogo[p_destino - 1].PilhaCheia():
                answer = False
                if not pilhas_jogo[p_destino - 1].PilhaVazia() and not pilhas_jogo[p_destino - 1].PilhaCheia():
                    answer = True
    else:
        answer = False   
    return answer

def valida_vitoria(pilhas_jogo, qtde_pilhas) -> bool:
    '''
    verifica se todos os elementos das pilhas são iguais. Caso sejam, o jogo acaba.
    '''
    for p in range(qtde_pilhas):
        primeiro_num = pilhas_jogo[p].elem[0]
        for j in range(1, pilhas_jogo[p].topo + 1):
            if pilhas_jogo[p].elem[j] != primeiro_num:
                return False
    return True

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

        win = valida_vitoria(pilhas_jogo, qtde_pilhas)
        pilha_origem = int(input('De qual pilha você quer tirar? Digite: '))
        pilha_destino = int(input('Em qual pilha você quer colocar? Digite: '))

        if validade_entradas(pilha_origem,pilha_destino,qtde_pilhas):
            if condicoes_troca(pilhas_jogo,pilha_origem,pilha_destino):
                os.system('cls' if os.name == 'nt' else 'clear')
                po = pilhas_jogo[pilha_origem - 1].Desempilha()
                pilhas_jogo[pilha_destino - 1].Empilha(po)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Troca Inválida.Selecione novamente: ')           
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Troca Inválida.Selecione novamente: ')

    for i, pilha in enumerate(pilhas_jogo):
        print(f"Pilha {i + 1}: {pilha.mostrar_elementos()}")

    print('Parabéns! Você venceu!')

if __name__ == '__main__':
    main()
