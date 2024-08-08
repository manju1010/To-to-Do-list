user_input = "random"
data=[]
def show_menu():
    print("Menu ")
    print("1.Add an item")
    print("2.Mark as Done")
    print("3.View items")
    print("4.Exit")
    
while user_input != 4:
    show_menu()
    user_input=input("Enter Your Choice: ")
    if user_input=="1":
        item = input("Item to be added: ")
        data.append(item)
        print("Added item: ",item)
    elif user_input == "2":
        item=input("Item Marked to be done: ")
        for i in data:
            if i==item:
                data.remove(item)
                print(item,"Marked as Completed")
            else:
                print("The item is not in the To-do-list")
       
    elif user_input == "3":
        print("The List Of Items:" , data)
    elif user_input == "4":
        print("GoodBye!")
