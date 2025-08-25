from constants import *
from player import *
from asteroidfield import *
import pygame
import sys
import math
def main():

    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_object = pygame.time.Clock()
    dt = 0
    shots_group = []
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = ((updatable))
    AsteroidField_object = AsteroidField()
    Player.containers = (updatable, drawable)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draw_item in drawable:
            draw_item.draw(screen)
        player.update(dt)
        player.draw(screen)
        for each_asteroid in asteroids_group:
            if player.check_for_collisions(each_asteroid):
                print("Game over!")
                sys.exit()
        for each_asteroid in asteroids_group:
            for shot in shots_group:
                distance = math.dist(shot.position, each_asteroid.position)
                if distance < shot.radius + each_asteroid.radius:
                    shot.kill()
                    each_asteroid.split()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot()
        for shot in shots_group:
            shot.update(dt)
            shot.draw(screen)

        updatable.update(dt)
        pygame.display.flip()
        passed_time = clock_object.tick(60)
        dt = passed_time/1000
        
if __name__ == "__main__":
    main()
    


