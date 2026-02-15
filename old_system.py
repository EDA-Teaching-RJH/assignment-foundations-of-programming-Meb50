n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        loading = loading + 1
        print("Loading module " + str(loading))
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  
            print("Current Crew List:")
            
            for i in range(len(n)): #originally stated as for i in range(10), error not solved yet tho, Sets the range for the for loop as the number of items in the list
                print(n[i] + " - " + r[i] + " - " + d[i]) 

        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
            if rem not in n:
                print("Provided name is not in database")
            else:
                 if n.count(rem) > 1:
                     remr = input("Rank of person to remove: ")
                     for x in range(len(n)):
                         if n[x] == rem:
                             Current_rank = r[x]
                             if Current_rank == remr:
                                  n.pop(x)
                                  r.pop(x)
                                  d.pop(x)
                                  print("Removed.")
                                  break
            
                 else:
                     idxn = n.index(rem)
                     n.pop(idxn)        #trying to get it where if multiple of same name, asks to specify the rank that the name has to remove that specific name 
                     r.pop(idxn)
                     d.pop(idxn)       
                     print("Removed.")

            
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or rank == "Commander": 
                    count = count + 1
            print("High ranking officers: " + str(count)) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith()
