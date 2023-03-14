import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="laplateforme"
)

cursor = bd.cursor()

query = "CREATE TABLE etage (id INT primary key AUTO_INCREMENT, nom VARCHAR(255), numero INT, superficie INT);"
query2 = "CREATE TABLE salles (id INT primary key AUTO_INCREMENT, nom VARCHAR(255), id_etage INT, capacite INT);"

cursor.execute(query) # Execute une requête en fonction de sa base de données
cursor.execute(query2)

cursor.close()

# +------------------------+
# | Tables_in_laplateforme |
# +------------------------+
# | etage                  |
# | etudiants              |
# | salles                 |
# +------------------------+
# 3 rows in set (0.00 sec)