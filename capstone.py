from tabulate import tabulate 
from calendar import monthrange
import datetime

#headers
header = ["Category","Date","Description","Amount (Rupiah)"]
header_dream = ["Dream","Target","Amount (Rupiah)"]
header_analysis = ["Dream","Target","Days Left","Amount (Rupiah)"]
#lists needed for analysis function
analysis_list=[]
dream_list = []
dreams = [] #contains only the values in digits 
#wallet = the combined income history list and expense history
wallet = []
income_history = []
expense_history = []
incomes = [] #contains only the values in digits
expenses = [] #contains only the values in digits


#adding user name
def name():
    global user_name
    user_name = input("Hello ! Who will be using this service ? \n")
    return user_name

#adding wishlist to dream_list and the total price to dreams
def add_dream():
    now = datetime.datetime.now() #needed for comparing current date with year and month input
    dream = input("What do you want to achieve ? \n")
    while True :
        year_dream = input("What year do you want to achieve this wishlist ? (in YYYY format) \n")
        if year_dream.isdigit(): #to make sure the correct response from user
            year_dream = int(year_dream)
            if year_dream < now.year : #has to be current or upcoming years
                print("Input must be current year or upcoming year \n")
            elif year_dream >= 10000 :
                print("Please enter 4 digit number ! ")
            else :
                break
        else : 
            print("Incorrect input ! \n")

    while True:
        month_dream = input("What month do you want to achieve this wishlist ? (in digit 1 to 12)\n")
        if month_dream.isdigit(): #to make sure the correct response from user
            month_dream = int(month_dream)
            if year_dream == now.year :
                if month_dream < now.month: # for current year inputs, the month has to be current month or upcoming months
                    print("Please input correct month\n")
                else:
                    break
            elif year_dream > now.year:
                if month_dream <1 or month_dream > 12: #from january to december
                    print("Please input correct month\n")
                else:
                    break
        else:
            print("Incorrect input !\n")

    while True:
        price_dream = input("How much is this wishlist in IDR give or take? \n")
        if price_dream.isdigit():
            price_dream = int(price_dream)
            dream_time = datetime.datetime(year_dream,month_dream,1)
            formatted_dream_time = dream_time.strftime("%B-%Y") #formatted as month-YYYY
            temp_list = [dream,formatted_dream_time,price_dream]
            time_delta = dream_time - now 
            days_left = int(time_delta.days) #to find the time remaining in days 
            if days_left < 0:
                analysis_temp_list = [dream,formatted_dream_time, " 0 (current month)" ,price_dream]
            else :
                analysis_temp_list = [dream,formatted_dream_time, days_left ,price_dream]
            dream_list.append(temp_list)
            dreams.append(price_dream)
            analysis_list.append(analysis_temp_list)
            print("Wishlist added !\n")
            break
        else :
            print("Please enter correct input !")

#show tabulated data of existing wishlist along with their total
def show_dream():
    global total_dream
    total_dream = sum(dreams)
    dream_list_total = dream_list + [["TOTAL","",sum(dreams)]]
    print(tabulate(dream_list_total,headers=header_dream))

#delete existing wishlist
def delete_dream():
    print(tabulate(dream_list,headers=header_dream,showindex="always"))
    while True :
        if len(dream_list) == 0: #if the wishlist is empty
            print("There is no data ! ")
            break
        else: 
            del_dream_user = input("delete which wishlist ? ")
            if del_dream_user.isdigit():
                del_dream_user = int(del_dream_user)
                if del_dream_user > len(dream_list) -1 or del_dream_user < 0:
                    print("Incorrect input !")
                else :
                    del dream_list[del_dream_user]
                    del dreams[del_dream_user]
                    del analysis_list[del_dream_user]
                    print("Dream successfully deleted !")
                    break
            else :
                print("Incorrect input !")

