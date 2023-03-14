import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="laplateforme"
)

cursor = bd.cursor()

query = "INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500), ('R+1', 1, 500);"
query2 = "INSERT INTO salles (nom, id_etage, capacite) VALUES ('Lounge', 1, 100), ('Studio Son', 1, 5), ('Broadcasting', 2, 50), ('Bocal Peda', 2, 4), ('Coworking', 2, 80), ('Studio Video', 2, 5);"

# Export : mysqldump -u root -p laplateforme > C:\Users\tophe\Desktop\jour02\job03.sql"

cursor.execute(query) # Execute une requête en fonction de sa base de données
cursor.execute(query2)

cursor.close()