import customtkinter as CTK
import Model
import tkinter as TK

CTK.set_appearance_mode("dark")
CTK.set_default_color_theme("dark-blue")

screen = CTK.CTk()
screen.title("Air Port Luggage System")
screen.geometry("1200x900")

frame = CTK.CTkFrame(master=screen, fg_color="black", bg_color="aqua",border_color="#17AB99", border_width=1)
frame.pack(pady=50, padx=50, fill="both", expand=True)

title = CTK.CTkLabel(master=frame, text="Air Port Luggage System", font=CTK.CTkFont(family="terminal", size=32, weight="bold"))
title.pack(pady=15)


luggage_list_div = CTK.CTkFrame(master=frame, width=400,  fg_color="black", bg_color="aqua",border_color="#17AB99", border_width=1)
luggage_list_div.pack(pady=20, padx=20,side="left", fill="both")
luggage_list_title = CTK.CTkLabel(master=luggage_list_div, width=400, text="Luggage's list", font=CTK.CTkFont(family="terminal", size=20, weight="bold"))
luggage_list_title.pack(pady=25)



for i in Model.baggages:
    listbox = CTK.CTkTextbox(master=luggage_list_div, width=400, height=20, fg_color="black", border_color="#17AB99", activate_scrollbars=False, border_width=1)
    listbox.pack(pady=0)
    listbox.insert("end", f" ID:  {i.luggage_id}          Type:    {i.type}           \n")
    listbox.configure(state='disabled')



work_zone = CTK.CTkFrame(master=frame, width=800,  fg_color="black", border_color="#17AB99", border_width=1)
work_zone.pack(pady=20, padx=20,side="left", fill="both")
work_zone_title = CTK.CTkLabel(master=work_zone, width=800, text="Control panel", font=CTK.CTkFont(family="terminal", size=20, weight="bold"))
work_zone_title.pack(pady=25)








screen.mainloop()




