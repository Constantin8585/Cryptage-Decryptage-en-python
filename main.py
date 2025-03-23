import DBconnect
from cryptography.fernet import Fernet
import os

# Dossier pour sauvegarder les clés
keys_folder = r"D:\main data\Abed work\Cryptage&Decryptage en python\Keys"

# Assurez-vous que le dossier Keys existe
if not os.path.exists(keys_folder):
    os.makedirs(keys_folder)

# Connexion à la base de données
connexion = DBconnect.connecter_bd()
curseur = connexion.cursor()

# Création de la table avec une colonne pour la clé associée
curseur.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_utilisateur VARCHAR(255),
    mot_de_passe TEXT,
    cle_fichier TEXT
)
""")


# Fonction pour générer une nouvelle clé et la sauvegarder
def generer_cle(nom_utilisateur):
    cle = Fernet.generate_key()
    chemin_cle = os.path.join(keys_folder, f"{nom_utilisateur}_key.key")
    with open(chemin_cle, "wb") as fichier_cle:
        fichier_cle.write(cle)
    return cle, chemin_cle


# Fonction pour insérer un utilisateur
def inserer_utilisateur(nom_utilisateur, mot_de_passe):
    # Générer une nouvelle clé pour l'utilisateur
    cle, chemin_cle = generer_cle(nom_utilisateur)
    cryptage = Fernet(cle)

    # Crypter le mot de passe avec la clé générée
    mot_de_passe_crypte = cryptage.encrypt(mot_de_passe.encode())

    # Insérer les données dans la base de données
    requete = "INSERT INTO utilisateurs (nom_utilisateur, mot_de_passe, cle_fichier) VALUES (%s, %s, %s)"
    curseur.execute(requete, (nom_utilisateur, mot_de_passe_crypte, chemin_cle))
    connexion.commit()
    print(
        f"Utilisateur inséré : Nom = {nom_utilisateur}, Mot de passe crypté = {mot_de_passe_crypte.decode()}, Clé sauvegardée = {chemin_cle}")


# Fonction pour afficher les utilisateurs avec décryptage
def afficher_utilisateurs():
    curseur.execute("SELECT nom_utilisateur, mot_de_passe, cle_fichier FROM utilisateurs")
    resultats = curseur.fetchall()
    utilisateurs = []

    for nom_utilisateur, mot_de_passe_crypte, cle_fichier in resultats:
        try:
            # Charger la clé depuis le fichier
            with open(cle_fichier, "rb") as fichier_cle:
                cle = fichier_cle.read()
            cryptage = Fernet(cle)

            # Décrypter le mot de passe
            mot_de_passe_decrypte = cryptage.decrypt(mot_de_passe_crypte.encode()).decode()
            utilisateurs.append(
                f"Nom d'utilisateur : {nom_utilisateur}, Mot de passe décrypté : {mot_de_passe_decrypte}")
        except Exception as e:
            utilisateurs.append(f"Nom d'utilisateur : {nom_utilisateur}, Erreur lors du décryptage : {str(e)}")

    return utilisateurs


# Fermer la connexion à la base
def fermer_connexion():
    connexion.close()