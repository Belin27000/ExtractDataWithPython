import pandas as pd
def txt_to_excel(input_file, output_file):
    #Lire le fichier texte dans un DataFrame pandas
    df=pd.read_csv(input_file, delimiter="\t", header=None) #Vous pouvez ajuster le delimiteur selon votre fichier

    # Enregistrer le dataframe dans un fichier Excel
    df.to_excel(output_file, index=False, header=False)  # Vous pouvez ajuster les options selon vos besoins

# chemin du fichier texte d'entrée et du fichier Excel de sortie
input_file = "adresse_email_To_Clean.txt"
output_file = "adresses_email_uniques.xlsx"

# Convertir le fichier texte en fichier Excel
txt_to_excel(input_file, output_file)

print("Convertion du fichier texte en fichier Excel terminée. Le fichier Excel est enregistré sous le nom adresses_email_uniques.xlsx")