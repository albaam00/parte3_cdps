from subprocess import call
import os
import sys
from os import remove
import webbrowser

#clonar aplicación
call(["git clone https://github.com/CDPS-ETSIT/practica_creativa2.git",  "-y"], shell=True)


#instalación pip 
#call(["sudo apt-get install pip",  "-y"], shell=True)
#call(["sudo apt-get install python3-pip",  "-y"], shell=True)
call(["curl -O https://bootstrap.pypa.io/get-pip.py",  "-y"], shell=True)
call(["python3 get-pip.py",  "-y"], shell=True)


#instalar dependencias
fin = open("practica_creativa2/bookinfo/src/productpage/requirements.txt", 'r') # in file
os.chdir("practica_creativa2")
for line in fin:
    call(["pip3 install " + line,  "-y"], shell=True)
fin.close()
os.chdir("../")


#cambiar titulo
#os.environ['GROUP_NUMBER']="3"
fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r') # in file
fout = open("productpage2.html", 'w') # out file
for line in fin:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
        fout.write("{% block title %} Equipo: "+str(os.environ.get('GROUP_NUMBER'))+"{% endblock %}")
    else:
        fout.write(line)
fin.close()
fout.close()

call(["mv","productpage2.html","practica_creativa2/bookinfo/src/productpage/templates/productpage.html"])

#Arrancar la aplicación
#os.chdir("practica_creativa2/bookinfo/src/productpage")
#webbrowser.open('http://192.168.122.218:9080/productpage')
#call(["python3 productpage_monolith.py 9080",  "-y"], shell=True)
