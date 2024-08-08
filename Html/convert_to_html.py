import pandas as pd 

Municio = pd.read_csv('C:\Users\yurii\Documents\GitHub\respositorio erosão costeira\CSV archives\postos\1.txt', delimiter = ';')

Municio.to_html('C:\Users\yurii\Documents\GitHub\respositorio erosão costeira\CSV archives\postos\1.txt.html')

