from random import uniform
import pygame as pg

class Boid(pg.sprite.Sprite):

    min_speed = .2
    max_speed = .5
    max_force = .2
    neighbors_area = 30 # показатель расстояния до соседей
    min_distance = 17 # минимальное расстояние до соседей
    
    def __init__(self, max_x, max_y) -> None:
        super().__init__()

        self.max_x = max_x
        self.max_y = max_y

        # базовые коэффициенты сил
        self.k_separation = self.max_force
        self.k_alignment = self.max_force
        self.k_cohesion = self.max_force

        # координаты и скорость представляют собой векторы
        self.coords = pg.math.Vector2(uniform(0, self.max_x), uniform(0, self.max_y))
        self.velocity = pg.math.Vector2(uniform(-1, 1) * self.max_speed, uniform(-1, 1) * self.max_speed)

        # прорисовка бойда
        self.image = pg.Surface((10, 10))
        # self.image.fill('green')
        self.rect = self.image.get_rect(center=self.coords)
        pg.draw.circle(self.image, pg.Color('white'), (5, 5), 5)
    
    def update(self, dt, boids):

        acceleration = pg.math.Vector2() # вектор ускорения
        
        neighbors = self.get_neighbors(boids)
        if neighbors:
            separation = self.separation(neighbors, self.k_separation)
            alignment = self.alignment(neighbors, self.k_alignment)
            cohesion = self.cohesion(neighbors, self.k_cohesion)
            acceleration += separation + alignment + cohesion
        
        # проверка на достижение максимальной скорости
        speed, self.heading = self.velocity.as_polar()
        if speed < self.min_speed:
            self.velocity.scale_to_length(self.min_speed)

        if speed > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)
        
        # перемещение
        self.velocity += acceleration * dt
        self.coords += self.velocity * dt
        self.rect = self.image.get_rect(center=self.coords)
        self.transition()

    # смена кооринат при выходе за границы экрана
    def transition(self):
        if self.coords[0] < 0:
            self.coords[0] += self.max_x
        elif self.coords[0] > self.max_x:
            self.coords[0] -= self.max_x

        if self.coords[1] < 0:
            self.coords[1] += self.max_y
        elif self.coords[1] > self.max_y:
            self.coords[1] -= self.max_y

    
    # разделение
    def separation(self, boids, k=1):
        acceleration = pg.Vector2()
        for boid in boids:
            dist = self.coords.distance_to(boid.coords)
            if dist < self.min_distance:
                acceleration -= (boid.coords - self.coords) / 4
        acceleration = self.limit_force(acceleration)
        return acceleration * k

    # выравнивание
    def alignment(self, boids, k=1):
        acceleration = pg.Vector2()
        for boid in boids:
            acceleration += boid.velocity
        acceleration /= len(boids) # средный вектор ускорения
        acceleration -= self.velocity / 2
        acceleration = self.limit_force(acceleration)
        return acceleration * k


    # сцепление/притяжение
    def cohesion(self, boids, k=1):
        acceleration = pg.Vector2()
        for boid in boids:
            acceleration += boid.coords
        acceleration /= len(boids)
        acceleration -= self.coords / 4
        acceleration = self.limit_force(acceleration)
        return acceleration / 100 * k

    def get_neighbors(self, boids):
        neighbors = []
        for boid in boids:
            if boid != self:
                dist = self.coords.distance_to(boid.coords)
                if dist < self.neighbors_area:
                    neighbors.append(boid)
        return neighbors

    # ограничение силы
    def limit_force(self, force, limit=max_force):
        if 0 < force.magnitude() > limit:
            force.scale_to_length(limit)
        return force