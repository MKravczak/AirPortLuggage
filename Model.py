import Luggage
import random
import numpy
import customtkinter as CTK
import Flyers

from random import choices



names = ["John", "Jane", "Jack", "Jill", "James", "Jenny", "Jasper", "Jasmine", "Jared", "Jade"]
surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
types= ["suitcase","hiking bag","backpack"]
departures = ["New York", "Lodon", "Paris", "Berlin", "Tokyo", "Beijing"]
baggages = []
passengers_list = []


def date_of_birth():
    return f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1950, 2004)}"
def LuggageCreate():
    baggages.clear()
    passengers_list.clear()
    for i in range(1, 11):
        name = random.choice(names)
        surname = random.choice(surnames)
        passport = random.randint(100000, 999999)
        date_of = date_of_birth()
        baggage = Luggage.Luggage(i, name, surname, str(passport), round(random.uniform(8, 20), 2),
                                  random.choice(departures), str((numpy.random.choice(types, 1, p=[0.7, 0.2, 0.1])[0])))
        print(baggage)
        baggages.append(baggage)
        owner = Flyers.passengers(name, surname, date_of, "USA", passport)
        passengers_list.append(owner)
        print(owner)

def clear_luggage_list_div(luggage_list_div):
    for widget in luggage_list_div.winfo_children():
        widget.destroy()

def LuggageList(luggage_list_div):
    clear_luggage_list_div(luggage_list_div)
    for i in baggages:
        listbox = CTK.CTkTextbox(master=luggage_list_div, width=400, height=20, fg_color="black", border_color="#17AB99", activate_scrollbars=False, border_width=1)
        listbox.pack(pady=0)
        listbox.delete("1.0", "end")
        listbox.insert("end", f" ID:  {i.luggage_id}          Type:    {i.type}           \n")
        listbox.configure(state='disabled')


def FlyersList(luggage_list_div):
    clear_luggage_list_div(luggage_list_div)
    for i in passengers_list:
        listbox = CTK.CTkTextbox(master=luggage_list_div, width=400, height=20, fg_color="black", border_color="#17AB99", activate_scrollbars=False, border_width=1)
        listbox.pack(pady=0)
        listbox.delete("1.0", "end")
        listbox.insert("end", f"   {i.name} {i.surname}                      Passport: {i.passport_number}\n")
        listbox.configure(state='disabled')

def clear_work_zoneB(work_zoneB):
    for widget in work_zoneB.winfo_children():
        if not isinstance(widget, CTK.CTkLabel) or widget.cget("text") != "Luggage's Data:":
            widget.destroy()

def LuggageByID(luggage_id, work_zoneB):
    clear_work_zoneB(work_zoneB)
    try:
        luggage_id = int(luggage_id)
    except ValueError:
        error_label = CTK.CTkLabel(master=work_zoneB, text="Invalid luggage ID. Please enter a number.", text_color="red")
        error_label.pack(pady=5, padx=5, side="top")
        return
    for i in baggages:
        if i.luggage_id == luggage_id:
            id_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" ID:  {i.luggage_id} \n", text_color="white")
            id_label.pack(pady=5, padx=5, side="top", anchor="nw")
            type_label = CTK.CTkLabel(master=work_zoneB,font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Type:  {i.type}\n", text_color="White")
            type_label.pack(pady=5, padx=5, side="top",anchor="nw")
            owner_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Owner:  {i.owner_name} {i.owner_surnname}\n ", text_color="White")
            owner_label.pack(pady=5, padx=5, side="top",anchor="nw")
            ownerPassport_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"),
                                       text=f" Passport Number:  {i.passport}\n ", text_color="White")
            ownerPassport_label.pack(pady=5, padx=5, side="top", anchor="nw")
            if i.weight > 15:
                weight_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Weight:  {i.weight}kg \n ", text_color="red")
            else:
                weight_label = CTK.CTkLabel(master=work_zoneB,font=CTK.CTkFont(family="terminal", size=15, weight="normal"),  text=f" Weight:  {i.weight}kg\n ", text_color="green")
            weight_label.pack(pady=5, padx=5, side="top",anchor="nw")
            destination_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Destination:  {i.destination}\n ", text_color="White")
            destination_label.pack(pady=5, padx=5, side="top",anchor="nw")
            return
    error_label = CTK.CTkLabel(master=work_zoneB, text="No luggage found with the given ID.", text_color="red")
    error_label.pack(pady=5, padx=5, side="top")


def LuggageByOwner(passport_number, work_zoneB):
    clear_work_zoneB(work_zoneB)
    try:
        passport_number = int(passport_number)
    except ValueError:
        error_label = CTK.CTkLabel(master=work_zoneB, text="Invalid passport number. Please enter a number.", text_color="red")
        error_label.pack(pady=5, padx=5, side="top")
        return

    for i in baggages:
        if i.passport == passport_number:
            id_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" ID:  {i.luggage_id} \n", text_color="white")
            id_label.pack(pady=5, padx=5, side="top", anchor="nw")
            type_label = CTK.CTkLabel(master=work_zoneB,font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Type:  {i.type}\n", text_color="White")
            type_label.pack(pady=5, padx=5, side="top",anchor="nw")
            owner_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Owner:  {i.owner_name} {i.owner_surnname}\n ", text_color="White")
            owner_label.pack(pady=5, padx=5, side="top",anchor="nw")
            ownerPassport_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"),
                                       text=f" Passport Number:  {i.passport}\n ", text_color="White")
            ownerPassport_label.pack(pady=5, padx=5, side="top", anchor="nw")
            if i.weight > 15:
                weight_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Weight:  {i.weight}kg \n ", text_color="red")
            else:
                weight_label = CTK.CTkLabel(master=work_zoneB,font=CTK.CTkFont(family="terminal", size=15, weight="normal"),  text=f" Weight:  {i.weight}kg\n ", text_color="green")
            weight_label.pack(pady=5, padx=5, side="top",anchor="nw")
            destination_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=15, weight="normal"), text=f" Destination:  {i.destination}\n ", text_color="White")
    else:
        error_label = CTK.CTkLabel(master=work_zoneB, text="No luggage found with the given ID.", text_color="red")
        error_label.pack(pady=5, padx=5, side="top")