import pandas as pd

def date_filter_file(file_path_in,file_path_out, date_filter):
    print("Ejecutando filtro de fechas")
    input_cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    df = pd.read_excel(file_path_in, index_col=0, header=0, usecols=input_cols)

    df_cols_name = df.columns
    print(df_cols_name)
    print(f"La fecha que se esta filtrando es: ",date_filter)

    #Aplicacion de un filtro
    df1 = df[df["DATA DE ADMISSÃO"] == date_filter]
    print(df1)
    df1.append({"SOLICITAÇÃO DE DNA": "Bot agent 6"}, ignore_index=True)

    #Exportar el dataframe
    df1.to_excel(file_path_out, header = True, index= True)
    
    # Filas y columnas para evaluar si hay o no informacion filtrada
    (row,col) = df1.shape
    if(row < 2):
        return "No existen datos"
    if(row >1):
        return "Estado ok"