#update existing wishlist (the product name, amount and the target date)
def change_dream():
    print(tabulate(dream_list,headers=header_dream,showindex="always"))
    while True:
        if len(dream_list) == 0:
            print("There is no data ! ")
            break
        else: 
            change_index = input("Which index? ")
            if change_index.isdigit():
                change_index = int(change_index)
                if change_index < 0 or change_index > len(dream_list)-1 : # to make sure the data exists
                    print("Please input the correct digit ! ")
                else :
                    change_value = input("Type 1 to change wishlist product, type 2 for the amount, type 3 for the date : ")
                    if change_value == "1":
                        change_name = input("Change into : ")
                        dream_list[change_index][0] = change_name
                        analysis_list[change_index][0] = change_name
                        print("change successful !")
                        break
                    elif change_value == "2":
                        change_amount = input("Change into : ")
                        if change_amount.isdigit():
                            change_amount = int(change_amount)
                            dream_list[change_index][2] = change_amount
                            dreams[change_index] = change_amount
                            analysis_list[change_index][3] = change_amount
                            print("Change successful !")
                            break
                        else :
                            print("Please input digits !")
                    elif change_value == "3":
                        now = datetime.datetime.now()
                        while True :
                            year_dream = input("What year do you want to achieve this wishlist ? (in YYYY format) \n")
                            if year_dream.isdigit():
                                year_dream = int(year_dream)
                                if year_dream < now.year :
                                    print("Input must be this year or upcoming year \n")
                                else :
                                    break
                            else : 
                                print("please input digit !\n")

                        while True:
                            month_dream = input("What month do you want to achieve this wishlist ? (in digit 1 to 12)\n")
                            if month_dream.isdigit():
                                month_dream = int(month_dream)
                                if year_dream == now.year :
                                    if month_dream < now.month:
                                        print("please input correct month\n")
                                    else:
                                        break
                                elif year_dream > now.year:
                                    if month_dream <1 or month_dream > 12:
                                        print("please input correct month\n")
                                    else:
                                        break
                            else:
                                print("please input digit !\n")
                        dream_time = datetime.datetime(year_dream,month_dream,1)
                        formatted_dream_time = dream_time.strftime("%B-%Y")
                        time_delta = dream_time - now
                        days_left = time_delta.days
                        dream_list[change_index][1] = formatted_dream_time
                        analysis_list[change_index][1] = formatted_dream_time
                        analysis_list[change_index][2] = days_left
                        print("Change successful !")
                        break
                    else : 
                        print("Please input correct response ! ")
                        


            else:
                print("Please enter the correct inputs  ")

#showing the tabulated data of income history and expense history along with their total respectively
def show_wallet():
    global total
    total = sum(incomes) - sum(expenses)
    wallet = income_history + [["TOTAL INCOMES","","",sum(incomes)]] + expense_history + [["TOTAL EXPENSES","","",sum(expenses)]]
    print(tabulate(wallet,headers=header))
    if total < 0 :
        print(f"You have to stop now because your total balance is {total}\n")
    else :
        print(f"Your total balance is {total}\n")

#adding income to income_history and incomes list, along with the time added
def add_balance():
    while True :
        while True :
            add_balance = input("Enter the amount : \n")
            if add_balance.isdigit():
                add_balance = int(add_balance)
                balance = 0
                balance += add_balance
                description = input("For what occasion : \n")
                t = datetime.datetime.now()
                formatted_time = t.strftime("%Y-%m-%d %H:%M:%S")
                temp_list = ["INCOME",formatted_time,description,balance]
                income_history.append(temp_list)
                incomes.append(add_balance)
                print("Income successfully added !\n")
                break
            else :
                print("Incorrect input !\n")

        while True :
            again = input("add another ? Y for yes , N for no\n")
            if again.upper() != "Y" and again.upper() != "N":
                print("input correct response\n")
            elif again.upper() == "Y":
                break
            elif again.upper() == "N":
                break
        if again.upper() == "N":
            break

