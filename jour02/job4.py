import mysql.connector

bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpwd",
    database="laplateforme"
)

cursor = bd.cursor()

query = "select nom, capacite from salles;"

cursor.execute(query)

cursor.close()

# +--------------+----------+
# | nom          | capacite |
# +--------------+----------+
# | Lounge       |      100 |
# | Studio Son   |        5 |
# | Broadcasting |       50 |
# | Bocal Peda   |        4 |
# | Coworking    |       80 |
# | Studio Video |        5 |
# +--------------+----------+
# 6 rows in set (0.00 sec)