label tryscene:
    scene Bridge

    show screen selectable_characters

    # Espera hasta que el jugador haga clic en un personaje
    $ renpy.pause()

    return  # Volver al script principal si no pasa nada

# Definimos una transformación para reducir el tamaño
transform small:
    zoom 0.7

# Pantalla con opciones de personajes
screen selectable_characters():
    # Botón para Paiint1 (izquierda, más pequeño)
    imagebutton:
        idle "Paiint1"
        hover "Paiint1"
        action [Hide("selectable_characters"), Jump("start_game")]
        xpos 0.2  # Posición izquierda
        ypos 0.5
        anchor (0.5, 0.5)
        at small  # Reduce el tamaño

    # Botón para Amber (derecha)
    imagebutton:
        idle "Amber"
        hover "Amber"
        action [Hide("selectable_characters"), Jump("amber_scene")]
        xpos 0.7  # Posición derecha
        ypos 0.5
        anchor (0.5, 0.5)

# 💾 Cuando se elige Paiint1, empieza el capítulo 1
label start_game:
    jump chapter1_start  # Empieza el juego normalmente

# 📖 Escena alternativa si el jugador elige a Amber
label amber_scene:
    
    jump amberchapter_start  # Empieza el juego normalmente
    

