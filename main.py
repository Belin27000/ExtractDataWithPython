# import re
# import pdfplumber
# with pdfplumber.open("votre_fichier.pdf") as pdf:
#     page = pdf.pages[27]
#     text= page.extract_text()
# print(text)
# # for line in text.split('\n'):
# #     print(line)

# #Contact company
# company_re=re.compile("(?=PRÉSENTATION DE L’ENTREPRISE)")
# company = company_re.search(text).group(0)
# # email_re=re.compile("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)")
# # text_email=email_re.search(text).group(0)
# # print(text_email)
# print(company)

#---------------------------------------------
# import re
# import pdfplumber

# def extract_company_info(page_text):
#     company_info_list = []
#     blocks = re.split(r'\n-{5,}\n', page_text)
#     # Utilisation de regex pour trouver toutes les occurrences de l'entreprise et ses informations
#     matches = re.findall(r"(.*?)\nPRÉSENTATION DE L’ENTREPRISE(.*?)CONTACT\n(.*?)\n", page_text, re.DOTALL)
#     for match in matches:
#         company_info = {}
#         company_info["nom_entreprise"] = match[0].strip()
#         company_info["presentation"] = match[1].strip()
#         company_info["contact"] = match[2].strip()
#         company_info_list.append(company_info)
#     return company_info_list

# with pdfplumber.open("votre_fichier.pdf") as pdf:
#     all_company_info = []

#     for page_number in range(23,27):
#         page=pdf.pages[page_number]
#         text = page.extract_text()
#         company_info = extract_company_info(text)
#         all_company_info.extend(company_info)

# # Affichage des informations extraites pour chaque entreprise
# for company_info in all_company_info:
#     print("Nom de l'entreprise:", company_info.get("nom_entreprise"))
#     # print("Présentation:", company_info.get("presentation"))
#     print("Contact:", company_info.get("contact"))
#     print("-" * 50)
#---------------------------------------------
# import re
# import pdfplumber

# def extract_company_info(page_text):
#     company_info_list = []
#     # Utilisation de regex pour trouver les informations de chaque entreprise
#     matches = re.finditer(r"(.*?)\nPRÉSENTATION DE L’ENTREPRISE(.*?)CONTACT\n(.*?)\n", page_text, re.DOTALL)
#     for match in matches:
#         company_info = {}
#         company_info["nom_entreprise"] = match.group(1).strip()
#         company_info["presentation"] = match.group(2).strip()
#         company_info["contact"] = match.group(3).strip()
#         company_info_list.append(company_info)
#     return company_info_list

# with pdfplumber.open("votre_fichier.pdf") as pdf:
#     all_company_info = []

#     for page_number in range(23,27):
#         page = pdf.pages[page_number]
#         text = page.extract_text()
#         company_info = extract_company_info(text)
#         all_company_info.extend(company_info)

# # Affichage des informations extraites pour chaque entreprise
# for company_info in all_company_info:
#     print("Nom de l'entreprise:", company_info.get("nom_entreprise"))
#     # print("Présentation:", company_info.get("presentation"))
#     print("Contact:", company_info.get("contact"))
#     print("-" * 50)

# import re
# import pdfplumber

# def extract_company_info(page_text):
#     company_info_list = []
#     # Utilisation de regex pour trouver les informations de chaque entreprise
#     matches = re.finditer(r"(.*?)\nPRÉSENTATION DE L’ENTREPRISE(.*?)CONTACT\n(.*?)\n", page_text, re.DOTALL)
#     for match in matches:
#         company_info = {}
#         company_info["nom_entreprise"] = match.group(1).strip()
#         company_info["presentation"] = match.group(2).strip()
#         company_info["contact"] = match.group(3).strip()
#         company_info_list.append(company_info)
#     return company_info_list

# with pdfplumber.open("votre_fichier.pdf") as pdf:
#     all_company_info = []

#     for page_number in range(23, 27):
#         page = pdf.pages[page_number]
#         text = page.extract_text()
#         num_presentations = text.count("PRÉSENTATION DE L’ENTREPRISE")
#         companies = extract_company_info(text)
#         for i in range(min(num_presentations, len(companies))):
#             company_info = companies[i]
#             all_company_info.append(company_info)

# # Affichage des informations extraites pour chaque entreprise
# for company_info in all_company_info:
#     print("Nom de l'entreprise:", company_info.get("nom_entreprise"))
#     # print("Présentation:", company_info.get("presentation"))
#     print("Contact:", company_info.get("contact"))
#     print("-" * 50)
# import pdfplumber

# # Chemin vers le fichier PDF
# pdf_file = "votre_fichier.pdf"

# # Pages à extraire
# start_page = 23
# end_page = 25

# # Nom du fichier texte de sortie
# output_file = "pages_23_25.txt"

# # Ouvrir le fichier PDF
# with pdfplumber.open(pdf_file) as pdf:
#     # Créer un fichier texte de sortie
#     with open(output_file, "w", encoding="utf-8") as output:
#         # Parcourir les pages spécifiées
#         for page_number in range(start_page, end_page + 1):
#             # Extraire le texte de la page
#             page = pdf.pages[page_number]
#             text = page.extract_text()
            
#             # Écrire le texte dans le fichier de sortie
#             output.write(f"Page {page_number}:\n{text}\n\n")

# print("Extraction terminée. Le texte a été enregistré dans", output_file)

# import pdfplumber
# from pprint import pprint

# # Chemin vers le fichier PDF
# pdf_file = "votre_fichier.pdf"

