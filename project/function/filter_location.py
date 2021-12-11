import pandas as pd
import json
# Lectura archivo json
with open('project/function/config/location.json') as file:
    data = json.load(file)


def filter_location(params):
    text = params.split(";")
    path_temp = text[0]
    file_name = text[1]
    # Dividir el nombre del archivo para captura la ciudad
    city = file_name.split(" ")
    print(file_name)
    # Lectura del archivo
    input_cols = list(range(20))
    df = pd.read_excel(path_temp+"/"+file_name+".xlsx", index_col=0, header=0, usecols=input_cols)
    
    state = []

    to_loop = data['rn'] if city[1] == 'RN' else data['sp']
    print(f"Ejecutando filtro de locacion ",city[1], " Para los sitios de entrenamiento de: ",data['rn'])
    for local in to_loop:
        df_local = df[df["Local de Treinamento"] == local]
        
        # Filas y columnas para evaluar si hay o no informacion filtrada
        rows = len(df)
        if(rows < 2):
            state.append({"local": "No hay datos relacionado con: "+local})
        else:
            df_local["SOLICITAÇÃO DE DNA"] = "AgentBot"
            df_local.to_excel(path_temp+"/"+local+".xlsx", header = True, index= True)
            state.append({"local": "Filtrados por: "+local})
    return json.dumps(state)
