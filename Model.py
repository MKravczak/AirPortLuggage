import Luggage
import random
import numpy
import customtkinter as CTK

from random import choices



names = ["John", "Jane", "Jack", "Jill", "James", "Jenny", "Jasper", "Jasmine", "Jared", "Jade"]
surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
types= ["suitcase","hiking bag","backpack"]
departures = ["New York", "Lodon", "Paris", "Berlin", "Tokyo", "Beijing"]
baggages = []

def LuggageCreate():
    baggages.clear()
    for i in range(1, 11):
        baggage = Luggage.Luggage(i, random.choice(names), random.choice(surnames), round(random.uniform(8, 20), 2),
                                  random.choice(departures), str((numpy.random.choice(types, 1, p=[0.7, 0.2, 0.1])[0])))
        print(baggage)
        baggages.append(baggage)

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