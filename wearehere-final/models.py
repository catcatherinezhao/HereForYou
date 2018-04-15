import sqlite3 as sql

def insertUser(user_name, perp_name , perp_descrip, location, inc_date, inc_time, incident, contact):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO records (user_name, perp_name , perp_descrip, location, inc_date, inc_time, incident, contact) VALUES (?,?,?,?,?,?,?,?)",(user_name, perp_name , perp_descrip, location, inc_date, inc_time, incident, contact))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM records")
	records = cur.fetchall()
	con.close()
	return records