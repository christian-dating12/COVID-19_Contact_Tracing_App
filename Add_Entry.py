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

    def clear_name_text(self, event):
        self.name_entry.delete(0, tk.END)
        self.name_entry.config(fg="black")