#personaje indefinidi

define xs = Character("????")

# protagonistas
 
define ae = Character("Aether") 
define pa = Character("Paimon. Pleisure")

# personajes femenininos monstad




# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    

    # Presenta las líneas del diálogo.

    xs "bienvenido, esta es una obra fictisia "

    xs "Por lo tanto su mundo y situaciones son irreales, asi como todos sus personajes son mayores de edad"

    xs "Dicho esto espero disfrutes de tu aventura en este mundo desconocido\n
    espero pronto poder conocerte pronto... jeje"

    scene intro1
    ae "¿Que fue lo que sucedio?"

    scene intro2
    ae "Estabasmos tan cerca...."

    scene intro3
    ae "¿Entonces porque ?"

    scene intro4
    ae "¿porque tuvo que pasar esto?"

    scene intro5
    ae "LUMINE......!!!!!!!!"

    scene black

    xs "Heeeeeeeeee..... "

    xs "Para ser alguien que estuvo sellado en el fondo\n del mar por miles de años si que tienes energia... "
  
    scene PlayaN1
    show Paiint1
    ae "Ahhhhh...!!!"
    xs "Buenos dias dormilos, ohhh es verdad lo correcto seria decir noches... "
    hide Paiint1
    show Paiint2
    xs "Y dime. ¿te encuentas bien? \n ¿Puedes hablar...? "
    xs "La caida desde el cielo y el golpe contra el mar \n ¿no te frieron el cerebro verdad? "
    hide Paiint2
    show Paiint3
    xs "......."
    xs "¿Puedes hacer algo aparte de quedarte mirandome como un estupido? \n es bastante incomodo sabes"
    xs "......."
    hide Paiint3
    show Paiint2
    xs "Ohhhhh ya lo entiendo..."
    hide Paiint2
    show Paiint4
    xs "Como no me di cuenta antes, no tienes practicamente energia\n elemental sin duda esa mujer penso en todo"
    xs "Ha este paso lo mas seguro es que mueras de inanicion, pero no tienes de que preocuparte"
    hide Paiint4
    show Paiint5
    xs "Esta amable bruja se encargara de transferirte un poco de energia elemental"
    xs "Tan solo relajate y trata de no ser muy codisioso esta bien...♥"
    hide Paiint5
    show Paiint6
    ae "*¿Quien es esta persona?, no lo enteiendo*"
    ae "*¿Que es lo que pretende hacer....!!!*"
    hide Paiint6
    show Paiint7
    ae "Ummhgg.....!?!?!"
    hide Paiint7
    show Paiint8
    ae "Que calida sensacion"
    hide Paiint8
    show Paiint9
    ae "Es como si todo mi cuerpo"
    hide Paiint9
    show Paiint10
    ae "Se llenara de energia de golpe"
    hide Paiint10
    show Paiint11
    ae "Es similar a si estuviera llenando mi estomago"
    hide Paiint11
    show Paiint12
    ae "Luego de estar a punto de morir de hambre"
    hide Paiint12
    show Paiint13
    ae "No lo entiendo muy bien porque esta \n esta usando este metodo....."
    hide Paiint13
    show Paiint14
    ae "Pero al menos no parece ser una mala persona"
    hide Paiint14
    show Paiint15
    ae "ni tampoco parece estar relacionada con esa persona"
    hide Paiint15
    show Paiint16
    ae "Ademas, no lo habia notado pero ahora que \n regreso a mis sentidos"
    hide Paiint16
    show Paiint17
    ae "Me doy cuenta de que sus labios son realmente suaves \n y su aroma es realmete agradable"
    hide Paiint17
    show Paiint18 
    ae "Puede que esto realmente no sea tan malo"
    ae "Claro si no tenemos en cuenta que me llamo idiota"
    hide Paiint18
    show Paiint19
    xs "Eso deberia de ser sufiente por ahora, aun que sigue siendo solo medida temporal"
    xs "Pero bueno"
    hide Paiint19
    show Paiint20
    xs "Crees que podrias levantarte ya, estas arrugando mi traje\n señor viajero de otro mundo"


    # Finaliza el juego:

    return
