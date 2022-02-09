from time import sleep

from tabulate import tabulate

import globalvars
import cosmFuncs
import userFuncs


@userFuncs.login_required
@userFuncs.forCustomer
def viewCart(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT ISBN, Title, Author, Series, Pages, Language, Cover, Price FROM (Books inner join Carts on Books.ISBN = Carts.cartISBN) where cartOwner = '{}';".format(globalvars.CURR_USER))
    records = cursor.fetchall()
    books = [i[1:] for i in records]
    isbns = [i[0] for i in records]
    total = sum([i[7] for i in records])
    cosmFuncs.prnHeader("Cart")
    print(tabulate(books, headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(1,len(books)+1)))
    print("\n Total: ${}\n".format(total))
    choice = cosmFuncs.prnOptions(["Checkout", "Edit Cart", "Back to Main Menu"])
    if choice == '1':
        userFuncs.userCheckout(cursor, total, isbns)
        cnx.commit()
        return
    elif choice == '2':
        editCart(cnx, books, isbns)
    else:
        return #returned to go to main menu in main.py to prevent import loops.


@userFuncs.login_required
@userFuncs.forCustomer
def editCart(cnx, books, isbns):
    cursor = cnx.cursor()
    cosmFuncs.prnHeader("Edit Cart")
    print(tabulate(books, headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(1,len(books)+1)))
    while True:
        while True:
            try:
                index = int(input("Enter # of book to remove: "))
                if 0 < index <= len(books):
                    break
                print("Enter valid no.")
            except:
                print("Enter valid input.")
        cursor.execute("DELETE FROM Carts WHERE cartISBN = '{}' AND cartOwner = '{}'".format(isbns[index-1], globalvars.CURR_USER))
        cnx.commit()
        print("{} removed from cart succesfully!".format(books[index-1][0])) 
        del books[index-1]
        del isbns[index-1]
        if len(books) == 0:
            viewCart(cnx)
            break
        choice = input("Do you want to remove any more books? (y/n): ")
        if choice.lower() == 'n':
            viewCart(cnx)
            break


@userFuncs.login_required
@userFuncs.forCustomer
def viewWishlist(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT ISBN, Title, Author, Series, Pages, Language, Cover, Price FROM (Books INNER JOIN Wishlists on Books.ISBN = Wishlists.wishBook) where wishOwner = '{}';".format(globalvars.CURR_USER))
    records = cursor.fetchall()
    books = [i[1:] for i in records]
    isbns = [i[0] for i in records]
    cosmFuncs.prnHeader("Wishlist")
    print(tabulate(books, headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(1,len(books)+1)))
    choice = cosmFuncs.prnOptions(["Edit Wishlist", "Back to Main Menu"])
    if choice == '1':
        editWishlist(cnx, books, isbns)
    else:
        return #returned to go to main menu in main.py to prevent import loops.


@userFuncs.login_required
@userFuncs.forCustomer
def editWishlist(cnx, books, isbns):
    cursor = cnx.cursor()
    cosmFuncs.prnHeader("Edit Wishlist")
    print(tabulate(books, headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(1,len(books)+1)))
    while True:
        while True:
            try:
                index = int(input("Enter # of book to remove: "))
                if 0 < index <= len(books):
                    break
                print("Enter valid no.")
            except:
                print("Enter valid input.")
        cursor.execute("DELETE FROM Wishlists WHERE wishBook = '{}' AND wishOwner = '{}'".format(isbns[index-1], globalvars.CURR_USER))
        cnx.commit()
        print("{} removed from wishlist succesfully!".format(books[index-1][0]))    
        del books[index-1]
        del isbns[index-1]
        if len(books) == 0:
            viewWishlist(cnx)
            break
        choice = input("Do you want to remove any more books? (y/n): ")
        if choice.lower() == 'n':
            viewWishlist(cnx)
            break
