import pygame
from os.path import join

SCREEN_WIDTH: int = 1600
SCREEN_HEIGHT: int = 900

def main():
    print("hello world")
    pygame.init()
    pygame.display.set_caption("Platformer")
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    draw_brackground(window, "Blue.png")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

def draw_brackground(window: pygame.Surface, name: str) -> None:
    image: pygame.Surface  = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tile_grid = []
    
    for column in range(SCREEN_WIDTH // width + 1):
        for row in range(SCREEN_HEIGHT // height + 1):
            coordinate = (column * width, row * height)
            tile_grid.append(coordinate)
    
    for tile_coord in tile_grid:
        window.blit(image, tile_coord)
    
    pygame.display.update()
         
if __name__ == "__main__":
    main()