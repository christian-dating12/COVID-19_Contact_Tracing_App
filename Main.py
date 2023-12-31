# DATING, CHRISTIAN M | BSCPE 1-5


import tkinter as tk
from Add_Entry import add_entry
from Search_Entry import search_entry
from tkinter import *
import csv
from tkinter import PhotoImage

class App_Window:
    def __init__(self):

        # window title
        self.window = tk.Tk()
        self.window.title("COVID-19 CONTACT TRACING APP")
        self.window.geometry("1000x2000")
        self.window.configure(bg="#FFFFFF")

        # set the background image for the window
        self.window = Canvas(self.window, width = 5, height = 5 )
        self.window.pack(fill = "both", expand = True)
        self.image = PhotoImage (file = "C:\\Users\\Christian\\Downloads\\covid bg.png")
        self.window.create_image(0,0, anchor= NW, image = self.image)

        # LABEL
        tk.Label(self.window, text=" COVID-19 CONTACT TRACING ", font=("Impact", 40, "bold"),bg="#FFFFFF", fg="#800000").pack(pady=250)
     
        # add button for main page
        add_button = tk.Button(self.window, text="Add Entry", command=self.add_entry, height=2, bg="white", fg="black", font=("Monteserrat", 10, "bold"))
        add_button.place(x=500, y=400, width=150)

        # search button for main page
        search_button = tk.Button(self.window, text="Search Entry", command=self.search_entry, height=2, bg="white", fg="black", font=("Monteserrat", 10, "bold"))
        search_button.place(x=730, y=400, width=150)

        self.window.mainloop()

    def add_entry(self):
        frame_frame = add_entry()
        frame_frame.place(x=0, y=0, relwidth=1, relheight=1)

    def search_entry(self):
        frame_frame = search_entry()
        frame_frame.place(x=0, y=0, relwidth=1, relheight=1)

    def close_window(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()

        

App_Window()        








    






