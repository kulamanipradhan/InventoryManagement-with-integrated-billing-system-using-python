#!/usr/bin/env python
# coding: utf-8

# In[25]:


from tkinter import*


# In[26]:


from PIL import Image,ImageTk


# In[27]:


from tkinter import ttk,messagebox


# In[28]:


import sqlite3


# In[35]:


class categoryClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Employee")
        self.root.config(bg="white")
        self.root.focus_force()
        #+++variale
        self.var_cat_id= StringVar()
        self.var_name= StringVar()
        #=======================title=========
        lbl_title=Label(self.root,text="Manage product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)
        btn_add=Button(self.root,text="Add",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
        #============category details
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=120)
        
        scrolly= Scrollbar(cat_frame,orient=VERTICAL)
        scrollx= Scrollbar(cat_frame,orient=HORIZONTAL)
        self.categoryTable=ttk.Treeview(cat_frame,column=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill= X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.heading("cid",text="CID")
        self.categoryTable.heading("name",text="Name")
        self.categoryTable["show"]="headings"
        
        self.categoryTable.column("cid",width=90)
        self.categoryTable.column("name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        #images
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,250),Image.ANTIALIAS)
        self.im1 =ImageTk.PhotoImage(self.im1)
        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)
        
        self.im2=Image.open("images/category.jpg")
        self.im2=self.im2.resize((500,250),Image.ANTIALIAS)
        self.im2 =ImageTk.PhotoImage(self.im2)
        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)
        self.show()
        
    #functions
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","category id must be required",parent=self.root)
            else:
                cur.execute("select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","category already available,try diffrerent",parent=self.root)
                else:
                    cur.execute("Insert into category(name)values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("success","category added Successfully",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
        
         
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                
                messagebox.showerror("Error","please select category name",parent=self.root)
            else:
                cur.execute("select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","category deleted",parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)        
if __name__=="__main__":
    root=Tk()
    obj =categoryClass(root)
    root.mainloop()


# In[ ]:





# In[ ]:




