import pandas as pd
datos = pd.read_csv('descarga.csv', header = 0)
df = pd.DataFrame(datos)

Asia = 0
Europe = 0
Africa = 0
America = 0
Oceania = 0

for i in range(1, len(df)):
    if df.loc[i,'continentExp'] == 'Asia':
        Asia = Asia + 1
    elif df.loc[i,'continentExp'] == 'Europe':
        Europe = Europe + 1
    elif df.loc[i,'continentExp'] == 'Africa':
        Africa = Africa + 1
    elif df.loc[i,'continentExp'] == 'America':
        America = America + 1
    elif df.loc[i,'continentExp'] == 'Oceania':
        Oceania = Oceania + 1
print('Numero de reportes en Asia', Asia)
print('Numero de reportes en Europa', Europe)
print('Numero de reportes en Africa',Africa)
print('Numero de reportes en America', America)
print('Numero de reportes en Oceania', Oceania)
print('\n')

Colombia = 0
for i in range(1, len(df)):
    if df.loc[i,'countriesAndTerritories'] == 'Colombia':
        Colombia = Colombia + 1
print('Numero de reportes en Colombia',Colombia)