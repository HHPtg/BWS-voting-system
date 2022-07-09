import sqlite3

db = sqlite3.connect('website/database.db')
cursor = db.cursor()
cursor.execute("SELECT * FROM head_boy WHERE vote_choice == 'Aarush Verma'")
res = cursor.fetchall()
print(res)