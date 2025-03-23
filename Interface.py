import tkinter as tk
from tkinter import messagebox
from Function import gestion_insertion, gestion_affichage
from main import fermer_connexion

# Fonction pour gérer l'insertion via l'interface
def inserer_utilisateur_interface():
    nom_utilisateur = entry_nom_utilisateur.get()
    mot_de_passe = entry_mot_de_passe.get()
    message = gestion_insertion(nom_utilisateur, mot_de_passe)

    if "succès" in message.lower():
        messagebox.showinfo("Succès", message)
        entry_nom_utilisateur.delete(0, tk.END)
        entry_mot_de_passe.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", message)

# Fonction pour afficher les utilisateurs décryptés
def afficher_utilisateurs_interface():
    resultats = gestion_affichage()
    texte_zone.delete("1.0", tk.END)
    for ligne in resultats:
        texte_zone.insert(tk.END, f"{ligne}\n")
    messagebox.showinfo("Succès", "Données décryptées et affichées.")

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Gestion des Utilisateurs")

# Champ pour le nom d'utilisateur
label_nom_utilisateur = tk.Label(fenetre, text="Nom d'utilisateur :")
label_nom_utilisateur.grid(row=0, column=0, padx=10, pady=5)
entry_nom_utilisateur = tk.Entry(fenetre, width=40)
entry_nom_utilisateur.grid(row=0, column=1, padx=10, pady=5)

# Champ pour le mot de passe
label_mot_de_passe = tk.Label(fenetre, text="Mot de passe :")
label_mot_de_passe.grid(row=1, column=0, padx=10, pady=5)
entry_mot_de_passe = tk.Entry(fenetre, show="*", width=40)
entry_mot_de_passe.grid(row=1, column=1, padx=10, pady=5)

# Bouton pour insérer les données
btn_inserer = tk.Button(fenetre, text="Insérer l'utilisateur", command=inserer_utilisateur_interface)
btn_inserer.grid(row=2, column=0, padx=10, pady=5)

# Bouton pour afficher les utilisateurs
btn_afficher = tk.Button(fenetre, text="Afficher les utilisateurs", command=afficher_utilisateurs_interface)
btn_afficher.grid(row=2, column=1, padx=10, pady=5)

# Zone de texte pour afficher les données
texte_zone = tk.Text(fenetre, height=10, width=50)
texte_zone.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



# Fermeture propre
fenetre.protocol("WM_DELETE_WINDOW", lambda: [fermer_connexion(), fenetre.destroy()])
fenetre.mainloop()