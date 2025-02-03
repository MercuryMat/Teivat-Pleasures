# Personaje indefinido
define xs = Character("????")

# Protagonistas
define ae = Character("Aether")
define pa = Character("Paimon. Pleisure")

# Personajes femeninos monstad

# Llamamos a las escenas desde la etiqueta chapter1.start
label chapter1_start:
    call bienvenida
    call intro
    call encuentro_en_la_playa

    return

# Escena de bienvenida
label bienvenida:
    xs "Bienvenido, esta es una obra ficticia."
    xs "Por lo tanto su mundo y situaciones son irreales, así como todos sus personajes son mayores de edad."
    xs "Dicho esto espero disfrutes de tu aventura en este mundo desconocido.\nEspero pronto poder conocerte pronto... jeje."
    return

# Escena de introducción
label intro:
    scene intro1 # O define imágenes intro1, intro2, etc.
    ae "¿Que fue lo que sucedió?"

    scene intro2 # O define imágenes intro1, intro2, etc.
    ae "Estábamos tan cerca...."

    scene intro3 # O define imágenes intro1, intro2, etc.
    ae "¿Entonces porque?"

    scene intro4 # O define imágenes intro1, intro2, etc.
    ae "¿Porque tuvo que pasar esto?"

    scene intro5 # O define imágenes intro1, intro2, etc.
    ae "LUMINE......!!!!!!!!"

    scene black
    xs "Heeeeeeeeee..... "

    xs "Para ser alguien que estuvo sellado en el fondo\ndel mar por miles de años si que tienes energía... "
    return

# Escena del encuentro en la playa
label encuentro_en_la_playa:
    scene PlayaN1
    show Paiint1
    ae "Ahhhhh...!!!"
    xs "Buenos días dormilón, ohhh es verdad lo correcto sería decir noches... "
    hide Paiint1
    show Paiint2
    xs "Y dime. ¿te encuentras bien?\n¿Puedes hablar...? "
    xs "La caída desde el cielo y el golpe contra el mar\n¿no te frieron el cerebro verdad? "
    hide Paiint2
    show Paiint3
    xs "......."
    xs "¿Puedes hacer algo aparte de quedarte mirándome como un estúpido?\nEs bastante incómodo sabes."
    xs "......."
    hide Paiint3
    show Paiint4
    xs "Ohhhhh ya lo entiendo..."
    xs "Como no me di cuenta antes, no tienes prácticamente energía\nelemental sin duda esa mujer pensó en todo."
    xs "A este paso lo más seguro es que mueras de inanición, pero no tienes de que preocuparte."
    hide Paiint4
    show Paiint5
    xs "Esta amable bruja se encargará de transferirte un poco de energía elemental."
    xs "Tan solo relájate y trata de no ser muy codicioso está bien...♥"
    hide Paiint5
    show Paiint6
    ae "*¿Quién es esta persona?, no lo entiendo.*"
    ae "*¿Qué es lo que pretende hacer....!!!*"
    hide Paiint6
    show Paiint7
    ae "Ummhgg.....!?!?!"
    hide Paiint7
    show Paiint8
    ae "Que cálida sensación."
    hide Paiint8
    show Paiint9
    ae "Es como si todo mi cuerpo"
    hide Paiint9
    show Paiint10
    ae "Se llenara de energía de golpe."
    hide Paiint10
    show Paiint11
    ae "Es similar a si estuviera llenando mi estómago"
    hide Paiint11
    show Paiint12
    ae "Luego de estar a punto de morir de hambre."
    hide Paiint12
    show Paiint13
    ae "No lo entiendo muy bien porque está\nusando este método....."
    hide Paiint13
    show Paiint14
    ae "Pero al menos no parece ser una mala persona."
    hide Paiint14
    show Paiint15
    ae "Ni tampoco parece estar relacionada con esa persona."
    hide Paiint15
    show Paiint16
    ae "Además, no lo había notado pero ahora que\nregreso a mis sentidos"
    hide Paiint16
    show Paiint17
    ae "Me doy cuenta de que sus labios son realmente suaves\ny su aroma es realmente agradable."
    hide Paiint17
    show Paiint18
    ae "Puede que esto realmente no sea tan malo."
    ae "Claro si no tenemos en cuenta que me llamó idiota."
    hide Paiint18
    show Paiint19
    xs "Eso debería de ser suficiente por ahora, aunque sigue siendo solo una medida temporal."
    xs "Pero bueno."
    hide Paiint19
    show Paiint20
    xs "Crees que podrías levantarte ya, estás arrugando mi traje\nseñor viajero de otro mundo."
    return