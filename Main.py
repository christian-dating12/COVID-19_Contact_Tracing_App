# DATING, CHRISTIAN M | BSCPE 1-5

# PSEUDOCODE
# Ask user for typical informations
# Write collected informations in a file
# Add Entry
# Search Entry

import tkinter as tk



class App_Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("COVID-19 CONTACT TRACING APP")
        self.window.geometry("800x600")
        self.window.configure(bg="#C1C1CD")

        tk.Label(self.window, text="COVID-19 CONTACT TRACING APP",
                 font=("Impact", 30, "bold"),bg="#C1C1CD", fg="#800000").pack(pady=20)
     
       # Create add entry button.
        add_button = tk.Button(self.window, text="Add Entry", command=self.add_entry, height=3, bg="yellow", fg="black", font=("Arial", 10, "bold"))
        add_button.place(x=450, y=290, width=200)

        # Create search entry button.
        search_button = tk.Button(self.window, text="Search Entry", command=self.search_entry, height=3, bg="pink", fg="black", font=("Arial", 10, "bold"))
        search_button.place(x=450, y=360, width=200)

        
        self.window.mainloop()


    
App_Window()        








    






