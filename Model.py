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

