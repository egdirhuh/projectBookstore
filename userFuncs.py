from time import sleep
from datetime import datetime

from tabulate import tabulate

import globalvars
import cosmFuncs

def checkLuhn(cardNo): #to verify card number
    nSum = 0
    isSecond = False
    for i in range(len(cardNo) - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2
  
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False
 

def login_required(func): #decorator to check if a function can be executed
    def inner(*args, **kwargs):
        if globalvars.CURR_USER:
            returned = func(*args, **kwargs)
            return returned
        else:
            print("Login required!")
    return inner


def forCustomer(func): #decorator to check if a customer is logged in and can execute a function
    def inner(*args, **kwargs):
        if globalvars.USER_TYPE == "Customer":
            returned = func(*args, **kwargs)
            return returned
        else:
            print("Only for customers!")
    return inner 


def forPublisher(func): #decorator to check if a publisher is logged in and can execute a function
    def inner(*args, **kwargs):
        if globalvars.USER_TYPE == "Publisher":
            returned = func(*args, **kwargs)
            return returned
        else:
            print("Only for publishers!")
    return inner 


def registerUser(cursor):
    cursor.execute("SELECT userName from Users;")
    usernames = [i[0] for i in cursor.fetchall()]
    while True:
        username = input("Please enter a username: ")
        if username not in usernames:
            break
        print("Username already exixts, please try another.")
    while True:
        email = input("Enter your email: ")
        if 2 > email.count("@") > 0 and email.split("@")[1].count(".") > 0: #validating email
            break
        print("Invalid email. Please enter a valid email.")
    while True:
        password = input("Enter password (8-20 char): ")
        if 21 > len(password) > 7:
            break
        print("Password must be between 8 and 20 characters.")
    while True:
        type = input("Are you a customer or a publisher?: ")
        if type.lower() == "customer" or type.lower() == 'publisher':
            break
        print("Input invalid. Please try again.")
    if type.lower() == "customer":
        name = input("Enter your name: ")
    else:
        name = input("Enter publisher's name: ")
    query = "INSERT INTO Users VALUES (%s, %s, %s, %s, %s);"
    values = (username, password, type.title(), email, name)
    cursor.execute(query, values)
    print("You have registered succesfully! Now you can login.")


def loginUser(cursor):
    cursor.execute("SELECT userName, passWord, userType from Users;")
    records = cursor.fetchall()
    usernames = [i[0] for i in records]
    while True:
        username = input("Please enter your username: ")
        if username in usernames:
            break
        print("Entered username does not exist.")
        choice = input("Do you want to register? (y/n): ")
        if choice.lower() == "y":
            registerUser(cursor)
            break
    for record in records:
        if record[0] == username:
            curr_record = record
    for i in range(3):
        password = input("Enter your password : ")
        if password == curr_record[1]:
            print("Login Succesful!")
            return username, curr_record[2]
        print("Invalid password! {} attempts left.".format(2-i))
    return False


@login_required
@forCustomer
def userCheckout(cursor, total, isbns):
    cosmFuncs.prnHeader("Checkout")
    print("To pay: {}".format(total))

    while True:
        cardno = input("Enter card number: ") #valid: 5555555555554444
        if (checkLuhn(cardno)):
            break
        print("Card is invalid!")
    while True:
        cvv = input("Enter cvv: ")
        if len(cvv) == 3:
            try:
                int(cvv)
                break
            except:
                print("Please enter only digits!")
        else:
            print("Please enter only 3 digits!")
    while True:
        exp = input("Enter expiration month and year(in mm/yy): ")
        try:
            exp = datetime.strptime(exp, '%m/%y')
            break
        except:
            print("Enter vaild date in given format!")
    for isbn in isbns:
        values = (isbn, globalvars.CURR_USER)
        cursor.execute("INSERT INTO Sales (productISBN, Purchaser) VALUES (%s, %s)", values)
        cursor.execute("DELETE FROM Carts WHERE cartISBN = '{}' AND cartOwner = '{}'".format(isbn, globalvars.CURR_USER))

    print("Payment Succesful!")
    print("Purchases will be mailed to you as soon as possible!")
    sleep(3)


@login_required
@forCustomer
def seePurchases(cursor):
    cursor.execute("SELECT ISBN, Title, Author, Series, PurchasedOn, Price  FROM (Sales inner join Books on Sales.productISBN = Books.ISBN) where Sales.Purchaser = '{}' ORDER BY PurchasedOn DESC;".format(globalvars.CURR_USER))
    records = cursor.fetchall()
    cosmFuncs.prnHeader("Purchases")
    print(tabulate(records, headers=["#", "ISBN", "Title", "Author", "Series", "Purchased On", "Price"], tablefmt='fancy_grid', showindex=range(1,len(records)+1)))
    input("\nPress Enter to exit...")



@login_required
def viewProfile(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * From Users WHERE userName = '{}'".format(globalvars.CURR_USER))
    record = cursor.fetchone()
    cosmFuncs.prnHeader(globalvars.USER_TYPE + " Profile")
    print(globalvars.USER_TYPE + " Name: {}".format(record[4]))
    print("Email: {}".format(record[3]))
    print("Username: {}".format(record[0]))
    print("Password: "+ "*"*len(record[1]))

    choice = cosmFuncs.prnOptions(["Update Profile", "Back to Main Menu"])
    if choice == '1':
        updateProfile(cnx)
    else:
        return


@login_required
def updateProfile(cnx):
    cursor = cnx.cursor()
    cosmFuncs.prnHeader("Update Profile")
    while True:
        cursor.execute("SELECT userName,passWord from Users;")
        records = cursor.fetchall()
        usernames = [i[0] for i in records]
        print("Update:")
        choice = cosmFuncs.prnOptions(["Username", "Password", "Email", "Name"])
        if choice == '1':
            while True:
                username = input("Please enter new username: ")
                if username not in usernames:
                    break
                print("Username already exixts, please try another.")
            query = "UPDATE Users SET userName = '{}' where userName = '{}';".format(username, globalvars.CURR_USER)
            globalvars.CURR_USER = username
            cursor.execute(query)
            cnx.commit()
        elif choice == '2':
            while True:
                password = input("Enter new password (8-20 char): ")
                if 21 > len(password) > 7:
                    break
                print("Password must be between 8 and 20 characters.")
            query = "UPDATE Users SET passWord = '{}' where userName = '{}';".format(password, globalvars.CURR_USER)
            cursor.execute(query)
            cnx.commit()
        elif choice == '3':
            while True:
                email = input("Enter new email: ")
                if 2 > email.count("@") > 0 and email.split("@")[1].count(".") > 0:
                    break
                print("Invalid email. Please enter a valid email.")
            query = "UPDATE Users SET eMail = '{}' where userName = '{}';".format(email, globalvars.CURR_USER)
            cursor.execute(query)
            cnx.commit()
        elif choice == '4':
            name = input("Enter new name: ")
            query = "UPDATE Users SET Name = '{}' where userName = '{}';".format(name, globalvars.CURR_USER)
            cursor.execute(query)
            cnx.commit()
        c = input("Update something else? (y/n): ")
        if c.lower() == 'n':
            break


@login_required
@forPublisher
def seeSales(cursor):
    cursor.execute("SELECT Name FROM Users WHERE userName = '{}';".format(globalvars.CURR_USER))
    pubname = cursor.fetchone()[0]
    cursor.execute("SELECT ISBN, Title, Author, Series, Price, COUNT(*) AS `Units Sold` FROM (Sales inner join Books on Sales.productISBN = Books.ISBN) where Books.Publisher = '{}' GROUP BY Books.ISBN ORDER BY COUNT(*) DESC;".format(pubname))
    records = cursor.fetchall()
    total = sum([i[4]*i[5] for i in records])
    cosmFuncs.prnHeader("Sales")
    print(tabulate(records, headers=["#", "ISBN", "Title", "Author", "Series", "Price", "Units Sold"], tablefmt='fancy_grid', showindex=range(1,len(records)+1)))
    cosmFuncs.prnCenter("Total Value of Books Sold: ${}".format(total))
    input("\nPress Enter to exit...")