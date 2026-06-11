from tkinter import *
from tkinter import messagebox
import sqlite3


class RegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account")
        self.root.geometry("500x420")
        self.root.config(bg="#f4f6f7")

        # ================= HEADER =================
        Label(root,
              text="WELCOME TO STUDENT PORTAL",
              font=("Arial", 16, "bold"),
              bg="#f4f6f7",
              fg="#2c3e50").pack(pady=15)

        Label(root,
              text="Create your account to continue",
              font=("Arial", 10),
              bg="#f4f6f7",
              fg="gray").pack()

        # ================= CENTER CARD =================
        self.card = Frame(root, bg="white", bd=1, relief=SOLID)
        self.card.place(x=90, y=90, width=320, height=280)

        Label(self.card,
              text="REGISTER",
              font=("Arial", 14, "bold"),
              bg="white").pack(pady=10)

        # ================= VARIABLES =================
        self.user = StringVar()
        self.password = StringVar()

        # ================= FORM =================
        self.build_field("Username", self.user)
        self.build_field("Password", self.password, show="*")

        # ================= BUTTON =================
        Button(self.card,
               text="CREATE ACCOUNT",
               bg="#27ae60",
               fg="white",
               font=("Arial", 11, "bold"),
               command=self.register).pack(pady=15, fill=X, padx=20)

        # ================= FOOTER LINK =================
        Button(self.card,
               text="Clear Fields",
               bg="white",
               fg="#2980b9",
               bd=0,
               command=self.clear).pack()

    # ================= INPUT DESIGN FUNCTION =================
    def build_field(self, label, var, show=None):
        Label(self.card,
              text=label,
              bg="white",
              anchor="w").pack(fill=X, padx=20)

        Entry(self.card,
              textvariable=var,
              show=show,
              bd=1,
              relief=SOLID).pack(fill=X, padx=20, pady=5)

    # ================= REGISTER =================
    def register(self):
        con = sqlite3.connect("PYTHON_PROJECT.db")
        cur = con.cursor()

        if self.user.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields required")
            return

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        """)

        cur.execute("INSERT INTO users(username,password) VALUES(?,?)",
                    (self.user.get(), self.password.get()))

        con.commit()
        con.close()

        messagebox.showinfo("Success", "Account Created Successfully")
        self.clear()

    # ================= CLEAR =================
    def clear(self):
        self.user.set("")
        self.password.set("")


if __name__ == "__main__":
    root = Tk()
    RegisterPage(root)
    root.mainloop()