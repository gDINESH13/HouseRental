import House
class Owner:
    totalOwners = 0
    def __init__(self,name) -> None:
        Owner.totalOwners +=1
        self.name = name
        #self.ownedHouses = []
        self.id = Owner.totalOwners

    def __str__(self) -> str:
        
        return f"Name: {self.name} id:{self.id}"

    def getOwnedHouses(self,houses):
        ownedHouses = []
        for house in houses:
            if house.owner.id  == self.id:
                ownedHouses.append(house)
        return ownedHouses 

    def getHousedWithRequests(self,ownedHouses):
        return list(filter(lambda h:len(h.requests)>0 ,ownedHouses))