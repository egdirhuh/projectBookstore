from datetime import datetime

from tabulate import tabulate

import globalvars
import cosmFuncs
import userFuncs


@userFuncs.login_required
@userFuncs.forCustomer
def searchBooks(cursor):
    cosmFuncs.prnHeader("Search")
    while True:
        print("Search By: ")
        choice = cosmFuncs.prnOptions(["Title", "Author", "ISBN", "Publisher", "Series"])
        search = input("Enter term to search: ")
        if choice == '1':
            colname = 'Title'
        elif choice == '2':
            colname = 'Author'
        elif choice == '3':
            colname = 'ISBN'
        elif choice == '4':
            colname = 'Publisher'
        else:
            colname = 'Series'
    
        cursor.execute("SELECT ISBN, Title, Author, Series, Pages, Language, Cover, Price FROM Books WHERE {} LIKE '%{}%'".format(colname, search))
        records = cursor.fetchall()
        if len(records) == 0:
            print("No Results found!")
            continue
        books = [i[1:] for i in records]
        cosmFuncs.prnHeader("Search Results")
        print(tabulate(books, headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(1,len(books)+1)))
        choice = cosmFuncs.prnOptions(['View Specific Book in Results', 'Search Again', 'Back to Main Menu'])
        if choice == '1':
            while True:
                try:
                    index = int(input("Enter # of book to view: "))
                    if 0 < index <= len(books):
                        break
                    print("Enter valid no.")
                except:
                    print("Enter valid input.")
            viewSpecificBook(cursor, records[index-1][0])
            break
        elif choice == '2':
            continue
        else:
            return


@userFuncs.login_required
@userFuncs.forCustomer
def viewBooks(cursor):
    cursor.execute("SELECT ISBN, Title, Author, Series, Pages, Language, Cover, Price FROM Books;")
    records = cursor.fetchall()
    books = [i[1:] for i in records]
    i = 0
    j = 1
    while i < len(books):
        cosmFuncs.prnHeader("Books - Page {}".format(j))
        if i == 0:
            print(tabulate(books[i:i+10], headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(i+1,i+11)))
            choice = cosmFuncs.prnOptions(["Next Page", "View Book", "Back to Main Menu"])
            if choice == '1':
                i += 10
                j += 1
                continue
            elif choice == '2':
                while True:
                    chosen = int(input("Enter the # of book to view: "))
                    if chosen < len(books):
                        break
                    print("Invalid input")
                viewSpecificBook(cursor, records[chosen-1][0])
                break
            elif choice == '3':
                break      
        if i +  10 > len(books):
            print(tabulate(books[i:len(books)], headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(i+1,len(books)+1)))
            choice = cosmFuncs.prnOptions(["Prev Page", "View Book", "Back to Main Menu"])
            if choice == '1':
                i -= 10
                j -= 1
                continue
            elif choice == '2':
                while True:
                    chosen = int(input("Enter the # of book to view: "))
                    if chosen < len(books):
                        break
                    print("Invalid input")
                viewSpecificBook(cursor, records[chosen-1][0])
                break
            elif choice == '3':
                break         
        else:
            print(tabulate(books[i:i+10], headers=['#', 'Title', 'Author', 'Series', 'Pages', 'Language', 'Cover', 'Price'], tablefmt='fancy_grid', showindex=range(i+1,i+11)))
        choice = cosmFuncs.prnOptions(["Next Page", "Prev Page", "View Book", "Back to Main Menu"])
        if choice == '1':
            i += 10
            j += 1
        elif choice == '2':
            i -= 10
            j -= 1
        elif choice == '3':
            while True:
                chosen = int(input("Enter the # of book to view: "))
                if chosen < len(books):
                    break
                print("Invalid input")
            viewSpecificBook(cursor, records[chosen-1][0])
            break
        else:
            break


@userFuncs.login_required
@userFuncs.forCustomer
def viewSpecificBook(cursor, chosen):
    cursor.execute("SELECT * FROM Books WHERE ISBN = '{}';".format(chosen))
    data = cursor.fetchone()
    cosmFuncs.prnHeader(data[1])
    print("Book: {}".format(data[1]))
    print("By {}".format(data[2]))
    if data[8]:
        print("Part of: {}, Volume No. {}\n".format(data[8].split("#")[0], data[8].split("#")[1]))
    else:
        print("\n")
    print("Price: {}".format(data[3]))
    print("Format: {}\n".format(data[4]))
    print("{} Pages".format(data[6]))
    print("Published On: {}".format(data[9].strftime('%b %d,%Y')))
    print("Published By: {}".format(data[5]))
    print("Language: {}\n\n".format(data[7]))
    while True:
        choice= cosmFuncs.prnOptions(["Add to Cart", "Add To Wishlist", "Back to Main Menu"])
        if choice == '1':
            values = (chosen, globalvars.CURR_USER)
            cursor.execute("INSERT INTO Carts (cartISBN, cartOwner) VALUES (%s, %s);", values)
            print("{} added to cart successfully.".format(data[1]))
        elif choice == '2':
            values = (chosen, globalvars.CURR_USER)
            cursor.execute("INSERT INTO Wishlists (wishBook, wishOwner) VALUES (%s, %s);", values)
            print("{} added to wishlist successfully.".format(data[1]))
        else:
            return


@userFuncs.login_required
@userFuncs.forPublisher
def addBook(cursor):
    cursor.execute("SELECT Name From Users WHERE userName = '{}'".format(globalvars.CURR_USER))
    pubname = cursor.fetchone()[0]
    cosmFuncs.prnHeader("Add Book")
    print("ISBN: without hyphens (10 or 13 chars)")
    while True:
        isbn = input("Enter ISBN: ")
        if len(isbn) == 13:
            try:
                int(isbn)
                break
            except:
                print("Please enter only digits")
        elif len(isbn) == 10:
            try:
                int(isbn)
                isbn = '000' + isbn
                break
            except:
                print("Please enter only digits")
                continue
        else:
            print("Please enter valid ISBN")
    
    title = input("Enter Title: ")
    author = input("Enter author: ")
    print("Series: (Name of Series) #(No. of Book) like 'Jason Bourne #2'")
    series = input("Enter series(if any, leave blank if not): ")
    format = input("Enter format: (Paperback, Hardcover, etc.): ")
    while True:
        price = input("Enter price (in $): ")
        try:
            float(price)
            break
        except:
            print("Please enter valid price!")
    while True:
        pubdate = input("Please enter publishing date in YYYY-MM-DD: ")
        try:
            pubdate = datetime.strptime(pubdate, '%Y-%m-%d')
            break
        except:
            print("Enter vaild date in given format!")
    while True:
        pages = input("Enter no. of pages: ")
        try:
            int(pages)
            break
        except:
            print("Please enter numbers only!")
    lang = input("Enter language of book: ")


    values = (isbn, title, author, price, format, pubname, pages, lang, series, pubdate)
    cursor.execute("INSERT INTO Books VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", values)
    print("Added successfully!")
