#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import time
from datetime import datetime
import pytz

class WordClock:
        def __init__(self):
                self.root = Tk()
                self.root.geometry("500x250")
                self.root.title("World Time")
                self.clock = Label(self.root,font=("times",50,"bold"))
                self.clock.grid(row=2,column=1,pady=65,padx=110)
                self.locations = {"Alaska":"US/Alaska","Amsterdam":"Europe/Amsterdam","Berlin":"Europe/Berlin","Budapest":"Europe/Budapest","Buenos Aires":"America/Buenos_Aires","Caracas":"America/Caracas",
                                  "Chicago":"America/Chicago","Dublin":"Europe/Dublin","Lisbon":"Europe/Lisbon",
                                  "London":"Europe/London","Los Angeles":"America/Los_Angeles","New York":"America/New_York","Moscow":"Europe/Moscow","Paris":"Europe/Paris",
                                  "Rome":"Europe/Rome","Seoul":"Asia/Seoul","Sydney":"Australia/Sydney","Tokyo":"Asia/Tokyo"}
                self.location_label = Label(self.root,text="Local Time",width=26,font="arial 24 bold",fg="red")
                self.location_label.place(x=0,y=20)
                self.entry = ttk.Combobox(self.root,width=42)
                self.entry["values"]=["Local Time","Alaska","Amsterdam","Berlin","Budapest","Buenos Aires","Caracas","Chicago","Dublin","Lisbon","London","Los Angeles",
                                     "New York","Moscow","Paris","Rome","Seoul","Sydney","Tokyo"]
                self.entry.set("Local Time")
                self.entry.place(x=110,y=175)

                self.times()

                self.root.mainloop()

        def times(self):
                if self.entry.get()!="Local Time":
                        tz = pytz.timezone(self.locations[self.entry.get()])
                        zone_time = datetime.now(tz)
                        current_time = zone_time.strftime("%H:%M:%S")
                        self.location_label.configure(text='{} Time'.format(self.entry.get()))
                else:
                        current_time=time.strftime("%H:%M:%S")
                        self.location_label.configure(text=self.entry.get())
                self.clock.config(text=current_time,bg="black",fg="green",font="Arial 50 bold")
                self.clock.after(200,self.times)


if __name__=="__main__":
        WordClock()

