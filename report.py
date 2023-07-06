from tkinter import Tk, Frame, Label, Entry
def report(data_list, plec, wiek):
    
    root = Tk()
    root.title('Raport')
    root.geometry('500x500')
    root["bg"]='blanchedalmond'

    
    title_frame = Frame(root)
    
    title = Label(title_frame, text="Raport", fg="white")
    title.pack()

    
    title_frame.pack(fill='x')
    
    show_data(root, data_list, plec, wiek)



def show_data(root, data_list, plec, wiek):
    
    data = Frame(root, pady=50)
    data.pack()

    # BMI
    re_bmi_label = Label(data, text="BMI:")
    re_bmi_label.grid(column=0, row=0, sticky='w')
    
    re_bmi_entry = Entry(data)
    re_bmi_entry.grid(column=1, row=0, sticky='e')

    # Cisnienie
    re_ck_label = Label(data, text="Ciśnienie:")
    re_ck_label.grid(column=0, row=1, sticky='w')
    
    re_ck_entry = Entry(data)
    re_ck_entry.grid(column=1, row=1, sticky='e')

    # Puls
    re_puls_rate_label = Label(data, text="Puls:")
    re_puls_rate_label.grid(column=0, row=2, sticky='w')
   
    re_puls_rate_entry = Entry(data)
    re_puls_rate_entry.grid(column=1, row=2, sticky='e')

    # Erytrocyty
    re_rbc_label = Label(data, text="Erytrocyty RBC:")
    re_rbc_label.grid(column=0, row=3, sticky='w')
    
    re_rbc_entry = Entry(data)
    re_rbc_entry.grid(column=1, row=3, sticky='e')

    # WBC 
    re_wbc_label = Label(data, text="Leukocyty WBC:")
    re_wbc_label.grid(column=0, row=4, sticky='w')
    
    re_wbc_entry = Entry(data)
    re_wbc_entry.grid(column=1, row=4, sticky='e')

    # tromb
    re_tromb_label = Label(data, text="Trombocyty:")
    re_tromb_label.grid(column=0, row=5, sticky='w')
    
    re_tromb_entry = Entry(data)
    re_tromb_entry.grid(column=1, row=5, sticky='e')

    # Hemoglobina
    re_hg_label = Label(data, text="Hemoglobina:")
    re_hg_label.grid(column=0, row=6, sticky='w')
    # Create entry for hg
    re_hg_entry = Entry(data)
    re_hg_entry.grid(column=1, row=6, sticky='e')

    # Kwas
    re_km_label = Label(data, text="Kwas moczowy:")
    re_km_label.grid(column=0, row=7, sticky='w')
   
    re_km_entry = Entry(data)
    re_km_entry.grid(column=1, row=7, sticky='e')

    # Cholesterol
    re_cholesterol_label = Label(data, text="Cholesterol:")
    re_cholesterol_label.grid(column=0, row=8, sticky='w')
    
    re_cholesterol_entry = Entry(data)
    re_cholesterol_entry.grid(column=1, row=8, sticky='e')

    #insert
    insert_data(re_bmi_entry, re_ck_entry, re_puls_rate_entry, re_rbc_entry, re_wbc_entry, re_tromb_entry,
                re_hg_entry, re_km_entry, re_cholesterol_entry, data_list, plec, wiek)



def insert_data(re_bmi_entry, re_ck_entry, re_puls_rate_entry, re_rbc_entry, re_wbc_entry, re_tromb_entry,
                re_hg_entry, re_km_entry, re_cholesterol_entry, data_list, plec, wiek):
    
    re_bmi_entry.insert(0, bmi(data_list[0].get(), data_list[1].get()))
    re_ck_entry.insert(0, ck_check(data_list[2].get(), data_list[3].get()))
    re_puls_rate_entry.insert(0, puls_check(plec.get(), data_list[4].get(), wiek.get()))
    re_rbc_entry.insert(0, rbc_check(plec.get(), data_list[5].get()))
    re_wbc_entry.insert(0, wbc_check(data_list[6].get()))
    re_tromb_entry.insert(0, tromb_check(data_list[7].get()))
    re_hg_entry.insert(0, hg_check(plec.get(), data_list[8].get()))
    re_km_entry.insert(0, km_check(plec.get(), data_list[9].get()))
    re_cholesterol_entry.insert(0, cholesterol_check(data_list[10].get()))


