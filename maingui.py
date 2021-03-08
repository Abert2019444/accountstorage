
#work on display and also maybe get tab 
import tkinter as tk 
from tkinter import *
from tkinter import ttk
import sqlite3

root=tk.Tk()
root.title('tabsapp')
root.geometry('600x500')
#root['bg']='blue'
#logo=tk.PhotoImage(file='/Users/albert/bin/Desktop/program_pY_DB/accountstorage/icontry.ico')
root.iconbitmap("icontry.ico") 


# Setting icon of master window


connect = sqlite3.connect('accounts.db')

c= connect.cursor()


notebook=ttk.Notebook(root)
notebook.pack()
#frames (or tabs )
maintab=Frame(notebook,width=600,height=500)
maintab.pack(fill="both", expand=1)

frameadd= Frame(notebook,width=600,height=500)
frameadd.pack(fill='both', expand=1)

frameget=  Frame (notebook,width=600,height=500)
frameget.pack(fill='both', expand=1)

update=  Frame (notebook,width=600,height=500)
update.pack(fill='both', expand=1)

delete=  Frame (notebook,width=600,height=500)
delete.pack(fill='both', expand=1)




# main labels 
label=Label(maintab,text='Welcome this is the main page', width=50,height=23,fg='green')
label.grid(row=0,columnspan=4)
label1=Label(frameadd,text='Welcome this page will obtain info to be saved',width=50,height=13,fg='blue')
label1.grid(row=0,columnspan=3)
label2=Label(frameget,text='Welcome this page will output your information',width=50,height=9,fg='blue')
label2.grid(row=0,columnspan=4)
label3=Label(update,text='Welcome this page will output your information',width=50,height=13,fg='blue')
label3.grid(row=0,columnspan=4)
label4=Label(delete,text='Welcome this page will output your information',width=50,height=13,fg='blue')
label4.grid(row=0,columnspan=4)






#entry widgets for add and their lables 
label=Label(frameadd,text='enter a username')
label1=Label(frameadd,text='enter a password')
label2=Label(frameadd,text='enter type of accounts',height=3)
label.grid(row=1,column=0)
label1.grid(row=2,column=0)
label2.grid(row=3,column=0)
username=Entry(frameadd,width=25)
username.grid(row=1,column=1)
password=Entry(frameadd,width=25)
password.grid(row=2,column=1)
Type=Entry(frameadd,width=25)
Type.grid(row=3, column=1)

#entry widgets for get and their lables 
label3=Label(frameget,text='enter a username')
label4=Label(frameget,text='enter type of accounts')
label5=Label(frameget,text='Type',height=3)
label6=Label(frameget,text='username',height=3)
label7=Label(frameget,text='password',height=3)

label3.grid(row=1,column=0)
label4.grid(row=2,column=0)
label5.grid(row=3,column=0)
label6.grid(row=4,column=0)
label7.grid(row=5,column=0)
username1=Entry(frameget,width=25)
username1.grid(row=1,column=1)
Type1=Entry(frameget,width=25)
Type1.grid(row=2, column=1)
typedata=Entry(frameget, state='disabled', width=35)
typedata.grid(row=3,column=1)
userdata=Entry(frameget,state='disabled',width=35)
userdata.grid(row=4,column=1)
passdata=Entry(frameget,state='disabled',width=35)
passdata.grid(row=5,column=1)




#entry widgets for update page and their lables:
label6=Label(update,text='enter a username')
label7=Label(update,text='enter type of accounts')
label8=Label(update,text='enter password',height=3)
label6.grid(row=1,column=0)
label7.grid(row=2,column=0)
label8.grid(row=3,column=0)
username2=Entry(update,width=25)
username2.grid(row=1,column=1)
Type2=Entry(update,width=25)
Type2.grid(row=2, column=1)
password2=Entry(update,width=25)
password2.grid(row=3,column=1)

