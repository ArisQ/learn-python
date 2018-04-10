#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.helloLabel = Label(self, text='Hello World!')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.greetButton = Button(self, text='Enter', command=self.greet)
        self.greetButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def greet(self):
        name = self.nameInput.get() or 'World'
        greeting = 'Hello %s!' % name
        self.helloLabel['text'] = greeting
        messagebox.showinfo('Greeting', greeting)


app = Application()
app.master.title('Hello World')
app.mainloop()
