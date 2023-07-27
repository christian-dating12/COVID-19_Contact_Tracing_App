import tkinter as tk
import csv
from tkinter import *
from PIL import ImageTk, Image

# Search Entry

class search_entry(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.add_image = "C:\\Users\\Christian\\Downloads\\1.png"
        self.add_original_image = Image.open(self.add_image)
        self.add_resized_image = self.add_original_image.resize((520, 700))
        self.background_image = ImageTk.PhotoImage(self.add_resized_image)
        canvas = tk.Canvas(self, width=250, height=150)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        # label
        self.search_label = tk.Label(self, text=" Search entered name:  ", height=2, width = 35, font=("Monteserrat", 10, "bold"))
        self.search_label.place(x=780, y=50)
        self.search_label.config(bg="#800000")
        self.search_entry = tk.Text(self, width=73, height=2, font=("Montesarrat", 12, "bold"))
        self.search_entry.place(x=530, y=100)
        
        # search button
        search_button = tk.Button(self, text="Search",bg="#FFFFFF", height=2, width = 16, font=("Montesarrat", 10, "bold"),  command=self.search)
        search_button.place(x=1187, y=98)
        self.result = tk.Canvas(self, width=800, height=490, bg="white")
        self.result.place(x=530, y=150)

        # ok button
        ok_button = tk.Button(self, text="OK", command=self.close, bg="maroon", font=("Montesarrat", 12))
        ok_button.place(x=900, y=643)

        # back button to return at main page
        back_button = tk.Button(self, text="Back", command=self.main, bg="maroon", font=("Montesarrat", 12))
        back_button.place(x=970, y=643)


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
                    result = f"PERSONAL INFORMATION\nName: {row[0]}\nSex: {row[1]}\nAge: {row[2]}\nAddress: {row[3]}\nE-mail Address: {row[4]}\n\n"
                    result += f"HEALTH STATUS\nAre you experiencing any symptoms in the past 7 days such as: {row[5]}\n"

                    self.symptoms = []
                    if row[6] == "Yes":
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


