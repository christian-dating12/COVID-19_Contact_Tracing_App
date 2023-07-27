import tkinter as tk

class search_entry(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.search_label = tk.Label(self, text=" Search entered name:  ", height=2, width = 35, font=("Monteserrat", 10, "bold"))
        self.search_label.place(x=320, y=50)
        self.search_label.config(bg="#800000")
        self.search_entry = tk.Text(self, width=73, height=2, font=("Montesarrat", 12, "bold"))
        self.search_entry.place(x=50, y=100)

        search_button = tk.Button(self, text="Search",bg="#FFFFFF", height=2, width = 16, font=("Montesarrat", 10, "bold"),  command=self.search)
        search_button.place(x=713, y=98)

        self.first_result = tk.Canvas(self, width=800, height=490, bg="white")
        self.first_result.place(x=50, y=150)

        ok_button = tk.Button(self, text="OK", command=self.close, bg="maroon", font=("Montesarrat", 12))
        ok_button.place(x=420, y=643)

        back_button = tk.Button(self, text="Back", command=self.main, bg="maroon", font=("Montesarrat", 12))
        back_button.place(x=470, y=643)

    def search(self):
        self.first_result.delete("See more")
        self.second_result.delete("See more")

    def close(self):
        self.destroy()

    def main(self):
        self.destroy()
        self.deiconify() 

    def open_main(self):
        app = self.App_Window()
        app.main_window()


