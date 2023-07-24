# DATING, CHRISTIAN M | BSCPE 1-5

# PSEUDOCODE
# Ask user for typical informations
# Write collected informations in a file
# Add Entry
# Search Entry

import csv
import tkinter as tk
from tkinter import messagebox, ttk
import time

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

    def window_load(self):

        window_load = tk.Toplevel()
        window_load.geometry("300x100")
        window_load.title("Loading...")
        window_load.config(bg="#E8D9CD")

        style = ttk.Style()
        style.theme_use('alt')
        style.configure("Custom.Horizontal.TProgressbar", background='#794F2E')

        progressbar = ttk.Progressbar(window_load, mode='determinate', length=250, style="Custom.Horizontal.TProgressbar")
        progressbar.pack(pady=40)

        progressbar.start()

        for i in range(101):
            progressbar['value'] = i
            window_load.update()  # Update the loading screen
            # Simulate a delay
            time.sleep(0.008)
        progressbar.stop()
        window_load.destroy()
        self.show_main_gui()
        window_load.after(99)
        window_load.mainloop()

    def show_main_gui(self):
        self.window.deiconify()
        self.window.destroy()
        x = App_Window()


try:
    app = App_Window()
except Exception as error:
    App_Window.error("Error", str(error))





