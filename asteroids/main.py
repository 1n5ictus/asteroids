# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    asteroid_field = AsteroidField()
    
    while True:
        for obj in updatables:
            obj.update(dt)
        screen.fill((0, 0, 0))
        for obj in drawables:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collides_with(player):
                print("Game Over!")
                sys.exit()
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot):
                    obj.split()
                    shot.kill()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()