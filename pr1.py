from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from matplotlib import pyplot as plt
import cx_Oracle
import socket
import requests
import bs4


#----------------------------Root Frame Functions & Code------------------------------------------------------------

def f1():       # ADD
	adst.deiconify()
	root.withdraw()

def f2():       #VIEW
	viSt.deiconify()
	root.withdraw()
	con = None
	cursor = None

	try:
		con = cx_Oracle.connect("system/abc123")	
		cursor = con.cursor()
		sql="select * from Student"
		
		cursor.execute(sql)
		data = cursor.fetchall()
		msg=""
		for d in data:
			msg = msg+"rno= "+str(d[0])+" name= "+str(d[1])+" marks= "+str(d[2])+"\n"
		stData.configure(state='normal')
		stData.insert(INSERT,msg)
		stData.configure(state='disabled')
		
	
	except cx_Oracle.DatabaseError as e:
		print("insert issue ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def f3():           # UPDATE
	udst.deiconify()
	root.withdraw()

def f4():          # DELETE
	dst.deiconify()
	root.withdraw()

def f5():           # GRAPH
	con = None
	cursor = None

	try:
		con = cx_Oracle.connect("system/abc123")	
		gcursor = con.cursor()
		gsql="select * from Student"
		
		gcursor.execute(gsql)
		gdata = gcursor.fetchall()
		namelist=[]
		markslist=[]

		for g in gdata:

			namelist.append(g[1])
			markslist.append(g[2])

		print(namelist)
		print(markslist)
		
		plt.bar(namelist,markslist)
		plt.show()
	
	except cx_Oracle.DatabaseError as e:
		print("insert issue ",e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


#----------------------------Weather & City---------------------------------------------------------------------------

try:
    socket.create_connection(("www.google.com",80))
    res = requests.get("https://ipinfo.io/")
    data = res.json()
    city = data['city']
    a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
    a2="&q="+city
    a3="&appid=c6e315d09197cec231495138183954bd"
    api_address=a1+a2+a3
    res1=requests.get(api_address)
    data=res1.json()
    temp1=data['main']['temp']
except OSError as e:
    temp2=print("Check Network")

#--------------------------------Daily Quote-------------------------------------------------------------------------

try:
	res=requests.get("https://www.brainyquote.com/quote_of_the_day.html")
	soup=bs4.BeautifulSoup(res.text,'lxml')
	quote=soup.find('img',{"class":"p-qotd"})
	msg=quote['alt']
except:
	msg1=print("Check Network")

#-------------------------------CODE FOR MAIN ROOT FRMME-------------------------------------------------------------

root = Tk()
root.title("S. M. S.")
root.geometry("500x450+400+100")
root.configure(background ='dark blue')

#-------------------------------CREATING BUTTON---------------------------------------------------------------------

btnAdd = Button(root, text="Add", font=("arel",16,'bold'),width =10,background ='light blue',command=f1)
btnView = Button(root, text="View", font=("arel",16,'bold'),width =10,background ='light blue',command=f2)
btnUpdate = Button(root, text="Update", font=("arel",16,'bold'),width =10,background ='light blue',command=f3)
btnDelete = Button(root, text="Delete", font=("arel",16,'bold'),width =10,background ='light blue',command=f4)
btnGraph = Button(root, text="Graph", font=("arel",16,'bold'),width =10,background ='light blue',command=f5)
lblCity= Label(root,text=city,font=("arel",12,'bold'),width =10,background ='light blue')
lblTemp= Label(root,text=temp1,font=("arel",12,'bold'),width =10,background ='light blue')
lblQuote= Label(root,text=msg,font=("arel",10,'italic'),background ='light blue')

#-------------------------------PACKING BUTTON---------------------------------------------------------------

btnAdd.pack(pady=10)
btnView.pack(pady=10) 
btnUpdate.pack(pady=10) 
btnDelete.pack(pady=10) 
btnGraph.pack(pady=10)
lblCity.pack()
lblTemp.pack()
lblQuote.pack(pady=10)

'''------------------------------------------------------------------------------------------------------------------------------------'''

#--------------------------------ADD FRAME-----------------------------------------------------------------
adst= Toplevel(root)
adst.title("Add Student")
adst.geometry("500x450+400+100")
adst.configure(background ='dark blue')
adst.withdraw()

def fa1():
	root.deiconify()
	adst.withdraw()

def fa2():
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		
		srno = entAddRno.get()
		if srno.isdigit() and int(srno) > 0:
			rno = int(srno)
		else:
			messagebox.showerror("mistake ","incorrect roll no")
			entAddRno.delete(0,END)
			entAddRno.focus()
			return

		sname = entAddName.get()
		if sname.isalpha():
			name = sname
		else:
			messagebox.showerror("mistake ","incorrect input name")
			entAddName.delete(0,END)
			entAddName.focus()
			return

		smarks = entAddMarks.get()
		if smarks.isdigit() and int(smarks) > 0:
			marks = int(smarks)
		else:
			messagebox.showerror("mistake ","incorrect input marks")
			entAddMarks.delete(0,END)
			entAddMarks.focus()
			return
			
		cursor= con.cursor()
		sql="insert into Student values('%d','%s','%d')"
		args = (rno,name,marks)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+"row inserted"
		messagebox.showinfo("success ",msg)
		entAddName.delete(0,END)
		entAddRno.delete(0,END)
		entAddMarks.delete(0,END)
		entAddRno.focus()
		
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure ",e)
		entAddName.delete(0,END)
		entAddRno.delete(0,END)
		entAddMarks.delete(0,END)
		entAddRno.focus()

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close() 
#----------labeling
lblAddRno = Label(adst,text="enter no")
lblAddName = Label(adst,text="enter name")
lblAddMarks = Label(adst,text="enter marks")
#----------entry text
entAddRno = Entry(adst,bd=5)
entAddName = Entry(adst,bd=5)
entAddMarks = Entry(adst,bd=5)

btnAddSave = Button(adst, text="Save",command=fa2)
btnAddBack = Button(adst, text="Back",command=fa1)
#-----------packing

lblAddRno.pack(pady=10) 
entAddRno.pack(pady=10)

lblAddName.pack(pady=10)  
entAddName.pack(pady=10) 

lblAddMarks.pack(pady=10)  
entAddMarks.pack(pady=10) 

btnAddSave.pack(pady=10) 
btnAddBack.pack(pady=10)

#------------------------------------VIEW FRAME-------------------------------------------------

def fv1():
	stData.configure(state='normal')
	stData.delete('1.0', END)
	root.deiconify()
	viSt.withdraw()

viSt = Toplevel(root)    
viSt.title("View Student")
viSt.geometry("500x450+400+100")
viSt.configure(background ='dark blue')
viSt.withdraw()

stData = scrolledtext.ScrolledText(viSt, width = 30, height =5)
btnViewBack = Button(viSt, text="Back",command=fv1)

stData.pack(pady=10)
btnViewBack.pack(pady=10)

#------------------------------------UPDATE FRAME----------------------------------------------------
udst= Toplevel(root)
udst.title("Update Student")
udst.geometry("500x450+400+100")
udst.configure(background ='dark blue')
udst.withdraw()

def fu1():
	root.deiconify()
	udst.withdraw()

def fu2():
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")
		
		srnoo = entUpdRno.get()
		if srnoo.isdigit() and int(srnoo) > 0:
			rnoo = int(srnoo)
		else:
			messagebox.showerror("mistake ","incorrect roll no")
			entUpdRno.delete(0,END)
			entUpdRno.focus()
			return

		snamee = entUpdName.get()
		if snamee.isalpha():
			namee = snamee
		else:
			messagebox.showerror("mistake ","incorrect input name")
			entUpdName.delete(0,END)
			entUpdName.focus()
			return

		smarkss = entUpdMarks.get()
		if smarkss.isdigit() and int(smarkss) > 0:
			markss = int(smarkss)
		else:
			messagebox.showerror("mistake ","incorrect input marks")
			entUpdMarks.delete(0,END)
			entUpdMarks.focus()
			return
			
		cursor= con.cursor()
		sql="update Student set NAME ='%s',MARKS = '%d' where RNO = '%d'"
		args = (namee,markss,rnoo)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+"row updated"
		messagebox.showinfo("success ",msg)

		entUpdMarks.delete(0,END)
		entUpdName.delete(0,END)
		entUpdRno.delete(0,END)
		entUpdRno.focus()
		
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure ",e)
		entUpdMarks.delete(0,END)
		entUpdName.delete(0,END)
		entUpdRno.delete(0,END)
		entUpdRno.focus()

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close() 
#----------------labeling
lblUpdRno = Label(udst,text="enter no")
lblUpdName = Label(udst,text="enter name")
lblUpdMarks = Label(udst,text="enter marks")
#----------------entry text
entUpdRno = Entry(udst,bd=5)
entUpdName = Entry(udst,bd=5)
entUpdMarks = Entry(udst,bd=5)

btnUpdSave = Button(udst, text="Save",command=fu2)
btnUpdBack = Button(udst, text="Back",command=fu1)
#----------------udst packing
lblUpdRno.pack(pady=10) 
entUpdRno.pack(pady=10)

lblUpdName.pack(pady=10)  
entUpdName.pack(pady=10) 

lblUpdMarks.pack(pady=10)  
entUpdMarks.pack(pady=10) 

btnUpdSave.pack(pady=10) 
btnUpdBack.pack(pady=10)

#---------------------------------------DELETE FRAME----------------------------------------------------------

dst= Toplevel(root)
dst.title("Delete Student")
dst.geometry("500x450+400+100")
dst.configure(background ='dark blue')
dst.withdraw()

def fd1():
	root.deiconify()
	dst.withdraw()

def fd2():
	con = None
	cursor = None
	try:
		con = cx_Oracle.connect("system/abc123")


		drno = entDelRno.get()
		if drno.isdigit() and int(drno) > 0:
			rrno = int(drno)
		else:
			messagebox.showerror("Mistake", "incorrect rno ")
			entDelRno.focus()
			return
					
		cursor= con.cursor()
		sql="delete from Student where RNO = '%d'"
		args = (rrno)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+" row Deleted"
		messagebox.showinfo("success ",msg)

		entDelRno.delete(0,END)
		entDelRno.focus()
		
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure ",e)
		entDelRno.delete(0,END)
		entDelRno.focus()

	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close() 
#---------------------labeling
lblDelRno = Label(dst,text="enter no")
#---------------------entry text
entDelRno = Entry(dst,bd=5)
btnDelSave = Button(dst, text="Delete",command=fd2)
btnDelBack = Button(dst, text="Back",command=fd1)
#---------------------packing
lblDelRno.pack(pady=10) 
entDelRno.pack(pady=10)
btnDelSave.pack(pady=10) 
btnDelBack.pack(pady=10)


root.mainloop()