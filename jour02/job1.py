import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="laplateforme"
)

cursor = bd.cursor()

query = "SELECT * FROM etudiants"

cursor.execute(query) # Execute une requête en fonction de sa base de données

cursor.close()

# +----+-----------+----------+-----+---------------------------------+
# | id | nom       | prenom   | age | email                           |
# +----+-----------+----------+-----+---------------------------------+
# |  1 | Spaghetti | Betty    |  20 | betty.spaghetti@laplateforme.io |
# |  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
# |  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
# |  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
# |  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
# +----+-----------+----------+-----+---------------------------------+
# 5 rows in set (0.00 sec)