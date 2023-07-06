from tkinter import *
import sqlite3
import PyPDF2
from tkinter import filedialog

root = Tk()
root.title('Aktywności')
root.geometry("500x500")
root["bg"]='blanchedalmond'

# Baza
conn = sqlite3.connect('cwiczenia.db')

c = conn.cursor()

#tabela (w kom żeby jej nie powtarzać)
'''
c.execute("""CREATE TABLE diagnoza(
        imie text,
        wiek integer,
        plec text,
        weight integer,
        wzrost integer,
        ck_dol integer,
        ck_gora integer,
        puls integer,
        rbc integer,
        wbc integer,
        tromb integer,
        hg integer,
        km integer,
        cholesterol integer
        )""")'''
        
def update():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor() 
    
    record_id = delete_box.get()
    
    c.execute("""UPDATE diagnoza SET 
        imie = :imie,
        wiek = :wiek,
        plec = :plec,
        waga = :waga,
        wzrost = :wzrost ,
        ck_dol = :ck_dol,
        ck_gora = :ck_gora,
        puls = :puls,
        rbc = :rbc,
        wbc = :wbc,
        tromb = :tromb,
        hg = :hg,
        km = :km,
        cholesterol = :cholesterol
        
        WHERE oid = :oid""",
        {
            'imie': imie_edit.get(),
            'wiek': wiek_edit.get(),
            'plec': plec_edit.get(),
            'waga': waga_edit.get(),
            'wzrost': wzrost_edit.get(),
            'ck_dol': ck_dol_edit.get(),
            'ck_gora': ck_gora_edit.get(),
            'puls': puls_edit.get(),
            'rbc': rbc_edit.get(),
            'wbc' : wbc_edit.get(),
            'tromb': tromb_edit.get(),
            'hg': hg_edit.get(),
            'km' : km_edit.get(),
            'cholesterol': cholesterol_edit.get(),
            
            'oid': record_id
            
        } )
    
    conn.commit()

    conn.close()
    
    editor.destroy()
    
#pdf
def pdfopen():
    root = Tk()
    root.title('Dokumenty dotyczące badań')
    root.geometry("500x500")
    root["bg"]='blanchedalmond'

    my_text = Text(root, height=30, width=60)
    my_text.pack(pady=10)

    def clear_text_box():
        my_text.delete(1.0, END)
    
    def open_pdf():
        open_file = filedialog.askopenfilename(
            initialdir="C:/Users/qqryq/flask/projekt dane-python/badania pdf",
            title="open pdf",
            filetypes=(
                ("PDF files", "*.pdf"), ("all files", "*.*")))
        if open_file:
            pdf_file = PyPDF2.PdfReader(open_file)
            pwiek = pdf_file.pwieks[0]
            pwiek_stuff = pwiek.extract_text()
        
            my_text.insert(1.0, pwiek_stuff)

    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="open", command=open_pdf)
    file_menu.add_command(label="clear", command=clear_text_box)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    root.mainloop()
