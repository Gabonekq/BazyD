from tkinter import *
#import library
import sqlite3
#open databse

#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=haslo.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("Wprowadź dane")
    else:
      #open database
      conn = sqlite3.connect('cwiczenia.db')
      #select query
      cursor = conn.execute('SELECT * from user where nick="%s" and haslo="%s"'%(uname,pwd))
      #fetch data 
      if cursor.fetchone():
       message.set("Zalogowano")
      else:
       message.set("Błędne dane")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Logowanie")
    #setting height and width of screen
    login_screen.geometry("350x250")
    login_screen["bg"]='blanchedalmond'
    #declaring variable
    global  message;
    global username
    global haslo
    username = StringVar()
    haslo = StringVar()
    message=StringVar()
    #Creating layout of login form
    Label(login_screen,width="300", text="Wpisz dane", bg='tan',fg="saddlebrown",font=("Arial",12,"bold")).pack()
    #Username Label
    Label(login_screen, text="Nick * ",bg="blanchedalmond",fg="saddlebrown",font=("Arial",12,"bold")).place(x=20,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username,bg='blanchedalmond',fg="saddlebrown",font=("Arial",12,"bold")).place(x=120,y=42)
    #haslo Label
    Label(login_screen, text="Hasło * ",bg="blanchedalmond",fg="saddlebrown",font=("Arial",12,"bold")).place(x=20,y=80)
    #haslo textbox
    Entry(login_screen, textvariable=haslo ,show="*",bg='blanchedalmond',fg="saddlebrown",font=("Arial",12,"bold")).place(x=120,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message,bg='blanchedalmond',fg="saddlebrown",font=("Arial",12,"bold")).place(x=95,y=120)
    #Login button
    Button(login_screen, text="Zaloguj", width=10, height=1, command=login, bg='tan',fg="saddlebrown",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()
#calling function Loginform
Loginform()
'''
conn.execute("""
CREATE TABLE user(
user_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
nick TEXT NOT NULL, 
haslo TEXT NOT NULL)
""")
print ("Table user created successfully")
"""
###Output###
Database Opened successfully
Table ADMIN created successfully
"""
'''
'''
conn.execute("INSERT INTO user(nick,haslo) VALUES ('Gabi', 'haslo')");

conn.execute("INSERT INTO user(nick,haslo) VALUES ('Krzysiek', 'haslo')");

conn.commit()
print ("Records inserted successfully")
conn.close()
"""
###Output###
Database Opened successfully
Records inserted successfully
"""'''
'''cursor = conn.execute("SELECT * from user")
print("ID\tnick\thaslo")
for row in cursor:
   print ("{}\t{}\t\t{}".format(row[0],row[1],row[2]))
conn.close()'''