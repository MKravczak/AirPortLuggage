import customtkinter as CTK

import Model
import tkinter as TK

CTK.set_appearance_mode("dark")
CTK.set_default_color_theme("dark-blue")

screen = CTK.CTk()
screen.title("Air Port Luggage System")
screen.geometry("1600x900")

frame = CTK.CTkFrame(master=screen, fg_color="black", bg_color="aqua",border_color="#17AB99", border_width=1)
frame.pack(pady=50, padx=50, fill="both", expand=True)

title = CTK.CTkLabel(master=frame, text="Air Port Luggage System", font=CTK.CTkFont(family="terminal", size=32, weight="bold"))
title.pack(pady=15)


luggage_list_divA = CTK.CTkFrame(master=frame, width=400,  fg_color="black", bg_color="aqua",border_color="#17AB99", border_width=1)
luggage_list_divA.pack(pady=20, padx=20,side="left", fill="both")
luggage_list_title = CTK.CTkLabel(master=luggage_list_divA, width=200, text="Luggage's list", font=CTK.CTkFont(family="terminal", size=20, weight="bold"))
luggage_list_title.pack(pady=25)
luggage_list_div = CTK.CTkFrame(master=luggage_list_divA, width=400,  fg_color="black", border_color="#17AB99", border_width=0)
luggage_list_div.pack(pady=20, padx=20,side="left", fill="both")







work_zoneA = CTK.CTkFrame(master=frame, width=800,  fg_color="black", border_color="#17AB99", border_width=1)
work_zoneA.pack(pady=20, padx=20,side="left", fill="both")

work_zone_title = CTK.CTkLabel(master=work_zoneA, width=800, text="Control panel", font=CTK.CTkFont(family="terminal", size=20, weight="bold"))
work_zone_title.pack(pady=25)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
work_zone = CTK.CTkFrame(master=work_zoneA, width=200,  fg_color="black", border_color="#17AB99", border_width=1)
work_zone.pack(pady=20, padx=20,side="left", fill="both")

button = CTK.CTkButton(master=work_zone, width=250, height= 40, corner_radius=3,  text_color="Black",fg_color="#17AB99", hover_color="#84AAAF",font=CTK.CTkFont(family="terminal", size=20, weight="normal"),  text="Generate Data", command=lambda: Model.LuggageCreate())
button.pack(pady=10, padx=50, side="top", anchor="nw")


button = CTK.CTkButton(master=work_zone, width=250, height= 40, corner_radius=3,  text_color="Black",fg_color="#17AB99", hover_color="#84AAAF", font=CTK.CTkFont(family="terminal", size=20, weight="normal"), text="Show Luggage List", command=lambda: Model.LuggageList(luggage_list_div))
button.pack(pady=10, padx=50, side="top", anchor="nw")

button = CTK.CTkButton(master=work_zone, width=250, height= 40, corner_radius=3,  text_color="Black",fg_color="#17AB99", hover_color="#84AAAF", font=CTK.CTkFont(family="terminal", size=20, weight="normal"), text="Show Passangers List", command=lambda: Model.FlyersList(luggage_list_div))
button.pack(pady=10, padx=50, side="top", anchor="nw")

button = CTK.CTkButton(master=work_zone, width=250, height= 40, corner_radius=3,  text_color="Black",fg_color="#17AB99", hover_color="#84AAAF",font=CTK.CTkFont(family="terminal", size=20, weight="normal"),  text="Show Expected Departures", command=lambda: Model.Departures(departures_div))
button.pack(pady=10, padx=50, side="top", anchor="nw")

baggage_refusal_button = CTK.CTkButton(
    master=work_zone,
    width=250,
    height=40,
    corner_radius=3,
    text_color="Black",
    fg_color="#17AB99",
    hover_color="#84AAAF",
    font=CTK.CTkFont(family="terminal", size=20, weight="normal"),
    text="Send Baggage to Gates",
    command=lambda: [Model.DeparturesWithWeightLimit(departures_div,15), Model.RejectedBaggage(rejected_baggage_textbox)]
)
baggage_refusal_button.pack(pady=10, padx=50, side="top", anchor="nw")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

