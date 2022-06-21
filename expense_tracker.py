group= []

def create_group():
    name = input("Enter the name of the group\n")
    if(name in group):
        print("The Group name already exits .")
    else:
        group.append(name)
        print("The group is created")
        print(group)
        user_in = input("Do you want to add expenses 'y' or 'n': ")
        if (user_in.lower()== 'y'):
            expense_creator(name)
        else: 
            return group
            #exit()


def expense_creator(naming):
    """
    expenses = {"names" :'',
                "items" : [{"name" : '',
                            "value" : '', 
                            "paid_by" :[] , 
                            "owed_by" : []}]}

    grp_exp = {name : expenses}
    """

    grp_exp = {}

    expenses = {"names" :'',
                "items" : []}
    # this would contain an expense 
    """
    {
   "name": "Fruits and Milk",
   "items": [{"name": "milk", "value": 50, "paid_by": [{"A": 40, "B": 10}], "owed_by": [{"A": 20,"B": 20, "C": 10}]},
             {"name": "fruits", "value": 50, "paid_by": [{"A": 50}], "owed_by": [{"A": 10,"B": 30, "C": 10}]}]
    }
    """
    name_input = input("Enter the expense name\n")
    expenses["names"] = name_input

    
    

    n = int(input('No. of Items\n'))
    for i in range(n):
        
        items_dict = {"name" : '',
                      "value" : '', 
                      "paid_by" :[] , 
                      "owed_by" : []}

        itemName = input('Name: ')
        itemvalue = input('Value: ')
        items_dict["name"] = itemName
        items_dict["value"] = itemvalue

        nPaidBy = int(input('Paid by how many: '))
        paidBy = {}
        for i in range(nPaidBy):
            paidByName = input('Paid by: ')
            #paidBy[0][paidByName] = int(input("Paid Amount: "))
            paidAmount = int(input("Paid Amount : "))
            paidBy[paidByName] = paidAmount

        nOwedBy = int(input('Owed by how many: '))
        owedBy = {}
        for i in range(nOwedBy):
            owedByName = input('Owed by: ')
            #owedBy[0][owedByName] = int(input("Owed Amount: "))
            owedAmount = int(input("Owed Amount "))
            owedBy[owedByName] = owedAmount

        items_dict["paid_by"] = paidBy
        items_dict["owed_by"] = owedBy

        expenses["items"].append(items_dict)

    grp_exp = {naming:[expenses]}

    print("This is the Expenses Dictionary")
    print(expenses)
    print("This is the link of the expenses to name of the group")
    print(grp_exp)
    InputAns = input("Do you want to know the Toatl Balance ? 'y' or 'n' \n")
    if (InputAns.lower() == 'y'):
        balance_tracker(grp_exp,expenses)
    else:
        return grp_exp,expenses
        #exit()
    

        
def balance_tracker(grp_exp,expenses):
    
    """
    {
  "name": "Home",
  "balances": {
    "A": {
      "total_balance": -100.0
      "owes_to": [{"C": 100}],
      "owed_by": []
    },
    "B": {
      "total_balance": 0.0
      "owes_to": [],
      "owed_by": []
    },
    "C": {
      "total_balance": 100.0
      "owes_by": [{"A": 100}],
      "owed_to": []
    }
  }
  }
    """
    
    balance_dict = {"name" : '',
                    "balances" : {}}

    eachName = {}
    
    owesTo = {}
    owesBy = {}

    name = input("Enter the name of the group\n")
    if(name in grp_exp.keys()):
        print("The Group name exits .")
        balance_dict["name"] = name
        for i in grp_exp[name]:
            for j in expenses["items"]:
                for k in j["paid_by"]:
                    eachBalance = {"total_balance" : [],
                                    "owes_to": [],
                                    "owed_by": []}
                    personName = k
                    personPays = j["paid_by"][k]
                    if k in j["owed_by"]:
                        personOwes = j["owed_by"][k]
                        #print(personPays, personOwes)
                        totalBalance = personPays - personOwes
                        #print(totalBalance)
                    else:
                        totalBalance = personPays
                        eachBalance["total_balance"] = totalBalance
                    #eachName[personName] = eachBalance 
                    
                    if len(j["paid_by"]) > 2:
                        pass
                    else:
                        if totalBalance < 0:
                            #print("This is less than 0 value")
                            eachBalance["owed_by"] = []
                            eachBalance["total_balance"] = totalBalance

                            #inv_map = {v: k for k, v in expenses["items"]["paid_by"].items()}
                            #Keymax = max(zip(Tv.values(), Tv.keys()))[1]
                            keymax = max(zip(j["paid_by"].values(),j["paid_by"].keys()))[1]
                            #print(keymax)
                            owesTo[keymax] = totalBalance
                            eachBalance["owes_to"] = owesTo

                        elif totalBalance == 0:
                            eachBalance["owed_by"] = []
                            eachBalance["owes_to"] = []
                        elif totalBalance > 0:
                            #print("This is greater than o value")
                            eachBalance["total_balance"] = totalBalance
                            eachBalance["owes_to"] = []
                            keymin = min(zip(j["paid_by"].values(),j["paid_by"].keys()))[1]
                            #print(keymin)
                            owesBy[keymin] = totalBalance
                            eachBalance["owed_by"] = owesBy
                        eachName[personName] = eachBalance
                        balance_dict["balances"] = eachName
                    #print(balance_dict)


    else:
        print("The user does not exits")
    
    print(balance_dict)
    return balance_dict
    
    

