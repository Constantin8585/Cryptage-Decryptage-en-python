from main import inserer_utilisateur, afficher_utilisateurs, fermer_connexion

# Fonctions centralisées pour l'interface graphique
def gestion_insertion(nom_utilisateur, mot_de_passe):
    if nom_utilisateur and mot_de_passe:
        inserer_utilisateur(nom_utilisateur, mot_de_passe)
        return "Utilisateur inséré avec succès."
    else:
        return "Erreur : Les champs doivent être remplis."

def gestion_affichage():
    resultats = afficher_utilisateurs()
    return resultats