# !/usr/bin/env-python
# -*- coding: utf-8 -*-

import pygame

# -COLORES
negro    = ( 0   , 0   , 0   )
blanco   = ( 255 , 255 , 255 )
rojo     = ( 200 , 0   , 0   )
verde    = ( 0   , 200 , 00  )
azul     = ( 0   , 0   , 200 )
amarillo = ( 255 , 255 , 0   )

# -VENTANA
tamaño    = ancho,alto = 300,300            # Tamaño de la pantalla
pantalla  = pygame.display.set_mode(tamaño) # Se cre una pantall con pygame con el tamaño prediseñado
pygame.display.set_caption("Gravedad")      # Se le pone un nombre al borde de la pantalla

# -DATOS DE LA PELOTA 
class Pelota:

    def __init__(self, x , y , radio , color):
        self.x      = x
        self.y      = y
        self.radio  = radio
        self.color  = color
        self.grosor = 0 

    def mostrar(self):
        pygame.draw.circle ( pantalla , self.color , (  self.x , self.y ) , self.radio , self.grosor )

# -DATOS
velocidad = 0

balon = Pelota ( 150 , 20 , 20 , rojo)
# -BUCLÉ 
while True:
    for accion in pygame.event.get():
        # Si se presiona el boton 'X' salimos
        if accion.type == pygame.QUIT:
            quit()
        if accion.type    == pygame.KEYDOWN:
            # Si presionamos la tecla 'c'
            if accion.key == pygame.K_c:
               velocidad = 10 

    # Muestra la pantalla con fondo de color
    pantalla.fill(blanco)

    # Movimiento en el eje Y
    balon.y += velocidad 

    # Muestra la pelota
    balon.mostrar()

    # Condición para no rebasar el suelo
    if balon.y >= 300:
        velocidad *= -1

    # Condición para no rebadar el techo
    if balon.y < 0: 
        velocidad *= -1
    
    # Manejo de la pantalla
    pygame.display.update()

    # Actualización de la pantalla
    pygame.time.delay(30)
