


class Tenant:
    tenantCounts = 0
    def __init__(self,name,house=None,owner=None) -> None:
        Tenant.tenantCounts+=1
        self.name = name
        self.id = Tenant.tenantCounts
        self.houseId = house
        self.owner = owner
        self.RequestedHouses=[]

    def updateHouse(self,house):   
        self.houseId = house.id
        self.owner = house.owner

    def __str__(self) :
        return f"Tenant name:{self.name} House:{self.houseId}"

    def updateRequestedHouses(self,house):
        self.RequestedHouses.append(house)

    def getRequestedHouses(self):
        return self.RequestedHouses
