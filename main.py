from time import sleep

import mysql.connector
from mysql.connector import errorcode

import globalvars
import initDatabase
import cosmFuncs
import userFuncs
import bookFuncs
import cartWishFuncs

cnx = mysql.connector.connect(user='root', password='MySQL8.0', host='localhost', database=globalvars.DB_NAME)

cursor = cnx.cursor()


def main():
    cosmFuncs.prnHeader("BookStore")
    print("Welcome to the online BookStore, to proceed please choose one of the options below.")

    choice = cosmFuncs.prnOptions(["Login", "Register", "Exit"])

    if choice == '1':
        cosmFuncs.prnHeader("Login")
        result = userFuncs.loginUser(cursor)
        if not result:
            print("Login Failed!")
            sleep(2)
            main()
        globalvars.CURR_USER, globalvars.USER_TYPE = result
        print(globalvars)
        if globalvars.USER_TYPE == "Customer":
            customerMainMenu()
        else:
            publisherMainMenu()
    if choice == '2':
        cosmFuncs.prnHeader("Registration")
        userFuncs.registerUser(cursor)
        cnx.commit()
        main()
    if choice == '3':
        exit()


@userFuncs.login_required
@userFuncs.forCustomer
def customerMainMenu():
    cosmFuncs.prnHeader("Main Menu")

    choice = cosmFuncs.prnOptions(["Search", "Browse", "Cart", "Wishlist", "See Purchases", "Profile","Logout"])

    if choice == '1':
        chosen = bookFuncs.searchBooks(cursor)
        cnx.commit()
        if not chosen:
            customerMainMenu()
    elif choice == '2':
        chosen = bookFuncs.viewBooks(cursor)
        cnx.commit()
        if not chosen:
            customerMainMenu()
    elif choice == '3':
        ret = cartWishFuncs.viewCart(cnx)
        if not ret:
            customerMainMenu()
    elif choice == '4':
        ret = cartWishFuncs.viewWishlist(cnx)
        if not ret:
            customerMainMenu()
    elif choice == '5':
        userFuncs.seePurchases(cursor)
        customerMainMenu()
    elif choice == '6':
        ret = userFuncs.viewProfile(cnx)
        if not ret:
            customerMainMenu()
    else:
        globalvars.CURR_USER = None
        globalvars.USER_TYPE = None
        print("You have logged out successfully!")
        exit()


@userFuncs.login_required
@userFuncs.forPublisher
def publisherMainMenu():
    cosmFuncs.prnHeader("Main Menu")

    choice = cosmFuncs.prnOptions(["Add Book","See Sales","Profile","Logout"])

    if choice == '1':
        bookFuncs.addBook(cursor)
        cnx.commit()
        sleep(2)
        publisherMainMenu()
    elif choice == '2':
        userFuncs.seeSales(cursor)
        publisherMainMenu()
    elif choice == '3':
        ret = userFuncs.viewProfile(cnx)
        if not ret:
            publisherMainMenu()
    else:
        globalvars.CURR_USER = None
        globalvars.USER_TYPE = None
        print("You have logged out successfully!")
        exit()

main()
# #Register
# cnx.commit()