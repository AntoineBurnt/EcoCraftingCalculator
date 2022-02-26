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

def getTargetedCost(*args):
    try:
        recipe_name = str(recipe.get()).lower()
        value = float(number.get())
        targetlist = targetitemsdict[targetlbox.curselection()]
        cost.set(ut.dictTotext(ecc.loadedComps[recipe_name].targetedCosts(value,targetlist)))
        ecc.rawNeeded.clear()
    except (ValueError, KeyError):
        cost.set("Value and/or Key Error!")

def openUpgradeDialog(*args):
    try:
        pass
    except:
        pass

def openTargetItemsDialog(*args):
    try:
        pass
    except:
        pass


targetitems1 = ["iron gear","screws","iron pipe","iron wheel","iron axle","fiberglass","steel plate","steel gear","steel gearbox","steel axle"]
targetitems2 = []
targetitems3 = []
targetitemsdict = {"Target Items 1":targetitems1,"Target Items 2":targetitems2,"Target Items 3":targetitems3}

#main root stuff
root = Tk()
root.title("Eco crafting calculator")

#mainframe stuff
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#menu stuff
root.option_add('*tearOff', FALSE)
menubar = Menu(root)
root['menu'] = menubar
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='Options')
menu_file.add_command(label='Configure Upgrades', command=openUpgradeDialog)
menu_file.add_command(label='Configure Target Items', command=openTargetItemsDialog)


#control frame stuff
controlframe = ttk.Frame(mainframe)
controlframe.grid(column=0, row=0, sticky=(N, W, E, S))


recipe = StringVar()
recipe_entry = ttk.Entry(controlframe, width=28, textvariable=recipe)
recipe_entry.grid(column=2, columnspan=2, row=1, sticky=(W, E))

number = StringVar()
number_entry = ttk.Entry(controlframe, width=7, textvariable=number)
number_entry.grid(column=2, row=2, sticky=(W))

cost = StringVar()
ttk.Label(mainframe, textvariable=cost).grid(column=0, columnspan=3, row=4, sticky=(W, E))

ttk.Button(controlframe, text="Recipe", command=getRecipe).grid(column=2, row=3, sticky=W)
ttk.Button(controlframe, text="Cost", command=getRawCost).grid(column=1, row=3, sticky=W)
ttk.Button(controlframe, text="Targeted Cost", command=getTargetedCost).grid(column=3, row=3, sticky=W)

ttk.Label(controlframe, text="Recipe").grid(column=1, row=1, sticky=E)
ttk.Label(controlframe, text="Number").grid(column=1, row=2, sticky=E)
ttk.Label(controlframe, text="Target Filter").grid(column=4, row=1, sticky=(S))


#target list
targets = ["Target Items 1","Target Items 2","Target Items 3"]
targetvar = StringVar(value=targets)
targetlbox = Listbox(controlframe, listvariable=targetvar, height=3).grid(column=4, row=2, rowspan=2, sticky=(N))

for child in controlframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
