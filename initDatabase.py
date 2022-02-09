import mysql.connector
from mysql.connector import errorcode

import globalvars

cnx = mysql.connector.connect(user='root', password='MySQL8.0', host='localhost')

cursor = cnx.cursor()

globalvars.DB_NAME = "BookStore"

tables = {}

tables['Books'] = (
    "CREATE TABLE `Books` ("
    "`ISBN` VARCHAR(13) NOT NULL,"
    "`Title` VARCHAR(45) NOT NULL,"
    "`Author` VARCHAR(128) NOT NULL,"
    "`Price` DECIMAL(5,2) NOT NULL,"
    "`Cover` VARCHAR(10) NOT NULL,"
    "`Publisher` VARCHAR(256) NOT NULL,"
    "`Pages` INT NOT NULL,"
    "`Language` VARCHAR(45) NOT NULL,"
    "`Series` VARCHAR(128) NULL,"
    "`PubDate` DATE NOT NULL,"
    "PRIMARY KEY (`ISBN`),"
    "UNIQUE INDEX `ISBN_UNIQUE` (`ISBN` ASC) INVISIBLE);"
)

tables["Users"] = (
    "CREATE TABLE `Users` ("
    "`userName` VARCHAR(45) NOT NULL,"
    "`passWord` VARCHAR(20) NOT NULL,"
    "`userType` VARCHAR(20) NOT NULL,"
    "`eMail` VARCHAR(128) NOT NULL,"
    "`Name` VARCHAR(128) NOT NULL,"
    "PRIMARY KEY (`userName`),"
    "UNIQUE INDEX `username_UNIQUE` (`userName` ASC) INVISIBLE);"
)

tables["Carts"] = (
    "CREATE TABLE `Carts` ("
    "`idCart` INT NOT NULL AUTO_INCREMENT,"
    "`cartISBN` VARCHAR(13) NOT NULL,"
    "`cartOwner` VARCHAR(45) NOT NULL,"
    "PRIMARY KEY (`idCart`),"
    "INDEX `fk_cartISBN_idx` (`cartISBN` ASC) INVISIBLE,"
    "INDEX `fk_cartOwner_idx` (`cartOwner` ASC) INVISIBLE,"
    "CONSTRAINT `fk_cISBN` "
        "FOREIGN KEY (`cartISBN`) "
        "REFERENCES `Books` (`ISBN`) "
        "ON DELETE NO ACTION "
        "ON UPDATE NO ACTION,"
    "CONSTRAINT `fk_cuserName` "
        "FOREIGN KEY (`cartOwner`) "
        "REFERENCES `Users` (`userName`) "
        "ON DELETE CASCADE "
        "ON UPDATE CASCADE);"
)

tables["Sales"] = (
    "CREATE TABLE `Sales` ("
    "`idSales` INT NOT NULL AUTO_INCREMENT,"
    "`productISBN` VARCHAR(13) NOT NULL,"
    "`Purchaser` VARCHAR(45) NOT NULL,"
    "`PurchasedOn` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`idSales`),"
    "INDEX `fk_sISBN_idx` (`productISBN` ASC) INVISIBLE,"
    "INDEX `fk_suserName_idx` (`Purchaser` ASC) INVISIBLE,"
    "CONSTRAINT `fk_sISBN` "
        "FOREIGN KEY (`productISBN`) "
        "REFERENCES `Books` (`ISBN`) "
        "ON DELETE NO ACTION "
        "ON UPDATE NO ACTION,"
    "CONSTRAINT `fk_suserName` "
        "FOREIGN KEY (`Purchaser`) "
        "REFERENCES `Users` (`userName`) "
        "ON DELETE CASCADE "
        "ON UPDATE CASCADE);"
)

tables["Wishlists"] = (
    "CREATE TABLE `Wishlists` ("
    "`idWishlists` INT NOT NULL AUTO_INCREMENT,"
    "`wishOwner` VARCHAR(45) NOT NULL,"
    "`wishBook` VARCHAR(13) NOT NULL,"
    "PRIMARY KEY (`idWishlists`),"
    "INDEX `fk_wISBN_idx` (`wishBook` ASC) INVISIBLE,"
    "INDEX `fk_wuserName_idx` (`wishOwner` ASC) INVISIBLE,"
    "CONSTRAINT `fk_wISBN` "
        "FOREIGN KEY (`wishBook`) "
        "REFERENCES `Books` (`ISBN`) "
        "ON DELETE NO ACTION "
        "ON UPDATE NO ACTION,"
    "CONSTRAINT `fk_wuserName` "
        "FOREIGN KEY (`wishOwner`) "
        "REFERENCES `Users` (`userName`) "
        "ON DELETE CASCADE "
        "ON UPDATE CASCADE);"
)

createTables = False

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {};".format(globalvars.DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))

def create_table(cursor, query):
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print("Failed creating table: {}".format(err))
    else:
        print("OK")

try:
    cursor.execute("USE {};".format(globalvars.DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(globalvars.DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(globalvars.DB_NAME))
        cnx.database = globalvars.DB_NAME
        createTables = True
    else:
        print(err)

if createTables:
    for table_name in tables:
        print("Creating table {}".format(table_name), end='')
        create_table(cursor, tables[table_name])


