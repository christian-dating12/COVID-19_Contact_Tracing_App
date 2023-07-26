import tkinter as tk

class add_entry(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.personal_info_label = tk.Label(self, text=" PERSONAL INFORMATIONS ", height=2, font=("Monteserrat", 10, "bold"))
        self.personal_info_label.place(x=300, y=50)
        self.personal_info_label.config(bg="#800000")