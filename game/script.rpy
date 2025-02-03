# Definimos a los personajes
define xs = Character("????")
define ae = Character("Aether") 
define pa = Character("Paimon. Pleisure")

# El juego comienza aquí
label start:
    # Mostramos la escena de prueba antes del capítulo 1
    call tryscene
    
    # Iniciamos el capítulo 1
    jump chapter1_start
    
