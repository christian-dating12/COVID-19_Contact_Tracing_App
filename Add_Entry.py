import tkinter as tk
from tkinter import StringVar

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

        self.symptoms = tk.Label(self, text=" Are you experiencing any symptoms in the past 7 days such as: ", width=50, height=2, font=("Montesarrat", 10, "bold"))
        self.symptoms.place(x=0, y=350)
        self.symptoms.config(bg="#808080")

        self.fever = StringVar(value="No")
        self.headache = StringVar(value="No")
        self.cough = StringVar(value="No")
        self.colds = StringVar(value="No")
        self.loss_of_taste = StringVar(value="No")
        self.loss_of_smell = StringVar(value="No")
        self.diarrhea = StringVar(value="No")
        self.shortness_of_breath = StringVar(value="No")
        self.difficulty_of_breathing = StringVar(value="No")
        self.body_pains = StringVar(value="No")

        self.fever_checkbox = tk.Checkbutton(self, text="Fever", font=("Montesarrat", 10), variable=self.fever, onvalue="Yes", offvalue="No")
        self.fever_checkbox.place(x=50, y=400)
        self.fever_checkbox.config(bg="#FFFFFF")

        self.headache_checkbox = tk.Checkbutton(self, text="Headache", font=("Montesarrat", 10), variable=self.headache, onvalue="Yes", offvalue="No")
        self.headache_checkbox.place(x=50, y=430)
        self.headache_checkbox.config(bg="#FFFFFF")

        self.cough_checkbox = tk.Checkbutton(self, text="Cough", font=("Montesarrat", 10), variable=self.cough, onvalue="Yes", offvalue="No")
        self.cough_checkbox.place(x=50, y=460)
        self.cough_checkbox.config(bg="#FFFFFF")

        self.colds_checkbox = tk.Checkbutton(self, text="Colds", font=("Montesarrat", 10), variable=self.colds, onvalue="Yes", offvalue="No")
        self.colds_checkbox.place(x=50, y=490)
        self.colds_checkbox.config(bg="#FFFFFF")

        self.loss_of_taste_checkbox = tk.Checkbutton(self, text="Loss of taste", font=("Montesarrat", 10), variable=self.loss_of_taste, onvalue="Yes", offvalue="No")
        self.loss_of_taste_checkbox.place(x=50, y=520)
        self.loss_of_taste_checkbox.config(bg="#FFFFFF")

        self.loss_of_smell_checkbox = tk.Checkbutton(self, text="Loss of smell", font=("Montesarrat", 10), variable=self.loss_of_smell, onvalue="Yes", offvalue="No")
        self.loss_of_smell_checkbox.place(x=200, y=400)
        self.loss_of_smell_checkbox.config(bg="#FFFFFF")

        self.diarrhea_checkbox = tk.Checkbutton(self, text="Diarrhea", font=("Montesarrat", 10), variable=self.diarrhea, onvalue="Yes", offvalue="No")
        self.diarrhea_checkbox.place(x=200, y=430)
        self.diarrhea_checkbox.config(bg="#FFFFFF")

        self.shortness_of_breath_checkbox = tk.Checkbutton(self, text="Shortness of breath", font=("Montesarrat", 10), variable=self.shortness_of_breath, onvalue="Yes", offvalue="No")
        self.shortness_of_breath_checkbox.place(x=200, y=460)
        self.shortness_of_breath_checkbox.config(bg="#FFFFFF")

        self.difficulty_of_breathing_checkbox = tk.Checkbutton(self, text="Difficulty of breathing", font=("Montesarrat", 10), variable=self.difficulty_of_breathing, onvalue="Yes", offvalue="No")
        self.difficulty_of_breathing_checkbox.place(x=200, y=490)
        self.difficulty_of_breathing_checkbox.config(bg="#FFFFFF")

        self.body_pains_checkbox = tk.Checkbutton(self, text="Body pains", font=("Montesarrat", 10), variable=self.body_pains, onvalue="Yes", offvalue="No")
        self.body_pains_checkbox.place(x=200, y=520)
        self.body_pains_checkbox.config(bg="#FFFFFF")





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