from flask import Flask, render_template
import os,sys
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import xlwt
import xlsxwriter
from xlwt import Workbook
import pandas as pd
from PIL import Image
from flask_socketio import SocketIO,send
from pymongo import MongoClient
from usuarios import Usuario


app= Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)


mongoClient = MongoClient('localhost',27017)

db = mongoClient.Usuario

collection = db.Uuario

with open('comand.json') as file:
    data = json.load(file)
    o=[]
    for iter in data['comandos']:
        otracosa = iter
        for h in iter:
            o.append(iter['comando'])

@app.route('/')
def inicio():

    return render_template('Desing.html')

@app.route('/inicio/<user>')
def menu_comandos(user):

    return render_template('columnas.html',usuario=user)

@socketio.on('message')
def handleMessage(msg):
    print(msg)


@app.route('/resultadols')
def elresultado():  
    os.system(o[0]+' > ls.txt')
    archivo= open ('ls.txt','r')
    respuesta=archivo.read()
    cs = "<nav color: #151965>"+respuesta+"</nav>"+"<h2> Crear pdf:  </h2>"+"<a href='pdf/ps'>Enlace a otra pagina</a> <br><h2> Crear excel: </h2>"+"<a href='excel/ps'>Enlace a otra pagina</a>"
    return cs

@app.route('/resultadops')
def elps():
    os.system(o[1]+' > ps.txt')
    archivo= open ('ps.txt','r')
    respuesta=archivo.read()
    cs = "<nav color: #151965>"+respuesta+"</nav>"+"<h2> Crear pdf:  </h2>"+"<a href='pdf/ps'>Enlace a otra pagina</a> <br><h2> Crear excel: </h2>"+"<a href='excel/ps'>Enlace a otra pagina</a>"
    return cs

@app.route('/resultadoifconfig')
def elifconfig():
    os.system(o[2]+' > ifconfig.txt')
    archivo= open ('ifconfig.txt','r')
    respuesta=archivo.read()
    cs = respuesta + "<h2> Crear pdf:  </h2>"+"<a href='pdf/ifconfig'>Enlace a otra pagina</a> <br><h2> Crear excel: </h2>"+"<a href='excel/ifconfig'>Enlace a otra pagina</a>"
    return cs

@app.route('/pdf/<arch>',methods=['GET'])
def archivo_pdf(arch):
    if arch == "ifconfig":
        cs = "el archivo es :"+arch
        archivo= open ('ifconfig.txt','r')
        respuesta=archivo.read()

    elif arch == "ls":
        cs = "el archivo es :"+arch
        archivo= open ('ls.txt','r')
        respuesta=archivo.read()

    elif arch == "ps":
        cs = "el archivo es :"+arch
        archivo= open ('ps.txt','r')
        respuesta=archivo.read()
    
    w, h = A4
    c = canvas.Canvas(arch+".pdf", pagesize=A4)       
    c.drawString(50, h - 50, ""+respuesta)
    c.showPage()
    c.save()

    return cs

@app.route('/excel/<arch>',methods=['GET'])
def archivo_excel(arch):
    if arch == "ifconfig":
        cs = "el archivo es :"+arch
        archivo= open ('ifconfig.txt','r')
        
        respuesta=archivo.read()

    elif arch == "ls":
        cs = "el archivo es :"+arch
        archivo= open ('ls.txt','r')
        respuesta=archivo.read()

    elif arch == "ps":
        cs = "el archivo es :"+arch
        archivo= open ('ps.txt','r')
        respuesta=archivo.read()

    datos = pd.read_csv(arch+'.txt',error_bad_lines=False,engine="python",index_col=False,header=None)
    datos.to_excel(arch+".xlsx", index=False,header=False)

    return cs

@app.route("/imagen")
def laimagen():
    imagen.show()
    return "hola"

app.run(debug=True, port=5000)
