import os, sys
from flask import Flask, render_template, abort
from fabiker import tanper
app = Flask(__name__)
@app.route('/')
def pintahola():
    try:
        tanteo = open('envivo.csv', 'r')
        parciales, teams = tanper(tanteo)
        tanteo.close()
    except IOError:
        abort(404)
    return render_template('template5.html', teams=teams, parciales=parciales)

if __name__ == '__main__':
    app.run()


#salida=''
#    for cuarto, parcial in parciales.items():
#        salida+='{}º Cuarto.&emsp;'.format(cuarto)
#        for equipo, puntos in parciales.items():
#            salida+='{}:{}:&emsp;'.format(teams[equipo], puntos)
#        salida+='<br>'