import time
l=[]
while(1):
    print()
    print("Welcome to your Personal Expense Tracker")
    print()
    print("What do you wanna do today:")
    print("1 -> ADD a new Expense")
    print("2 -> VIEW all Expenses")
    print("3 -> VIEW Total Expense Amount")
    print("4 -> EXIT")
    print()
    ch=int(input("Enter your choice :"))
    print()
    if(ch not in (1,2,3,4)):
        print("Oops! Invalid Choice. Please try again.")
        continue
    elif(ch==4):
        print("Thank you for using Expense Tracker. Kindly visit again. Goodbye!")
        break
    elif(ch==1):
        print("...")
        time.sleep(1)
        print("Enter the details of your new Expense")
        print()
        date=input("Enter today's date (DD/MM/YYYY): ")
        category=input("Enter Expense Category (e.g., Food, Transport, Shopping, etc.): ")
        amount=float(input("Enter Expense Amount: "))
        desc=input("Enter a brief Description of the Expense: ")
        l.append({"date":date,"category":category,"amount":amount,"description":desc})
        print()
        print("...")
        time.sleep(1)
        print("Expense Added Successfully!")
    elif(ch==2):
        print("...")
        time.sleep(1)
        if len(l)==0:
            print("No Expenses to show. Please add some Expenses first.")
            continue
        print("Here are all your Expenses")
        print()
        for expense in l:
            print("\n Date :",expense["date"],"\n Category :",expense["category"],"\n Amount :",expense["amount"],"\n Description :",expense["description"])
    elif(ch==3):
        print("Calculating Total Expense Amount",end=" ")
        time.sleep(0.35)
        print(".",end=" ")
        time.sleep(0.35)
        print(".",end=" ")
        time.sleep(0.35)
        print(".")
        print()
        total=0 
        for expense in l:
            total+=expense["amount"]
        print("Your Total Expense Amount is: ",total)
