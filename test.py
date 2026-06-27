import sqlite3


conn = sqlite3.connect("tickets.db" , check_same_thread=False)
cursor = conn.cursor()
cursor.execute("DROP TABLE tickets")
conn.commit()
conn.close()