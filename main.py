import House
import Owner
import Tenant

#creating owners
Dinesh = Owner.Owner("Dinesh")
Dishal = Owner.Owner("Dishal")

trail = 1
#creating houses
houses=[
    House.House("chennai",15000,Dinesh),
    House.House("Tiruchy",15000,Dinesh),
    House.House("chennai",15000,Dishal),
    House.House("chennai",15000,Dishal)
]

tenants=[
    Tenant.Tenant("Rocky")
]

def TenantLogin():
    print("\n1->Login with Existing Tenant\n2->Create Tenant Account:  ")
    c = int(input())
    currTenant = None
    if c==2:
        print("\nEnter your name: ")
        name = input().strip()
        currTenant = Tenant.Tenant(name)
        tenants.append(currTenant)
    if c==1:
        print("\nEnter Login Id: ")
        id = int(input())
        for tenant in tenants:
            if tenant.id == id:
                currTenant = tenant
    
    while True:
        print("\n1->Request for Rental\n2->See Request status\n3.Print Available Houses\n 4->Logout: ")
        choice = int(input())
        if choice == 4:
            break
        elif choice==1:
            print("Enter the Id of House to request for renting:  ")
            id = int(input())
            house  = list(filter(lambda h:h.id==id,houses))[0]
            existingRequests = house.getRequests()
            if house in existingRequests:
                print("You have already requested to this house wait for owner's response...")
            else:
                house.addRequest(currTenant)
                currTenant.updateRequestedHouses(house)
                print("Your request is added to view")
        elif choice==2:
            requestedHouses = currTenant.getRequestedHouses()
            if not requestedHouses:
                print("You haven't requested for any houses")
            for house in requestedHouses:
                if currTenant in house.getRequests():
                    print(f"{house.id}  status: Owner Hasn't viewed Your request")
                else:
                    if house.tenant == currTenant:
                        print(f"{house.id} status: Owner Accepted Your request, you are the Tenant!!!!!")
                    else:
                        print(f"{house.id} status: Owner Declined Your request for renting")
        elif choice ==3:
            print("\nAvailable Houses for Renting")
            availableHouses = House.House.housesAvailableForRent(houses)
            
            for house in availableHouses:
                house.printHouseDetails()
    

def OwnerLogin():
    print("Enter Owner ID")
    id = int(input())
    loggedInOwner = None
    if Dinesh.id!=id and Dishal.id!=id:
        print("Owner Id not exist")
        return
    elif Dinesh.id == id:
        loggedInOwner = Dinesh
        #print(loggedInOwner)
        print("Welcome Dinesh...")
    else:
        loggedInOwner = Dishal
        print("Welcome Dishal...")

    while True:
        print("\n1.Post New House \n2.Remove House \n3.Accept/Decline Requests \n4.See all Owned Houses \n5.Logout")
        choice = int(input("Your Choice: "))
        #logout
        if choice==5:
            break
        
        if choice ==1:
            print("\nEnter House Deatils")
            location = input("Location: ").strip()
            Rent = int(input("Rent: "))
            newHouse = House.House(location,Rent,loggedInOwner)
            houses.append(newHouse)
            print("Your New House is posted")
            print("-----------------------------------------------------------")
        elif choice == 2:
            ownedHouses = loggedInOwner.getOwnedHouses(houses)
            print("Enter house Id for removal")
            houseID = int(input())
            for house in ownedHouses:
                if house.id == houseID:
                    houses.remove(house)
                    print("House Removed successfully.....")
                    break
            else:
                print(f"Id {houseID} doesn't match to your owned houses")
            print("-----------------------------------------------------------")

        elif choice == 3:
            ownedHouses = loggedInOwner.getOwnedHouses(houses)
            housesWithRequests = loggedInOwner.getHousedWithRequests(ownedHouses)
            
            if not housesWithRequests:
                print("No houses are requested for Rent")
            else:
                print("Houses with tenant Requests")
                for house in housesWithRequests:
                    house.printHouseDetails()
                houseId = int(input("Enter House Id to accept/decline tenant request:   "))
                editHouse = list(filter(lambda h:h.id==houseId,housesWithRequests))[0]
                editHouse.printHouseDetails()
                print(f" Enter \n1-> Clear all reuqest for houseId:{houseId} \n2->Accept particular Request for houseId:{houseId} ")
                c = int(input())
                if c!=1 and c!=2:continue
                elif c == 1:
                    editHouse.clearAllRequests()
                    print(f"All reuqests for houseId:{houseId} is cleared...\n")
                elif c == 2:
                    print("Enter id of tenant to accept the request")
                    reqId = int(input())
                    if reqId not in editHouse.requests:
                        print(f"Entered Id:{reqId} is not in requests of this house. Try Again.....")
                    else:
                        for tenant in tenants:
                            if tenant.id == reqId:
                                editHouse.acceptRequest(tenant)
                                break
                        #editHouse.clearAllRequests()
                        print(f"House is alloted to tenant:{tenant.id}")
            print("-----------------------------------------------------------")
        
        elif choice == 4:
            ownedHouses = loggedInOwner.getOwnedHouses(houses)
            
            for house in ownedHouses:
                # global trail
                # if trail == 1:
                #     house.requests.append(1) 
                #     trail +=1
                house.printHouseDetails()
            print("-----------------------------------------------------------")

Logins={
    1:TenantLogin,
    2:OwnerLogin
}
#driver code
while True:
    print("Enter \n 1.TenantLogin \n 2.OwnerLogin")
    choice = int(input())
    if choice!=1 and choice!=2:
        break
    Logins[choice]()
