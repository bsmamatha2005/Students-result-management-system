from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()

        self.roll_list = []
        self.fetch_roll()

        # Title
        title = Label(
            self.root,
            text="Add Student Result Details",
            font=("goudy old style", 20, "bold"),
            bg="#23AC23",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        # Labels
        Label(
            self.root,
            text="Select Student",
            font=("goudy old style", 20, "bold"),
            bg="white"
        ).place(x=10, y=60)

        Label(
            self.root,
            text="Name",
            font=("goudy old style", 20, "bold"),
            bg="white"
        ).place(x=10, y=100)

        Label(
            self.root,
            text="Course",
            font=("goudy old style", 20, "bold"),
            bg="white"
        ).place(x=10, y=140)

        Label(
            self.root,
            text="Marks Obtained",
            font=("goudy old style", 20, "bold"),
            bg="white"
        ).place(x=10, y=180)

        Label(
            self.root,
            text="Full Marks",
            font=("goudy old style", 20, "bold"),
            bg="white"
        ).place(x=10, y=220)

        # Roll Combobox
        self.txt_student = ttk.Combobox(
            self.root,
            textvariable=self.var_roll,
            values=self.roll_list,
            font=("goudy old style", 15, "bold"),
            state="readonly",
            justify=CENTER
        )
        self.txt_student.place(x=280, y=60, width=180)
        self.txt_student.set("Select")

        # Search Button
        btn_search = Button(
            self.root,
            text="Search",
            font=("goudy old style", 15, "bold"),
            bg="blue",
            fg="white",
            cursor="hand2",
            command=self.search
        )
        btn_search.place(x=480, y=60, width=100, height=34)

        # Entries
        txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15, "bold"),
            bg="#ffff6f",
            state="readonly"
        )
        txt_name.place(x=280, y=100, width=300)

        txt_course = Entry(
            self.root,
            textvariable=self.var_course,
            font=("goudy old style", 15, "bold"),
            bg="#ffff6f",
            state="readonly"
        )
        txt_course.place(x=280, y=140, width=300)

        txt_marks = Entry(
            self.root,
            textvariable=self.var_marks,
            font=("goudy old style", 15, "bold"),
            bg="#ffff6f"
        )
        txt_marks.place(x=280, y=180, width=300)

        txt_full_marks = Entry(
            self.root,
            textvariable=self.var_full_marks,
            font=("goudy old style", 15, "bold"),
            bg="#ffff6f"
        )
        txt_full_marks.place(x=280, y=220, width=300)

        # Buttons
        btn_add = Button(
            self.root,
            text="Submit",
            font=("goudy old style", 15, "bold"),
            bg="lightgreen",
            fg="black",
            cursor="hand2",
            command=self.add_result
        )
        btn_add.place(x=300, y=420, width=120, height=34)

        btn_clear = Button(
            self.root,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="lightgrey",
            fg="black",
            cursor="hand2",
            command=self.clear
        )
        btn_clear.place(x=430, y=420, width=120, height=34)

        # Image
        try:
            self.bg_img = Image.open("images/result.png")
            self.bg_img = self.bg_img.resize((500, 300), Image.Resampling.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)

            self.lbl_bg = Label(self.root, image=self.bg_img)
            self.lbl_bg.place(x=630, y=100)
        except:
            pass

    # ==================================
    # Fetch Roll Numbers
    # ==================================
    def fetch_roll(self):
        try:
            con = sqlite3.connect("PYTHON_PROJECT.db")
            cur = con.cursor()

            cur.execute("SELECT roll FROM student")
            rows = cur.fetchall()

            self.roll_list.clear()

            for row in rows:
                self.roll_list.append(row[0])

            con.close()

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

    # ==================================
    # Search Student
    # ==================================
    def search(self):
        try:
            if self.var_roll.get() == "Select":
                messagebox.showerror(
                    "Error",
                    "Please select a Roll Number",
                    parent=self.root
                )
                return

            con = sqlite3.connect("PYTHON_PROJECT.db")
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM student WHERE roll=?",
                (self.var_roll.get(),)
            )

            row = cur.fetchone()

            if row is not None:
                self.var_name.set(row[1])     # name
                self.var_course.set(row[7])   # course
            else:
                messagebox.showerror(
                    "Error",
                    "Student not found",
                    parent=self.root
                )

            con.close()

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

    # ==================================
    # Add Result
    # ==================================
    def add_result(self):
        try:
            if self.var_roll.get() == "Select":
                messagebox.showerror(
                    "Error",
                    "Please select a student",
                    parent=self.root
                )
                return

            percentage = (
                float(self.var_marks.get()) /
                float(self.var_full_marks.get())
            ) * 100

            con = sqlite3.connect("PYTHON_PROJECT.db")
            cur = con.cursor()

            cur.execute("""
                INSERT INTO result
                (roll,name,course,marks_obtained,total_marks,percentage)
                VALUES(?,?,?,?,?,?)
            """, (
                self.var_roll.get(),
                self.var_name.get(),
                self.var_course.get(),
                self.var_marks.get(),
                self.var_full_marks.get(),
                round(percentage, 2)
            ))

            con.commit()
            con.close()

            messagebox.showinfo(
                "Success",
                "Result Added Successfully",
                parent=self.root
            )

        except Exception as ex:
            messagebox.showerror(
                "Error",
                f"Error due to {str(ex)}",
                parent=self.root
            )

    # ==================================
    # Clear Fields
    # ==================================
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()