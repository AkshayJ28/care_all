def initialization():
    
    Older_Adults = {"Names":[],"Rates":[]}
    
    Young_Adults = {"Names":[],"Rates":[]}
    
    while True:
        try:
            no_of_older_people = int(input("ENTER THE NUMBER OF OLDER PEOPLES IN THE HOME : "))
            break
        except ValueError:
            print("Invaild Number... Plese enter valid Number of olders !! ")
        except:
            print("Undefined Error")
    
    while True:
        try:
            no_of_younger_people = int(input("ENTER THE NUMBER OF YOUNGER PEOPLES IN THE HOME : "))
            break
        except ValueError:
            print("Invaild Number... Plese enter valid Number of Youngers !! ")
        except:
            print("Undefined Error")
    
    for i in range(0,no_of_older_people):
        while True:
            try:
                Older_Adults['Names'].append(input("ENTER NAMES OF OLDERS : "))
                break
            except:
                print("Invalid Name.. Plese enter valid Name !! ")
        while True:
            try:    
                Older_Adults['Rates'].append(int(input("ENTER RATES OF OLDERS : ")))
                break
            except ValueError:
                print("Invalid Rate.. Plese enter valid Rate !! ")
            except:
                print("Undefined Error")
    
    for i in range(0,no_of_younger_people):
        while True:
            try:
                Young_Adults['Names'].append(input("ENTER NAMES OF YOUNGERS : "))
                break
            except:
                print("Invalid Name.. Plese enter valid Name !! ")
        while True:
            try:
                Young_Adults['Rates'].append(int(input("ENTER RATES OF YOUNGERS : ")))
                break
            except ValueError:
                print("Invalid Rate.. Plese enter valid Rate !! ")
            except:
                print("Undefined Error")
        
    Assigned_Older_Adults = {}
    
    for i in Young_Adults['Names']:
        Assigned_Older_Adults[i] = []
    
    return Older_Adults,Young_Adults,Assigned_Older_Adults

def Work_assigning(Older_Adults,Young_Adults,Assigned_Older_Adults):
    Available_adults = Older_Adults['Names']
    Available_young = Young_Adults['Names']

    print(Available_adults)
    print(Available_young)

    Name_of_request_younger = input("ENTER THE NAME OF YOUNG ADULT WHO IS REQUESTING FOR CARE : ")
    Name_of_request_older = input("ENTER THE OLDER ADULT NAME WHO YOU WANT TO GIVE THE CARE : ")
            
    
    if len(Assigned_Older_Adults[Name_of_request_younger]) >= 3:
        Available_young.remove(Name_of_request_younger)
    
    Ans = input("ENTER YES FOR ACCEPT/ NO FOR REJECT : ")
    
    if Ans.lower() == 'yes':
        Assigned_Older_Adults[Name_of_request_younger].append(Name_of_request_older)
        Available_adults.remove(Name_of_request_older)
    else:
        print("Sorry!! You are Rejected by Older Adult.. Please try Again..")
        
    output1 = []
    output2 = {}
        
    for i in Assigned_Older_Adults.keys():
        if len(Assigned_Older_Adults[i]) > 0:
            output1.append(i)
            output2[i] = Assigned_Older_Adults[i]
    
    return output1,output2

Older_Adults,Young_Adults,Assigned_Older_Adults = initialization()
output1,output2 = Work_assigning(Older_Adults,Young_Adults,Assigned_Older_Adults)
print(output1)
print(output2)

ans1= input("Want to countinue.. YES/NO = ")
if ans1.lower() == 'yes':
    Work_assigning(Older_Adults,Young_Adults,Assigned_Older_Adults)
else:
    print("Thank you for the care !")
