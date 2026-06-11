import sqlite3

# Connect to source database
con1 = sqlite3.connect("student.db")
cur1 = con1.cursor()

# Connect to destination database
con2 = sqlite3.connect("PYTHON_PROJECT.db")
cur2 = con2.cursor()

# Read all students from student.db
cur1.execute("SELECT * FROM student")
rows = cur1.fetchall()

# Insert into PYTHON_PROJECT.db
for row in rows:
    cur2.execute("""
        INSERT INTO student
        (roll, name, email, gender, dob, contact,
         addmission, course, state, city, pin, address)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, row)

con2.commit()

print(f"{len(rows)} records copied successfully.")

con1.close()
con2.close()