# # Pages à extraire
# start_page = 23
# end_page = 245

# # Nom du fichier texte de sortie
# output_file = (f"extraction Page_{start_page}_To_{end_page}.txt")

# # Ouvrir le fichier PDF
# with pdfplumber.open(pdf_file) as pdf:
#     # Ouvrir le fichier de sortie en mode écriture
#     with open(output_file, "w", encoding="utf-8") as output:
#         # Parcourir les pages spécifiées
#         for page_number in range(start_page, end_page + 1):
#             # Extraire le texte de la page
#             page = pdf.pages[page_number]
#             text = page.extract_text()

#             # Ajouter les étiquettes devant les champs appropriés
#             text_with_labels = text.replace("Adresse", "Adresse:").replace("Téléphone", "Téléphone:").replace("Email", "Email:").replace("Site web", "Site web:")

#             # Écrire le texte avec les étiquettes dans le fichier de sortie
#             output.write(f"Page {page_number}:\n{text_with_labels}\n\n")

# print("Extraction terminée. Le texte avec les étiquettes a été enregistré dans", output_file)

# import pdfplumber

# # Chemin vers le fichier PDF
# pdf_file = "votre_fichier.pdf"

# # Pages à extraire
# start_page = 23
# end_page = 245

# # Nom du fichier texte de sortie
# output_file = f"extraction_Page_{start_page}_To_{end_page}.txt"

# # Ouvrir le fichier PDF
# with pdfplumber.open(pdf_file) as pdf:
#     # Ouvrir le fichier de sortie en mode écriture
#     with open(output_file, "w", encoding="utf-8") as output:
#         # Parcourir les pages spécifiées
#         for page_number in range(start_page, end_page + 1):
#             # Extraire le texte de la page
#             page = pdf.pages[page_number]
#             text = page.extract_text()

#             # Diviser le texte en lignes
#             lines = text.split("\n")

#             # Parcourir chaque ligne
#             for line in lines:
#                 # Vérifier si la ligne est en majuscules et n'est pas CONTACT ou PRÉSENTATION DE L'ENTREPRISE
#                 if line.isupper() and "CONTACT" not in line and "PRÉSENTATION DE L’ENTREPRISE" not in line:
#                     # Ajouter le numéro de page devant la ligne
#                     output.write(f"Page {page_number}: {line}\n")

# print("Extraction terminée. Le texte avec les numéros de page a été enregistré dans", output_file)
# import pdfplumber
# import re

# # Chemin vers le fichier PDF
# pdf_file = "votre_fichier.pdf"

# # Pages à extraire
# start_page = 23
# end_page = 245

# # Nom du fichier texte de sortie
# output_file = f"texte_majuscules_sans_emails_Page_{start_page}_To_{end_page}.txt"

# # Expression régulière pour rechercher les adresses e-mail
# email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# # Ouvrir le fichier PDF
# with pdfplumber.open(pdf_file) as pdf:
#     # Ouvrir le fichier de sortie en mode écriture
#     with open(output_file, "w", encoding="utf-8") as output:
#         # Parcourir les pages spécifiées
#         for page_number in range(start_page, end_page + 1):
#             # Extraire le texte de la page
#             page = pdf.pages[page_number]
#             text = page.extract_text()

#             # Extraire le nom de l'entreprise
#             company_name = None
#             match = re.search(r"PRÉSENTATION DE L’ENTREPRISE\n(.*?)\n", text)
            
#             # Rechercher toutes les adresses e-mail dans le texte de la page
#             email_matches = re.findall(email_regex, text)

#             for email in email_matches:
#                 text = text.replace(email, "")
#             # Extraire les lignes en majuscules qui ne sont pas des adresses e-mail
#             upper_lines = [line.strip() for line in text.split("\n") if line.isupper() and "PRÉSENTATION DE L’ENTREPRISE" not in line]

#             # Ecrire les ligne en majuscules dans le fichier de sortie
#             for line in upper_lines:
#                 output.write(line + "\n")

# print("Extraction des lignes en majuscules terminée. Les données ont été enregistrées dans", output_file)

import pdfplumber
import re

# Chemin vers le fichier PDF
pdf_file = "votre_fichier.pdf"

# Pages à extraire
start_page = 23
end_page = 28

# Nom du fichier texte de sortie
output_file = f"texte_ordonne_Page_{start_page}_To_{end_page}.txt"

# Expression régulière pour rechercher les adresses e-mail
email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

# Ouvrir le fichier PDF
with pdfplumber.open(pdf_file) as pdf:
    # Ouvrir le fichier de sortie en mode écriture
    with open(output_file, "w", encoding="utf-8") as output:
        # Parcourir les pages spécifiées
        for page_number in range(start_page, end_page + 1):
            # Extraire le texte de la page
            page = pdf.pages[page_number]
            text = page.extract_text()

            # Diviser le texte en blocs de lignes
            lines = text.split("\n")

            # Écrire chaque bloc de lignes dans le fichier de sortie
            for line in lines:
                # Rechercher toutes les adresses e-mail dans la ligne
                email_matches = re.findall(email_regex, line)

                # Supprimer les adresses e-mail de la ligne
                for email in email_matches:
                    line = line.replace(email, "")

                # Si la ligne contient du texte, écrire la ligne dans le fichier de sortie
                if line.strip():
                    output.write(line.strip() + "\n")

                # Écrire les adresses e-mail trouvées dans la ligne
                for email in email_matches:
                    output.write(email + "\n")

print("Extraction du texte ordonné terminée. Les données ont été enregistrées dans", output_file)
