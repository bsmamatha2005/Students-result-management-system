import sqlite3

def create_database():
    con = sqlite3.connect("PYTHON_PROJECT.db")
    cur = con.cursor()

    # ================= USERS TABLE =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # ================= COURSE TABLE =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS course(
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        duration TEXT,
        charges TEXT,
        description TEXT
    )
    """)

    # ================= STUDENT TABLE =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        roll INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        addmission TEXT,
        course TEXT,
        state TEXT,
        city TEXT,
        pin TEXT,
        address TEXT
    )
    """)

    # ================= RESULT TABLE =================
    cur.execute("""
    CREATE TABLE IF NOT EXISTS result(
        rid INTEGER PRIMARY KEY AUTOINCREMENT,
        roll TEXT,
        name TEXT,
        course TEXT,
        marks_obtained TEXT,
        full_marks TEXT,
        percentage TEXT
    )
    """)

    con.commit()
    con.close()

    print("Database Created Successfully")


if __name__ == "__main__":
    create_database()