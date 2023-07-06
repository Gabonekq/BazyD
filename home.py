from tkinter import *
from tkinter import Tk, Frame, Label, Entry, IntVar, Radiobutton, Button, messagebox
from report import report
import PyPDF2
from tkinter import filedialog

data_list = []
plec_value = 0
age_entry = 0


def home():
    
    root = Tk()
    root.title("Twoje zdrowie")
    root.geometry('500x600')
    root["bg"]='blanchedalmond'
    
    fields(root)
    
    root.mainloop()


def fields(root):
    
    imie_wiek_field(root)

    plec_field(root)

    data_field(root)

    generate = Button(root, text="Sprawdź raport z wyników", command=check, height=2, bg='tan',fg="saddlebrown")
    generate.pack(pady=20)
    
    generate = Button(root, text="Sprawdź PDF", command=pdfopen, height=2, bg='tan',fg="saddlebrown")
    generate.pack(pady=20)
    
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
            page = pdf_file.pages[0]
            page_stuff = page.extract_text()
        
            my_text.insert(1.0, page_stuff)

    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="open", command=open_pdf)
    file_menu.add_command(label="clear", command=clear_text_box)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

#root.filename = filedialog.askopenfilename(initialdir="C:/Users/qqryq/flask/5/badania", title="Wybierz plik z wynikami badań", filetypes=(("pdf files", "*.pdf"),("all files", "*.*"))) #*.* wszystkie pliki
#my_label = Label(root, text=root.filename).pack()
#my_image = ImageTk.PhotoImage(Image.open(root.filename))
#my_image_label = Label(image=my_image).pack()

    root.mainloop()
#end pdf
    

def imie_wiek_field(root):
#imie
    imie_wiek_frame = Frame(root)
    imie_wiek_frame.pack(pady=20)

    name_label = Label(imie_wiek_frame, text="Imię:", bg='tan',fg="saddlebrown")
    name_label.grid(column=0, row=0)

    name_entry = Entry(imie_wiek_frame, bd=1)
    name_entry.grid(column=1, row=0, padx=5)
#wiek
    wiek_label = Label(imie_wiek_frame, text="Wiek:", bg='tan',fg="saddlebrown")
    wiek_label.grid(column=3, row=0)

    global wiek_entry
    wiek_entry = Entry(imie_wiek_frame, bd=1)
    wiek_entry.grid(column=4, row=0, padx=5)

def plec_field(root):
#plec  
    plec_frame = Frame(root)
    plec_frame.pack()

    plec_label = Label(plec_frame, text="Płeć:", bg='tan',fg="saddlebrown")
    plec_label.grid(column=0, row=0)

    global plec_value
    plec_value = IntVar()

    male_radio = Radiobutton(plec_frame, text="Mężczyzna", variable=plec_value, value=0, bg='tan',fg="saddlebrown")
    male_radio.grid(column=1, row=0)
    female_radio = Radiobutton(plec_frame, text="Kobieta", variable=plec_value, value=1, bg='tan',fg="saddlebrown")
    female_radio.grid(column=2, row=0)


def data_field(root):
   
    data_frame = Frame(root, pady=50, bg='blanchedalmond')
    data_frame.pack()

    # waga
    weight_label = Label(data_frame, text="Waga (Kg):", bg='tan',fg="saddlebrown")
    weight_label.grid(column=0, row=0, sticky='w')
    
    weight_entry = Entry(data_frame, bd=1)
    weight_entry.grid(column=1, row=0, sticky='e')
    
    data_list.append(weight_entry)

    # wzrost
    height_label = Label(data_frame, text="Wzrost oddzielony kropką (M ):", bg='tan',fg="saddlebrown")
    height_label.grid(column=0, row=1, sticky='w')
   
    height_entry = Entry(data_frame, bd=1)
    height_entry.grid(column=1, row=1, sticky='e')
    
    data_list.append(height_entry)

    # cisnienie low
    bp_low_label = Label(data_frame, text="Ciśnienie dolne (mmHg):", bg='tan',fg="saddlebrown")
    bp_low_label.grid(column=0, row=2, sticky='w')
    
    bp_low_entry = Entry(data_frame, bd=1)
    bp_low_entry.grid(column=1, row=2, sticky='e')
    
    data_list.append(bp_low_entry)

    # cisnienie high
    bp_high_label = Label(data_frame, text="Ciśnienie górne (mmHg):", bg='tan',fg="saddlebrown")
    bp_high_label.grid(column=0, row=3, sticky='w')
    
    bp_high_entry = Entry(data_frame, bd=1)
    bp_high_entry.grid(column=1, row=3, sticky='e')
    
    data_list.append(bp_high_entry)

    # puls
    pulse_rate_label = Label(data_frame, text="Puls (bpm):", bg='tan',fg="saddlebrown")
    pulse_rate_label.grid(column=0, row=4, sticky='w')
    
    pulse_rate_entry = Entry(data_frame, bd=1)
    pulse_rate_entry.grid(column=1, row=4, sticky='e')
    
    data_list.append(pulse_rate_entry)

    # RBC
    rbc_label = Label(data_frame, text="Erytrocyty RBC (million/mm3):", bg='tan',fg="saddlebrown")
    rbc_label.grid(column=0, row=5, sticky='w')
    
    rbc_entry = Entry(data_frame, bd=1)
    rbc_entry.grid(column=1, row=5, sticky='e')
    
    data_list.append(rbc_entry)

    # WBC
    wbc_label = Label(data_frame, text="Leukocyty WBC (cells/mm3):", bg='tan',fg="saddlebrown")
    wbc_label.grid(column=0, row=6, sticky='w')
    
    wbc_entry = Entry(data_frame, bd=1)
    wbc_entry.grid(column=1, row=6, sticky='e')
    
    data_list.append(wbc_entry)

    # Platelets
    platelets_label = Label(data_frame, text="Trombocyty (billion/L):", bg='tan',fg="saddlebrown")
    platelets_label.grid(column=0, row=7, sticky='w')
    
    platelets_entry = Entry(data_frame, bd=1)
    platelets_entry.grid(column=1, row=7, sticky='e')
    
    data_list.append(platelets_entry)

    # hemoglobina
    hb_label = Label(data_frame, text="Hemoglobina (g/dl):", bg='tan',fg="saddlebrown")
    hb_label.grid(column=0, row=8, sticky='w')
    
    hb_entry = Entry(data_frame, bd=1)
    hb_entry.grid(column=1, row=8, sticky='e')
    
    data_list.append(hb_entry)

    # Uric Acid
    uric_acid_label = Label(data_frame, text="Kwas moczowy (mg/dl):", bg='tan',fg="saddlebrown")
    uric_acid_label.grid(column=0, row=9, sticky='w')
    
    uric_acid_entry = Entry(data_frame, bd=1)
    uric_acid_entry.grid(column=1, row=9, sticky='e')
    
    data_list.append(uric_acid_entry)

    # Cholesterol
    cholesterol_label = Label(data_frame, text="Cholesterol (mg/dl):", bg='tan',fg="saddlebrown")
    cholesterol_label.grid(column=0, row=10, sticky='w')
    
    cholesterol_entry = Entry(data_frame, bd=1)
    cholesterol_entry.grid(column=1, row=10, sticky='e')
    
    data_list.append(cholesterol_entry)



def check():

    for data in data_list:

        if data.get() == "":
            messagebox.showwarning("Wypełnij wszystkie pola")
            break
    else:
    
        report(data_list, plec_value, wiek_entry)
