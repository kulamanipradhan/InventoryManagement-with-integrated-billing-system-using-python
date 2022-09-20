#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import*


# In[2]:


from PIL import Image,ImageTk


# In[3]:


from employee import employeeClass


# In[4]:


from supplier import supplierClass


# In[5]:


from category import categoryClass


# In[6]:


from product import productClass


# In[7]:


from sales import salesClass


# In[8]:


import sqlite3


# In[9]:


from tkinter import messagebox


# In[10]:


import os


# In[12]:


from billing import BillClass


# In[ ]:


class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("inventory management system")
        self.root.config(bg="white")
        self.icon_title=PhotoImage(file="images/logo1.png")
        title= Label(self.root,text="Inventory management system",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #btn_logout
        btn_billing =Button(self.root,text="Billing",command=self.billing,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #clock
        self.lbl_clock= Label(self.root,text="Welcome to Inventory management system",font=("times new roman",15),bg="#4d636d",fg="white",padx=20)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        
        #leftMenu
        self.MenuLogo =Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        lbl_menuLogo = Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu =Label(LeftMenu,text="Menu",font=("times new roman",20),bg="yellow").pack(side=TOP,fill=X)
        Btn_employee =Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_supplier =Button(LeftMenu,text="supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_category =Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_product=Button(LeftMenu,text="product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_sales =Button(LeftMenu,text="sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Btn_exit =Button(LeftMenu,text="exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        #content
        self.lbl_Employee= Label(self.root,text="Total Employee\n[0]",bd=5, relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_supplier= Label(self.root,text="Total Supplier\n[0]",bd=5, relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)
        
        self.lbl_category= Label(self.root,text="Total Category \n[0]",bd=5, relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category .place(x=1000,y=120,height=150,width=300)
        
        self.lbl_product= Label(self.root,text="Total Product \n[0]",bd=5, relief=RIDGE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_sales= Label(self.root,text="Total Sales\n[0]",bd=5, relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        #FOOTER
        footer= Label(self.root,text="Inventory management system| Developed by Kulamani  and pritam \n for any technical issue contact: 7606962245",font=("times new roman",12),bg="#4d636d",fg="white",padx=20).pack(side=BOTTOM,fill=X)
        self.update_content()
        
        
        
        #==========================================================================================================
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)
    def billing(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)
        
    def update_content(self):
        con = sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f"Total Product \n[{str(len(product))}]")
            
            
            
            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier \n[{str(len(supplier))}]")
            
            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f"Total Category \n[{str(len(category))}]")
            
            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_Employee.config(text=f"Total Employee \n[{str(len(employee))}]")
            bill=len(os.listdir("bill"))
            self.lbl_sales.config(text=f"Total Sales [{str(bill)}]")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
            
            
            
            
        
            
    
        

        
        
if __name__=="__main__":
    root=Tk()
    obj =IMS(root)
    root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




