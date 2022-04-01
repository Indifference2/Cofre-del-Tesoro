print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
                    
print ("Bienvenido/a a la isla del tesoro.")
print ("Tú misión es encontrar el tesoro")
#INPUTS PRIMERA ELECCION#
choice = input ("Has ingresado a una ruina y tienes dos caminos.\n¿Que camino elijes?\nEscribe 'izquierda' o 'derecha' para elegir a donde quieres:----->").lower()
if(choice=="derecha"):
  print('\n\n')
  print ("Has elegido el camino de la derecha.\nPisaste una trampa y una flecha te atraveso la cabeza.")
  print('''
      |-  -|    //
 <----|O  O|---<<<
      |  ^ |    \\
      | -- |
       \__/
''')
  print("Has muerto.")
elif (choice == "izquierda"): 
  print ("\n\n")
  #INPUTS SEGUNDA ELECCION#
  choice = input ("Has elegido el camino de la izquierda. \nHas llegado a una camara llena de agua.\n¿Qué deseas hacer? \n Escribe 'nadar' para adentrarte al agua o 'esperar' para ver si el agua disminuye:----->").lower()
  if(choice == "nadar"):
    print("\n\n")
    print('''
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.      cjr
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`

       
    ''')
    print("Habia una serpiente en el agua, te mordio y te enveneno.\nHas Muerto")
  elif (choice == "esperar"):
    print("\n\n")
    #INPUTS TERCERA ELECCION#
    choice = input ("Has esperado y encontraste un pasaje secreto en la que hay 3 puertas. Una roja,azul y amarilla\n¿Que puerta quieres abrir\n.Escribe 'roja' 'azul' 'amarilla' para elegir la puerta----->").lower()
    if(choice =="roja"):
      print("\n\n")
      print('''
      ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..jb
          
      ''')
      print("En el interior habia una llamarada, has sido quemado vivo.\nHas muerto")
    elif(choice == "azul"):
       print("\n\n") 
       print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
       ''')
       print("Una bestia te asesino.\nHas Muerto")
    elif(choice == "amarilla"):
      print("\n\n")
      print('''
                                        _       
                                        | |      
          ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
        / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
        | (_| (_) | | | | (_| | | | (_| | |_\__ \
        \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                          __/ |                  
                        |___/          
              
      ''')
      print("Has encontrado el cofre del tesoro")






    
  



