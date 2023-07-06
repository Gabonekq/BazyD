from tkinter import *
import sqlite3

def login():
    
    uname=username.get()
    pwd=haslo.get()
    
    if uname=='' or pwd=='':
        message.set("Wprowadź dane")
    else:
      conn = sqlite3.connect('cwiczenia.db')
      
      cursor = conn.execute('SELECT * from user where nick="%s" and haslo="%s"'%(uname,pwd))
      
      if cursor.fetchone():
       message.set("Zalogowano")
      else:
       message.set("Błędne dane")

def Loginform():
    global login_screen
    login_screen = Tk()
    
    login_screen.title("Logowanie")
    login_screen.geometry("350x250")
    login_screen["bg"]='blanchedalmond'
    
    global  message;
    global username
    global haslo
    username = StringVar()
    haslo = StringVar()
    message=StringVar()
    
    Label(login_screen,width="300", text="Wpisz dane", bg='tan',fg="saddlebrown",font=("Arial",12,"bold")).pack()
    
    Label(login_screen, text="Nick * ",bg="blanchedalmond",fg="saddlebrown",font=("Arial",12,"bold")).place(x=20,y=40)
    
    Entry(login_screen, textvariable=username,bg='blanchedalmond',fg="saddlebrown",font=("Arial",12,"bold")).place(x=120,y=42)
    #haslo 
    Label(login_screen, text="Hasło * ",bg="blanchedalmond",fg="saddlebrown",font=("Arial",12,"bold")).place(x=20,y=80)
    
    Entry(login_screen, textvariable=haslo ,show="*",bg='blanchedalmond',fg="saddlebrown",font=("Arial",12,"bold")).place(x=120,y=82)
    
    Label(login_screen, text="",textvariable=message,bg='blanchedalmond',fg="saddlebrown",font=("Arial",12,"bold")).place(x=95,y=120)
    
    Button(login_screen, text="Zaloguj", width=10, height=1, command=login, bg='tan',fg="saddlebrown",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()

Loginform()

#notatki
'''
conn.execute("""
CREATE TABLE user(
user_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
nick TEXT NOT NULL, 
haslo TEXT NOT NULL)
""")
print ("Table user created successfully")
"""

'''
'''
conn.execute("INSERT INTO user(nick,haslo) VALUES ('Gabi', 'haslo')");

conn.execute("INSERT INTO user(nick,haslo) VALUES ('Krzysiek', 'haslo')");

conn.commit()
print ("Records inserted successfully")
conn.close()
"""
"""'''
'''cursor = conn.execute("SELECT * from user")
print("ID\tnick\thaslo")
for row in cursor:
   print ("{}\t{}\t\t{}".format(row[0],row[1],row[2]))
conn.close()'''