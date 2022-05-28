import pygame as pg
from pygame.locals import *
from sys import exit
from boid import Boid

WIDTH = 800
HEIGHT = 600
FPS = 90
def_boids_amount = 150

def main():
    
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Boids")
    bg = pg.Surface(screen.get_size()).convert()
    bg.fill(pg.Color('black'))
    clock = pg.time.Clock()
    
    boids = pg.sprite.RenderUpdates()
    for _ in range(def_boids_amount):
        boids.add(Boid(WIDTH, HEIGHT))

    # Цикл игры
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

            # Управление: 
            # зажать первую букву силы (a - alignment, s - separation, c - cohesion) и команду: 
            # - для уменьшения силы
            # =/+ для увеличения силы
            # 1 для включения значения силы по умолчанию
            # 0 для полного отключения силы
            
            elif event.type == KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_c]:
                    if keys[pg.K_MINUS]: 
                        for boid in boids:
                            boid.k_cohesion -= 0.05
                        print(f'Коэффициент сцепления {boids.sprites()[0].k_cohesion}')
                    elif keys[pg.K_EQUALS]:
                        for boid in boids:
                            boid.k_cohesion += 0.05
                        print(f'Коэффициент сцепления {boids.sprites()[0].k_cohesion}')
                    elif keys[pg.K_0]:
                        for boid in boids:
                            boid.k_cohesion = 0
                        print(f'Коэффициент сцепления {boids.sprites()[0].k_cohesion}')
                    elif keys[pg.K_1]:
                        for boid in boids:
                            boid.k_cohesion = boid.max_force
                        print(f'Коэффициент сцепления {boids.sprites()[0].k_cohesion}')
                elif keys[pg.K_s]:
                    if keys[pg.K_MINUS]: 
                        for boid in boids:
                            boid.k_separation -= 0.05
                        print(f'Коэффициент разделения {boids.sprites()[0].k_separation}')
                    elif keys[pg.K_EQUALS]:
                        for boid in boids:
                            boid.k_separation += 0.05
                        print(f'Коэффициент разделения {boids.sprites()[0].k_separation}')
                    elif keys[pg.K_0]:
                        for boid in boids:
                            boid.k_separation = 0
                        print(f'Коэффициент разделения {boids.sprites()[0].k_separation}')
                    elif keys[pg.K_1]:
                        for boid in boids:
                            boid.k_separation = boid.max_force
                        print(f'Коэффициент разделения {boids.sprites()[0].k_separation}')
                elif keys[pg.K_a]:
                    if keys[pg.K_MINUS]: 
                        for boid in boids:
                            boid.k_alignment -= 0.05
                        print(f'Коэффициент выравнивания {boids.sprites()[0].k_alignment}')
                    elif keys[pg.K_EQUALS]:
                        for boid in boids:
                            boid.k_alignment += 0.05
                        print(f'Коэффициент выравнивания {boids.sprites()[0].k_alignment}')
                    elif keys[pg.K_0]:
                        for boid in boids:
                            boid.k_alignment = 0
                        print(f'Коэффициент выравнивания {boids.sprites()[0].k_alignment}')
                    elif keys[pg.K_1]:
                        for boid in boids:
                            boid.k_alignment = boid.max_force
                        print(f'Коэффициент выравнивания {boids.sprites()[0].k_alignment}')

        for b in boids:
            b.update(3, boids)
        
        boids.clear(screen, bg)
        boids.draw(screen)
        pg.display.update()

if __name__ == '__main__':
    main()


