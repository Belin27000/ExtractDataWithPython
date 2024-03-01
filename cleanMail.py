
#Lire les adresses mail dans un fichier texte
with open('adresse_email_To_Clean.txt',"r") as file:
    emails = file.readlines()
    print(emails)
# Retirer les doublons en convertissant la liste en un ensemble (set)
unique_emails = set(emails)
with open("adresses_email_uniques.txt","w") as file:
    for email in unique_emails:
        file.write(email)
print("Les adresses e-mail uniques ont été enregistrées dans adresses_email_uniques.txt")
