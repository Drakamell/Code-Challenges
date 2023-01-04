'''
  Escribe un programa que reciba un texto y transforme lenguaje natural a
  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
   se caracteriza por sustituir caracteres alfanuméricos.
  - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
    con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''
print("Hola, vas a poder traducir textos con este programa a 'lenguaje hacker'. Introduce a continuación el texto que quieras para ver el restulado:")

text = input("Escriba un mensaje:")

for char in text:
  if char == "a":
    text = text.replace("a","4")
  elif char == "b":
    text = text.replace("b","13")
  elif char == "c":
    text = text.replace("c","[")
  elif char == "d":
    text = text.replace("d",")")
  elif char == "e":
    text = text.replace("e","3")
  elif char == "f":
    text = text.replace("f","|=")  
  elif char == "g":
    text = text.replace("g","&")
  elif char == "h":
    text = text.replace("h","#")
  elif char == "i":
    text = text.replace("i","1")
  elif char == "j":
    text = text.replace("j",",_|")
  elif char == "k":
    text = text.replace("k",">|")
  elif char == "l":
    text = text.replace("l","1")
  elif char == "m":
    text = text.replace("m","^^")
  elif char == "n":
    text = text.replace("n","^/")
  elif char == "ñ":
    text = text.replace("ñ","^`/")
  elif char == "o":
    text = text.replace("o","0")
  elif char == "p":
    text = text.replace("p","|*")
  elif char == "q":
    text = text.replace("q","(_,)")
  elif char == "r":
    text = text.replace("r","12")
  elif char == "s":
    text = text.replace("s","5")
  elif char == "t":
    text = text.replace("t","7")
  elif char == "u":
    text = text.replace("u","(_)")
  elif char == "v":
    text = text.replace("v","\/")
  elif char == "w":
    text = text.replace("w","\/\/")
  elif char == "x":
    text = text.replace("x","><")
  elif char == "y":
    text = text.replace("y","j")
  elif char == "z":
    text = text.replace("z","2")

print("Su texto es el siguiente: ")
print(text)
    
    
