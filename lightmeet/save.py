
# Sauvegarde de base avant migration vers la nouvelle base créé avec la nouvelle structure
# Enregistrer la base db.sqlite3 présente sur le serveur et la renommer en dbsave.sqlite3
#
# Étape 1 : Migrer la table dbsave vers tables dump sans une base car elle doit être renouvellé :

# sqlite3 dbsave.sqlite3 ".dump" > tables_dump.sql


# Étape 2 : Créer la nouvelle base :
# python manage.py runserver 8081
# python manage.py makemigrations
# python manage.py migrate

# Envoyer l'ancienne base enregistrée sur la nouvelle
# Étape 3 : Envoyer la table dump vers la nouvelle base :
# sqlite3 db.sqlite3 < tables_dump.sql