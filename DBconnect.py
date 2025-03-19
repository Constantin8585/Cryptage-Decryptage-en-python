import mysql.connector

def connecter_bd():
    # Détails de connexion à la base de données
    connexion = mysql.connector.connect(
        host="localhost",  # Adresse du serveur MySQL
        user="root",       # Ton nom d'utilisateur
        password="8585Abed8585oK",  # Ton mot de passe MySQL
        database="crypt_decrypt_python"  # Nom de ta base de données
    )
    return connexion
