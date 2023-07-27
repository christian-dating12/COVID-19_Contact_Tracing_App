import tkinter as tk
from tkinter import StringVar
import csv

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
        self.name_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.sex = tk.Label(self, text="   Sex:   ", height=2, font=("Monteserrat", 10, "bold"))
        self.sex.place(x=492, y=110)
        self.sex.config(bg="#808080")
        self.sex_entry = tk.Entry(self, width=20)
        self.sex_entry.place(x=550, y= 115)
        self.sex_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.age = tk.Label(self, text="  Age:  ", height=2, font=("Monteserrat", 10, "bold"))
        self.age.place(x=0, y=170)
        self.age.config(bg="#808080")
        self.age_entry = tk.Entry(self, width=20)
        self.age_entry.place(x=51, y= 176)
        self.age_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.email = tk.Label(self, text=" E-mail Address:  ", height=2, font=("Montesarrat", 10, "bold"))
        self.email.place(x=330, y=170)
        self.email.config(bg="#808080")
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.place(x=446, y= 176)
        self.email_entry.config(fg="black", bg="#FFFFFF", font=("Montesarrat", 15))

        self.address = tk.Label(self, text=" Current Address: ", height=2, font=("Montesarrat", 10, "bold"))
        self.address.place(x=0, y=235)
        self.address.config(bg="#808080")
        self.address_entry = tk.Entry(self, width=60)
        self.address_entry.place(x=118, y= 240)
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
        self.none = StringVar(value="No")

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

        self.none_checkbox = tk.Checkbutton(self, text="None of the above", font=("Montesarrat", 10), variable=self.none, onvalue="Yes", offvalue="No")
        self.none_checkbox.place(x=125, y=550)
        self.none_checkbox.config(bg="#FFFFFF")

        self.vaccine_label = tk.Label(self, text="Have you been vaccinated for COVID-19?", width=40, height=2,  font=("Monteserrat", 10, "bold"))
        self.vaccine_label.place(x=450, y=350)
        self.vaccine_label.config(bg="#808080")

        self.first = StringVar(value="No")
        self.second = StringVar(value="No")
        self.first_booster = StringVar(value="No")
        self.second_booster = StringVar(value="No")
        self.not_yet = StringVar(value="No")

        self.first_checkbox = tk.Checkbutton(self, text="Vaccinated, 1st Dose", font=("Montesarrat", 10), variable=self.first, onvalue="Yes", offvalue="No")
        self.first_checkbox.place(x=525, y=400)
        self.first_checkbox.config(bg="#FFFFFF")

        self.second_checkbox = tk.Checkbutton(self, text="Fully Vaccinated, 2nd Dose", font=("Montesarrat", 10), variable=self.second, onvalue="Yes", offvalue="No")
        self.second_checkbox.place(x=525, y=430)
        self.second_checkbox.config(bg="#FFFFFF")

        self.first_booster_checkbox = tk.Checkbutton(self, text="1st Booster Shot", font=("Montesarrat", 10), variable=self.first_booster, onvalue="Yes", offvalue="No")
        self.first_booster_checkbox.place(x=525, y=460)
        self.first_booster_checkbox.config(bg="#FFFFFF")

        self.second_booster_checkbox = tk.Checkbutton(self, text="2nd Booster Shot", font=("Montesarrat", 10), variable=self.second_booster, onvalue="Yes", offvalue="No")
        self.second_booster_checkbox.place(x=525, y=490)
        self.second_booster_checkbox.config(bg="#FFFFFF")

        self.not_yet_checkbox = tk.Checkbutton(self, text="Not Yet", font=("Montesarrat", 10), variable=self.not_yet, onvalue="Yes", offvalue="No")
        self.not_yet_checkbox.place(x=525, y=520)
        self.not_yet_checkbox.config(bg="#FFFFFF")

        self.contact_person_label = tk.Label(self, text=" CONTACT PERSON DETAILS ", height=2, font=("Montesarrat", 10, "bold"))
        self.contact_person_label.place(x=950, y=50)
        self.contact_person_label.config(bg="#800000")

        self.contact_name = tk.Label(self, text=" Name: ", height=2, font=("Montesarrat", 10, "bold"))
        self.contact_name.place(x=900, y=110)
        self.contact_name.config(bg="#808080")
        self.contact_name_entry = tk.Entry(self, width=35)
        self.contact_name_entry.place(x=950, y=150)
        self.contact_name_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.contact_number = tk.Label(self, text=" Contact Number: ", height=2, font=("Montesarrat", 10, "bold"))
        self.contact_number.place(x=900, y=210)
        self.contact_number.config(bg="#808080")
        self.contact_number_entry = tk.Entry(self, width=35)
        self.contact_number_entry.place(x=950, y=250)
        self.contact_number_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.contact_email = tk.Label(self, text=" E-mail Address: ", height=2, font=("Montesarrat", 10, "bold"))
        self.contact_email.place(x=900, y=310)
        self.contact_email.config(bg="#808080")
        self.contact_email_entry = tk.Entry(self, width=35)
        self.contact_email_entry.place(x=950, y=350)
        self.contact_email_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        self.contact_relationship = tk.Label(self, text=" Relationship to the contact person: ", height=2, font=("Montesarrat", 10, "bold"))
        self.contact_relationship.place(x=900, y=410)
        self.contact_relationship.config(bg="#808080")
        self.contact_relationship_entry = tk.Entry(self, width=35)
        self.contact_relationship_entry.place(x=950, y=450)
        self.contact_relationship_entry.config(fg="black", bg="#FFFFFF", font=("Monteserrat", 15))

        submit = tk.Button(self, text=" SUBMIT ", command= self.submit_data, bg="#800000", height=2, width = 25)
        submit.place(x=700, y=550)

    def submit_data(self):

        user_name = self.name_entry.get()
        user_sex = self.sex_entry.get()
        user_age = self.age_entry.get()
        user_email = self.email_entry.get()
        user_address = self.address_entry.get()

        user_fever = self.fever.get()
        user_headache = self.headache.get()
        user_cough = self.cough.get()
        user_colds = self.colds.get()
        user_loss_of_taste = self.loss_of_taste.get()
        user_loss_of_smell = self.loss_of_smell.get()
        user_diarrhea = self.diarrhea.get()
        user_shortness_of_breath = self.shortness_of_breath.get()
        user_difficulty_of_breathing = self.difficulty_of_breathing.get()
        user_body_pains = self.body_pains.get()
        user_none = self.none.get()

        user_first = self.first.get()
        user_second = self.second.get()
        user_first_booster = self.first_booster.get()
        user_second_booster = self.second_booster.get()
        user_not_yet = self.not_yet.get()

        user_contact_name = self.contact_name_entry.get()
        user_contact_number = self.contact_number_entry.get()
        user_contact_email = self.contact_email_entry.get()
        user_contact_relationship = self.contact_relationship_entry.get()

        with open('Entry.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_name, user_sex, user_age, user_address, user_fever, user_headache, user_cough, user_colds, user_loss_of_taste, user_loss_of_smell, user_diarrhea, user_shortness_of_breath, user_difficulty_of_breathing, user_body_pains, user_none, user_first, user_second, user_first_booster, user_second_booster, user_not_yet, user_contact_name, user_contact_number, user_contact_email, user_contact_relationship])

