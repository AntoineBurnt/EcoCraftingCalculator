loadedComps = {}
# name:object
rawNeeded = {}
# name:amount
tables = {"workbench": 1, "carpentry":1,"masonry":1,"sawmill":1,"kiln":1,"cementkiln":1,"machinist":1,"screwpress":1,"wainwright":1,"anvil":1,"robotic assembly line":1,"test":1,"shaper":1,"lathe":1,"assembly line":1,"elec machinist":1,"stamping press":1,"planer":1,"elec assembly":1,"elec lathe":1,"refinery":1 }
# name: modifer
from math import ceil


class Component(object):

    def __init__(self,name,result,cost,calories,calorietype,time,modifier,table,isEnd):
        self.name = name
        self.result = result # or {}
        self.cost = cost or {}
        self.calories = calories
        self.calorietype = calorietype
        self.time = time
        self.modifier = modifier
        self.table = table
        self.isEnd = isEnd

    def getRecipe(self):
        return self.cost
    #Dont touch first it's to differentiate betwwen the recursive calls and the user asking for the costs
    #Additive stops it from clearing the "rawNeeded" list after printing the results
    def rawCosts(self,n,first = True,additive = False): 
        
        if self.isEnd:
            rawNeeded[self.name] = n + rawNeeded.get(self.name,0)
        else:
            for x in self.cost: 
                #Recursive cancer that calculates the stuff
                loadedComps[str(x)].rawCosts(ceil(self.cost[x]/self.result*n*self.modifier*tables[self.table]),False,False)
        
        if first:
            print("Calcs Complete") 
            print(rawNeeded)
            if not additive:
                rawNeeded.clear() #Print in console to manually clear results
    #["iron gear","iron plate","screws","iron pipe","iron wheel","iron axle","fiberglass","steel plate","steel gear","steel gearbox","steel axle"]
    def targetedCosts(self,n,stop,first = True,additive = False):
        condition = False
        for x in stop:
            if x == self.name:
                
                condition = True
                
        if self.isEnd:
            rawNeeded[self.name] = n + rawNeeded.get(self.name,0)
        elif condition:
            rawNeeded[self.name] = n + rawNeeded.get(self.name,0)
        else:
            for x in self.cost: 
                #Recursive cancer that calculates the stuff
                loadedComps[str(x)].targetedCosts(ceil(self.cost[x]/self.result*n*self.modifier*tables[self.table]),stop,False,False)
        
        if first:
            print("Calcs Complete")
            print(rawNeeded)
            if not additive:
                rawNeeded.clear() #Print in console to manually clear results        


def loadComps():
    loadedComps.clear()
    with open("Components.txt","r") as file:

        for x in file.readlines():
            parms = x.split("/")
            loadedComps[parms[0]] = Component(parms[0],int(parms[1]),eval(parms[2]),parms[3],parms[4],parms[5],float(parms[6]),parms[7],bool(int(parms[8])))
            #name/result amount/recipe dict/calories/calorie type/time/modifer/workbench/is end
        file.close()

loadComps()