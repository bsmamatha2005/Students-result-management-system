from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

# ================= DATABASE =================
def create_db():
    con = sqlite3.connect("PYTHON_PROJECT.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        roll TEXT PRIMARY KEY,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        admission TEXT,
        course TEXT,
        state TEXT,
        city TEXT,
        pin TEXT,
        address TEXT
    )
    """)
    con.commit()
    con.close()

create_db()

# ================= MAIN CLASS =================
class StudentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x600+30+30")
        self.root.config(bg="white")

        # VARIABLES
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_admission = StringVar()
        self.var_course = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        # TITLE
        Label(self.root, text="🎓 STUDENT MANAGEMENT SYSTEM",
              font=("Arial", 24, "bold"),
              bg="#2c6c9c", fg="white").pack(fill=X)

        label_font = ("Arial", 13, "bold")
        entry_font = ("Arial", 13)

        # ===== LEFT FRAME (FORM) =====
        form = Frame(self.root, bg="white")
        form.place(x=20, y=80, width=650, height=480)

        # Row spacing
        y = 11
        gap = 48

        def entry_box(x, y, var):
            return Entry(form, textvariable=var, font=entry_font,
                         bg="#fff9c4", relief=SOLID)

        # Row 1
        Label(form, text="Roll No", font=label_font, bg="white").place(x=10, y=y)
        entry_box(120, y, self.var_roll).place(x=120, y=y, width=220)

        Label(form, text="DOB", font=label_font, bg="white").place(x=350, y=y)
        entry_box(430, y, self.var_dob).place(x=430, y=y, width=200)

        y += gap

        # Row 2
        Label(form, text="Name", font=label_font, bg="white").place(x=10, y=y)
        entry_box(120, y, self.var_name).place(x=120, y=y, width=220)

        Label(form, text="Contact", font=label_font, bg="white").place(x=350, y=y)
        entry_box(430, y, self.var_contact).place(x=430, y=y, width=200)

        y += gap

        # Row 3
        Label(form, text="Email", font=label_font, bg="white").place(x=10, y=y)
        entry_box(120, y, self.var_email).place(x=120, y=y, width=220)

        Label(form, text="Admision", font=label_font, bg="white").place(x=350, y=y)
        entry_box(430, y, self.var_admission).place(x=430, y=y, width=200)

        y += gap

        # Row 4
        Label(form, text="Gender", font=label_font, bg="white").place(x=10, y=y)
        ttk.Combobox(form, textvariable=self.var_gender,
                     values=["Male", "Female", "Other"],
                     font=entry_font, state="readonly").place(x=120, y=y, width=220)

        Label(form, text="Course", font=label_font, bg="white").place(x=350, y=y)
        ttk.Combobox(form, textvariable=self.var_course,
                     values=["Python", "Java", "C++", "PHP"],
                     font=entry_font, state="readonly").place(x=430, y=y, width=200)

        y += gap

        # Row 5
        Label(form, text="State", font=label_font, bg="white").place(x=10, y=y)
        ttk.Combobox(form, textvariable=self.var_state,
                     values=["Karnataka","Tamil Nadu","Kerala","Maharashtra","Delhi","UP"],
                     font=entry_font, state="readonly").place(x=120, y=y, width=220)

        Label(form, text="City", font=label_font, bg="white").place(x=350, y=y)
        entry_box(430, y, self.var_city).place(x=430, y=y, width=200)

        y += gap

        # Row 6
        Label(form, text="Pin", font=label_font, bg="white").place(x=10, y=y)
        entry_box(120, y, self.var_pin).place(x=120, y=y, width=220)

        y += gap

        # Address
        Label(form, text="Address", font=label_font, bg="white").place(x=10, y=y)
        self.txt_address = Text(form, font=("Arial", 12), bg="#fff9c4")
        self.txt_address.place(x=120, y=y, width=510, height=80)

        # ===== BUTTONS =====
        btn_y = 380

        Button(form, text="Save", bg="#1f6ae0", fg="white",
               font=("Arial", 13, "bold"), width=10,
               command=self.add).place(x=60, y=btn_y)

        Button(form, text="Update", bg="#28a745", fg="white",
               font=("Arial", 13, "bold"), width=10,
               command=self.update).place(x=180, y=btn_y)

        Button(form, text="Delete", bg="#dc3545", fg="white",
               font=("Arial", 13, "bold"), width=10,
               command=self.delete).place(x=300, y=btn_y)

        Button(form, text="Clear", bg="#6c757d", fg="white",
               font=("Arial", 13, "bold"), width=10,
               command=self.clear).place(x=420, y=btn_y)

        # ===== RIGHT SIDE (SEARCH + TABLE) =====
        Label(self.root, text="Search Roll / Name",
              font=("Arial", 13, "bold"), bg="white").place(x=700, y=90)

        Entry(self.root, textvariable=self.var_search,
              font=("Arial", 13), bg="#fff9c4").place(x=900, y=90, width=220)

        Button(self.root, text="Search", bg="green", fg="white",
               font=("Arial", 12, "bold"),
               command=self.search).place(x=1130, y=88, width=100)

        # Table Frame
        frame = Frame(self.root, bd=2, relief=RIDGE)
        frame.place(x=700, y=130, width=620, height=400)

        scroll_x = Scrollbar(frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(frame, orient=VERTICAL)

        self.table = ttk.Treeview(frame,
            columns=("roll","name","email","gender","dob","contact",
                     "admission","course","state","city","pin","address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        for col in self.table["columns"]:
            self.table.heading(col, text=col.upper())
            self.table.column(col, width=130)

        self.table["show"] = "headings"
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # ================= FUNCTIONS =================
    def add(self):
        con = sqlite3.connect("PYTHON_PROJECT.db")
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
                self.var_roll.get(),
                self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_contact.get(),
                self.var_admission.get(),
                self.var_course.get(),
                self.var_state.get(),
                self.var_city.get(),
                self.var_pin.get(),
                self.txt_address.get("1.0", END)
            ))
            con.commit()
            self.show()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show(self):
        con = sqlite3.connect("PYTHON_PROJECT.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", END, values=row)

    def get_data(self, ev):
        row = self.table.item(self.table.focus())["values"]
        if row:
            self.var_roll.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_admission.set(row[6])
            self.var_course.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])
            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, row[11])

    def update(self):
        con = sqlite3.connect("PYTHON_PROJECT.db")
        cur = con.cursor()
        cur.execute("""UPDATE student SET name=?,email=?,gender=?,dob=?,contact=?,
                       addmission=?,course=?,state=?,city=?,pin=?,address=? WHERE roll=?""", (
            self.var_name.get(),
            self.var_email.get(),
            self.var_gender.get(),
            self.var_dob.get(),
            self.var_contact.get(),
            self.var_admission.get(),
            self.var_course.get(),
            self.var_state.get(),
            self.var_city.get(),
            self.var_pin.get(),
            self.txt_address.get("1.0", END),
            self.var_roll.get()
        ))
        con.commit()
        self.show()

    def delete(self):
        try:
            con = sqlite3.connect("PYTHON_PROJECT.db")
            cur = con.cursor()

            print("Deleting Roll No:", self.var_roll.get())

            cur.execute(
            "DELETE FROM student WHERE roll=?",
            (self.var_roll.get(),)
            )
            print("Student rows deleted:", cur.rowcount)

            cur.execute(
            "DELETE FROM result WHERE roll=?",
            (self.var_roll.get(),)
            )
            print("Result rows deleted:", cur.rowcount)

            con.commit()

            messagebox.showinfo(
            "Success",
            "Delete operation completed"
            )

            con.close()

        except Exception as ex:
            print("ERROR:", ex)
            messagebox.showerror(
            "Error",
            str(ex)
            )

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_admission.set("")
        self.var_course.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete("1.0", END)

    def search(self):
        con = sqlite3.connect("PYTHON_PROJECT.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM student WHERE roll LIKE ? OR name LIKE ?",
                    ('%'+self.var_search.get()+'%', '%'+self.var_search.get()+'%'))
        rows = cur.fetchall()
        self.table.delete(*self.table.get_children())
        for row in rows:
            self.table.insert("", END, values=row)

    def fetch_course(self):
        con = sqlite3.connect(database="PYTHON_PROJECT.db")
        cur = con.cursor()

        try:
            cur.execute("select name from course")
            rows = cur.fetchall()

            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])

        except Exception as ex:
            messagebox.showerror(
            "Error",
            f"Error due to {str(ex)}"
        )


# RUN
# RUN
if __name__ == "__main__":
    root = Tk()
    obj = StudentSystem(root)
    root.mainloop()