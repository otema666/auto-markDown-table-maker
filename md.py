import pandas as pd
from tabulate import tabulate

# Leemos el archivo de texto con la información de los archivos
with open('downloads.txt') as f:
    lines = f.readlines()

# Creamos una lista de diccionarios con la información de cada archivo
data = []
for line in lines:
    url, filepath = line.strip().split('\t')
    data.append({'url': url, 'path': filepath})

# Creamos un DataFrame con los datos de los archivos
df = pd.DataFrame(data, columns=["url", "path"])

# Creamos la tabla de Markdown
table = tabulate(df, headers="keys", tablefmt="pipe", showindex=False)

# Agregamos un título a la tabla
title = "Archivos descargados"
table = f"{title}\n\n{table}"

# Guardamos la tabla de Markdown en un archivo .md
with open("tabla.md", "w") as f:
    f.write(table)