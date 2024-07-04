import Luggage
import random
import numpy
import customtkinter as CTK
import Flyers

from random import choices

names = ["John", "Mary", "Tom", "Albert", "Will", "Micheal", "Yamal", "Peter", "Ola", "Matthew", "Nicholas", "Jane",
         "Jack", "Jill", "James", "Jenny", "Jasper", "Jasmine", "Jared", "Jade"]
surnames = ["Smith", "Johnson", "Williams", "Jones", "Polansky", "Jordan", "Tailor", "Terry", "Brown", "Green",
            "Gordon", "La Vine", "Chamberlain", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
types = ["Suitcase", "Hiking bag", "Backpack"]
departures = ["New York", "London", "Paris", "Berlin", "Tokyo", "Beijing"]
citizenship = ["USA", "UK", "France", "Germany", "Japan", "China", "Russia", "Italy", "Spain", "Canada", "Australia","Turkey","Poland","Brazil","Mexico","Argentina","India","South Africa","Egypt","Greece"]
baggages = []
passengers_list = []
baggage = []
pssenger_list = []


def date_of_birth():
    return f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(1950, 2004)}"


def LuggageCreate():
    baggages.clear()
    passengers_list.clear()
    for i in range(1, 21):
        name = random.choice(names)
        surname = random.choice(surnames)
        passport = random.randint(100000, 999999)
        date_of = date_of_birth()
        baggage = Luggage.Luggage(i, name, surname, str(passport), round(random.uniform(8, 20), 2),
                                  random.choice(departures), str((numpy.random.choice(types , 1, p=[0.7, 0.2, 0.1])[0])))
        print(baggage)
        baggages.append(baggage)
        owner = Flyers.passengers(name, surname, date_of, random.choice(citizenship), passport)
        passengers_list.append(owner)
        print(owner)


def Departures(thegates):
    clear_work_zoneB(thegates)
    departures_list = sorted(set(baggage.destination for baggage in baggages))
    main_color = "#17AB99"

    for index, destination in enumerate(departures_list):
        # Create the main gate textbox
        gate = CTK.CTkTextbox(
            master=thegates,
            width=300,
            height=120,
            fg_color="black",
            font=CTK.CTkFont(family="terminal", size=20, weight="bold"),
            text_color=main_color,
            border_color=main_color,
            activate_scrollbars=True,
            border_width=2
        )
        gate.grid(row=index*2, column=0, pady=5, sticky="nsew")
        gate.insert("end", f"Gate {index + 1} -> {destination}\n\n")


        for baggage in baggages:
            if baggage.destination == destination:
                baggage_info = f"■ ID: {baggage.luggage_id} passport:{baggage.passport}"
                if baggage.weight > 15:
                    gate.insert("end", baggage_info + "\n", 'darkred')
                else:
                    gate.insert("end", baggage_info + "\n")

        gate.tag_config('darkred', foreground='#990000')
        gate.configure(state='disabled')
def clear_luggage_list_div(luggage_list_div):
    for widget in luggage_list_div.winfo_children():
        widget.destroy()


def LuggageList(luggage_list_div):
    clear_luggage_list_div(luggage_list_div)
    for i in baggages:
        listbox = CTK.CTkTextbox(master=luggage_list_div, width=400, height=20, fg_color="black",
                                 border_color="#17AB99",  font=CTK.CTkFont(family="terminal", size=20, weight="normal"), activate_scrollbars=False, border_width=1)
        listbox.pack(pady=0)
        listbox.delete("1.0", "end")
        listbox.insert("end", f" ID:  {i.luggage_id}     Type:    {i.type}           \n")
        listbox.configure(state='disabled')