def update_dict(grp_exp,expenses):
    uin = input("Do you want to change the 1.Group name , 2.Expense Name ,\n 3.Expense Value , 4.Paid by ,\n 5.Owed By \n enter the number")
    if (uin == '1'):
        name = input("Enter the old name of the group\n")
        if(name in grp_exp.keys()):
            print("The Group name exits .")
            utext = input("Enter the new name ")
            grp_exp[utext] = grp_exp.pop(name)
            print("The value is updated")
            print(grp_exp)
    elif (uin == '2'):
        name = input("Enter the old name of the expense\n")
        if(name in expenses["names"]):
            print("The expense name exits .")
            utext = input("Enter the new name ")
            expenses.update({"names": utext})
            for i in expenses["items"]:
                if (name in i.values()):
                    i.update({"name": utext})
                    print("For loop executed")
            print("The value is updated")
            print(expenses)
    elif (uin == '3'):
        name = input("Enter the old value of the expense\n")
        #if not any(d['main_color'] == 'red' for d in a):
        #if(name in expenses["items"]["value"]):
        if not any (d["value"] == name for d in expenses["items"]):
            print("Not updated")
        else:
            utext = int(input("Enter the new value "))
            for i in expenses["items"]:
                if (name in i.values()):
                    i.update({"value": utext})
            print("The value is updated")
            print(expenses)
            
    else:
        quit()
    return expenses


def del_dict(grp_exp,expenses):
    uin = input("Do you want to change the 1.Group name , 2.Expense Name \n Enter the number : ")
    if (uin == '1'):
        name = input("Enter the name of the group\n")
        if(name in grp_exp.keys()):
            print("The Group name exits .")
            grp_exp.pop(name)
            print("Deleted the name")
        else:
            print("Not deleted")
    elif (uin == '2'):
        name = input("Enter the name of the expense\n")
        if(name in expenses["names"]):
            print("The expense name exits .")
            expenses = {key:val for key, val in expenses.items() if val != name}
            #expenses.pop(name)
            for i in expenses["items"]:
                if (name in i.values()):
                    i = {key:val for key, val in i.items() if val != name}
            print("Deleted")
    else:
        quit()


#create_group()

## Trying the function
#expenses1 = {'names': 'fruits', 'items': [{'name': 'fruits', 'value': '50', 'paid_by': {'a': 20, 'b': 30}, 'owed_by': {'a': 30, 'b': 20}}]}

#grp_exp1 = {'abc': [{'names': 'fruits', 'items': {'name': 'fruits', 'value': '50', 'paid_by': {'a': 20, 'b': 30}, 'owed_by': {'a': 30, 'b': 20}}}]}

#balance_tracker(grp_exp1 , expenses1)

#del_dict(grp_exp1,expenses1)



print("Hello to the program")
#userinput = input("")
a = create_group()
userinp = input("Do you want to add the expenses to the program \n")
if (userinp.lower() == 'y'):
    b,c = expense_creator(a)
    uinp = input("Do you want to see the balance among the groups\n ")
    if (uinp.lower() == 'y'):
        balance_tracker(b,c)
    usinp = input("Do you want to update the expenses among the groups\n ")
    if (usinp.lower() == 'y'):
        d = update_dict(b,c)
    usin = input("Do you want to delete the expenses among the groups\n ")
    if (usin.lower() == 'y'):
        del_dict(b,c)
else :
    quit()


