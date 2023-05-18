import pygame
from overworld_controller import OverworldController

WIDTH:int = 1000
HEIGTH: int = 800
def main():
    pygame.init()
    pygame.display.set_caption("platformer")
    window = pygame.display.set_mode((1000, 800))
    c = OverworldController(window)
    
    run = True
    while run:
        run = c.game_loop()
    pygame.quit()

         

     
if __name__ == "__main__":
    main()