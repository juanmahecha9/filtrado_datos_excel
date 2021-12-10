import pandas as pd
import json
# Lectura archivo json
with open('project/function/config/location.json') as file:
    data = json.load(file)


def filter_location(path_in,file_name, path_out):
    # Dividir el nombre del archivo para captura la ciudad
    city = file_name.split()
    print(file_name)
    # Lectura del archivo
    input_cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    df = pd.read_excel(path_in+file_name+".xlsx", index_col=0, header=0, usecols=input_cols)
    
    state = []

    if(city[1] == "RN"):
       print(f"Ejecutando filtro de locacion ",city[1], " Para los sitios de entrenamiento de: ",data['rn'])
       for local in data['rn']:
           df1 = df[df["Local de Treinamento"] == local]
           
           # Filas y columnas para evaluar si hay o no informacion filtrada
           (row,col) = df1.shape
           if(row < 2):
              state.append({"local": "No hay datos relacionado con: "+local})
           if(row >1):
                df1.to_excel(path_out+local+".xlsx", header = True, index= True)
                state.append({"local": "Filtrados por: "+local})
    else:
        print(f"Ejecutando filtro de locacion ",city[1], " Para los sitios de entrenamiento de: ",data['sp'])
        for local in data['sp']:
            df1 = df[df["Local de Treinamento"] == local]
            
            (row,col) = df1.shape
            if(row < 2):
                state.append({"local": "No hay datos relacionado con: "+local})
            if(row >1):
                df1.to_excel(path_out+local+".xlsx", header = True, index= True)
                state.append({"local": "Filtrados por: "+local})

    return state
