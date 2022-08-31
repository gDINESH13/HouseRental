import Tenant

class House:
    housesCount = 0

    def __init__(self,location,Rent,Owner,Tenant=None) -> None:
        House.housesCount+=1
        self.location = location
        self.rent = Rent
        self.owner = Owner
        self.occupied = False
        self.tenant = Tenant
        self.id = House.housesCount
        self.requests = []

    def __str__(self) -> str:
        return f"House ID: {self.id} Location:{self.location} Owner: {self.owner.name} Occupied:{self.occupied} Tenant:{self.tenant.name} Requests:{self.requests}"
    def printHouseDetails(self):
        tenantName = "None" if self.tenant==None else self.tenant.name
        requests =[]
        for req in self.requests:
            requests.append(req.name)
        print()
        print("House ID:      Location:      Owner:       Occupied:      Tenant:      Requests:")
        print(f"    {self.id}           {self.location}      {self.owner.name}           {str(self.occupied)}         {tenantName}      {requests}")
        print()
    def clearAllRequests(self):
        self.requests = []

    def acceptRequest(self,tenant):
        self.tenant = tenant
        self.occupied = True
        self.clearAllRequests()
        tenant.updateHouse(self)

    @staticmethod
    def housesAvailableForRent(houses):
        return list(filter(lambda house:not house.occupied,houses))
    
    def addRequest(self,tenant):
        self.requests.append(tenant)
    
    def getRequests(self):
        return self.requests


    

    
    


# h = House("Chennai",12000,"Dinesh")
# print(h)

