import DBconnect
from cryptography.fernet import Fernet


cle_path = r"D:\main data\Abed work\Cryptage&Decryptage en python\cle.key"


try:

    with open(cle_path, "rb") as fichier_cle:
        cle = fichier_cle.read()
    print(f"Clé chargée depuis : {cle_path}")
except FileNotFoundError:

    cle = Fernet.generate_key()
    with open(cle_path, "wb") as fichier_cle:
        fichier_cle.write(cle)
    print(f"Nouvelle clé générée et sauvegardée à : {cle_path}")

# Initialisation de l'objet de cryptage avec la clé chargée
cryptage = Fernet(cle)


connexion = DBconnect.connecter_bd()
curseur = connexion.cursor()


curseur.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    message_crypte TEXT
)
""")


def inserer_donnees(nom, message):
    message_crypte = cryptage.encrypt(message.encode())
    requete = "INSERT INTO utilisateurs (nom, message_crypte) VALUES (%s, %s)"
    curseur.execute(requete, (nom, message_crypte))
    connexion.commit()
    print(f"Données insérées : Nom = {nom}, Message crypté = {message_crypte.decode()}")


def afficher_donnees():
    curseur.execute("SELECT nom, message_crypte FROM utilisateurs")
    for nom, message_crypte in curseur.fetchall():
        # Décryptage des messages récupérés
        message_decrypte = cryptage.decrypt(message_crypte.encode()).decode()
        print(f"Nom : {nom}, Message décrypté : {message_decrypte}")



#inserer_donnees("Cryptage", "bonjour tout le monde")

afficher_donnees()


connexion.close()
