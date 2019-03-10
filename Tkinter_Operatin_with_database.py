from tkinter import *
import MySQLdb

conn=MySQLdb.connect(host='localhost',password='',user='root',db='tkinter')
curs=conn.cursor()




def do_insert():
	global p,p1
	global stringvars
	global stringvars1
	sql="insert into login(Username,Password) values('%s','%s');"%(p.get(),p1.get())
	curs.execute(sql)
	conn.commit()
	stringvars.set("")
	stringvars1.set("")
	message.config(text='Successfully Inserted',fg='red')

def do_update():
	global p2,p3,L
	sql="update login set password='%s' where username ='%s';"%(p3.get(),p2.get())
	curs.execute(sql)
	conn.commit()
	stringvars.set("")
	stringvars1.set("")
	L.config(text="Successfully Updated")

def Update():
	global p2,p3,L,parent
	global UpdateParent
	stringvars=StringVar()
	stringvars1=StringVar()
	parent.withdraw()
	
	UpdateParent=Tk()
	window1=Frame(UpdateParent)
	window1.pack(side='left',fill='y')
	l=Label(window1, text="Username")
	l.grid(row=0,column=0)

	p2=Entry(window1,textvariable=stringvars)
	p2.grid(row=0,column=1)

	l1=Label(window1,text="password")
	l1.grid(row=1,column=0)
	p3=Entry(window1,show="*",textvariable=stringvars1)
	p3.grid(row=1,column=1)

	ButtUp=Button(window1,text="Update",command=do_update)
	ButtUp.grid(row=2,column=1)
	L=Label(window1,text="")
	L.grid(row=3,column=0)
	ButtonBack=Button(window1,text="Back",relief=RIDGE,command=go_to_Insert) # calling new fuction i.e go_to_insert() instead of calling insert() directy
	ButtonBack.grid(row=2,column=0)

	UpdateParent.mainloop()


def go_to_Insert():

	global UpdateParent
	UpdateParent.withdraw()
	Insert()

def go_to_Inserted():

	global UpdateParent
	UpdatedParent.withdraw()
	Insert()

def do_delete():

	global L6,stringvars4,stringvars5,p4
	sql="delete from login where username='%s';"%(p4.get())
	curs.execute(sql)
	conn.commit()
	stringvars4.set("")
	stringvars5.set("")
	L6.config(text="Successfully Deleted")

def Delete():
	global p4,p5,L6
	global UpdatedParent,stringvars5,stringvars4
	stringvars4=StringVar()
	stringvars5=StringVar()
	parent.withdraw()
	UpdatedParent=Tk()
	window2=Frame(UpdatedParent)
	window2.pack(side="left",fill="y")

	l4=Label(window2, text="Username")
	l4.grid(row=0,column=0)

	p4=Entry(window2,textvariable=stringvars4)
	p4.grid(row=0,column=1)

	l5=Label(window2,text="password")
	l5.grid(row=1,column=0)
	
	p5=Entry(window2,show="*",textvariable=stringvars5)
	p5.grid(row=1,column=1)
	
	L6=Label(window2,text="")
	L6.grid(row=3,column=0)

	
	SubButt=Button(window2,text="Delete",command=do_delete)
	SubButt.grid(row=2,column=1)


	BackButton=Button(window2,text='Back',command=go_to_Inserted)
	BackButton.grid(row=2,column=0)

def filltable():
	global windowRight
	sql='select * from login'
	curs.execute(sql)
	result=curs.fetchall()
	conn.commit()
	L=Label(windowRight,text="studentId")
	L.grid(row=1,column=0)
	L1=Label(windowRight,text="Password")
	L1.grid(row=1,column=1)
		
	for i in range(len(result)):
		for j in range(len(result[i])):
			l=Label(windowRight,text='%s'%(result[i][j]),relief=RIDGE)
			l.grid(row=i+2,column=j,sticky=NSEW)






def Insert():
	global p,p1
	global stringvars
	global parent
	global stringvars1
	global message,windowRight
	
	parent=Tk()
	parent.title("Practising")
	stringvars=StringVar()
	stringvars1=StringVar()
	window =Frame(parent,relief=RIDGE)
	window.pack(side="left",fill="y")
	
	windowRight=Frame(parent,relief=RIDGE)
	windowRight.pack(side='right',fill='y')

	l=Label(window, text="Username")
	l.grid(row=0,column=0)

	p=Entry(window,textvariable=stringvars)
	p.grid(row=0,column=1)

	l1=Label(window,text="password")
	l1.grid(row=1,column=0)
	p1=Entry(window,show="*",textvariable=stringvars1)
	p1.grid(row=1,column=1)

	SubBut=Button(window,text="submit",command=do_insert)
	SubBut.grid(row=2,column=1)

	InsBut=Button(window,text="Update",command=Update)
	InsBut.grid(row=2,column=0)

	DelBut=Button(window,text='Delete',command=Delete)
	DelBut.grid(row=2,column=2)

	message=Label(window, text="")
	message.grid(row=3,column=1)

	ButtonRefresh=Button(windowRight,text='Refresh',command=filltable)
	ButtonRefresh.grid(row=0,column=0)

	
	parent.mainloop()

Insert()




