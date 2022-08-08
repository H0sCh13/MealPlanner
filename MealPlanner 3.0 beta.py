import os
import random 

Essens_list_screen = ["Fischbrötchen" , "Tomatensuppe" , "Asiatisch" , "Wraps" , "Sandwich" , "Bolognese" ,
                        "Gulasch" , "Calzone" , "Rösti" , "Döner" , "Kartoffelgratin" ,
                        "Möhreneintopf" , "Schafskäse" , "Flammenkuchen" , "Blätterteigecken" ,
                        "Nudelauflauf" , "Nudelsalat" , "Carbonara" , "Pizza"]
                        
Essens_list_search = {"Fischbrötchen" : 10 , "Tomatensuppe" : 20 , "Asiatisch" : 30 , "Wraps" : 40 , "Sandwich" : 50} # Work in Progress



print("Meal Planner 3.0 beta\n")

print("Type [list] to check the original list")
print("Type [add] to add new Item to list")
print("Type [remove] to remove Item from list")
print("Type [calory] to get the amount of specific item 'Work in Progress'")
print("Type [clear] to clear text")
print("Type [x] to randomize")
print("Type [s] to save file 'Work in Progress]'\n")


for x in range(19):
    print("Meal " + str(x+1) + ": " + Essens_list_screen[x])


Entry = input("\nWelcome!")

while Entry != "exit":

    x = input("\nEingabe:")
    
    if x == "x":
    
        sample = random.sample(range(17), 7), "Meals in one Week"
        
        print(sample)
        
    
    elif x == "calory":
    
        calory = input("\nWhich Item:")
        calory = Essens_list_search.get(calory)
        print(calory)
    
       
    elif x == "list":
        
        for x in range(19):
            try:
                print("Meal " + str(x+1) + ": " + Essens_list_screen[x])
            except:
                print("Meal ?")
        
    elif x == "add":
    
        More_Item = input("\nNew Item:")        
        Essens_list_screen.append(More_Item)
        print(Essens_list_screen)
            
                
    elif x == "remove":
    
        try:
        
            Less_Item = input("\nWhich Item:")
            Essens_list_screen.remove(Less_Item)
            print(Essens_list_screen)
            
        except:    
        
            print("Not in list")
    
    elif x == "clear":
      
        os.system("cls")
        print("Essensplaner\n")

        print("Type [list] to check the original list")
        print("Type [add] to add a new Item to list")
        print("Type [remove] to remove an Item from the list")
        print("Type [calory] to get the amount of the item")
        print("Type [clear] to clear text")
        print("Type [x] to randomize")
        print("Type [s] to save file\n")
        
        for x in range(19):
            try:
            
                print("Meal " + str(x+1) + ": " + Essens_list_screen[x])
                
            except:
                
                print("Meal ?")
                
                
    elif x == "s":  #Work in Progress
    
        try:
            Essens_planer = open("Essens_planer.txt" , "w")
            Essens_planer.write(Essens_list_screen)
            Essens_planer.close()
            print("\nSaved!")
            
        except:
            
            print("\nError...")


    elif x =="exit":
    
        break
         
    
    else:
        print("\nSorry?")
        
    
print("Have a nice day!")

input()