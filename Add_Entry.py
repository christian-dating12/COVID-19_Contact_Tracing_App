import tkinter as tk

class add_entry(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.personal_info_label = tk.Label(self, text=" PERSONAL INFORMATIONS ", height=2, font=("Monteserrat", 10, "bold"))
        self.personal_info_label.place(x=300, y=50)
        self.personal_info_label.config(bg="#800000")

        self.name = tk.Label(self, text="Name: ", height=2, font=("Monteserrat", 10, "bold"))
        self.name.place(x=0, y=110)
        self.name.config(bg="#808080")
        self.name_entry = tk.Entry(self, width=35)
        self.name_entry.place(x=50, y=115)
        self.name_entry.insert(0, " Surname, Given Name, Middle Name")  
        self.name_entry.bind("<FocusIn>", self.clear_name_text)
        self.name_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.sex = tk.Label(self, text="   Sex:   ", height=2, font=("Monteserrat", 10, "bold"))
        self.sex.place(x=492, y=110)
        self.sex.config(bg="#808080")
        self.sex_entry = tk.Entry(self, width=20)
        self.sex_entry.place(x=550, y= 115)
        self.sex_entry.insert(0, " Male / Female")  
        self.sex_entry.bind("<FocusIn>", self.clear_sex_text)
        self.sex_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.age = tk.Label(self, text="  Age:  ", height=2, font=("Monteserrat", 10, "bold"))
        self.age.place(x=0, y=170)
        self.age.config(bg="#808080")
        self.age_entry = tk.Entry(self, width=20)
        self.age_entry.place(x=51, y= 176)
        self.age_entry.insert(0, " Age ")  
        self.age_entry.bind("<FocusIn>", self.clear_age_text)
        self.age_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.email = tk.Label(self, text=" E-mail Address:  ", height=2, font=("Montesarrat", 10, "bold"))
        self.email.place(x=330, y=170)
        self.email.config(bg="#808080")
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.place(x=446, y= 176)
        self.email_entry.insert(0, " -----------------@gmail.com")  
        self.email_entry.bind("<FocusIn>", self.clear_email_text)
        self.email_entry.config(fg="black", bg="#FFFFFF", font=("Montesarrat", 15))

        self.address = tk.Label(self, text=" Current Address: ", height=2, font=("Montesarrat", 10, "bold"))
        self.address.place(x=0, y=235)
        self.address.config(bg="#808080")
        self.address_entry = tk.Entry(self, width=60)
        self.address_entry.place(x=118, y= 240)
        self.address_entry.insert(0, " House no. , Street, Village, Barangay, City ")  
        self.address_entry.bind("<FocusIn>", self.clear_address_text)
        self.address_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.health_status_label = tk.Label(self, text=" HEALTH STATUS ", height=2, font=("Montesarrat", 10, "bold"))
        self.health_status_label.place(x=330, y=290)
        self.health_status_label.config(bg="#800000")



    def clear_name_text(self, event):
        self.name_entry.delete(0, tk.END)
        self.name_entry.config(fg="black")

    def clear_sex_text(self, event):
        self.sex_entry.delete(0, tk.END)
        self.sex_entry.config(fg="black")

    def clear_age_text(self, event):
        self.age_entry.delete(0, tk.END)
        self.age_entry.config(fg="black")

    def clear_email_text(self, event):
        self.email_entry.delete(0, tk.END)
        self.email_entry.config(fg="black")

    def clear_address_text(self, event):
        self.address_entry.delete(0, tk.END)
        self.address_entry.config(fg="black")