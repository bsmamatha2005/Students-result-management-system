from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("student result management system")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        title=Label(self.root,text="manage course detail",font=("goudy old style",20,"bold"),bg="#238AAC",fg="white").place(x=0,y=0,relwidth=1,height=50)
        # =======variable======
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()

        lbl_courseName=Label(self.root,text="Course name",font=("goudy old style",20,"bold"),bg="white",).place(x=10,y=60)
        lbl_duration=Label(self.root,text="duration",font=("goudy old style",20,"bold"),bg="white",).place(x=10,y=100)
        lbl_charges=Label(self.root,text="charges",font=("goudy old style",20,"bold"),bg="white").place(x=10,y=140)
        lbl_description=Label(self.root,text="description",font=("goudy old style",20,"bold"),bg="white",).place(x=10,y=180)

        # entry feild
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg="lightyellow",)
        self.txt_courseName.place(x=170,y=60,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",20,"bold"),bg="lightyellow",).place(x=170,y=100,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=170,y=140,width=200)
        self.txt_description=Text(self.root,font=("goudy old style",20,"bold"),bg="lightyellow",)
        self.txt_description.place(x=170,y=180,width=500,height=100)

        # ====button====
        self.btn_add=Button(self.root,text="Save",font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=180,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2",command=self.update)
        self.btn_add.place(x=300,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="orange",fg="white",cursor="hand2",command=self.delete)
        self.btn_add.place(x=420,y=400,width=110,height=40)
        self.btn_add=Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="grey",fg="white",cursor="hand2",command=self.clear)
        self.btn_add.place(x=540,y=400,width=110,height=40)

        # =====search panel======
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name:",font=("goudy old style",20,"bold"),bg="white",).place(x=720,y=60)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,"bold"),bg="lightyellow",).place(x=890,y=60,width=180)
        btn_search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.search).place(x=1080,y=60,width=110,height=36)
        
        # =====content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340) 

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL) 
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL) 

        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="duration")
        self.CourseTable.heading("charges",text="charges")
        self.CourseTable.heading("description",text="description")
        self.CourseTable["show"]="headings"
        
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


        # =================================

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0", END)
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="PYTHON_PROJECT.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name is required", parent=self.root)

            else:
                cur.execute("SELECT * FROM course WHERE name=?", (self.var_course.get(),))
                row = cur.fetchone()

            # FIX: check for None (not found)
                if row is None:
                    messagebox.showerror("Error", "Please select a valid course from the list", parent=self.root)

                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM course WHERE name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    def get_data(self, event):
        selected = self.CourseTable.focus()
        values = self.CourseTable.item(selected, 'values')

        if values:
            print(values)   # Now this WILL print in terminal

            self.var_course.set(values[1])
            self.var_duration.set(values[2])
            self.var_charges.set(values[3])

            self.txt_description.delete("1.0", END)
            self.txt_description.insert(END, values[4])
    

    def add(self):
        con=sqlite3.connect(database="PYTHON_PROJECT.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","course name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","course name already present",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("success","Course added successfully",parent=self.root)
                    self.show()

                    
        except Exception as ex:
            messagebox.showerror("Error" ,f"error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="PYTHON_PROJECT.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Select course from list", parent=self.root)
            else:
                cur.execute(
                    "update course set duration=?, charges=?, description=? where name=?",
                (
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0", END).strip(),
                    self.var_course.get()
                )
            )
                con.commit()
                messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="PYTHON_PROJECT.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)
        except Exception as ex:
            messagebox.showerror("Error" ,f"error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="PYTHON_PROJECT.db")
        cur = con.cursor()
        try:
            search_txt = self.var_search.get()

            cur.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + search_txt + '%',))
            rows = cur.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
                self.CourseTable.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")






   
if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()
