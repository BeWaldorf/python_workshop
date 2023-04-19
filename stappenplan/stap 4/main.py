import pygame
import os
from os.path import join

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for column in range(1000// width + 1):
        for row in range(800 // height + 1):
            position = (column * width, row * height)
            tiles.append(position)

    return tiles, image

def main():
    print("hello world")
    pygame.init()
    pygame.display.set_caption("Platformer")
    pygame.display.set_mode((1000, 800))
    background, bg_image = get_background("Blue.png")
    bg_image.blit(background, (0,0))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        

if __name__ == "__main__":
    main()











