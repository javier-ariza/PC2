import sys
import os
from subprocess import call


os.environ['GROUP_NUMBER'] = '22'
call(["sudo","apt-get","install","-y","git"])
call(["git","clone","https://github.com/CDPS-ETSIT/practica_creativa2.git"])
call(["sudo","apt-get","update"])
call(["sudo","apt-get","install","-y","python3-pip"])




fin = open("practica_creativa2/bookinfo/src/productpage/requirements.txt", 'r')
fout = open("practica_creativa2/bookinfo/src/productpage/requirements2.txt", 'w')
for line in fin:
   if "urllib3==1.26.5" in line:
      fout.write("urllib3  \n")
   else:
      fout.write(line)
fin.close()
fout.close()
call(['mv', 'practica_creativa2/bookinfo/src/productpage/requirements2.txt', 'practica_creativa2/bookinfo/src/productpage/requirements.txt'])
call(['rm', '-f', 'practica_creativa2/bookinfo/src/productpage/requirements2.txt"'])


fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r')
fout = open("practica_creativa2/bookinfo/src/productpage/templates/productpage2.html", 'w')
for line in fin:
   if "{% block title %}Simple Bookstore App{% endblock %}" in line:
      fout.write(line.replace("{% block title %}Simple Bookstore App{% endblock %}", "{% block title %}Grupo "+os.environ['GROUP_NUMBER']+"{% endblock %}"))
   else:
      fout.write(line)
fin.close()
fout.close()
call(['mv', 'practica_creativa2/bookinfo/src/productpage/templates/productpage2.html', 'practica_creativa2/bookinfo/src/productpage/templates/productpage.html'])
call(['rm', '-f', 'practica_creativa2/bookinfo/src/productpage/templates/productpage2.html'])






call(["pip3","install","-r","practica_creativa2/bookinfo/src/productpage/requirements.txt"])

call(["python3","practica_creativa2/bookinfo/src/productpage/productpage_monolith.py","9080"])