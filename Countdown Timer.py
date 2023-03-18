from tkinter import *
from tkinter import Button
import tkinter.messagebox as tmsg


class Timer(Tk):

    def __init__(self):
        super().__init__()
        self.thread = False
        self.title("Countdown Timer")
        self.maxsize(300, 200)
        self.minsize(300, 200)

    def interface(self):
        self.time_val = IntVar()

        self.text = Label(self, text="Set the time in secounds: ", fg="red")
        self.text.grid(row=0, column=0)

        self.entry = Entry(self, textvariable=self.time_val, fg="blue")
        self.entry.grid(row=1, column=0)

        self.label = Label(self, text="00:00:00", font="Calibri 44", width=10, relief=RIDGE, fg="blue")
        self.label.grid(row=2, column=0)

        self.time_label = Label(self, text="Hours     Minutes     Secounds", font="Calibri 12", fg="red")
        self.time_label.grid(row=3, column=0)

        self.start = Button(self, text="Start", command=self.start, padx=16, fg="blue")
        self.start.grid(row=4, column=0, sticky="W")

        self.pause_button = Button(self, text="Pause", command=self.pause,padx=13, fg="blue")
        self.pause_button.grid(row=5, column=0, stick="W")

        self.reset = Button(self, text="Reset", command=self.reset, padx=13, fg="blue")
        self.reset.grid(row=4, column=0, sticky="NE")

        self.quit = Button(self, text="Quit", command=quit, padx=16, fg="blue")
        self.quit.grid(row=5, column=0, sticky="NE")

    def calc(self):
        m, s = divmod(self.timevar, 60)
        h = self.timevar // 3600
        return '{:02d}:{:02d}:{:02d}'.format(h,m,s)

    def timer(self):
        if self.thread:
         if self.timevar > 0:
            self.label.configure(text=self.calc())
            self.timevar -= 1
            self.after(1000, self.timer)

    def start(self):

        self.timevar = self.time_val.get()

        if self.timevar <= 0:
            self.label.configure(text="Time's Up")
        else:
            self.thread = True
            self.timer()

    def quit(self):
        if tmsg.askokcancel("Exit", "Do you want to Exit"):
            self.destroy()


    def pause(self):
        self.pause_button.configure(text="Resume", command=lambda: self.resume())
        self.bind("<Return>", lambda: self.resume())
        if self.thread==True:
            self.thread = False
        self.timer()

    def resume(self):
        self.pause_button.configure(text="Pause", command=lambda: self.pause())
        self.bind("<Return>", lambda: self.pause())
        if self.thread==False:
            self.thread = True
        self.timer()

    def reset(self):
        self.thread = False
        self.label.configure(text="00:00:00", font="Calibri 44", fg="blue")

if __name__ =='__main__':
    app = Timer()
    app.interface()
    app.mainloop()