from tkinter import *
from tkinter import ttk
import ECC as ecc
import util as ut

def getRawCost(*args):
    try:
        recipe_name = str(recipe.get()).lower()
        value = float(number.get())
        cost.set(ut.dictTotext(ecc.loadedComps[recipe_name].rawCosts(value)))
        ecc.rawNeeded.clear()
    except (ValueError, KeyError):
        cost.set("Value and/or Key Error!")
        
def getRecipe(*args):
    try:
        recipe_name = str(recipe.get()).lower()
        cost.set(ut.dictTotext(ecc.loadedComps[recipe_name].getRecipe()))
    except KeyError:
        cost.set("Key Error!")

root = Tk()
root.title("Eco crafting calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

controlframe = ttk.Frame(mainframe)
controlframe.grid(column=0, row=0, sticky=(N, W, E, S))


recipe = StringVar()
recipe_entry = ttk.Entry(controlframe, width=7, textvariable=recipe)
recipe_entry.grid(column=2, row=1, sticky=(W, E))

number = StringVar()
number_entry = ttk.Entry(controlframe, width=7, textvariable=number)
number_entry.grid(column=2, row=2, sticky=(W, E))

cost = StringVar()
ttk.Label(mainframe, textvariable=cost).grid(column=0, columnspan=3, row=4, sticky=(W, E))

ttk.Button(controlframe, text="Get Cost", command=getRawCost).grid(column=2, row=3, sticky=W)
ttk.Button(controlframe, text="Get Recipe", command=getRecipe).grid(column=1, row=3, sticky=W)

ttk.Label(controlframe, text="Recipe").grid(column=1, row=1, sticky=E)
ttk.Label(controlframe, text="Number").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text="Cost").grid(column=1, row=3, sticky=E)

for child in controlframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