# bmi
def bmi(waga, wzrost):
    
    waga = eval(waga)
    wzrost = eval(wzrost)

    return waga / wzrost ** 2


# cisnienie
def ck_check(dol, gora):
    
    dol = eval(dol)
    gora = eval(gora)

    if dol <= 60 or gora <= 90:
        return "Niski"
    elif dol <= 80 or gora <= 120:
        return "Średni"
    else:
        return "Wysoki"


# puls
def puls_check(plec, puls, wiek):
    
    plec = int(plec)
    puls = eval(puls)
    wiek = eval(wiek)

    if plec == 0:
        if wiek < 18:
            if puls > 63:
                return "Wysoki"
            elif puls < 61:
                return "Niski"
            else:
                return "Średni"
        elif wiek < 35:
            if puls > 65:
                return "Wysoki"
            elif puls < 62:
                return "Niski"
            else:
                return "Średni"
        elif wiek < 45:
            if puls > 66:
                return "Wysoki"
            elif puls < 63:
                return "Niski"
            else:
                return "Średni"
        elif wiek <= 65:
            if puls > 67:
                return "Wysoki"
            elif puls < 62:
                return "Niski"
            else:
                return "Średni"
        elif wiek > 65:
            if puls > 65:
                return "Wysoki"
            elif puls < 62:
                return "Niski"
            else:
                return "Średni"
    else:
        if wiek < 18:
            if puls > 63:
                return "Wysoki"
            elif puls < 61:
                return "Niski"
            else:
                return "Średni"
        elif wiek < 35:
            if puls > 68:
                return "Wysoki"
            elif puls < 65:
                return "Niski"
            else:
                return "Średni"
        elif wiek < 45:
            if puls > 66:
                return "Wysoki"
            elif puls < 63:
                return "Niski"
            else:
                return "Średni"
        elif wiek <= 65:
            if puls > 68:
                return "Wysoki"
            elif puls < 65:
                return "Niski"
            else:
                return "Średni"
        elif wiek > 65:
            if puls > 65:
                return "Wysoki"
            elif puls < 62:
                return "Niski"
            else:
                return "Średni"


# rbc
def rbc_check(plec, rbc):
    
    plec = int(plec)
    rbc = eval(rbc)

    if plec == 0:
        if rbc < 4.7:
            return "Niski"
        elif rbc > 6.1:
            return "Wysoki"
        else:
            return "Średni"
    else:
        if rbc < 4.2:
            return "Niski"
        elif rbc > 5.4:
            return "Wysoki"
        else:
            return "Średni"


# wbc
def wbc_check(wbc):
    
    wbc = eval(wbc)

    if wbc < 4000:
        return "Niski"
    elif wbc > 11000:
        return "Wysoki"
    else:
        return "Średni"


# tromb
def tromb_check(tromb):
    
    tromb = eval(tromb)

    if tromb < 150000:
        return "Niski"
    elif tromb > 450000:
        return "Wysoki"
    else:
        return "Średni"


# hemoglobina
def hg_check(plec, hg):
    
    plec = int(plec)
    hg = eval(hg)

    if plec == 0:
        if hg < 13.5:
            return "Niski"
        elif hg > 17.5:
            return "Wysoki"
        else:
            return "Średni"
    else:
        if hg < 12.0:
            return "Niski"
        elif hg > 15.5:
            return "Wysoki"
        else:
            return "Średni"


# kwas
def km_check(plec, km):
    
    plec = int(plec)
    km = eval(km)

    if plec == 0:
        if km < 3.4:
            return "Niski"
        elif km > 7.0:
            return "Wysoki"
        else:
            return "Średni"
    else:
        if km < 2.4:
            return "Niski"
        elif km > 7.0:
            return "Wysoki"
        else:
            return "Średni"


# cholesterol
def cholesterol_check(cholesterol):
    
    cholesterol = eval(cholesterol)

    if cholesterol < 200:
        return "Niski"
    elif cholesterol > 240:
        return "Wysoki"
    else:
        return "Średni"