#end pdf
#funkcja aktualizcji        
def edit():
    global editor
    editor = Tk()
    editor.title('Wyniki badań laboratoryjnych')
    editor.geometry("500x500")
    editor["bg"]='blanchedalmond'
    
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor()   
    
    record_id = delete_box.get()
    
    c.execute("SELECT * FROM diagnoza WHERE oid = " + record_id)
    records = c.fetchall()
    
    #global
    global imie_edit
    global wiek_edit
    global plec_edit
    global waga_edit
    global wzrost_edit
    global ck_dol_edit 
    global ck_gora_edit
    global puls_edit
    global rbc_edit
    global wbc_edit
    global tromb_edit
    global hg_edit
    global km_edit
    global cholesterol_edit
    
    imie_edit = Entry(editor, width=30)
    imie_edit.grid(row=0, column=1, padx=20)
    
    wiek_edit = Entry(editor, width=30)
    wiek_edit.grid(row=1, column=1, padx=20)

    plec_edit = Entry(editor, width=30)
    plec_edit.grid(row=2, column=1, padx=20)

    waga_edit = Entry(editor, width=30)
    waga_edit.grid(row=3, column=1, padx=20)

    wzrost_edit = Entry(editor, width=30)
    wzrost_edit.grid(row=4, column=1, padx=20)

    ck_dol_edit = Entry(editor, width=30)
    ck_dol_edit.grid(row=5, column=1, padx=20)

    ck_gora_edit = Entry(editor, width=30)
    ck_gora_edit.grid(row=6, column=1, padx=20)
    
    puls_edit = Entry(editor, width=30)
    puls_edit.grid(row=7, column=1, padx=20)
    
    rbc_edit = Entry(editor, width=30)
    rbc_edit.grid(row=8, column=1, padx=20)
    
    wbc_edit = Entry(editor, width=30)
    wbc_edit.grid(row=9, column=1, padx=20)
    
    tromb_edit = Entry(editor, width=30)
    tromb_edit.grid(row=10, column=1, padx=20)
    
    hg_edit = Entry(editor, width=30)
    hg_edit.grid(row=11, column=1, padx=20)
    
    km_edit = Entry(editor, width=30)
    km_edit.grid(row=12, column=1, padx=20)
    
    cholesterol_edit = Entry(editor, width=30)
    cholesterol_edit.grid(row=13, column=1, padx=20)

    # do aktualizacji
    imie_label = Label(editor, text="Imię", bg='tan',fg="saddlebrown")
    imie_label.grid(row=0, column=0)
    
    wiek_label = Label(editor, text="wiek", bg='tan',fg="saddlebrown")
    wiek_label.grid(row=1, column=0)

    plec_label = Label(editor, text="Płeć", bg='tan',fg="saddlebrown")
    plec_label.grid(row=2, column=0)

    waga_label = Label(editor, text="Waga (kg)", bg='tan',fg="saddlebrown")
    waga_label.grid(row=3, column=0)

    wzrost_label = Label(editor, text="Wzrost (w m, oddzielone '.')", bg='tan',fg="saddlebrown")
    wzrost_label.grid(row=4, column=0)

    ck_dol_label = Label(editor, text="Ciśnienie dolne (mmHg)", bg='tan',fg="saddlebrown")
    ck_dol_label.grid(row=5, column=0)

    ck_gora_label = Label(editor, text="Ciśnienie górne (mmHg)", bg='tan',fg="saddlebrown")
    ck_gora_label.grid(row=6, column=0)
    
    puls_label = Label(editor, text="Puls (bpm)", bg='tan',fg="saddlebrown")
    puls_label.grid(row=7, column=0)
    
    rbc_label = Label(editor, text="Erytrocyty RBC (million/mm3)", bg='tan',fg="saddlebrown")
    rbc_label.grid(row=8, column=0)
    
    wbc_label = Label(editor, text="Leukocyty WBC (cells/mm3)", bg='tan',fg="saddlebrown")
    wbc_label.grid(row=9, column=0)
    
    tromb_label = Label(editor, text="Trombocyty (billion/L)", bg='tan',fg="saddlebrown")
    tromb_label.grid(row=10, column=0)
    
    hg_label = Label(editor, text="Hemoglobina (g/dl)", bg='tan',fg="saddlebrown")
    hg_label.grid(row=11, column=0)
    
    km_label = Label(editor, text="Kwas moczowy (mg/dl)", bg='tan',fg="saddlebrown")
    km_label.grid(row=12, column=0)
    
    cholesterol_label = Label(editor, text="Cholesterol (mg/dl)", bg='tan',fg="saddlebrown")
    cholesterol_label.grid(row=13, column=0)
    
    for record in records:
        imie_edit.insert(0, record[0])
        wiek_edit.insert(0, record[1])
        plec_edit.insert(0, record[2])
        waga_edit.insert(0, record[3])
        wzrost_edit.insert(0, record[4])
        ck_dol_edit.insert(0, record[5])
        ck_gora_edit.insert(0, record[6])
        puls_edit.insert(0, record[7])
        rbc_edit.insert(0, record[8])
        wbc_edit.insert(0, record[9])
        tromb_edit.insert(0, record[10])
        hg_edit.insert(0, record[11])
        km_edit.insert(0, record[12])
        cholesterol_edit.insert(0, record[13])
    
    save_btn = Button(editor, text="Zapisz", command=update)
    save_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

#delete funkcja
def delete():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor() 
    
    c.execute("DELETE from diagnoza WHERE oid = " + delete_box.get())

    conn.commit()

    conn.close()

#submit funkcja
def submit():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor()
    
    #insert into table
    c.execute("INSERT INTO diagnoza VALUES (:imie, :wiek, :plec, :waga, :wzrost, :ck_dol, :ck_gora, :puls, :rbc, :wbc, :tromb, :hg, :km, :cholesterol)",
            {
                'imie': imie.get(),
                'wiek': wiek.get(),
                'plec': plec.get(),
                'waga': waga.get(),
                'wzrost': wzrost.get(),
                'ck_dol': ck_dol.get(),
                'ck_gora': ck_gora.get(),
                'puls': puls_edit.get(),
                'rbc': rbc_edit.get(),
                'wbc' : wbc_edit.get(),
                'tromb': tromb_edit.get(),
                'hg': hg_edit.get(),
                'km' : km_edit.get(),
                'cholesterol': cholesterol_edit.get() 
            })

    conn.commit()

# zamkniecie 
    conn.close()


    imie.delete(0, END)
    wiek.delete(0, END)
    plec.delete(0, END)
    waga.delete(0, END)
    wzrost.delete(0, END)
    ck_dol.delete(0, END)
    ck_gora.delete(0, END)
    puls.delete(0, END)
    rbc.delete(0, END)
    wbc.delete(0, END)
    tromb.delete(0, END)
    hg.delete(0, END)
    km.delete(0, END)
    cholesterol.delete(0, END)
    
