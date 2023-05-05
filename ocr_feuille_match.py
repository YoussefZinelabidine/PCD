#un fichier csv unique qui contient toutes les tables:ETAPE1
import tabula
import pandas as pd
import csv
import json

pdf_path = "C:/Users/HP/Desktop/feuille_match.pdf"#chemin du fichier input
pages = "1-3"

# Créer une liste pour stocker les DataFrames de chaque page
dfs = []

# Boucler sur chaque page et extraire le tableau
for i, df in enumerate(tabula.read_pdf(pdf_path, pages=pages, pandas_options={'header': None})):
    # Ajouter une colonne pour identifier la page
    df["Page"] = i + 1
    dfs.append(df)

# Concaténer tous les DataFrames en un seul
merged_df = pd.concat(dfs)

# Supprimer la colonne "Page" du DataFrame fusionné
merged_df = merged_df.drop(columns=["Page"])

# Enregistrer le DataFrame fusionné en tant que fichier CSV sans en-tête
merged_df.to_csv("merged_tables.csv", header=None, index=False)


#séparer le fichier merged_table ,chaque tableau sera mis dans un fichier csv /ETAPE2
current_file = None
current_key = None

with open("merged_tables.csv", "r") as f:
    for line in f:
        if line.startswith(",,Titulaires"):
            current_key = "Titulaires"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif line.startswith(",,Remplacants"):
            current_key = "Remplacants"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif line.startswith(",,Staff"):
            current_key = "Staff"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif line.startswith(",REMPLACEMENTS"):
            current_key = "Remplacements"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif line.startswith(",OFFICIELS DU MATCH,,"):
            current_key = "Officiels"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif line.startswith(",JOUEURS AVERTIS"):
            current_key = "Avertissements"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif line.startswith(",JOUEURS EXPULS"):
            current_key = "Expulsions"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif current_file:
            current_file.write(line)
        elif line.startswith(",JOUEURS BLESS"):
            current_key = "Blessures"
            if current_file:
                current_file.close()
            current_file = open(f"{current_key}.csv", "w")
        elif current_file:
            current_file.write(line)
    if current_file:
        current_file.close()




#rtedefinir les colonnes correctement  /ETAPE3

with open('Titulaires.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

for row in data:
    row[2] = row[2].replace(' ', ',', 2)

with open('Titulaires.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)



with open('Remplacants.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

for row in data:
    row[2] = row[2].replace(' ', ',', 2)

with open('Remplacants.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)



df = pd.read_csv('Staff.csv')
df.iloc[:, 1] = df.iloc[:, 1].str.replace(' ', ',', 1)
df.to_csv('Staff.csv', index=False)



df = pd.read_csv('Remplacements.csv', header=None)
df.iloc[:, 0] = df.iloc[:, 0].str.replace(' ', ',', 2)
df.to_csv('Remplacements.csv', index=False, header=None)


df = pd.read_csv('Avertissements.csv', header=None)
df.iloc[:, 1] = df.iloc[:, 1].str.replace(' ', ',', 2)
df.to_csv('Avertissements.csv', index=False, header=None)

#prtie infos du match(metadata)

page_width =1000
page_height = 3000

left = 0
top = 0
right = page_width
bottom = page_height / 3

tabula.convert_into(pdf_path, "metadata.csv", output_format="csv", pages='1', area=[left, top, right, bottom])



# Spécifier l'encodage du fichier CSV à utiliser lors de la lecture
df = pd.read_csv("metadata.csv", header=None, encoding='ISO-8859-1')

df = df.iloc[1:5, 1:2]
df.to_csv("metadata.csv", index=False, header=False)




#convertir en fichier metadata.json
with open('metadata.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    lieu = next(csv_reader)[0]
    date, horaire = next(csv_reader)[0].split(' ')
    score = next(csv_reader)[0]
    equipes = next(csv_reader)[0]

   

metadata = {
    "lieu": lieu,
    "date": date,
    "horaire": horaire,
    "score": score,
    "equipess_adversaires":equipes
}

with open('metadata.json', mode='w') as json_file:
    json.dump(metadata, json_file,indent=4)



#conversiuon des fichiers csv en .json   :ETAPE4

titulaires = []

with open('Titulaires.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        values = row[0].split(',') + row[1].split(',') + row[2].split(',')
        num, nom_prenom, licence = values[0], values[1], values[2]
        obj = {'num': num, 'nom_prenom': nom_prenom, 'licence': licence}
        titulaires.append(obj)

with open('Titulaires.json', 'w') as file:
    json.dump({'titulaires': titulaires}, file, indent=4)





# Remplacants.csv
remplacants = []
with open('Remplacants.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        values = row[0].split(',') + row[1].split(',') + row[2].split(',')
        num, nom_prenom, licence = values[0], values[1], values[2]
        obj = {'num': num, 'nom_prenom': nom_prenom, 'licence': licence}
        remplacants.append(obj)
with open('Remplacants.json', 'w') as file:
    json.dump({'remplacants': remplacants}, file, indent=4)

# Staff.csv
staff = []
with open('Staff.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        values = row[0].split(',') + row[1].split(',')
        nom_prenom, licence = values[0], values[1]
        obj = {'nom_prenom': nom_prenom, 'licence': licence}
        staff.append(obj)
with open('Staff.json', 'w') as file:
    json.dump({'staff': staff}, file, indent=4)

# Remplacements.csv
remplacements = []
with open('Remplacements.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        values = row[0].split(',') + row[1].split(',') + row[2].split(',') + row[3].split(',')
        equipe, minute, joueur_entrant, joueur_sortant = values[0], values[1], values[2], values[3]
        obj = {'equipe': equipe, 'minute': minute, 'joueur_entrant': joueur_entrant, 'joueur_sortant': joueur_sortant}
        remplacements.append(obj)
with open('Remplacements.json', 'w') as file:
    json.dump({'remplacements': remplacements}, file, indent=4)

# Officiels.csv
officiels = []
with open('Officiels.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        values = row[0].split(',') + row[1].split(',')
        poste, nom_prenom = values[0], values[1]
        obj = {'poste': poste, 'nom_prenom': nom_prenom}
        officiels.append(obj)
with open('Officiels.json', 'w') as file:
    json.dump({'officiels': officiels}, file, indent=4)

# Avertissements.csv
avertissements = []
with open('Avertissements.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        values = row[0].split(',') + row[1].split(',') + row[2].split(',') + row[3].split(',')
        nom_prenom, licence, club, minute = values[0], values[1], values[2], values[3]
        obj = {'nom_prenom': nom_prenom, 'licence': licence, 'club': club, 'minute': minute}
        avertissements.append(obj)
with open('Avertissements.json', 'w') as file:
    json.dump({'avertissements': avertissements}, file, indent=4)



#fusionner les json files en un seul:ETAPE5
import json

file_names = ["metadata.json","Titulaires.json", "Remplacants.json", "Staff.json", "Remplacements.json", "Officiels.json", "Avertissements.json"]
output_file = "output.json"

data = {}
for file_name in file_names:
    with open(file_name) as f:
        data.update(json.load(f))

with open(output_file, "w") as f:
    json.dump(data, f, indent=4)


#les resultats sont dans le fichier output.json