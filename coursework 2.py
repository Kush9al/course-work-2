from tkinter import *
from tkinter import messagebox
import calendar
import datetime

def showCal():
    global fetch_year
    new_gui = Tk()

    new_gui.config(background="white")

    new_gui.title("CALENDAR")

    new_gui.geometry("800x800")
    fetch_year = int(year_field.get())

    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")

    cal_year.grid(row=5, column=1, padx=30)

    new_gui.mainloop()



if __name__ == "__main__":
    gui = Tk()

    gui.config(background="white")

    gui.title("CALENDAR")

    gui.geometry("300x300")

    cal = Label(gui, text="CALENDAR", bg="dark gray",
                font=("times", 28, 'bold'))

    year = Label(gui, text="Enter Year", bg="light green")

    year_field = Entry(gui)

    Show = Button(gui, text="Show Calendar", fg="Black",
                  bg="Red", command=showCal)

    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)

    events = Button(gui, text="Event", fg="Black", bg="Red", command=year_field)
    f = open('events1.txt', 'w')
    f.write(str(exit))
    f.seek(0)


    cal.grid(row=1, column=1)

    year.grid(row=2, column=1)

    year_field.grid(row=3, column=1)

    Show.grid(row=4, column=1)

    Exit.grid(row=6, column=1)

    events.grid(row=7, column=1)



    gui.mainloop()
else:
    pass
