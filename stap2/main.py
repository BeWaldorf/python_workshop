import pygame

def main():
    print("hello world")
    pygame.init()
    pygame.display.set_caption("Platformer")
    pygame.display.set_mode((1600, 900))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()
    
if __name__ == "__main__":
    main()