from PIL import Image

import os

carpetaDescargadas ="/Users/ericg/Download/Comprimir/"
comprimidos_guardados = "/Users/ericg/Pictures/carpetaDeDescargadas/"

if __name__ == "__main__":
    for filename in os.listdir(carpetaDescargadas):
        name, extension = os.path.splitext(carpetaDescargadas + filename)
        if( extension in [ ".jpg", ".jpeg", ".png"]):
            picture = Image.open(carpetaDescargadas + filename)
            picture.save(carpetaDescargadas + "compressed_" + filename, optimize = True , quality=60)
            os.remove(carpetaDescargadas + filename)#Para borrar el archivo en el momento
            print(name + ": " + extension)
        if(extension in [".mp3"]):
            carpetaMusica = "/Users/ericg/Music/"
            os.remove(carpetaDescargadas + filename, carpetaMusica + filename)#Mueve el archivo ????