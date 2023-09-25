import mysql.connector
def conn():
    db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
    if db_connection:
        return True
    else:
        print("unable to make conection")


def userEntry():
    db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE TABLE if not exists customerdetails(cid varchar(255) primary key,name VARCHAR(255), address VARCHAR(255))")
    cid=input("Enter cid:")
    name=input("Enter name:")
    address=input("Enter add:")
    sql = "INSERT INTO customerdetails(cid,name, address) VALUES (%s, %s, %s)"
    val = (cid,name, address)
    db_cursor.execute(sql, val)
    db_connection.commit()
    print(db_cursor.rowcount, "record inserted.")
    db_cursor.close()

def bookingRecord():
    global cid
    customer=searchCustomer()
    if customer:
        db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
        db_cursor = db_connection.cursor()
        db_cursor=db_connection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS bookingrecord(CID VARCHAR(255),CHECK_IN DATE ,CHECK_OUT DATE)"
        db_cursor.execute(createTable)
        checkin=input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
        checkout=input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
        sql= "INSERT INTO bookingrecord VALUES(%s,%s,%s)"
        values= (cid,checkin,checkout)
        db_cursor.execute(sql,values)
        db_cursor.execute("COMMIT")
        print("\nCHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !")
        db_cursor.close()
    

def roomRent():
    global cid
    customer=searchCustomer()
    if customer:
        global roomrent
        db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
        db_cursor = db_connection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS roomrent(CID VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT)"
        db_cursor.execute(createTable)
        print ("\n ##### We have The Following Rooms For You #####")
        print (" 1. Ultra Royal ----> 10000 Rs.")
        print (" 2. Royal ----> 5000 Rs. ")
        print (" 3. Elite ----> 3500 Rs. ")
        print (" 4. Budget ----> 2500 USD ")
        roomchoice =int(input("Enter Your Option : "))
        roomno=int(input("Enter Customer Room No : "))
        noofdays=int(input("Enter No. Of Days : "))
        if roomchoice==1:
            roomrent = noofdays * 10000
            print("\nUltra Royal Room Rent : ",roomrent)
        elif roomchoice==2:
            roomrent = noofdays * 5000
            print("\nRoyal Room Rent : ",roomrent)
        elif roomchoice==3:
            roomrent = noofdays * 3500
            print("\nElite Royal Room Rent : ",roomrent)
        elif roomchoice==4:
            roomrent = noofdays * 2500
            print("\nBudget Room Rent : ",roomrent)
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
            return
        sql= "INSERT INTO roomrent VALUES(%s,%s,%s,%s,%s)"
        values= (cid,roomchoice,noofdays,roomno,roomrent,)
        db_cursor.execute(sql,values)
        db_cursor.execute("COMMIT")
        print("Thank You , Your Room Has Been Booked For : ",noofdays , "Days" )
        print("Your Total Room Rent is : Rs. ",roomrent)
        db_cursor.close()
   
def Restaurent():
    global cid
    customer=searchCustomer()
    if customer:
        global restaurentbill
        db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
        db_cursor = db_connection.cursor()
        db_cursor=db_connection.cursor()
        createTable="CREATE TABLE IF NOT EXISTS restaurant(CID VARCHAR(20),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30))"
        db_cursor.execute(createTable)
        print("1. Vegetarian Combo -----> 300 Rs.")
        print("2. Non-Vegetarian Combo -----> 500 Rs.")
        print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
        choice_dish = int(input("Enter Your Cusine : "))
        quantity=int(input("Enter Quantity : "))
        if choice_dish==1:
            print("\nSO YOU HAVE ORDER: Vegetarian Combo ")
            restaurentbill = quantity * 300
        elif choice_dish==2:
            print("\nSO YOU HAVE ORDER: Non-Vegetarian Combo ")
            restaurentbill = quantity * 500
        elif choice_dish==3:
            print("\nSO YOU HAVE ORDER: Vegetarian & Non-Vegetarian Combo ")
            restaurentbill= quantity * 750
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
            return
        sql= "INSERT INTO restaurant VALUES(%s,%s,%s,%s)"
        values= (cid,choice_dish,quantity,restaurentbill)
        db_cursor.execute(sql,values)
        db_cursor.execute("COMMIT")
        print("Your Total Bill Amount Is : Rs. ",restaurentbill)
        print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n" )
        db_cursor.close()
