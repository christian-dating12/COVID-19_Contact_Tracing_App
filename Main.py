# DATING, CHRISTIAN M | BSCPE 1-5

# PSEUDOCODE
# Ask user for typical informations
# Write collected informations in a file
# Add Entry
# Search Entry

import tkinter as tk
from Add_Entry import add_entry


class App_Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("COVID-19 CONTACT TRACING APP")
        self.window.geometry("800x600")
        self.window.configure(bg="#808080")

        tk.Label(self.window, text="COVID-19 CONTACT TRACING APP", font=("Impact", 30, "bold"),bg="#808080", fg="#800000").pack(pady=20)
     
        
        add_button = tk.Button(self.window, text="Add Entry", command=self.add_entry, height=2, bg="white", fg="black", font=("Monteserrat", 10, "bold"))
        add_button.place(x=150, y=190, width=150)

        self.window.mainloop()

    def add_entry(self):
        frame_frame = add_entry()
        frame_frame.place(x=0, y=0, relwidth=1, relheight=1)
    
App_Window()        








    






