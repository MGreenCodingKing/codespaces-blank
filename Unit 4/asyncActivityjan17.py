campingSupplies = ['tent','sleeping bag','flash light','camping knife']

def ReverseList():
    campingSupplies.reverse()
    print(campingSupplies)

ReverseList()

def addCampSupplies(item):
    campingSupplies.append(item)
    print(campingSupplies)

addCampSupplies('Lighter')

campingFood = ['marshmellows','gram crackers','chocolate','chicken hot dogs','water',]

def combinerCamplist():
    campingSupplies.append(campingFood)
    print(campingSupplies)


combinerCamplist()


def flashlightReplacement():
    campingSupplies.remove('flash light')
    campingSupplies.insert(1, 'camp fire kit')
    print(campingSupplies)

flashlightReplacement()