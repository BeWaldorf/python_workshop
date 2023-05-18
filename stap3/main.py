import pygame
from os.path import join
def main():
    print("hello world")
    pygame.init()
    pygame.display.set_caption("platformer")
    window = pygame.display.set_mode((1000, 800))
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
    
    for column in range(1000 // width + 1):
        for row in range(800 // height + 1):
            coordinate = (column * width, row * height)
            tile_grid.append(coordinate)
    
    for tile_coord in tile_grid:
        window.blit(image, tile_coord)
    
    pygame.display.update()
         

     
if __name__ == "__main__":
    main()