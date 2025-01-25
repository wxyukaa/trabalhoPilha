class Pilha:
    def ___init___(self, tam_max):
        self.elemento = [None] * tam_max
        self.topo = -1
        self.tam_max = tam_max

    def InicializaPilha(self):
        self.topo = -1

    def PilhaVazia(self) -> bool:
        if self.topo == -1:
            vazia = True
        else:
            vazia = False
        return vazia
    
    def PilhaCheia(self) -> bool:
        if self.topo == self.tam_max - 1:
            cheia = True
        else:
            cheia = False
        return cheia
    
    def ElementoDoTopo(self) -> int:
        if not self.PilhaVazia:
            return self.elemento[self.topo]

    def Empilha(self, x: int):
        if not self.PilhaCheia:
            self.topo = self.topo + 1
            self.elemento[self.topo] = x

    def Desempilha(self) -> int:
        if not self.PilhaVazia:
            x = self.elemento[self.topo]
            self.topo = self.topo - 1
            if self.PilhaVazia:
                self.InicializaPilha
        return x
    