work_zoneB = CTK.CTkFrame(master=work_zoneA, width=400, height=600,  fg_color="black", border_color="#17AB99", border_width=1)
work_zoneB.pack(pady=20, padx=20,side="top", fill="both")

descriptionA = CTK.CTkLabel(master=work_zoneB, width=400,  text="Output Screen", font=CTK.CTkFont(family="terminal", size=20, weight="bold"))
descriptionA.pack(pady=5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
work_zoneC = CTK.CTkFrame(master=work_zoneA, width=400, height=350, fg_color="black", border_color="#17AB99", border_width=1)
work_zoneC.pack(pady=20, padx=20, side="top", fill="both")

luggage_frame = CTK.CTkFrame(master=work_zoneC, fg_color="black")
luggage_frame.pack(pady=10, padx=20, side="top", fill="x")

luggage_input = CTK.CTkEntry(master=luggage_frame, width=100, font=CTK.CTkFont(family="terminal", size=20, weight="bold"), height=40, corner_radius=3, text_color="Black", fg_color="#17AB99")
luggage_input.pack(pady=5, padx=5, side="left")

button1 = CTK.CTkButton(master=luggage_frame, width=200, height=40, corner_radius=3, text_color="Black", fg_color="#17AB99", font=CTK.CTkFont(family="terminal", size=20, weight="normal"), hover_color="#84AAAF", text="Check Luggage By ID", command=lambda: Model.LuggageByID(luggage_input.get(), work_zoneB))
button1.pack(pady=5, padx=5, side="left")

passanger_frame = CTK.CTkFrame(master=work_zoneC, fg_color="black")
passanger_frame.pack(pady=10, padx=20, side="top", fill="x")

passanger_input = CTK.CTkEntry(master=passanger_frame, width=100, font=CTK.CTkFont(family="terminal", size=20, weight="bold"), height=40, corner_radius=3, text_color="Black", fg_color="#17AB99")
passanger_input.pack(pady=5, padx=5, side="left")

button2 = CTK.CTkButton(master=passanger_frame, width=300, height=40, corner_radius=3, text_color="Black", fg_color="#17AB99", font=CTK.CTkFont(family="terminal", size=20, weight="normal"), hover_color="#84AAAF", text="Check Passanger By Passport Number", command=lambda: Model.OwnerProfile(passanger_input.get(), work_zoneB))
button2.pack(pady=5, padx=5, side="left")

rejected_baggage_frame = CTK.CTkFrame(master=work_zoneA, fg_color="black")
rejected_baggage_frame.pack(pady=10, padx=20, side="bottom", fill="x")

rejected_baggage_label = CTK.CTkLabel(master=rejected_baggage_frame, text="Rejected Baggage", font=CTK.CTkFont(family="terminal", size=20, weight="bold"))
rejected_baggage_label.pack(pady=5, padx=5, side="top")

rejected_baggage_frameB = CTK.CTkFrame(master=rejected_baggage_frame, fg_color="black")
rejected_baggage_frameB.pack(pady=1, padx=1, side="bottom", fill="x")

rejected_baggage_textbox = CTK.CTkTextbox(master=rejected_baggage_frameB, width=400, height=250, fg_color="black",
                                          border_color="#17AB99", activate_scrollbars=True, border_width=1,
                                          font=CTK.CTkFont(family="terminal", size=22, weight="bold"),text_color="red")
rejected_baggage_textbox.pack(pady=5, padx=5, side="top")







departures_div = CTK.CTkFrame(master=frame, width=800,  fg_color="black", bg_color="aqua",border_color="#17AB99", border_width=1)
departures_div.pack(pady=20, padx=20,side="left", fill="both")


departures_div_title = CTK.CTkLabel(master=departures_div, width=500, text="Departures", font=CTK.CTkFont(family="terminal", size=20, weight="bold"))
departures_div_title.pack(pady=25)


thegates = CTK.CTkFrame(master=departures_div, width=450, fg_color="black", border_color="#17AB99", border_width=0)
thegates.pack(pady=10, padx=20, side="left", fill="both", expand=True)







screen.mainloop()




