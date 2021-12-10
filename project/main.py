import requests
from flask import Flask, jsonify, request, render_template
import time
import os
from config import config
# Importar las funciones de filtro
from function.filter_date import date_filter_file
from function.filter_location import filter_location

# Iniciar servicio de flask
app = Flask(__name__)

@app.after_request
def after_request(response):
    # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

# Ruta principal
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Ruta pra filtro por fecha
@app.route('/filter_date/<file_name>/<date>/<month>/<year>/<file_out_name>', methods=['GET'])
def filter_date(file_name:None, file_out_name:None, date:None, month:None, year:None):

    path_in = "/Users/juanmaheha/Desktop/excel_filter/doc/"+file_name+".xlsx"
    path_out = "/Users/juanmaheha/Desktop/excel_filter/doc/"+file_out_name+".xlsx"
    filter =  str(year)+ "-" + str(month) + "-" + str(date)

    date_filter_file(path_in, path_out, filter)

    return {
        "Filtro de fecha aplicado a":path_in,
        "Filtro de fecha": filter,
        "Archivo de salida": path_out
    }
# Ruta de filtrado por locacion
@app.route('/locacion/<file_name>', methods=['GET'])
def locacion(file_name:None):
    path = "/Users/juanmaheha/Desktop/excel_filter/doc/"    
    data = filter_location(path,file_name, path)
    return data

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(host="0.0.0.0", port=5000)