#adding expense to expense_history and expenses list, along with the time added
def add_expense():
    while True :
        while True :
            add_expense = input("enter the amount : \n")
            if add_expense.isdigit():
                add_expense = int(add_expense)
                expense = 0
                expense += add_expense
                description = input("for what occasion : \n")
                t = datetime.datetime.now()
                formatted_time = t.strftime("%Y-%m-%d %H:%M:%S")
                temp_list = ["EXPENSE",formatted_time,description,expense]
                expense_history.append(temp_list)
                expenses.append(add_expense)
                print("expense successfully added !\n")
                break

            else :
                print("Incorrect input !\n")

        while True :
            again = input("add another ? Y for yes , N for no\n")
            if again.upper() != "Y" and again.upper() != "N":
                print("input correct response\n")
            elif again.upper() == "Y":
                break
            elif again.upper() == "N":
                break
        if again.upper() == "N":
            break

#delete existing income or expense
def delete_wallet():
    while True :
        user = input("income or expense ? I for income , E for expense : \n")
        if user.upper() == "I":
            print(tabulate(income_history,headers=header,showindex="always"))
            if len(income_history) == 0:
                print("There is no data ! ")
                break
            else:
                while True:
                    prompt = input("delete which index ? \n")
                    if prompt.isdigit():
                        prompt = int(prompt)
                        if prompt > len(income_history)-1 or prompt < 0:
                            print("index not available\n")
                        else :
                            del income_history[prompt]
                            del incomes[prompt]
                            print("income successfully deleted !\n")
                            break
                    else : 
                        print("incorrect input !")
                break
        elif user.upper() == "E":
            print(tabulate(expense_history,headers=header,showindex="always"))
            if len(expense_history) == 0:
                print("There is no data ! ")
                break
            else:
                while True:
                    prompt = input("delete which index ? ")
                    if prompt.isdigit():
                        prompt = int(prompt)
                        if prompt > len(expense_history)-1 or prompt < 0:
                            print("index not available\n")
                        else :
                            del expense_history[prompt]
                            del expenses[prompt]
                            print("expense successfully deleted !\n")
                            break
                    else :
                        print("incorrect input !")
            break
        else :
            print("Please input correct response\n")

#update income or expense details
def update_income_expense():
    while True:
        user = input("Type I to update income , E for expense : \n")
        if user.upper() == "I":
            print(tabulate(income_history,headers=header,showindex="always"))
            if len(income_history) == 0:
                print("There is no data ! ")
                break
            else:
                while True:
                    prompt = input("Update which index ? \n")
                    if prompt.isdigit():
                        prompt = int(prompt)
                        if prompt > len(income_history)-1 or prompt < 0:
                            print("index not available\n")
                        else :
                            update = input("Type 1 to update income description , 2 for amount : ")
                            if update == "1":
                                updated_income_name = input("Change into : ")
                                income_history[prompt][2] = updated_income_name
                                print("Income description successfully changed !\n")
                                break
                            elif update =="2":
                                updated_income_amount = input("Change into : ")
                                if updated_income_amount.isdigit():
                                    updated_income_amount = int(updated_income_amount)
                                    income_history[prompt][3] = updated_income_amount
                                    incomes[prompt] = updated_income_amount
                                    print("Income amount successfully changed ! ")
                                    break
                                else :
                                    print("please input correct amount !")
                            else :
                                print("please input correct response")
                    else : 
                        print("Incorrect input !")
                break
        elif user.upper() == "E":
            print(tabulate(expense_history,headers=header,showindex="always"))
            if len(income_history) == 0:
                print("There is no data ! ")
                break
            else: 
                while True:
                    prompt = input("delete which index ? ")
                    if prompt.isdigit():
                        prompt = int(prompt)
                        if prompt > len(expense_history)-1 or prompt < 0:
                            print("index not available\n")
                        else :
                            update = input("Type N to update expense description , A for amount : ")
                            if update.upper() == "N":
                                updated_expense_name = input("Change into : ")
                                expense_history[prompt][2] = updated_expense_name
                                print("Expense description successfully changed !\n")
                                break
                            elif update.upper() =="A":
                                updated_expense_amount = input("Change into : ")
                                if updated_expense_amount.isdigit():
                                    updated_expense_amount = int(updated_expense_amount)
                                    expense_history[prompt][3] = updated_expense_amount
                                    expenses[prompt] = updated_expense_amount
                                    print("Income amount successfully changed ! ")
                                    break
                                else :
                                    print("please input correct amount !")
                            else :
                                print("please input correct response")
                    else : 
                        print("incorrect input !")
                break
        else :
            print("Please input correct response\n")

