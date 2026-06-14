import mysql.connector

def connecter_bd():
   
    connexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crypt_decrypt_python"
    )
    return connexion
