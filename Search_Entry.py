import tkinter as tk
import csv
from PIL import ImageTk, Image

# Search Entry

class search_entry(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        # label
        self.search_label = tk.Label(self, text=" Search entered name:  ", height=2, width = 35, font=("Monteserrat", 10, "bold"))
        self.search_label.place(x=320, y=50)
        self.search_label.config(bg="#800000")
        self.search_entry = tk.Text(self, width=73, height=2, font=("Montesarrat", 12, "bold"))
        self.search_entry.place(x=50, y=100)
        
        # search button
        search_button = tk.Button(self, text="Search",bg="#FFFFFF", height=2, width = 16, font=("Montesarrat", 10, "bold"),  command=self.search)
        search_button.place(x=713, y=98)
        self.result = tk.Canvas(self, width=800, height=490, bg="white")
        self.result.place(x=50, y=150)

        # ok button
        ok_button = tk.Button(self, text="OK", command=self.close, bg="maroon", font=("Montesarrat", 12))
        ok_button.place(x=420, y=643)

        # back button to return at main page
        back_button = tk.Button(self, text="Back", command=self.main, bg="maroon", font=("Montesarrat", 12))
        back_button.place(x=470, y=643)


    def close(self):
        self.destroy()

    def main(self):
        self.destroy()
        self.deiconify() 

    def search(self):
        self.result.delete("See more")

        self.search_name = self.search_entry.get("1.0", "end-1c").strip()
        found = False

        # To read the written informations from the user
        with open('Entry.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.search_name:
                    found = True
                    result = f"PERSONAL INFORMATION\nName: {row[0]}\nSex: {row[1]}\nAge: {row[2]}\nAddress: {row[3]}\nE-mail Address: {row[3]}\n\n"
                    result += f"HEALTH STATUS\nAre you experiencing any symptoms in the past 7 days such as: \n\n"

                    selected_symptoms = []
                    if row[5] == "Yes":
                        if row[5] == "Fever":
                            selected_symptoms.append("Fever")
                        if row[5] == "Headache":
                            selected_symptoms.append("Headache")
                        if row[5] == "Sore throat":
                            selected_symptoms.append("Sore throat")
                        if row[5] == "Loss of taste":
                            selected_symptoms.append("Loss of taste")
                        if row[5] == "Loss of smell":
                            selected_symptoms.append("Loss of smell")
                        if row[5] == "Diarrhea":
                            selected_symptoms.append("Diarrhea")
                        if row[5] == "Shortness of breath":
                            selected_symptoms.append("Shortness of breath")
                        if row[5] == "Difficulty of breathing":
                            selected_symptoms.append("Difficulty of breathing")
                        if row[5] == "Body pain":
                            selected_symptoms.append("Body pain")
                        if row[5] == "None":
                            selected_symptoms.append("None")
                    print("\n")

                    result += f"Have you been vaccinated for COVID-19? {row[19]}\n\n"
                    print("\n")

                    result += f"CONTACT PERSON DETAILS\nName: {row[20]}\nContact number: {row[21]}\nE-mail Address: {row[22]}\nRelationship to the contact person: {row[23]}\n"
                    print("\n")
            
                    self.result.create_text(10, 10, anchor="nw", text=result, font=("Monteserrat", 10), fill="black")
                    break
        if not found:
            self.result.create_text(10, 10, anchor="nw", text="File not found.", font=("Montesarrat", 11, "bold"), fill="maroon")

        
    # to return at main page
    def open_main(self):
        app = self.App_Window()
        app.main_window()


