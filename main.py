import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk


photoList = []


class GUI(Tk):
    def __init__(self, size, title):
        super().__init__()
        self.geometry(size)
        self.wm_iconbitmap("Dtafalonso-Android-Lollipop-Calculator.ico")
        self.title(title)
        self.resizable(False, False)

    def entry(self):
        self.calcVar = StringVar()
        self.calcVar.set("0")
        self.screen = Label(self, textvariable=self.calcVar, font=("ms reference sans serif", 30, "bold"))
        self.screen.pack(side=TOP, anchor=N, fill=X, padx=10, pady=25)

    def hist(self):
        self.histLabel = Label(self, text="", font=("ms reference sans serif", 18, "bold"), fg="#646464")
        self.histLabel.pack(anchor=W, padx=65)

    @staticmethod
    def createButton(self, text, command, font, color="white", textColor="black"):
        if text == "C":
            Button(self, text=text, command=command, bg=color, fg=textColor, font=font, padx=9, pady=2).pack(side=LEFT, pady=5, padx=25)
        elif text == "=":
            Button(self, text=text, command=command, bg=textColor, fg=color, font=font, padx=12, pady=2).pack(side=LEFT, pady=5, padx=25)
        elif text == "(" or text == ")":
            Button(self, text=text, command=command, bg=color, fg=textColor, font=font, padx=16, pady=2).pack(side=LEFT, pady=5, padx=25)
        elif text == "\u221ax":
            Button(self, text=text, command=command, bg=color, fg=textColor, font=font, padx=2, pady=2).pack(side=LEFT, pady=5, padx=25)
        else:
            Button(self, text=text, command=command, bg=color, fg=textColor, font=font, padx=12, pady=2).pack(side=LEFT, pady=5, padx=25)

    def add(self, item):
        value = self.calcVar.get()
        if value == "0":
            self.calcVar.set(item)
        else:
            self.calcVar.set(value + item)

    def calculate(self):
        try:
            self.histLabel.configure(text=f"{self.calcVar.get()} =")
            self.calcVar.set(eval(self.calcVar.get()))
            self.screen.update()
            return eval(self.calcVar.get())
        except Exception:
            tkinter.messagebox.showerror(title="Error", message="Invalid operation!")

    def sqrt(self):
        self.histLabel.configure(text=f"\u221a({self.calcVar.get()}) =")
        self.calcVar.set(str(eval(f"{eval(self.calcVar.get())}**0.5")))

    def clearAll(self):
        self.calcVar.set("0")
        self.histLabel.configure(text="")
        self.screen.update()

    def removeLastChar(self, event):
        self.calcVar.set(self.calcVar.get()[:-1])

    def createFrame(self, item1, item2, item3, item4):
        self.frame1 = Frame(self)
        self.createButton(self.frame1, str(item1[0]), item1[1], "comicsansms 30 bold", textColor=item1[2])
        self.createButton(self.frame1, str(item2[0]), item2[1], "comicsansms 30 bold", textColor=item2[2])
        self.createButton(self.frame1, str(item3[0]), item3[1], "comicsansms 30 bold", textColor=item3[2])
        self.createButton(self.frame1, str(item4[0]), item4[1], "comicsansms 30 bold", textColor=item4[2])
        self.frame1.pack(side=TOP)

    def addBackspace(self):
        image = Image.open("F:\\Python GUI Tkinter Tutorial\\Project 1 - Calculator\\back.png")
        image = image.resize((50, 50), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        photoList.append(photo)
        label = Label(self, image=photo)
        label.pack(pady=10, anchor=E, padx=65)
        label.bind("<Button-1>", self.removeLastChar)


if __name__ == '__main__':
    window = GUI("600x680", "CalculatorP")
    window.hist()
    window.entry()
    window.addBackspace()
    window.createFrame(["C", window.clearAll, "#ff5500"], ["(", lambda: window.add("("), "#46b829"],
                       [")", lambda: window.add(")"), "#46b829"], ["÷", lambda: window.add("/"), "#46b829"])
    window.createFrame(["7", lambda: window.add("7"), "#000000"], ["8", lambda: window.add("8"), "#000000"],
                       ["9", lambda: window.add("9"), "#000000"], ["x", lambda: window.add("*"), "#46b829"])
    window.createFrame(["4", lambda: window.add("4"), "#000000"], ["5", lambda: window.add("5"), "#000000"],
                       ["6", lambda: window.add("6"), "#000000"], [" -", lambda: window.add("-"), "#46b829"])
    window.createFrame(["1", lambda: window.add("1"), "#000000"], ["2", lambda: window.add("2"), "#000000"],
                       ["3", lambda: window.add("3"), "#000000"], ["+", lambda: window.add("+"), "#46b829"])
    window.createFrame(["\u221ax", window.sqrt, "#46b829"], ["0", lambda: window.add("0"), "#000000"],
                       [". ", lambda: window.add("."), "#000000"], ["=", window.calculate, "#46b829"])
    window.mainloop()
