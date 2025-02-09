import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2, shots)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        asteroids_to_split = []
        shots_to_remove = []

        for asteroid in asteroids:
            if asteroid.collisionCheck(player):
                raise SystemExit("Game over!")
            
            for shot in shots:
                if asteroid.collisionCheck(shot):
                    asteroids_to_split.append(asteroid)
                    shots_to_remove.append(shot)
                    break

        for shot in shots_to_remove:
            shot.kill()
        for asteroid in asteroids_to_split:
            asteroid.split()
            
        screen.fill(color='black')

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()