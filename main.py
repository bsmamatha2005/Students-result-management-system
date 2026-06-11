from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import time

from dashboard import RMS


class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Learning Portal")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # ================= BACKGROUND IMAGE =================
        self.bg_img = Image.open("images/books_bg.png")  # your book image
        self.bg_img = self.bg_img.resize((1000, 600), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        bg = Label(self.root, image=self.bg_img)
        bg.place(x=0, y=0)

        # ================= TITLE =================
        Label(self.root,
              text="STUDENT LEARNING MANAGEMENT SYSTEM",
              font=("Arial", 18, "bold"),
              bg="#ffffff").place(x=250, y=30)

        # ================= LOGIN CARD =================
        self.frame = Frame(self.root, bg="white", bd=2)
        self.frame.place(x=350, y=150, width=320, height=320)

        Label(self.frame, text="LOGIN",
              font=("Arial", 16, "bold"),
              bg="white").pack(pady=15)

        # ================= VARIABLES =================
        self.user = StringVar()
        self.password = StringVar()

        # ================= FIELDS =================
        Label(self.frame, text="Username", bg="white").pack(anchor="w", padx=20)
        Entry(self.frame, textvariable=self.user,
              bd=1, relief=SOLID).pack(fill=X, padx=20)

        Label(self.frame, text="Password", bg="white").pack(anchor="w", padx=20, pady=(10, 0))
        Entry(self.frame, textvariable=self.password,
              show="*", bd=1, relief=SOLID).pack(fill=X, padx=20)

        # ================= BUTTON =================
        Button(self.frame,
               text="LOGIN",
               bg="#2ecc71",
               fg="white",
               font=("Arial", 12, "bold"),
               command=self.login).pack(fill=X, padx=20, pady=20)

        # ================= LINKS =================
        Button(self.frame,
               text="Register New Account",
               bg="white",
               fg="#2980b9",
               bd=0,
               command=self.register).pack()

        Button(self.frame,
               text="Forgot Password?",
               bg="white",
               fg="#e67e22",
               bd=0,
               command=self.forgot).pack()

    #========== LOGIN =================
    def login(self):
        con = sqlite3.connect("PYTHON_PROJECT.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                    (self.user.get(), self.password.get()))
        row = cur.fetchone()

        if row:
            self.root.destroy()
            root = Tk()
            RMS(root)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid Login")

    # ================= REGISTER =================
    def register(self):
        from register import RegisterPage
        RegisterPage(Toplevel(self.root))

    # ================= FORGOT =================
    def forgot(self):
        messagebox.showinfo("Info", "Password reset not implemented")


if __name__ == "__main__":
    root = Tk()
    LoginPage(root)
    root.mainloop()