import sqlite3

conn = sqlite3.connect('wordBase.db')
c = conn.cursor()

def createDB():
	c.execute("CREATE TABLE wordVals (word TEXT, value REAL)")


createDB()
