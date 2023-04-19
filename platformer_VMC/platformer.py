from Controllers.level_controller import LevelController as Controller
from Views.level1_view import Level1View as View
from Models.overworld_model import OverworldModel as Model




def main():
    run = True
    m = Model()
    v = View("Platformer", (1000, 800))
    c = Controller(m, v)
    
    c.start()
    while run:
        c.gameloop()
    c.exit()
    quit()

if __name__ == "__main__":
    main()