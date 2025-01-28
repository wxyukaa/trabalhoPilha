
class Pilha:
    def __init__(self, tam_max):
        self.elem = [None] * tam_max
        self.topo = -1 
        self.tam_max = tam_max


    def InicializaPilha(self):
        self.topo = -1

    def PilhaVazia(self):
        return self.topo == -1

    def PilhaCheia(self):
        return self.topo == self.tam_max - 1

    def ElementoDoTopo(self):
        if not self.PilhaVazia():
            return self.elem[self.topo]
        
    def Empilha(self, x):
        if not self.PilhaCheia():
            self.topo += 1
            self.elem[self.topo] = x

    def Desempilha(self):
        if not self.PilhaVazia():
            x = self.elem[self.topo]  # Pega o elemento do topo
            self.elem[self.topo] = None  # Mantém o espaço vazio para reutilização
            self.topo -= 1  # Atualiza o índice do topo

            if self.PilhaVazia():
                self.InicializaPilha()  # Reseta a pilha se necessário
            
            return x


        
    def mostrar_elementos(self):
        return self.elem
