
import zipfile as zipfile 
import pandas as pd

for_concat = []

import pandas as pd 
with zipfile.ZipFile ('Documents/projetos/Bolsa/jupyternotebooks/postos.zip', 'r') as t:
   
    for arq in t.namelist():
             
        if arq.endswith('.txt'):
                    
            with t.open(arq) as f:
                
                df = pd.read_csv(f,delimiter = ';')

                for_concat.append(df)

registros_chuvas = pd.concat(for_concat)
registros_chuvas.reset_index(drop=True, inplace=True)
registros_chuvas.to_json('registros_chuvas.json')

