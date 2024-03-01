
#Lire les adresses mail dans un fichier texte
with open('adresse_email_To_Clean.txt',"r") as file:
    emails = file.read()
    print(emails)
# Retirer les doublons en convertissant la liste en un ensemble (set)
    