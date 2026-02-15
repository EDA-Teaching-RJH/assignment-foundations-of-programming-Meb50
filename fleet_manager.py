
def init_database():
    Valid_Rank = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Cadet", "Ensign", "Lt.Jr Grade"]
    n = ["Picard", "Riker", "Data", "Worf", "Kirk "]
    r = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Captain"]
    d = ["Command", "Command", "Operations", "Security", "Command"]
    id = ["0001", "0002", "0003", "0004", "0005"]
    return Valid_Rank,n,r,d,id

init_database()

def display_menu(Valid_Rank,n,r,d,id):
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
                update_rank()
            case 4:
                display_roster()
            case 5:
                search_crew()
            case 6:
                filter_by_division()
            case 7:
                calculate_payroll()
            case 8:
                count_officers()
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
        print("Rank Updated")


def display_roster():
    for i in range(len(n)):
        print(n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])

def search_crew(): 
    pass

def filter_by_division():
    pass

def calculate_payroll():
    pass

def count_officers():
    pass

def Quit():
    pass


Valid_Rank,n,r,d,id = init_database()
display_menu(Valid_Rank,n,r,d,id)

    
 


 



    
