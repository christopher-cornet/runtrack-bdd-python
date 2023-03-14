import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="laplateforme"
)

cursor = bd.cursor()

query = "select sum(capacite) from salles"

cursor.execute(query)

data = cursor.fetchone()

print('La capacite de toutes les salles est de :', data[0])

cursor.close()

# La capacite de toutes les salles est de : 244