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
        mettre_a_jour_tableau()  # Met à jour le tableau des utilisateurs inscrits
    else:
        messagebox.showerror("Erreur", message)


# Fonction pour décrypter et afficher le mot de passe d'un utilisateur spécifique
def afficher_mot_de_passe(nom_utilisateur):
    resultats = gestion_affichage()
    for ligne in resultats:
        if nom_utilisateur in ligne:
            messagebox.showinfo("Mot de passe décrypté", ligne)
            break


# Fonction pour mettre à jour le tableau des utilisateurs inscrits
def mettre_a_jour_tableau():
    # Efface le tableau existant
    for widget in tableau_frame.winfo_children():
        widget.destroy()

    # Ajoute les en-têtes du tableau
    tk.Label(tableau_frame, text="Nom d'utilisateur", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(tableau_frame, text="Actions", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5, pady=5)

    # Récupère les utilisateurs inscrits
    resultats = gestion_affichage()
    for i, ligne in enumerate(resultats, start=1):
        nom_utilisateur = ligne.split(",")[0].split(":")[1].strip()  # Extrait le nom d'utilisateur
        tk.Label(tableau_frame, text=nom_utilisateur, font=("Arial", 10)).grid(row=i, column=0, padx=5, pady=5)

        # Ajoute un bouton pour décrypter et afficher le mot de passe
        btn_decrypter = tk.Button(tableau_frame, text="Déchiffrer",
                                  command=lambda u=nom_utilisateur: afficher_mot_de_passe(u))
        btn_decrypter.grid(row=i, column=1, padx=5, pady=5)


# Interface graphique principale
fenetre = tk.Tk()
fenetre.title("Gestion des Utilisateurs (Cryptés)")

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

# Bouton pour afficher les données (mise à jour tableau)
btn_afficher = tk.Button(fenetre, text="Mettre à jour le tableau", command=mettre_a_jour_tableau)
btn_afficher.grid(row=2, column=1, padx=10, pady=5)

# Zone pour afficher le tableau des utilisateurs inscrits
tableau_frame = tk.Frame(fenetre)
tableau_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Lancer la mise à jour initiale du tableau
mettre_a_jour_tableau()

# Fermeture propre
fenetre.protocol("WM_DELETE_WINDOW", lambda: [fermer_connexion(), fenetre.destroy()])
fenetre.mainloop()