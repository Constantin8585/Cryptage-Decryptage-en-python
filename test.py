# import mysql.connector
# from cryptography.fernet import Fernet
#
# # Chemin pour sauvegarder la clé
# cle_path = r"D:\main data\Abed work\Cryptage&Decryptage en python\cle.key"
#
# # Sauvegarder ou charger la clé
# try:
#     # Charger la clé si elle existe déjà
#     with open(cle_path, "rb") as fichier_cle:
#         cle = fichier_cle.read()
#     print(f"Clé chargée depuis : {cle_path}")
# except FileNotFoundError:
#     # Générer une nouvelle clé si le fichier n'existe pas
#     cle = Fernet.generate_key()
#     with open(cle_path, "wb") as fichier_cle:
#         fichier_cle.write(cle)
#     print(f"Nouvelle clé générée et sauvegardée à : {cle_path}")
#
# # Initialisation de l'objet de cryptage
# cryptage = Fernet(cle)
#
# # Connexion à la base de données MySQL
# connexion = mysql.connector.connect(
#     host="localhost",  # Remplace par l'adresse de ton serveur
#     user="root",  # Ton nom d'utilisateur MySQL
#     password="8585Abed8585oK",  # Ton mot de passe MySQL
#     database="crypt_decrypt_python"  # Le nom de ta base de données
# )
# curseur = connexion.cursor()
#
# # Création de la table si elle n'existe pas
# curseur.execute("""
# CREATE TABLE IF NOT EXISTS utilisateurs (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nom VARCHAR(255),
#     message_crypte TEXT
# )
# """)
#
# # Fonction pour insérer des données cryptées
# def inserer_donnees(nom, message):
#     message_crypte = cryptage.encrypt(message.encode())
#     requete = "INSERT INTO utilisateurs (nom, message_crypte) VALUES (%s, %s)"
#     curseur.execute(requete, (nom, message_crypte))
#     connexion.commit()
#     print(f"Données insérées : Nom = {nom}, Message (crypté) = {message_crypte.decode()}")
#
# # Fonction pour récupérer et décrypter les données
# def afficher_donnees():
#     curseur.execute("SELECT nom, message_crypte FROM utilisateurs")
#     for nom, message_crypte in curseur.fetchall():
#         # Convertir en bytes avant décryptage si nécessaire
#         message_decrypte = cryptage.decrypt(message_crypte.encode()).decode()
#         print(f"Nom : {nom}, Message décrypté : {message_decrypte}")
#
# # Exemple d'utilisation
# # Inserer une donnée
# inserer_donnees("Abed", "bonjour tout le monde")
#
# # Afficher les données décryptées
# afficher_donnees()
#
# # Fermer la connexion
# connexion.close()
