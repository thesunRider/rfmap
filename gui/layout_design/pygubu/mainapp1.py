#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class MainApp:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.head_label = ttk.Label(self.root)
        self.head_label.configure(text='RFMap')
        self.head_label.pack(side="top")
        self.main_tab = ttk.Notebook(self.root)
        self.main_tab.configure(height=200, width=200)
        button1 = ttk.Button(self.main_tab)
        button1.configure(text='button1')
        button1.pack(side="top")
        self.main_tab.add(
            button1,
            compound="top",
            state="normal",
            text='Capture')
        button2 = ttk.Button(self.main_tab)
        button2.configure(text='button2')
        button2.pack(side="top")
        self.main_tab.add(
            button2,
            compound="top",
            state="normal",
            text='Database')
        button3 = ttk.Button(self.main_tab)
        button3.configure(text='button3')
        button3.pack(side="top")
        self.main_tab.add(
            button3,
            compound="top",
            state="normal",
            text='Analyze')
        self.main_tab.pack(fill="both", side="top")

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = MainApp()
    app.run()
