from constants import *
from player import *
import pygame
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0
    player_object = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_object.draw(screen)
        player_object.update(dt)
        pygame.display.flip()
        passed_time = clock_object.tick(60)
        dt = passed_time/1000
        
if __name__ == "__main__":
    main()
    


