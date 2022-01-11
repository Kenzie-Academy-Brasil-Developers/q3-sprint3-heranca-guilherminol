from classes.copo import Copo
from classes.recipiente import Recipiente
if __name__ == "__main__":
    # Execute suas testagens manuais aqui
    copo = Copo(500)
    copo.encher()
    copo.beber(230)
    print(copo)
    copo.lavar()
    print(copo)