#entry widgets for delete and their lables: 
label9=Label(delete,text='enter a username')
label10=Label(delete,text='enter type of accounts')
label9.grid(row=1,column=0)
label10.grid(row=2,column=0)
username3=Entry(delete,width=25)
username3.grid(row=1,column=1)
Type3=Entry(delete,width=25)
Type3.grid(row=2, column=1)

#adding tabs 
notebook.add(maintab, text='main')
notebook.add(frameadd, text='addition')
notebook.add(frameget, text='Get')
notebook.add(update, text='update')
notebook.add(delete, text='delete')




#frame add button functions
def addbutton():
	var=username.get()
	username.delete(0,END)
	var2=password.get()
	password.delete(0,END)
	var3=Type.get()
	Type.delete(0,END)

	c.execute("SELECT * FROM USER WHERE type=? AND username=?",(var,var3 )) 
	DB= c.fetchone()

	if DB is None:

		if len(var)>4 and len(var2)>4 and len(var3)>4:
		
			c.execute(" INSERT INTO USER VALUES (:type, :username, :password)",{'type': var3, 'username': var, 'password':var2} )
			connect.commit()


		else:
			username.insert(0,'input is not valid ')
			
	else:
		username.insert(0,'account already exist ')


# frame get button functions 
def getbutton():
	var=username1.get()
	username1.delete(0,END)
	var3=Type1.get()
	Type1.delete(0,END)
	
	
	c.execute("SELECT * FROM USER WHERE type=? AND username=?",(var3,var )) 
	DB= c.fetchone()
	
	if DB is not None and var in DB and var3 in DB:
		typedata['state']='normal'
		userdata['state']='normal'
		passdata['state']='normal'



		#create those widget and entry widgets for get
		typedata.insert(0,f'the type is { DB[0] }' )
		userdata.insert(0,f'the username is { DB[1] }' )
		passdata.insert(0,f'the password is { DB[2] }' )

		#yourdata.delete(0,END)



	if DB is None:
		typedata.insert(0,'account not found')
		#yourdata.delete(0,END)
	connect.commit()


# frame update button functions 
def upbutton():
	var=username2.get()
	username2.delete(0,END)
	var2=Type2.get()
	Type2.delete(0,END)
	var3=password2.get()
	password2.delete(0,END)


	c.execute(" UPDATE USER SET password=? WHERE type=? AND username=?",(var3,var2,var ))

	connect.commit()


# frame delete button functions 	
def Deletebutton():
	var=username3.get()
	username3.delete(0,END)
	var2=Type3.get()
	Type3.delete(0,END)

	c.execute(" DELETE FROM USER WHERE type=? AND username=?",(var,var2))
	
	connect.commit()



# mainfrmame buttons
b1=Button(maintab,text="exit", highlightbackground="red", width=6, height=3,
	padx=3,pady=3, relief= SUNKEN,command=root.quit)
b1.grid(row=1,columnspan=6)




#frame add buttons
button2= Button(frameadd, text='add',highlightbackground="blue",command=addbutton)
button3= Button(frameadd, text='exit',highlightbackground="red" , command=root.quit)

button2.grid(row=4, column=0)
button3.grid(row=4, column=1)


#frame get buttons
button4= Button(frameget, text='get',  highlightbackground="blue", command=getbutton)
button5= Button(frameget, text='exit',  highlightbackground="red" ,command=root.quit)
button4.grid(row=6, column=0)
button5.grid(row=6, column=1)

#frame update
button6= Button(update, text='update',  highlightbackground="blue" ,command=upbutton)
button7= Button(update, text='exit',  highlightbackground="red",command=root.quit)
button6.grid(row=4, column=0)
button7.grid(row=4, column=1)

#frame delete
button12= Button(delete, text='delete',  highlightbackground="blue",command=Deletebutton)
button13= Button(delete, text='exit', highlightbackground="red", command=root.quit)
button12.grid(row=4, column=0)
button13.grid(row=4, column=1)

root.mainloop()
# connect.close()

def returning():
	c.execute("SELECT * FROM USER")
	db=c.fetchall()
	print(db)
returning()




