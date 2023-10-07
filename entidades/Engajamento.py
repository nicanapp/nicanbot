

class Engajamento:
    
    curtidas:int = 0
    visualizacoes:int = 0 
    compartilhamento:int = 0 

    def toString(self) -> str:
        return f"""[ curtidas:{self.curtidas} | visualizações:{self.visualizacoes} ]"""

