import DBconnect
from cryptography.fernet import Fernet

# Chemin pour sauvegarder ou récupérer la clé
cle_path = r"D:\main data\Abed work\Cryptage&Decryptage en python\Keys\cle.key"

# Charger ou générer une clé
def charger_cle():
    try:
        with open(cle_path, "rb") as fichier_cle:
            cle = fichier_cle.read()
        print(f"Clé chargée depuis : {cle_path}")
    except FileNotFoundError:
        cle = Fernet.generate_key()
        with open(cle_path, "wb") as fichier_cle:
            fichier_cle.write(cle)
        print(f"Nouvelle clé générée et sauvegardée à : {cle_path}")
    return cle

# Initialisation du cryptage
cle = charger_cle()
cryptage = Fernet(cle)

# Connexion à la base de données
connexion = DBconnect.connecter_bd()
curseur = connexion.cursor()

# Création de la table si elle n'existe pas
curseur.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_utilisateur VARCHAR(255),
    mot_de_passe TEXT
)
""")

# Fonction pour insérer un utilisateur
def inserer_utilisateur(nom_utilisateur, mot_de_passe):
    mot_de_passe_crypte = cryptage.encrypt(mot_de_passe.encode())
    requete = "INSERT INTO utilisateurs (nom_utilisateur, mot_de_passe) VALUES (%s, %s)"
    curseur.execute(requete, (nom_utilisateur, mot_de_passe_crypte))
    connexion.commit()
    print(f"Utilisateur inséré : Nom = {nom_utilisateur}, Mot de passe crypté = {mot_de_passe_crypte.decode()}")

# Fonction pour afficher les utilisateurs
def afficher_utilisateurs():
    curseur.execute("SELECT nom_utilisateur, mot_de_passe FROM utilisateurs")
    resultats = curseur.fetchall()
    utilisateurs = []
    for nom_utilisateur, mot_de_passe_crypte in resultats:
        mot_de_passe_decrypte = cryptage.decrypt(mot_de_passe_crypte.encode()).decode()
        utilisateurs.append(f"Nom d'utilisateur : {nom_utilisateur}, Mot de passe : {mot_de_passe_decrypte}")
    return utilisateurs

# Fermer la connexion à la base
def fermer_connexion():
    connexion.close()