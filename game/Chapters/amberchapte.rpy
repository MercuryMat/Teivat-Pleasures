define amb = Character("Amber", color="#ff0000")


label amberchapter_start:
    call charlaamb

    return



label charlaamb:

    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

 
    scene Diary with flashbulb  # Se asegura que el fondo se muestre correctamente
    
    show Amber at center

    amb "Bienvenido, esta es una obra ficticia."
    amb "Por lo tanto su mundo y situaciones son irreales, así como todos sus personajes son mayores de edad."
    amb "Dicho esto espero disfrutes de tu aventura en este mundo desconocido.\nEspero pronto poder conocerte pronto... jeje."

    hide Amber with dissolve

    
    amb "Por lo tanto su mundo y situaciones son irreales, así como todos sus personajes son mayores de edad."
    amb "Dicho esto espero disfrutes de tu aventura en este mundo desconocido.\nEspero pronto poder conocerte pronto... jeje."

return