import sqlite3

# * Connect to DB
con = sqlite3.connect("tutorial.db") # will create a file called this in the directory


# * Create DB Cursor (Database Look-Through Object)
cur = con.cursor()

# * Execute an SQL query (this makes a table called movie with 3 parameters)
# ! Changes are permanent, so reruns of the same program does not result in the same output
# ! If you run the below twice, you'll get an error the second time
cur.execute("CREATE TABLE movie(title, year, score)")

# * This time, do a select query to get data
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone()) # fetch the first piece of data received

# Purposefully querying something that does not exist and seeing the output
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)

# * Multiple Entry Insertion
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""") # ! Note that 'INSERT' implies a transaction has been opened, so a commit is necessary (not a git commit)
con.commit()

# * Verify data has been committed
res = cur.execute("SELECT score FROM movie")
print(res.fetchall()) # fetch all data received
# * Can also consider 'fetchone' as retrieve the first row, and 'fetchall' as retrieve all rows

# * Another way to insert a bunch of data
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)  # ! MUST use '?' placeholders as
                                                            # !   using f'{}' is subject to
                                                            # !   SQL injection
# * See https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders for more info on placeholders

con.commit()  # Remember to commit the transaction after executing INSERT.

# * Can loop through the data yielded from the execute call
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)


# * 'close' will close connection to the database. Since data is being written to disk,
# *    you can do this and then reconnect and the data will persist
con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

new_con.close()

# * For more documentation, see:
# *     https://docs.python.org/3/library/sqlite3.html