# query funkcja
def query():
    conn = sqlite3.connect('cwiczenia.db')

    c = conn.cursor()   
    
    c.execute("SELECT *, oid FROM diagnoza")
    records = c.fetchall()
    #print(records)
    
    #loop przez wyniki (\t robi tabulator)
    print_records = ''
    for record in records:
        print_records += "Wynik: " + str(record[0]) + "\n"
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=15, column=0, columnspan=2)
    
    
    conn.commit()

# zamkniecie 
    conn.close()
    
    
#na glownej
imie = Entry(root, width=30)
imie.grid(row=0, column=1, padx=20)

wiek_edit = Entry(root, width=30)
wiek_edit.grid(row=1, column=1, padx=20)

plec = Entry(root, width=30)
plec.grid(row=2, column=1, padx=20)

waga = Entry(root, width=30)
waga.grid(row=3, column=1, padx=20)

wzrost = Entry(root, width=30)
wzrost.grid(row=4, column=1, padx=20)

ck_dol = Entry(root, width=30)
ck_dol.grid(row=5, column=1, padx=20)

ck_gora = Entry(root, width=30)
ck_gora.grid(row=6, column=1, padx=20)

puls_edit = Entry(root, width=30)
puls_edit.grid(row=7, column=1, padx=20)
    
rbc_edit = Entry(root, width=30)
rbc_edit.grid(row=8, column=1, padx=20)
    
wbc_edit = Entry(root, width=30)
wbc_edit.grid(row=9, column=1, padx=20)
    
tromb_edit = Entry(root, width=30)
tromb_edit.grid(row=10, column=1, padx=20)
    
hg_edit = Entry(root, width=30)
hg_edit.grid(row=11, column=1, padx=20)
    
km_edit = Entry(root, width=30)
km_edit.grid(row=12, column=1, padx=20)
    
cholesterol_edit = Entry(root, width=30)
cholesterol_edit.grid(row=13, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=17, column=1)
# box labels
imie_label = Label(root, text="Imię", bg='tan',fg="saddlebrown")
imie_label.grid(row=0, column=0)

wiek_label = Label(root, text="wiek", bg='tan',fg="saddlebrown")
wiek_label.grid(row=1, column=0)

plec_label = Label(root, text="Płeć", bg='tan',fg="saddlebrown")
plec_label.grid(row=2, column=0)

waga_label = Label(root, text="Waga (kg)", bg='tan',fg="saddlebrown")
waga_label.grid(row=3, column=0)

wzrost_label = Label(root, text="Wzrost (w m, oddzielone '.')", bg='tan',fg="saddlebrown")
wzrost_label.grid(row=4, column=0)

ck_dol_label = Label(root, text="Ciśnienie dolne (mmHg)",bg='tan',fg="saddlebrown")
ck_dol_label.grid(row=5, column=0)

ck_gora_label = Label(root, text="Ciśnienie górne (mmHg)", bg='tan',fg="saddlebrown")
ck_gora_label.grid(row=6, column=0)

puls_label = Label(root, text="Puls (bpm)", bg='tan',fg="saddlebrown")
puls_label.grid(row=7, column=0)
    
rbc_label = Label(root, text="Erytrocyty RBC (million/mm3)", bg='tan',fg="saddlebrown")
rbc_label.grid(row=8, column=0)

wbc_label = Label(root, text="Leukocyty WBC (cells/mm3)", bg='tan',fg="saddlebrown")
wbc_label.grid(row=9, column=0)
    
tromb_label = Label(root, text="Trombocyty (billion/L)", bg='tan',fg="saddlebrown")
tromb_label.grid(row=10, column=0)
    
hg_label = Label(root, text="Hemoglobina (g/dl)", bg='tan',fg="saddlebrown")
hg_label.grid(row=11, column=0)
    
km_label = Label(root, text="Kwas moczowy (mg/dl)", bg='tan',fg="saddlebrown")
km_label.grid(row=12, column=0)
    
cholesterol_label = Label(root, text="Cholesterol (mg/dl)", bg='tan',fg="saddlebrown")
cholesterol_label.grid(row=13, column=0)

delete_box_label = Label(root, text="Wybierz nr ID", bg='tan',fg="saddlebrown")
delete_box_label.grid(row=17, column=0)
    
#przyciski
submit_btn = Button(root, text="Dodaj", command=submit, bg='tan',fg="saddlebrown")
submit_btn.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#query button
query_btn = Button(root, text="Pokaż", command=query, bg='tan',fg="saddlebrown")
query_btn.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#DELETE button
delete_btn = Button(root, text="Usuń", command=delete, bg='tan',fg="saddlebrown")
delete_btn.grid(row=18, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#PDF button
delete_btn = Button(root, text="PDF", command=pdfopen, bg='tan',fg="saddlebrown")
delete_btn.grid(row=19, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

conn.commit()

# zamkniecie 
conn.close()

root.mainloop()
