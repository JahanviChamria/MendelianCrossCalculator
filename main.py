BACKGROUND_COLOR = "#aeaed5"
GREEN="#07736A"
RED="#730707"
LB="#DBFFFF"

FONT="Courier"
from tkinter import *
current={}

def cross():
    trait1name=t1e.get()
    trait1d = t1de.get()
    trait1r = t1re.get()
    trait2name = t2e.get()
    trait2d = t2de.get()
    trait2r = t2re.get()

    A=trait1d[0:1].upper()
    a = A.lower()
    B = trait2d[0:1].upper()
    b = B.lower()

    cr = Label(text=f"Cross: {A}{a}{B}{b} X {A}{a}{B}{b}\n {A}={trait1d}, {a}={trait1r}, {B}={trait2d}, {b}={trait2r}", bg=BACKGROUND_COLOR, fg="white")
    cr.config(font=(FONT, 12, "bold"), padx=10, pady=10)
    cr.grid(row=6, column=1, columnspan=2)

    rowh=canvas.create_text(150, 30, text=f"{A}{B}     {A}{b}     {a}{B}     {a}{b}", font=(FONT, 10, "bold"))
    row1 = canvas.create_text(130, 70, text=f"{A}{B}   {A}{A}{B}{B}   {A}{A}{B}{b}   {A}{a}{B}{B}  {A}{a}{B}{b}", font=(FONT, 10, "bold"))
    row2 = canvas.create_text(130, 120, text=f"{A}{b}   {A}{A}{B}{b}   {A}{A}{b}{b}   {A}{a}{B}{b}  {A}{a}{b}{b}", font=(FONT, 10, "bold"))
    row3 = canvas.create_text(130, 180, text=f"{a}{B}   {A}{a}{B}{B}   {A}{a}{B}{b}   {a}{a}{B}{B}  {a}{a}{B}{b}", font=(FONT, 10, "bold"))
    row4 = canvas.create_text(130, 230, text=f"{a}{b}   {A}{a}{B}{b}   {A}{a}{b}{b}   {a}{a}{B}{b}  {a}{a}{b}{b}", font=(FONT, 10, "bold"))

    cr = Label(text=f"Phenotypic ratio obtained = 9:3:3:1\n9/16 are {trait1d}, {trait2d}\n3/16 are {trait1d}, {trait2r}\n3/16 are {trait1r}, {trait2d}\n1/16 is {trait1r}, {trait2r}",
               bg=BACKGROUND_COLOR, fg="white")
    cr.config(font=(FONT, 12, "bold"))
    cr.grid(row=8, column=4, columnspan=2)

    e = Button(text="Exit", command=ex)
    e.config(font=(FONT, 14, "bold"))
    e.grid(row=9, column=1, columnspan=2)


def ex():
    exit()

window=Tk()
window.title("Mendelian Cross Calculator")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=100, pady=40)



enterl=Label(text="Enter the traits:", bg=BACKGROUND_COLOR)
enterl.config(font=(FONT, 20, "bold"), padx=10, pady=10)
enterl.grid(row=0, column=1, columnspan=2)

canvas=Canvas(width=300, height=300, bg=LB, highlightthickness=0)
squares = PhotoImage(file="download.png")
canvas.create_image(150, 150, image=squares)
canvas.grid(row=8, column=0, columnspan=4)

t1=Label(text="Trait 1:")
t1.config(font=(FONT, 12, "bold"))
t1.grid(row=1, column=0)

t1e=Entry(width=20)
t1e.grid(row=1, column=1)
t1e.focus()

t1d=Label(text="Dominant:", bg=BACKGROUND_COLOR, fg=GREEN)
t1d.config(font=(FONT, 12, "bold"))
t1d.grid(row=2, column=0)

t1de=Entry(width=20)
t1de.grid(row=2, column=1)
t1de.insert(0,"A")
t1de.focus()

t1r=Label(text="Recessive:", bg=BACKGROUND_COLOR, fg=RED)
t1r.config(font=(FONT, 12, "bold"))
t1r.grid(row=3, column=0)

t1re=Entry(width=20)
t1re.grid(row=3, column=1)
t1re.insert(0,"a")
t1re.focus()

t2=Label(text="Trait 2:")
t2.config(font=(FONT, 12, "bold"))
t2.grid(row=1, column=2)

t2e=Entry(width=20)
t2e.grid(row=1, column=3)
t2e.focus()

t2d=Label(text="Dominant:", bg=BACKGROUND_COLOR, fg=GREEN)
t2d.config(font=(FONT, 12, "bold"))
t2d.grid(row=2, column=2)

t2de=Entry(width=20)
t2de.grid(row=2, column=3)
t2de.insert(0,"B")
t2de.focus()

t2r=Label(text="Recessive:", bg=BACKGROUND_COLOR, fg=RED)
t2r.config(font=(FONT, 12, "bold"))
t2r.grid(row=3, column=2)

t2re=Entry(width=20)
t2re.grid(row=3, column=3)
t2re.insert(0,"b")
t2re.focus()

gap=Label(text="   ", bg=BACKGROUND_COLOR)
gap.grid(row=4, column=0)

gen=Button(text="GENERATE PUNNETT SQUARE", command=cross)
gen.config(font=(FONT, 14, "bold"))
gen.grid(row=5, column=1, columnspan=2)


window.mainloop()