import pandas as pd

def censo(ruta_archivo_csv:str)->dict:
    if ruta_archivo_csv.endswith('.csv'):
        try:
            df = pd.read_csv(ruta_archivo_csv, sep=';')
        except:
            return 'Error al leer el archivo de datos'
        subconjunto=df[["DIRECTORIO","P1","P1S1","P8R","P9","P13","P23S1R"]]
        subconjunto2=df[["DIRECTORIO","P13"]]
        
        p13 = subconjunto2.groupby(['P13']).count()  
        print(p13)
    else:
        return 'Extension Invalida' 

    return p13.to_dict()

print(censo('https://raw.githubusercontent.com/bernoulli/MisionTIC2022/main/CHC_2020.csv'))