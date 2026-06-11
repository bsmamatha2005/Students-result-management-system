from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class reportClass:

    def __init__(self, root):
        self.root = root
        self.root.title("student result management system")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===== Title =====
        title = Label(self.root, text="View Student Result Details",
                      font=("goudy old style", 20, "bold"),
                      bg="#23AC23", fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # ===== Search =====
        self.var_search = StringVar()

        Label(self.root, text="Search by Roll No:",
              font=("goudy old style", 20, "bold"),
              bg="white").place(x=280, y=60)

        Entry(self.root, textvariable=self.var_search,
              font=("goudy old style", 20),
              bg="yellow").place(x=500, y=60)

        Button(self.root, text="Search",
               font=("goudy old style", 15, "bold"),
               bg="blue", fg="white",
               command=self.search).place(x=800, y=60, width=100, height=34)

        Button(self.root, text="Clear",
               font=("goudy old style", 15, "bold"),
               bg="grey", fg="white",
               command=self.clear).place(x=940, y=60, width=100, height=34)

        # ===== Labels =====
        Label(self.root, text="Roll No", bg="white", relief=GROOVE,
              font=("goudy old style", 20, "bold")).place(x=150, y=230, width=150, height=50)

        Label(self.root, text="Name", bg="white", relief=GROOVE,
              font=("goudy old style", 20, "bold")).place(x=300, y=230, width=150, height=50)

        Label(self.root, text="Course", bg="white", relief=GROOVE,
              font=("goudy old style", 20, "bold")).place(x=450, y=230, width=150, height=50)

        Label(self.root, text="Marks Obtained", bg="white", relief=GROOVE,
              font=("goudy old style", 20, "bold")).place(x=600, y=230, width=180, height=50)

        Label(self.root, text="Total Marks", bg="white", relief=GROOVE,
              font=("goudy old style", 20, "bold")).place(x=780, y=230, width=180, height=50)

        Label(self.root, text="Percentage", bg="white", relief=GROOVE,
              font=("goudy old style", 20, "bold")).place(x=960, y=230, width=150, height=50)

        # ===== Output Fields =====
        self.roll = Label(self.root, bg="white", relief=GROOVE,
                          font=("goudy old style", 20, "bold"))
        self.roll.place(x=150, y=280, width=150, height=50)

        self.name = Label(self.root, bg="white", relief=GROOVE,
                          font=("goudy old style", 20, "bold"))
        self.name.place(x=300, y=280, width=150, height=50)

        self.course = Label(self.root, bg="white", relief=GROOVE,
                            font=("goudy old style", 20, "bold"))
        self.course.place(x=450, y=280, width=150, height=50)

        self.marks_ob = Label(self.root, bg="white", relief=GROOVE,
                              font=("goudy old style", 20, "bold"))
        self.marks_ob.place(x=600, y=280, width=180, height=50)

        self.full = Label(self.root, bg="white", relief=GROOVE,
                          font=("goudy old style", 20, "bold"))
        self.full.place(x=780, y=280, width=180, height=50)

        self.per = Label(self.root, bg="white", relief=GROOVE,
                         font=("goudy old style", 20, "bold"))
        self.per.place(x=960, y=280, width=150, height=50)

        # ===== Buttons =====
        Button(self.root, text="Delete",
               font=("goudy old style", 15, "bold"),
               bg="red", fg="white",
               command=self.delete).place(x=450, y=370, width=150, height=40)

    # ================= SEARCH =================
    def search(self):
        con = sqlite3.connect(database="PYTHON_PROJECT.db")
        cur = con.cursor()

        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No is required", parent=self.root)
                return

            cur.execute("select * from result where roll=?",
                        (self.var_search.get(),))
            row = cur.fetchone()

            if row is not None:
                self.roll.config(text=row[1])
                self.name.config(text=row[2])
                self.course.config(text=row[3])
                self.marks_ob.config(text=row[4])
                self.full.config(text=row[5])
                self.per.config(text=row[6])
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        finally:
            con.close()

    # ================= CLEAR =================
    def clear(self):
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks_ob.config(text="")
        self.full.config(text="")
        self.per.config(text="")

    # ================= DELETE =================
    def delete(self):
        con = sqlite3.connect(database="PYTHON_PROJECT.db")
        cur = con.cursor()

        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Enter Roll No to delete", parent=self.root)
                return

            confirm = messagebox.askyesno("Confirm", "Do you want to delete this record?", parent=self.root)

            if confirm:
                cur.execute("delete from result where roll=?",
                            (self.var_search.get(),))
                con.commit()

                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()