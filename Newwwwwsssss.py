import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Thunder",
    database="sam"
)


def Inp():
    A = int(input("SCode:"))
    B = input("SName:")
    C = int(input("Value:"))
    D = int(input("Stock:"))
    E = input("Date:")

    mycursor = mydb.cursor()
    sql = ("insert into items (SCode,SName,Value,Stock,UpdatedDate) values(%s,%s,%s,%s,%s)")
    val = (A, B, C, D, E)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted")
    Ca = input("Enter more record? (Y/N):")


def Update():
    mycursor = mydb.cursor()

    print("1.Update SCode")
    print("2.Update SName")
    print("3.Update Values")
    print("4.Update Stock")
    print("5.Update Date")
    print("6.Exit")
    NO = (1, 2, 3, 4, 5, 6)

    UChoice = int(input("Enter your choice:"))
    if UChoice not in NO:
        print("Enter the correct value!!")
    if UChoice == 1:
        OldSCode = int(input("Enter the old SCode:"))
        NewSCode = int(input("Enter the new SCode:"))
        sql1 = ("update items set SCode=NewScode where SCode=OldSCode")
        mycursor.execute(sql1)

        mydb.commit()

        print(mycursor.rowcount, "Records Updated")

    elif UChoice == 2:
        OldSName = input("Enter the old SName:")
        NewSName = input("Enter the new SName:")
        sql2 = ("update items set SName=%s where SName=%s")
        val = (NewSName,OldSName)
        mycursor.execute(sql2, val)

        mydb.commit()

        print(mycursor.rowcount, "Records Updated")

    elif UChoice == 3:
        OldValue = int(input("Enter the old Value:"))
        NewValue = int(input("Enter the new Value:"))
        sql3 = ("update items set Value = NewValue where Value = OldValue")
        mycursor.execute(sql3)

        mydb.commit()

        print(mycursor.rowcount, "Records Updated")

    elif UChoice == 4:
        OldStock = int(input("Enter the old Stock:"))
        NewStock = int(input("Enter the new Stock:"))
        sql4 = ("update items set Stock=NewStock where Stock=OldStock")
        mycursor.execute(sql4)

        mydb.commit()

        print(mycursor.rowcount, "Records Updated")

    elif UChoice == 5:
        OldDate = input("Enter the old Date:")
        NewStock = input("Enter the new Date:")
        sql4 = ("update items set Stock=NewDate where Stock=OldDate")
        mycursor.execute(sql4)

        mydb.commit()

        print(mycursor.rowcount, "Records Updated")

    elif UChoice == 6:
        print("Exiting Update Menu")

    else:
        print("Enter correct value!!")

def Remove():
        mycursor = mydb.cursor()
        print("1.Remove the whole item")
        print("2.Remove SName")
        print("3.Remove Values")
        print("4.Remove Stock")
        print("5.Remove Date")
        print("6.Exit")
        Nu = (1, 2, 3, 4, 5, 6)
        RChoice = int(input("Enter your choice:"))
        if RChoice not in Nu:
            print("Enter the correct choice!!")

        if RChoice == 1:
            RemSCode = int(input("Enter the SCode to remove the whole item:"))
            sql5 = ("delete * from items where SCode=RemSCode")
            mycursor.execute(sql5)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")

        elif RChoice == 2:
            RemSName = input("Enter the SName to remove:")
            sql6 = ("update items set SName=null where SName=RemSName")
            mycursor.execute(sql6)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")

        elif RChoice == 3:
            RemValue = int(input("Enter the Value to remove:"))
            sql7 = ("update items set Value=null where Value=RemValue")
            mycursor.execute(sql7)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")

        elif RChoice == 4:
            RemStock = int(input("Enter the Stock to remove:"))
            sql8 = ("update items set Stock=null where Stock=RemStock")
            mycursor.execute(sql8)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")

        elif RChoice == 5:
            RemDate = input("Enter the Date to remove:")
            sql9 = ("update items set UpdatedDate=null where Date=RemDate")
            mycursor.execute(sql9)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")

        elif RChoice == 6:
            print("Exiting Remove Menu")

def Check():
        mycursor = mydb.cursor()
        print("1.Check SCode")
        print("2.Check SName")
        print("3.Check Values")
        print("4.Check Stock")
        print("5.Check Date")
        print("6.Exit")
        Nom = (1, 2, 3, 4, 5, 6)
        CChoice = int(input("Enter your choice:"))
        if CChoice not in Nom:
            print("Enter the correct choice!!")
        if CChoice == 1:
            ChScode = int(input("Enter the SCOde to check:"))
            sql10 = ("select SCode from item where SCode=ChSCode")
            mycursor.execute(sql10)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")
        elif CChoice == 2:
            ChSName = input("Enter the SName to check:")
            sql11 = ("select SName from item where SName=ChSName")
            mycursor.execute(sql11)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")
        elif CChoice == 3:
            ChValue = int(input("Enter the Value to remove:"))
            sql12 = ("select Value from item where Value=ChValue")
            mycursor.execute(sql12)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")
        elif CChoice == 4:
            ChStock = int(input("Enter the Stock to remove:"))
            sql13 = ("select stock from item where stock=ChStock")
            mycursor.execute(sql13)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")
        elif CChoice == 5:
            ChDate = input("Enter the Date to be remove:")
            sql14 = ("select updateddate from item where updateddate=ChDate")
            mycursor.execute(sql14)
            mydb.commit()

            print(mycursor.rowcount, "Records Updated")
        elif CChoice == 6:
            print("Exiting the Check Menu")

def Exit():
        bcd = input("Do you want to exit Employee menu?? (y/n):")

def Employee():
  print("1.Input A New Item")
  print("2.Update the Item")
  print("3.Remove the Item")
  print("4.Check the item")
  print("5.Exit the program")
  NN = (1, 2, 3, 4, 5)
  Coice = int(input("Enter your choice:"))
  if Coice not in NN:
      print("Enter the correct value!!")
  if Coice == 1:
      Inp()
  elif Coice == 2:
      Update()
  elif Coice == 3:
      Remove()
  elif Coice == 4:
      Check()
  elif Coice == 5:
      Exit()

Employee()