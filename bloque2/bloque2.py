from subprocess import call
import sys
import os
orden = sys.argv[1]
if orden == "arrancar":
    if len(sys.argv) == 2:
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y docker.io")
        os.system("sudo docker build -t g22/product-page .")
        os.system("sudo docker run -d --name g22-productpage -p9080:9080 g22/product-page")
    else:
        print("Debes introducir solamente el bloque y el comando a ejecutar")
elif orden == "parar":
    if len(sys.argv) == 2:
        os.system("sudo docker stop g22-productpage")
        os.system("sudo docker rm g22-productpage")
        os.system("sudo docker rmi g22/product-page")
    else:
        print("Debes introducir solamente el bloque y el comando a ejecutar")
else:
    print("Comando no existente, prueba 'arrancar' o 'parar'")