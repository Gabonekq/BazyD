from tkinter import *
import sqlite3
 
root = Tk()
root.geometry('500x450')
root.title("Zapisz się")
root["bg"]='blanchedalmond'
 
 
Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()
 
 
 
def database():
   name1=Fullname.get()
   email=Email.get()
   plec=var.get()
   miasto=c.get()
   cel=var1.get()
   conn = sqlite3.connect('cwiczenia.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS osoba (Fullname TEXT,Email TEXT,plec TEXT,miasto TEXT,cel TEXT)')
   cursor.execute('INSERT INTO osoba (Fullname,Email,plec,miasto,cel) VALUES(?,?,?,?,?)',(name1,email,plec,miasto,cel,))
   conn.commit()
    
    
              
label_0 = Label(root, text="Uzupełnij profil", bg='tan',fg="saddlebrown", width=20,font=("bold", 20))
label_0.place(x=90,y=53)
 
 
label_1 = Label(root, text="Imie", bg='tan',fg="saddlebrown", width=20,font=("bold", 10))
label_1.place(x=80,y=130)
 
entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)
 
label_2 = Label(root, text="Email",bg='tan',fg="saddlebrown", width=20,font=("bold", 10))
label_2.place(x=68,y=180)
 
entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)
 
label_3 = Label(root, text="Płeć",bg='tan',fg="saddlebrown", width=20,font=("bold", 10))
label_3.place(x=70,y=230)
 
Radiobutton(root, text="On", bg='tan',fg="saddlebrown", padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Ona", bg='tan',fg="saddlebrown", padx = 20, variable=var, value=2).place(x=290,y=230)
 
label_4 = Label(root, text="Miasto", bg='tan',fg="saddlebrown", width=20,font=("bold", 10))
label_4.place(x=70,y=280)
 
list1 = ['Rzeszów','Łańcut','Jarosław','Przemyśl','inne'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Wybierz') 
droplist.place(x=240,y=280)
droplist["bg"]='blanchedalmond'
 
label_4 = Label(root, text="Cel", bg='tan',fg="saddlebrown", width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="Waga", bg='tan',fg="saddlebrown", variable=var1).place(x=235,y=330)
 
Checkbutton(root, text="Zdrowie", bg='tan',fg="saddlebrown", variable=var2).place(x=290,y=330)
 
Button(root, text='Zapisz', bg='tan',fg="saddlebrown", width=20,command=database).place(x=180,y=380)
 
root.mainloop()