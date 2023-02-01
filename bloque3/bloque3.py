from subprocess import call
import sys
import os
orden = sys.argv[1]
if orden == "arrancar":
 if len(sys.argv) == 2:
  os.system('sudo apt-get install -y docker.io')
  os.system('sudo apt-get install -y docker-compose')
  os.system('sudo apt-get update')
  os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')
  os.system("cp -r practica_creativa2/bookinfo/src/productpage ProductPage/")
  os.system("cp practica_creativa2/bookinfo/src/details/details.rb Details/")
  os.system("cp practica_creativa2/bookinfo/src/ratings/package.json Ratings/")
  os.system("cp practica_creativa2/bookinfo/src/ratings/ratings.js Ratings/")
  os.chdir('practica_creativa2/bookinfo/src/reviews')
  os.system('sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/projec$
  os.system('sudo docker-compose build')
  os.system('sudo docker-compose up')

 else:
  print("Debes introducir solamente el bloque y el comando a ejecutar")
elif orden == "parar":
 if len(sys.argv) == 2:
  os.system("sudo docker-compose down")
  os.system("sudo docker rmi 22/details 22/productpage 22/reviews 22/ratings")
 else:
  print("Debes introducir solamente el bloque y el comando a ejecutar")
else:
 print("Comando no existente, prueba 'arrancar' o 'parar'")
