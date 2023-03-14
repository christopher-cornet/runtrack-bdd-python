import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="laplateforme"
)

cursor = bd.cursor()

query = "select sum(superficie) from etage"

cursor.execute(query)

data = cursor.fetchone()

print('La superficie de La Plateforme est de', data[0], 'm2')

cursor.close()

# La superficie de La Plateforme est de 1000 m2