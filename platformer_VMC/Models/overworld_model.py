from pygame.sprite import collide_mask

class OverworldModel():
    WIDTH, HEIGHT = 1000, 800
    FPS = 60
    GRAVITY = 1
    PLAYER_SPEED = 5
    TITLE = "Platformer"
    
    def handle_vertical_collision(player, objects, dy):
        collided_objects = []
        for obj in objects:
            if collide_mask(player, obj):
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hit_head()
                collided_objects.append(obj)
        return collided_objects

    def collide(player, objects, dx):
        player.move(dx, 0)
        player.update()
        collided_object = None
        for obj in objects:
            if collide_mask(player, obj):
                collided_object = obj
                break
        player.move(-dx, 0)
        player.update()
        return collided_object
    
