#!/usr/bin/env python
# coding: utf-8

# In[11]:


from tkinter import*


# In[12]:


from PIL import Image,ImageTk


# In[13]:


from tkinter import ttk,messagebox


# In[14]:


import sqlite3


# In[15]:


class productClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Product")
        self.root.config(bg="white")
        self.root.focus_force()
        #========================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        
        product_Frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480)
        #title
        title=Label(product_Frame,text="Manage Product details", font=("goudy old style",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        lbl_category=Label(self.root,text="Category", font=("goudy old style",15),bg="white").place(x=30,y=60)
        lbl_supplier=Label(self.root,text="Supplier", font=("goudy old style",15),bg="white").place(x=30,y=110)
    
        lbl_product_name=Label(self.root,text="Product Name", font=("goudy old style",15),bg="white").place(x=30,y=160)
       
        lbl_price=Label(self.root,text="Price", font=("goudy old style",15),bg="white").place(x=30,y=210)

        lbl_qty=Label(self.root,text="Quantity", font=("goudy old style",15),bg="white").place(x=30,y=260)
        lbl_status=Label(self.root,text="Status", font=("goudy old style",15),bg="white").place(x=30,y=310)
                
                
        cmb_cat =ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER,font=("goudy old styl",15))
        cmb_cat.place(x=150,y=50,width=200)
        cmb_cat.current(0)
        
        cmb_sup =ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER,font=("goudy old styl",15))
        cmb_sup.place(x=150,y=100,width=200)
        cmb_sup.current(0)
        
        txt_name =Entry(product_Frame,textvariable=self.var_name,font=("goudy old styl",15),bg="lightyellow").place(x=150,y=150,width=200)
        txt_price =Entry(product_Frame,textvariable=self.var_price,font=("goudy old styl",15),bg="lightyellow").place(x=150,y=200,width=200)
        txt_qty =Entry(product_Frame,textvariable=self.var_qty,font=("goudy old styl",15),bg="lightyellow").place(x=150,y=250,width=200)
        cmb_status =ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state="readonly",justify=CENTER,font=("goudy old styl",15))
        cmb_status.place(x=150,y=300,width=200)
        cmb_status.current(0)
        
        #button
        btn_add =Button(product_Frame,text="Save",command=self.add,font=("goudy old style",15),bg="blue",fg="white",cursor = "hand2").place(x=10,y=400,width=100,height=40)
        btn_update =Button(product_Frame,text="Update",command=self.update,font=("goudy old style",15),bg="green",fg="white",cursor = "hand2").place(x=120,y=400,width=100,height=40)
        btn_delete =Button(product_Frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="orange",fg="white",cursor = "hand2").place(x=225,y=400,width=100,height=40)
        btn_clear =Button(product_Frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="brown",fg="white",cursor = "hand2").place(x=330,y=400,width=100,height=40)
 #======================================================


        #=== searchFrame=====
        SearchFrame= LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)
        #options
        cmb_serach =ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state="readonly",justify=CENTER,font=("goudy old styl",15))
        cmb_serach.place(x=10,y=10,width=180)
        cmb_serach.current(0)
        #text serach
        txt_search =Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search =Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white",cursor = "hand2").place(x=420,y=9,width=140,height=28)
        
        
        #product details
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        
        scrolly= Scrollbar(p_frame,orient=VERTICAL)
        scrollx= Scrollbar(p_frame,orient=HORIZONTAL)
        self.ProductTable=ttk.Treeview(p_frame,column=("pid","Category","Supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill= X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.heading("pid",text="Category Id")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Qunatity")
        self.ProductTable.heading("status",text="Status")
        self.ProductTable["show"]="headings"
        
        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
    
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            
                
            
            
            
            
            cur.execute("select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            
                
            
            
            
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
            
            
            
        
    
    
    
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="Select":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
            else:
                cur.execute("select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This product already present,try diffrerent",parent=self.root)
                else:
                    cur.execute("Insert into product(Category,Supplier,name,price,qty,status)values(?,?,?,?,?,?)",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            ))
                    con.commit()
                    messagebox.showinfo("success","Product added Successfully",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
            
            
            
            
        
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])      
         
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","product Id Must be required",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid product id",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                            self.var_cat.get(),
                            self.var_sup.get(),
                            self.var_name.get(),
                            self.var_price.get(),
                            self.var_qty.get(),
                            self.var_status.get(),
                            self.var_pid.get()
                    
                    
                    
                    ))
                    con.commit()
                    messagebox.showinfo("success","product updated Successfully",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)

            
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                
                messagebox.showerror("Error","Select product from the list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","invalid product id",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","product deleted",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)

            
    def clear(self):
        self.var_pid.set("")
        self.var_cat.get(),
        self.var_sup.get(),
        self.var_name.get(),
        self.var_price.get(),
        self.var_qty.get(),
        self.var_status.get(),
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()
        
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select search by text input required",parent=self.root)
                
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","no record found",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
        
        
if __name__=="__main__":
    root=Tk()
    obj =productClass(root)
    root.mainloop()


# In[ ]:





# In[ ]:




