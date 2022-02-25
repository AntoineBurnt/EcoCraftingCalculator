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

    def getRecipe(self) -> dict:
        """
        Returns the cost of itself as a dictionary.
        
        >>>loadedComps["steam truck"].getRecipe()
        {'iron plate': 12, 'iron pipe': 8, 'screws': 24, 'portable steam engine': 1, 'iron wheel': 4, 'iron axle': 1}
        """
        return self.cost
    
    #Dont touch first it's to differentiate betwwen the recursive calls and the user asking for the costs
    #Additive stops it from clearing the "rawNeeded" list after printing the results
    def rawCosts(self,n: int,additive = False,first = True) -> None:
        """
        Calculates the costs of the "n" amnount of the component in terms of the
        lowest crafting component, raw resources. Prints the results to the console
        when finished. The additive argument can be set to true to add the consts
        if multiple recipes together, rawNeeded.clear() is used to clear the results.
        
        >>>loadedComps["steam truck"].rawCosts(1)
        Calcs Complete
        {'iron bars': 182}
        >>>loadedComps["portable steam engine"].rawCosts(10)
        Calcs Complete
        {'iron bars': 1290}
        
        >>loadedComps["steam truck"].rawCosts(1,True)
        Calcs Complete
        {'iron bars': 182}
        >>>loadedComps["steam truck"].rawCosts(1,True)
        Calcs Complete
        {'iron bars': 364}
        >>>loadedComps["portable steam engine"].rawCosts(10)
        Calcs Complete
        {'iron bars': 1654}
        """
        
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
    
    def targetedCosts(self,n: int,stop: list,additive = False,first = True) -> None:
        """
        Works similar to rawCosts but stop is used to defined the end components
        instead of using the lowest one.
        
        >>>loadedComps["skidsteer"].targetedCosts(1,["iron gear","iron plate","screws","iron pipe","iron wheel","iron axle","fiberglass","steel plate","steel gear","steel gearbox","steel axle"])
        Calcs Complete
        {'iron bars': 20, 'iron gear': 24, 'cellulose fibers': 8, 'steel plate': 56, 'steel bars': 68, 'iron pipe': 12, 'steel gearbox': 6, 'fiberglass': 174, 'epoxy': 144, 'gold bars': 138, 'copper bars': 432, 'synthetic rubber': 32, 'steel axle': 1}
        """
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
    #Load all the components from the text file, shouldn't ever need to call this function manualy 
    loadedComps.clear()
    with open("Components.txt","r") as file:

        for x in file.readlines():
            parms = x.split("/")
            loadedComps[parms[0]] = Component(parms[0],int(parms[1]),eval(parms[2]),parms[3],parms[4],parms[5],float(parms[6]),parms[7],bool(int(parms[8])))
            #name/result amount/recipe dict/calories/calorie type/time/modifer/workbench/is end
        file.close()

loadComps()