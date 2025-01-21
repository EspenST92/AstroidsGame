from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            right_vector = self.velocity.rotate(random_angle)
            left_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_1.velocity = right_vector * 1.2
            new_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_2.velocity = left_vector * 1.2
