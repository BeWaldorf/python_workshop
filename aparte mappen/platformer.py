import os
import pygame
from os.path import join
from overworld_object import OverworldObjectModel, OverworldObjectView, OverworldObjectController
from overworld import OverworldModel, OverworldView, OverworldController



def main():
    m = OverworldModel()
    v = OverworldView("Platformer",(1000, 800))
    c = OverworldController(m, v)
    
    c.start()
    c.gameloop()
    c.exit()
    quit()

if __name__ == "__main__":
    main()