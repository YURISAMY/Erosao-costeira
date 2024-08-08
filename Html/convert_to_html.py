# primeiramente importamos as bibliotecas que serão usadas no processo
import zipfile as zipfile 
import pandas as pd

#criação da lista vazia que receberá o conteudo de cada arquivo um apos o outro durante o for
for_concat = []

# AGORA PASSO A PASSO DA SINTAXE DE ABRIR UM ARQUIVO E INCLUI-LO NUMA SÓ LISTA

#with zipfile.ZipFile (caminho do arquivo, 'tipo da leitura (r,w)') as nome_da_variavel:

import pandas as pd 
with zipfile.ZipFile ('Documents/projetos/Bolsa/jupyternotebooks/postos.zip', 'r') as t:

# O comando with serve principalmente para garantir que o arquivo será finalizando ao fim da execução

    # for variavel_nome_arquivos in nome_da_variavel.namelist():
    for arq in t.namelist():
        
    # O variavel_nome_arquivos é uma variavel criada para receber o nome de cada arquivo dentro do zip
    # Basicamente, 'arq' vai receber o nome dos arquivos do zipfile conhecido como 't', um a um, e 
    # entrará no loop de repetição até que o ultimo arquivo seja lido e atribuido a 'arq'

        #if nome_do_arquivo.endswith(.extensão (txt,csv,zip,rar.xlss)):
        if arq.endswith('.txt'):
            
        # se o nome do arquivo terminar com .txt faça:

            # with nome_da_variavel.open(arq) as nome_do_arquivo_aberto
            with t.open(arq) as f:
                
            # abra o arquivo dentro do zip nomeado de 'arq' chamando ele de f

# DataFrame = pd.read_extensão(nome_do_arquivo_aberto ou caminho, delimiter = 'termo de seperação')
                df = pd.read_csv(f,delimiter = ';')

                #um dataframe recebe oque for lido do arquivo 'tal' separando por 'termo'

                for_concat.append(df)

                #a lista vazia criada antes, escreve na ultima posição oque tiver em 'df'

registros_chuvas = pd.concat(for_concat)

registros_chuvas.reset_index(drop=True, inplace=True)
registros_chuvas.to_json('registros_chuvas.json')