#analyze the saving progress towards the wishlist goals
def analysis(): 
    global total
    total = sum(incomes) - sum(expenses) #total balance in wallet
    now = datetime.datetime.now() #current time to be compared with the goal date
    analysis_total = analysis_list + [["","","",""]] + [["TOTAL TARGET","","",sum(dreams)]] + [["TOTAL BALANCE","","",total]]
    print(tabulate(analysis_total,headers=header_analysis))
    year = now.year
    month = now.month
    num_days_in_month = monthrange(year,month)[1] 
    daysleft = num_days_in_month - now.day #calculate the remaining days of current month

    if len(dream_list)==0:
        print("Hey you could use some wishlist in your life :D")
    elif sum(dreams) == total:
        print(f"Congrats ! You have exactly the amount of your target ! But isn't it wise to save some more money to survive the remaining {daysleft} days of this month?")
    elif total > sum(dreams):
        budget = round((total-sum(dreams)) / daysleft)
        print(f"Good job ! You have achieved your dream stuff ! You even have excess budget,Your budget for the rest of the month ({daysleft} days) is maximum {budget} per day\n")
    elif total == 0:
        print("The sooner you start your saving journey, the better !\n")
    else :
        print(f"Don't give up ! You are getting there ! You have {sum(dreams)-total} left to save !\n")

#adding heart art, the more the wishlist, the bigger the heart size
def byebye():
    heart = ""
    size = 6 + (len(dream_list) * 2)
    for i in range(1,size-round((size/2)),1):
        heart += " " * int((-i+((size/2)-1))) + "$" *(2*i+1) + " " * (-2*i+(size+1)) + "$" *(2*i+1)
        heart += "\n"
    for i in range(size,0,-1):
        heart += " " * (size-i+1)
        heart += "$" * (2*i-1)
        heart += "\n"

    print(heart)
    print(f"Thank you {user_name} for using this service ! \n")



name()
while True :
    print(f'''
            
                            Hello {user_name} ! Welcome to Dream/Wishlist Tracker !
    
    This service will help you track the journey progress of achieving your short or/long term wishlist ! 

    select option :
1. Show your current wishlist
2. Add a new wishlist
3. Remove existing wishlist
4. Change wishlist (product or amount or date)
5. Proceed to your journey !
0. End program\n''')

    user_choice = input("Choose option : \n")
    if user_choice == "1":
        show_dream()
    elif user_choice =="2":
        add_dream()
    elif user_choice =="3" :
        delete_dream()
    elif user_choice == "4":
        change_dream()
    elif user_choice == "0":
        byebye()
        break
    elif user_choice =="5":
        while True :
            print('''
        
                        This is your incomes and expenses tracker ! Don't spend too much now :D
        
            select option :
        
            1. show balance and history
            2. add balance
            3. add expense
            4. delete income or expense
            5. update income or expense
            6. analysis
            0. back to main menu\n
            ''')
            user = input("choose option: \n")
            if user == "1":
                show_wallet()
            elif user == "2":
                add_balance()
            elif user == "3":
                add_expense()
            elif user == "4":
                delete_wallet()
            elif user == "5":
                update_income_expense()
            elif user == "6":
                analysis()
            elif user == "0":
                break
            else :
                print("input correct response\n")
    else:
        print("input correct response !\n")