def FlyersList(luggage_list_div):
    clear_luggage_list_div(luggage_list_div)
    for i in passengers_list:
        listbox = CTK.CTkTextbox(master=luggage_list_div, width=400, height=20, fg_color="black",
                                 border_color="#17AB99", activate_scrollbars=False,font=CTK.CTkFont(family="terminal", size=19, weight="normal") ,border_width=1)
        listbox.pack(pady=0)
        listbox.delete("1.0", "end")
        listbox.insert("end", f" {i.name} {i.surname}   Passport: {i.passport_number}\n")
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
        error_label = CTK.CTkLabel(master=work_zoneB, text="Invalid luggage ID. Please enter a number.",
                                   text_color="red")
        error_label.pack(pady=5, padx=5, side="top")
        return
    for i in baggages:
        if i.luggage_id == luggage_id:
            id_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                    text=f" ID:  {i.luggage_id} \n", text_color="white")
            id_label.pack(pady=5, padx=5, side="top", anchor="nw")
            type_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                      text=f" Type:  {i.type}\n", text_color="White")
            type_label.pack(pady=5, padx=5, side="top", anchor="nw")
            owner_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                       text=f" Owner:  {i.owner_name} {i.owner_surnname}\n ", text_color="White")
            owner_label.pack(pady=5, padx=5, side="top", anchor="nw")
            ownerPassport_label = CTK.CTkLabel(master=work_zoneB,
                                               font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                               text=f" Passport Number:  {i.passport}\n ", text_color="White")
            ownerPassport_label.pack(pady=5, padx=5, side="top", anchor="nw")
            if i.weight > 15:
                weight_label = CTK.CTkLabel(master=work_zoneB,
                                            font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                            text=f" Weight:  {i.weight}kg \n ", text_color="red")
            else:
                weight_label = CTK.CTkLabel(master=work_zoneB,
                                            font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                            text=f" Weight:  {i.weight}kg\n ", text_color="green")
            weight_label.pack(pady=5, padx=5, side="top", anchor="nw")
            destination_label = CTK.CTkLabel(master=work_zoneB,
                                             font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                             text=f" Destination:  {i.destination}\n ", text_color="White")
            destination_label.pack(pady=5, padx=5, side="top", anchor="nw")
            return
    error_label = CTK.CTkLabel(master=work_zoneB, text="No luggage found with the given ID.", text_color="red")
    error_label.pack(pady=5, padx=5, side="top")


def OwnerProfile(passport_number, work_zoneB):
    clear_work_zoneB(work_zoneB)
    try:
        passport_number = int(passport_number)
    except ValueError:
        error_label = CTK.CTkLabel(master=work_zoneB, text="Invalid passport number. Please enter a number.",
                                   text_color="red")
        error_label.pack(pady=5, padx=5, side="top")
        return

    for i in passengers_list:
        if i.passport_number == passport_number:
            owner_label = CTK.CTkLabel(master=work_zoneB, font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                       text=f" Owner:  {i.name} {i.surname}\n ", text_color="White")
            owner_label.pack(pady=5, padx=5, side="top", anchor="nw")
            ownerPassport_label = CTK.CTkLabel(master=work_zoneB,
                                               font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                               text=f" Passport Number:  {i.passport_number}\n ", text_color="White")
            ownerPassport_label.pack(pady=5, padx=5, side="top", anchor="nw")
            ownerCitizenship_label = CTK.CTkLabel(master=work_zoneB,
                                                    font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                                    text=f" Citizenship:  {i.citizenship}\n ", text_color="White")
            ownerCitizenship_label.pack(pady=5, padx=5, side="top", anchor="nw")
            ownerDOB_label = CTK.CTkLabel(master=work_zoneB,
                                          font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                          text=f" Date of Birth:  {i.date_of_birth} \n ", text_color="White")
            ownerDOB_label.pack(pady=5, padx=5, side="top", anchor="nw")
            luggage_label = CTK.CTkLabel(master=work_zoneB,
                                         font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
                                         text=" Luggage: ", text_color="White")
            luggage_label.pack(pady=5, padx=5, side="top", anchor="nw")
            for j in baggages:
                if j.owner_name == i.name and j.owner_surnname == i.surname:
                    luggage_list = CTK.CTkLabel(master=work_zoneB,
                                                font=CTK.CTkFont(family="terminal", size=18, weight="normal"),
                                                text=f"   {j.type} registered with ID {j.luggage_id}.\nWeighing {j.weight}kg to {j.destination}\n",
                                                text_color="White")
                    luggage_list.pack(pady=5, padx=5, side="top", anchor="nw")
            return
    else:
        error_label = CTK.CTkLabel(master=work_zoneB, text="No luggage found with the given ID.", text_color="red")
        error_label.pack(pady=5, padx=5, side="top")
