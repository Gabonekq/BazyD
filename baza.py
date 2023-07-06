from tkinter import *
import sqlite3

root = Tk()
root.title('Aktywności')
root.geometry("500x500")
root["bg"]='blanchedalmond'

# Baza
conn = sqlite3.connect('cwiczenia.db')

c = conn.cursor()

#tabela (w kom żeby jej nie powtarzać)
'''
c.execute("""CREATE TABLE reps (
        data integer,
        nazwa_cw text,
        czas_tre integer,
        kalorie integer,
        ile_serii integer,
        czas_cardio integer
        )""")'''
        
def update():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor() 
    
    record_id = delete_box.get()
    
    c.execute("""UPDATE reps SET 
        data = :data,
        nazwa_cw = :nazwa_cw,
        czas_tre = :czas_tre,
        kalorie = :kalorie ,
        ile_serii = :ile_serii,
        czas_cardio = :czas_cardio
        
        WHERE oid = :oid""",
        {
            'data': data_edit.get(),
            'nazwa_cw': nazwa_cw_edit.get(),
            'czas_tre': czas_tre_edit.get(),
            'kalorie': kalorie_edit.get(),
            'ile_serii': ile_serii_edit.get(),
            'czas_cardio': czas_cardio_edit.get(),
            
            'oid': record_id
            
        })
    
    conn.commit()

    conn.close()
    
    editor.destroy()
    
#funkcja aktualizcji        
def edit():
    global editor
    editor = Tk()
    editor.title('Aktualizacja wpisu')
    editor.geometry("500x500")
    editor["bg"]='blanchedalmond'
    
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor()   
    
    record_id = delete_box.get()
    
    c.execute("SELECT * FROM reps WHERE oid = " + record_id)
    records = c.fetchall()
    
    #global, żeby móc ich używać w innych miejscach
    global data_edit
    global nazwa_cw_edit
    global czas_tre_edit
    global kalorie_edit
    global ile_serii_edit 
    global czas_cardio_edit
    
    data_edit = Entry(editor, width=30)
    data_edit.grid(row=0, column=1, padx=20)

    nazwa_cw_edit = Entry(editor, width=30)
    nazwa_cw_edit.grid(row=1, column=1, padx=20)

    czas_tre_edit = Entry(editor, width=30)
    czas_tre_edit.grid(row=2, column=1, padx=20)

    kalorie_edit = Entry(editor, width=30)
    kalorie_edit.grid(row=3, column=1, padx=20)

    ile_serii_edit = Entry(editor, width=30)
    ile_serii_edit.grid(row=4, column=1, padx=20)

    czas_cardio_edit = Entry(editor, width=30)
    czas_cardio_edit.grid(row=5, column=1, padx=20)

    # do aktualizacji
    data_label = Label(editor, text="Data treningu D/M", bg='tan',fg="saddlebrown")
    data_label.grid(row=0, column=0)

    nazwa_cw_label = Label(editor, text="Kategoria", bg='tan',fg="saddlebrown")
    nazwa_cw_label.grid(row=1, column=0)

    czas_tre_label = Label(editor, text="Czas treningu (w min)", bg='tan',fg="saddlebrown")
    czas_tre_label.grid(row=2, column=0)

    kalorie_label = Label(editor, text="Spalone kalorie", bg='tan',fg="saddlebrown")
    kalorie_label.grid(row=3, column=0)

    ile_serii_label = Label(editor, text="Ilość serii", bg='tan',fg="saddlebrown")
    ile_serii_label.grid(row=4, column=0)

    czas_cardio_label = Label(editor, text="Czas aktywności Cardio (min)", bg='tan',fg="saddlebrown")
    czas_cardio_label.grid(row=5, column=0)
    
    for record in records:
        data_edit.insert(0, record[0])
        nazwa_cw_edit.insert(0, record[1])
        czas_tre_edit.insert(0, record[2])
        kalorie_edit.insert(0, record[3])
        ile_serii_edit.insert(0, record[4])
        czas_cardio_edit.insert(0, record[5])
    
    save_btn = Button(editor, text="Zapisz", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

#delete funkcja
def delete():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor() 
    
    c.execute("DELETE from reps WHERE oid = " + delete_box.get())

    conn.commit()

    conn.close()

#submit funkcja
def submit():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor()
    
    #insert into table
    c.execute("INSERT INTO reps VALUES (:data, :nazwa_cw, :czas_tre, :kalorie, :ile_serii, :czas_cardio)",
            {
                'data': data.get(),
                'nazwa_cw': nazwa_cw.get(),
                'czas_tre': czas_tre.get(),
                'kalorie': kalorie.get(),
                'ile_serii': ile_serii.get(),
                'czas_cardio': czas_cardio.get() 
            })

    conn.commit()

# zamkniecie 
    conn.close()


    data.delete(0, END)
    nazwa_cw.delete(0, END)
    czas_tre.delete(0, END)
    kalorie.delete(0, END)
    ile_serii.delete(0, END)
    czas_cardio.delete(0, END)
    
# query funkcja
def query():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor()   
    
    c.execute("SELECT *, oid FROM reps")
    records = c.fetchall()
    #print(records)
    
    #loop przez wyniki (\t robi tabulator)
    print_records = ''
    for record in records:
        print_records += "Trening: " + str(record[6]) + "\t" + str(record[1]) + "\n"
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    
    
    conn.commit()

# zamkniecie 
    conn.close()
    
#na glownej
data = Entry(root, width=30)
data.grid(row=0, column=1, padx=20)

nazwa_cw = Entry(root, width=30)
nazwa_cw.grid(row=1, column=1, padx=20)

czas_tre = Entry(root, width=30)
czas_tre.grid(row=2, column=1, padx=20)

kalorie = Entry(root, width=30)
kalorie.grid(row=3, column=1, padx=20)

ile_serii = Entry(root, width=30)
ile_serii.grid(row=4, column=1, padx=20)

czas_cardio = Entry(root, width=30)
czas_cardio.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)
# box labels
data_label = Label(root, text="Data treningu D/M", bg='tan',fg="saddlebrown")
data_label.grid(row=0, column=0)

nazwa_cw_label = Label(root, text="Kategoria", bg='tan',fg="saddlebrown")
nazwa_cw_label.grid(row=1, column=0)

czas_tre_label = Label(root, text="Czas treningu (w min)", bg='tan',fg="saddlebrown")
czas_tre_label.grid(row=2, column=0)

kalorie_label = Label(root, text="Spalone kalorie", bg='tan',fg="saddlebrown")
kalorie_label.grid(row=3, column=0)

ile_serii_label = Label(root, text="Ilość serii",bg='tan',fg="saddlebrown")
ile_serii_label.grid(row=4, column=0)

czas_cardio_label = Label(root, text="Czas aktywności Cardio (min)", bg='tan',fg="saddlebrown")
czas_cardio_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Wybierz nr ID", bg='tan',fg="saddlebrown")
delete_box_label.grid(row=9, column=0)
#przyciski
submit_btn = Button(root, text="Dodaj", command=submit, bg='tan',fg="saddlebrown")
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#query button
query_btn = Button(root, text="Pokaż", command=query, bg='tan',fg="saddlebrown")
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#DELETE button
delete_btn = Button(root, text="Usuń", command=delete, bg='tan',fg="saddlebrown")
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

edit_btn = Button(root, text="Aktualizuj", command=edit, bg='tan',fg="saddlebrown")
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

conn.commit()

# zamkniecie 
conn.close()

root.mainloop()
