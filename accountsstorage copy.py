#import colorama 
#fix bugs and maybe try gui app
import sqlite3
import sys
from colorama import Fore
# all functions work but there are still some bugs      

connect = sqlite3.connect('accounts.db')
c= connect.cursor()
#how to create a table

c.execute(""" CREATE TABLE USER   
 (           
 	        type TEXT,
  			username TEXT,
 			password TEXT
 			
 			)
  			""" )
connect.commit()
#connect.close()

def adding_users(Type,username,password): #adding user to database
	#adding Users
	c.execute(" INSERT INTO USER VALUES (:type, :username, :password)",{'type': Type, 'username': username, 'password':password} )
	connect.commit()
	connect.close()


def get(Type,username):
	c.execute("SELECT * FROM USER WHERE type=? AND username=?",(Type,username )) 
	var= c.fetchone()
	if Type in var and username in var:
		print(var)
	elif var is None:
		print('account not found')
	connect.commit()
	connect.close()
#print(get())

def update(Type,username):
	c.execute("SELECT * FROM USER WHERE type=? AND username=?",(Type,username ))
	var= c.fetchone()
	if Type in var and username in var:
		password=str(input('enter a new password: '))
		c.execute(" UPDATE USER SET password=? WHERE type=? AND username=?",(password,Type,username ))
	elif var is None:
			print('username not found')
	connect.commit()
	connect.close()

def delete(Type,username):
	c.execute("SELECT * FROM USER WHERE type=? AND username=?",(Type,username ))
	var= c.fetchone()
	
	if Type in var and username in var:
		c.execute(" DELETE FROM USER WHERE type=? AND username=?",(Type,username ))
	elif var is None:
		print('account not found')

	connect.commit()
	connect.close()

	


if __name__ == '__main__':
	command=''
	while command!='exit':
		command=input(Fore.BLUE+ '''enter a command from the following:
		>enter get to get information.
		>enter add to add more accounts.
		>enter delete to delete an account.
		>enter change to update password.


		 ''')

		if command== 'add':
			Type=str(input(Fore.WHITE+'enter the type of account to save: '))
			username=str(input(Fore.WHITE+'enter a username: '))
			password=str(input(Fore.WHITE+'enter a password: '))
			adding_users(Type,username,password)
			print('\n')
		
		if command=='get':
			Type=str(input(Fore.WHITE+'enter the type of account: '))
			username=str(input(Fore.WHITE+'enter a username: '))
			get(Type,username)
				
				
		if command=='change':
			Type=str(input(Fore.WHITE+'enter the type of account: '))
			username=str(input(Fore.WHITE+'enter a username: '))
			update(Type,username)
			print('\n')
		if command== 'delete':
			Type=str(input(Fore.WHITE+'enter the type of account to delete: '))
			username=str(input(Fore.WHITE+'enter a username: '))
			delete(Type,username)
			print('\n')





			



			