def Gaming():
    global cid
    customer=searchCustomer()
    if customer:
        global gamingbill
        db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
        db_cursor = db_connection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS games(CID VARCHAR(20),GAMES VARCHAR(30),HOURS VARCHAR(30),GAMING_BILL VARCHAR(30))"
        db_cursor.execute(createTable)
        print("1. Table Tennis -----> 150 Rs./HR")
        print("2. Bowling -----> 100 Rs./HR")
        print("3. Snooker -----> 250 Rs./HR")
        print("4. VR World Gaming -----> 400 Rs./HR")
        print("5. Video Games -----> 300 Rs./HR")
        print("6. Swimming Pool Games -----> 350 Rs./HR")
        game=int(input("Enter What Game You Want To Play : "))
        hour=int(input("Enter No Of Hours You Want To Play : "))
        print("\n\n#################################################")
        if game==1:
            print("YOU HAVE SELECTED TO PLAY : Table Tennis")
            gamingbill = hour * 150
        elif game==2:
            print("YOU HAVE SELECTED TO PLAY : Bowling")
            gamingbill = hour * 100
        elif game==3:
            print("YOU HAVE SELECTED TO PLAY : Snooker")
            gamingbill = hour * 250
        elif game==4:
            print("YOU HAVE SELECTED TO PLAY : VR World Gaming")
            gamingbill = hour * 400
        elif game==5:
            print("YOU HAVE SELECTED TO PLAY : Video Games")
            gamingbill = hour * 300
        elif game ==6:
            print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
            gamingbill = hour * 350
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
            return
        sql= "INSERT INTO games VALUES(%s,%s,%s,%s)"
        values= (cid,game,hour,gamingbill)
        db_cursor.execute(sql,values)
        db_cursor.execute("COMMIT")
        print("Your Total Gaming Bill Is : Rs. ",gamingbill)
        print("FOR : ",hour," HOURS","\n *** WE HOPE YOU WILL ENJOY YOUR GAME ***")
        print("\n\n#################################################")
        db_cursor.close()
    
def Fashion():
    global cid
    customer=searchCustomer()
    if customer:
        global fashionbill
        db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
        db_cursor = db_connection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS wears(CID VARCHAR(20),DRESS VARCHAR(30),AMOUNT VARCHAR(30),BILL VARCHAR(30))"
        db_cursor.execute(createTable)
        print("1. Shirts -----> 1500 Rs.")
        print("2. T-Shirts -----> 300 Rs.")
        print("3. Pants -----> 2000 Rs.")
        print("4. Jeans -----> 4000 Rs.")
        print("5. Gown -----> 3000 Rs.")
        print("6. Western dress -----> 5000 Rs.")
        print("7. Skirts -----> 400 Rs.")
        print("8. Trousers -----> 200 Rs.")
        print("9. InnerWear -----> 30 Rs.")
        print("10. Socks -----> 50 Rs.")
        dress=int(input("Enter the your Choice wear: "))
        quantity=int(input("How many you want to buy: "))
        if dress==1:
            print("\nShirts")
            fashionbill = quantity * 1500
        elif dress==2:
            print("\nT-Shirts")
            fashionbill = quantity * 300
        elif dress==3:
            print("\nPants")
            fashionbill = quantity * 2000
        elif dress==4:
            print("\nJeans")
            fashionbill = quantity * 4000
        elif dress==5:
            print("\nGown")
            fashionbill = quantity * 3000
        elif dress==6:
            print("\nWestern dress")
            fashionbill = quantity * 5000
        elif dress==7:
            print("\nSkirts")
            fashionbill = quantity * 400
        elif dress==8:
            print("\nTrousers")
            fashionbill = quantity * 200
        elif dress==9:
            print("\nInnerWear")
            fashionbill = quantity * 30   
        elif dress==10:
            print("\nSocks")
            fashionbill = quantity * 50
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
            return
        sql= "INSERT INTO wears VALUES(%s,%s,%s,%s)"
        values= (cid,dress,quantity,fashionbill)
        db_cursor.execute(sql,values)
        db_cursor.execute("COMMIT")
        print("\n\n#################################################")
        print("\nYOU SELECT ITEM NO : ",dress,"\nYOUR QUANTITY IS : ",quantity," ITEMS","\nTHANK YOU FOR SHOPPING VISIT AGAIN!!!" )
        print("\nYour Total Bill Is : ",fashionbill)
        print("\n\n#################################################")
        db_cursor.close()

