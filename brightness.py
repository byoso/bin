#! /usr/bin/env python3

import tkinter as tk
import subprocess
import os


class Application(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.screens = []
        self.selected = tk.IntVar(value=0)

        self.slider = tk.Scale(orient="horizontal", from_=20, to=100, label="brightness level", command=self.set_brightness, )
        self.slider.pack(fill='both', expand=True)
        self.get_screens()
        # set slider to the value of the screen[0]
        self.slider.set(self.screens[0]['value']*100)


    def select(self) -> None:
        print(self.selected.get())
        value = self.screens[self.selected.get()].get("value", 1.0)
        self.slider.set(value*100)

    def get_screens(self) -> None:
        response = subprocess.check_output("xrandr -q | grep ' connected'", shell=True, text=True)
        lines = response.split("\n")
        index = 0
        for line in lines:
            display = line.split(" ")[0]
            if display:
                self.screens.append({"name": display, "value": 1.0})
                button = tk.Radiobutton(text=display, value=index, variable=self.selected, command=self.select)
                button.pack(fill='both', expand=True)
            index += 1
        response = subprocess.check_output("xrandr --verbose | grep 'Brightness'", shell=True, text=True)
        lines = response.split("\n")
        index = 0
        for line in lines:
            if line:
                value = float(line.split(":")[-1].strip())
                self.screens[index]['value'] = value
            index += 1

    def set_brightness(self, value) -> None:
        value = int(value) / 100
        self.screens[self.selected.get()]["value"] = value
        name = self.screens[self.selected.get()]["name"]
        os.system(f"xrandr --output {name} --brightness {value}")



app = tk.Tk()
app.title("Brightness Controller")
app.geometry("600x400")
print(app.size())
main_frame = Application()
app.mainloop()
