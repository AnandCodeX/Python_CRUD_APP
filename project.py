from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import cx_Oracle

#----------CODE FOR ROOT FRMME--------------------

root = Tk()
root.title("S. M. S.")
root.geometry("400x400+450+100")

#----------CREATING BUTTON------------------------
btnAdd = Button(root, text="Add", font=("arel",16,'bold'),width =10,command=None)
btnView = Button(root, text="View", font=("arel",16,'bold'),width =10,command=None)
btnUpdate = Button(root, text="Update", font=("arel",16,'bold'),width =10,command=None)
btnDelete = Button(root, text="Delete", font=("arel",16,'bold'),width =10,command=None)
btnGraph = Button(root, text="Graph", font=("arel",16,'bold'),width =10)


#----------PACKING BUTTON-------------------------
btnAdd.pack(pady=10)
btnView.pack(pady=10) 
btnUpdate.pack(pady=10) 
btnDelete.pack(pady=10) 
btnGraph.pack(pady=10)

root.mainloop()