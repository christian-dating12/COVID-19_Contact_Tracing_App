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
        
        tk.Button(self.window, text="START", font=("Montserrat", 15, "bold",), width=8,
                  command=self.window_load, bg="#800000", bd=0, fg="white").pack(pady=15)

        self.window.mainloop()

    


try:
    app = App_Window()
except Exception as error:
    App_Window.error("Error", str(error))





