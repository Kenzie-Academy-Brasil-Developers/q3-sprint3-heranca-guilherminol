from .recipiente import Recipiente

class Copo(Recipiente):

    bebida = None
    def __init__(self,tamanho):
        super().__init__(tamanho)

    def encher(self,bebida = 'água'):
        if not self.esta_limpo :
            return "Não se pode encher um copo sujo"

        self.conteudo += self.tamanho
        self.sujar()
        self.bebida = bebida

    def beber(self,quantidade):

        if quantidade < 0:
            return "Quantidade deve ser positiva"

        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"

        self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.limpo = True
        self.esvaziar()

    def __repr__(self):
        if not self.conteudo:

            return f"Um copo vazio de {self.tamanho}ml"

        return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

    def __str__(self):
        if not self.conteudo:

            return f"Um copo vazio de {self.tamanho}ml"

        return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

