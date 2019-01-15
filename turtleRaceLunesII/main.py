import pygame, sys


class Game():
    runners = []
    __starLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("image/background.png")#insertamos esta imagen como fondo de pantalla. pero no la hemos puesto en pantalla. Solo la hemmos puesto en una variable
        pygame.display.set_caption("carrera de bichos")#le poenmos este nombre
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            self.__screen.blit(self.__background, (0, 0))#Me pones en la pantalla, lo que hay en la variable backgruond(la imagen) en la posicion original (0, 0)
            
            pygame.display.flip()#refrescar la pantalla
            
        pygame.quit()#cierra pygame. sie el juego es muy complejo, es posible que tarde en cerrase o incluso se quede colgado mientras intenta cerrar
        sys.exit()#cierra python y nos aseguramos de cerrarlo
    
    
if __name__ == "__main__":
    game = Game()
    pygame.init()#si no unciona poner pygame.font.init()
    game.competir()