from tkinter import *
from PIL import Image, ImageTk
from sympy import ask

from tkinter import messagebox
from course import CourseClass
from student import StudentSystem
from result import resultClass
from report import reportClass
import create_db
import sqlite3


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student result management system")

        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        logo = Image.open("images/logo.png")
        logo = logo.resize((45, 45), Image.Resampling.LANCZOS)   # width, height
        self.logo_dash = ImageTk.PhotoImage(logo)

        title = Label(
            self.root,
            text="Student result management system",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)
        # ===== CLOCK IMAGE =====
        self.clock_img = Image.open("images/webclock.png")
        self.clock_img = self.clock_img.resize((350, 440), Image.Resampling.LANCZOS)
        self.clock_img = ImageTk.PhotoImage(self.clock_img)

        self.clock_icon = Label(
            self.root,
            image=self.clock_img,
            bg="#033054"
        )
        self.clock_icon.place(x=10, y=180)

            

        M_Frame = LabelFrame(self.root, text="Menus",
                             font=("times new roman", 15),
                             bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        Button(M_Frame, text="course",
               font=("goudy old style", 15, "bold"),
               bg="#0b7710", fg="black",
               cursor="hand2",
               command=self.add_course).place(x=20, y=5, width=200, height=30)

        Button(M_Frame, text="student",
               font=("goudy old style", 15, "bold"),
               bg="#0b7710", fg="black",
               cursor="hand2",
               command=self.add_student).place(x=240, y=5, width=200, height=30)

        Button(M_Frame, text="result",
               font=("goudy old style", 15, "bold"),
               bg="#0b7710", fg="black",
               cursor="hand2",
               command=self.add_result).place(x=460, y=5, width=200, height=30)

        Button(M_Frame, text="view",
               font=("goudy old style", 15, "bold"),
               bg="#0b7710", fg="black",
               cursor="hand2",
               command=self.add_report).place(x=680, y=5, width=200, height=30)

        # ================= FIXED =================
        Button(M_Frame, text="logout",
               font=("goudy old style", 15, "bold"),
               bg="#0b7710", fg="black",
               cursor="hand2",
               command=self.logout).place(x=900, y=5, width=200, height=30)

        Button(M_Frame, text="exit",
               font=("goudy old style", 15, "bold"),
               bg="#0b7710", fg="black",
               cursor="hand2",
               command=self.exit_app).place(x=1120, y=5, width=200, height=30)

        # ================= CONTENT =================
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)

        self.lbl_course = Label(self.root, text="total course\n[0]",
                                font=("goudy old style", 20),
                                bd=10, relief=RIDGE,
                                bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="total student\n[0]",
                                 font=("goudy old style", 20),
                                 bd=10, relief=RIDGE,
                                 bg="#21cb9e", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="total result\n[0]",
                                font=("goudy old style", 20),
                                bd=10, relief=RIDGE,
                                bg="#e4068f", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        footer = Label(
            self.root,
            text="GECC-student result management system | Contact: 63600xxxxx",
            font=("goudy old style", 12),
            bg="#BD4F8B",
            fg="white"
        )
        footer.pack(side=BOTTOM, fill=X)
        self.update_details()
    # ================= MODULES =================
    def add_course(self):
        self.new_win = Toplevel(self.root)
        CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        StudentSystem(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        reportClass(self.new_win)

    def logout(self):
        ask = messagebox.askyesno(
         "Logout",
         "Do you want to logout?"
         )

        if ask:
            self.root.destroy()

            from main import LoginPage

            root = Tk()
            LoginPage(root)
            root.mainloop()

    def update_details(self):
        try:
            con = sqlite3.connect("PYTHON_PROJECT.db")
            cur = con.cursor()

            # Course Count
            cur.execute("SELECT COUNT(*) FROM course")
            course = cur.fetchone()[0]

            # Student Count
            cur.execute("SELECT COUNT(*) FROM student")
            student = cur.fetchone()[0]

            # Result Count
            cur.execute("SELECT COUNT(*) FROM result")
            result = cur.fetchone()[0]

            self.lbl_course.config(text=f"total course\n[{course}]")
            self.lbl_student.config(text=f"total student\n[{student}]")
            self.lbl_result.config(text=f"total result\n[{result}]")

            con.close()

            self.root.after(2000, self.update_details)

        except Exception as ex:
            print("Dashboard Error:", ex)

    def exit_app(self):
        op = messagebox.askyesno(
        "Exit",
        "Do you want to exit the application?"
    )

        if op:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()