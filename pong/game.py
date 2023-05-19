import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Definir dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de Naves")

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagen = pygame.Surface([50, 50])
        self.imagen.fill(BLANCO)
        self.rect = self.imagen.get_rect()
        self.rect.x = ANCHO_PANTALLA // 2
        self.rect.y = ALTO_PANTALLA - 70
        self.velocidad_x = 0

    def update(self):
        self.rect.x += self.velocidad_x

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO_PANTALLA - 50:
            self.rect.x = ANCHO_PANTALLA - 50

# Clase Enemigo
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagen = pygame.Surface([30, 30])
        self.imagen.fill(NEGRO)
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randrange(ANCHO_PANTALLA - 30)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad_y = random.randrange(1, 3)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.y > ALTO_PANTALLA + 10:
            self.rect.x = random.randrange(ANCHO_PANTALLA - 30)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad_y = random.randrange(1, 3)

# Crear grupo de sprites
todos_los_sprites = pygame.sprite.Group()

# Crear jugador
jugador = Jugador()
todos_los_sprites.add(jugador)

# Crear enemigos
enemigos = pygame.sprite.Group()
for i in range(10):
    enemigo = Enemigo()
    enemigos.add(enemigo)
    todos_los_sprites.add(enemigo)

# Reloj para controlar la velocidad de actualización de la pantalla
reloj = pygame.time.Clock()

# Variable para controlar el bucle principal del juego
jugando = True

# Bucle principal del juego
while jugando:
    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador.velocidad_x = -5
            elif evento.key == pygame.K_RIGHT:
                jugador.velocidad_x = 5
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador.velocidad_x = 0

    # Actualizar sprites
    todos_los_sprites.update()

    # Comprobar colisiones
    colisiones = pygame.sprite.spritecollide(jugador, enemigos, True)

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar sprites en la pantalla
    todos_los_sprites.draw(pantalla)

    # Actualizar pantalla
    pygame.display.flip()

    # Limitar la velocidad de actualización de la pantalla
    reloj.tick(60)

# Salir del juego
pygame.quit()