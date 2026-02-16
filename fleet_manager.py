
def init_database():
    Valid_Rank = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Cadet", "Ensign", "Lt.Jr Grade"]
    Valid_Div = ["Command", "Operations", "Security", "Sciences", "Medical"]
    n = ["Picard", "Riker", "Data", "Worf", "Kirk "]
    r = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Captain"]
    d = ["Command", "Command", "Operations", "Security", "Command"]
    id = ["0001", "0002", "0003", "0004", "0005"]
    return Valid_Rank,n,r,d,id,Valid_Div

init_database()

def display_menu(Valid_Rank,Valid_Div,n,r,d,id):
    print("Systems Booting")
    print("...")
    print("Systems Online")
    name = input("What is your name?:")
    while True:
        print("---Student Logged In: " + name + "---")
        print("\n--- MENU ---")
        print("1. Add Member")
        print("2. Remove Member")
        print("3. Update Rank")
        print("4. Display Roster")
        print("5. Search Crew")
        print("6. Filter By Division")
        print("7. Calculate Payroll")
        print("8. Count Officers")
        print("9. Exit")
        
        input_Value = int(input("Selection Option: "))
        match input_Value:
            case 1:              
                add_member(Valid_Rank,n,r,d,id)
            case 2:
                remove_member(n,r,d,id) 
            case 3:
                update_rank(r,id)
            case 4:
                display_roster(n, r, d, id)
            case 5:
                search_crew(n, r, d, id)
            case 6:
                filter_by_division(n, r, d, id, Valid_Div)
            case 7:
                calculate_payroll(r)
            case 8:
                count_officers(r)
            case 9:
                Quit()

                

def add_member(Valid_Rank,n,r,d,id):
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_division = input("Division: ")
    new_id = input("ID: ")

    if new_rank not in Valid_Rank:
        print("This rank is invalid")
    else:
        if new_id in id:
            print("This id is already taken")
        else:
            n.append(new_name)
            r.append(new_rank)
            d.append(new_division) 
            id.append(new_id)
            print("Member Added.") #Adds a member to the lists based on information given by the user


def remove_member(n,r,d,id):
    idremove = input("ID of member to remove: ")
    if idremove not in id:
        print("This ID does not exist...")
    else:
        idxrem = id.index(idremove)
        n.pop(idxrem)
        r.pop(idxrem)
        d.pop(idxrem)
        id.pop(idxrem)
        print("Removed.") #Removes a member from the list based on the Id provided by the user


def update_rank(r,id):
    rankupdate = input("Enter The ID of the member to be updated: ")
    if rankupdate not in id:
        print("The ID provided is invalid")
    else:

        idxR = id.index(rankupdate)
        r[idxR] = input("What is the New Rank?: ")
        print("Rank Updated") #Changes the rank of a current member based on their ID


def display_roster(n,r,d,id):
    for i in range(len(n)):
        print(n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i]) #Displays all info about each member

def search_crew(n, r, d, id):
    searched = input("Enter a term to search for: ")
    found = False

    for i in range(len(n)):
        if (searched in n[i] or searched in r[i] or searched in d[i] or searched in id[i]):

            print(n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
            found = True

    if not found:
        print("No matching crew member found.") #Displays all info of members who's info contains a given key search term.
        

        

def filter_by_division(n, r, d, id, Valid_Div):
    div_input = input("Enter Division to filter by: ")
    found = False
    if div_input not in Valid_Div:
        print("Invalid Division.")
        return
    for i in range(len(n)):
        if d[i] == div_input:
            print(n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
            found = True
    if not found:
        print("No members found in that division.") #This function filters and prints members based on their division.


def calculate_payroll(r):
    total = 0

    for rank in r:
        if rank == "Captain":
            total += 1000
        elif rank == "Commander":
            total += 800
        elif rank == "Lt.Commander":
            total += 600
        elif rank == "Lieutenant":
            total += 500
        elif rank == "Lt.Jr Grade":
            total += 400
        elif rank == "Ensign":
            total += 200
        elif rank == "Cadet":
            total += 100
    print("The Total Cost of the crew is: " + str(total)) #This function assigns a value to each rank and then calculates the total value of the crew

def count_officers(r):
    count = 0           
    for rank in r:
        if rank == "Captain" or rank == "Commander": 
            count = count + 1
    print("High ranking officers: " + str(count)) #This function calculates how many captains and/or commanders there are and returns the value

def Quit():
    pass


Valid_Rank,n,r,d,id,Valid_Div = init_database()
display_menu(Valid_Rank, Valid_Div,n,r,d,id)

    
 


 



    
