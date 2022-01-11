class Recipiente:
    conteudo = 0
    limpo = True

    def __init__(self,tamanho):
        if tamanho >= 0:
            self.tamanho = tamanho
        else: 
            self.tamanho = 0

    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        return self.conteudo == 0

    def lavar(self):
        self.limpo = True

    def esta_limpo(self):
        return self.limpo == True

    def estado(self):
        return 'limpo' if self.limpo == True else 'sujo'

    def sujar(self):
        self.limpo = False

    def __repr__(self):
        return f"Um recipiente {self.estado()} não especificado"

    def __str__(self):
        return f"Um recipiente {self.estado()} não especificado"

copo = Recipiente(500)
copo.sujar()
print(copo)