def totalAmount():
    global cid
    customer=searchCustomer()
    if customer:
        global grandTotal
        global roomrent
        global restaurentbill
        global fashionbill
        global gamingbill
        db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel')
        db_cursor = db_connection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20),C_NAME VARCHAR(30),ROOMRENT INT ,RESTAURENTBILL INT ,GAMINGBILL INT,FASHIONBILL INT,TOTALAMOUNT INT)"
        db_cursor.execute(createTable)
        sql="INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)"
        name = input("Enter Customer Name : ")
        grandTotal=(roomrent + restaurentbill + fashionbill + gamingbill)
        values=(cid,name,roomrent,restaurentbill,gamingbill,fashionbill,grandTotal)
        db_cursor.execute(sql,values)
        db_cursor.execute("COMMIT")
        db_cursor.close()
        print("\n **** CROWN PLAZA MIAMI **** CUSTOMER BIILING ****")
        print("\n CUSTOMER NAME : " ,name)
        print("\nROOM_RENT : Rs. ",roomrent)
        print("\nRESTAURENT BILL : Rs. ",restaurentbill)
        print("\nFASHION BILL : Rs. ",fashionbill)
        print("\nGAMING BILL : Rs. ",gamingbill)
        print("___________________________________________________")
        print("\nTOTAL AMOUNT : Rs. ",grandTotal)
        db_cursor.close()        
        
        
def searchCustomer():
    global cid
    db_connection = mysql.connector.connect(host="localhost",user="root",passwd="135790",database='hotel',charset='utf8')
    db_cursor = db_connection.cursor()
    cid=input("ENTER CUSTOMER ID : ")
    sql="SELECT * FROM customerdetails WHERE CID= %s"
    db_cursor.execute(sql,(cid,))
    data=db_cursor.fetchall()
    if data:
        print(data)
        return True
    else:
        print("Record Not Found Try Again !")
        return False
        db_cursor.close()
if conn():
    while True:
        print("1--->Enter Customer Details")
        print("2--->Booking Record")
        print("3--->Calculate Room Rent")
        print("4--->Calculate Restaurant Bill")
        print("5--->Calculate Gaming Bill")
        print("6--->Calculate Fashion store Bill")
        print("7--->Display Total Amount")
        print("8--->Display Customer Details")
        print("9--->EXIT")
        choice=input("Enter Your Choice:")
        if choice=='1':
            userEntry()
        elif choice=='2':
            bookingRecord()
        elif choice=='3':
            roomRent()
        elif choice=='4':
            Restaurent()
        elif choice=='5':
            Gaming()
        elif choice=='6':
            Fashion()
        elif choice=='7':
            totalAmount()
        elif choice=='8':
            searchCustomer()
        elif choice=='9':
            break
        else:
            print('Invalid Choice, Please Try Again')
