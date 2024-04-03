
# CONNECTIVITY PROJECT
import mysql.connector as mc

con = mc.connect(host="localhost",
                 user="root", passwd = '123')

c = con.cursor()
c.execute("show databases")
dl = c.fetchall()
dl2 = []
for i in dl:
    dl2.append(i[0])
if 'kaffyn' in dl2:
    sql = "use kaffyn"
    c.execute(sql)
    con.commit()
else:
    sql1 = "create database kaffyn"
    c.execute(sql1)
    sql2 = "use kaffyn"
    c.execute(sql2)
    sql3 = """create table Dish ( Dish varchar(20), Cost integer, Cook varchar(50),
            DishID varchar(20))"""
    c.execute(sql3)
    sql4 = """create table Orders (DishIDs varchar(100), Cost integer, Date
             varchar(20) , Customer varchar(50), phone number Varchar(20))"""
    c.execute(sql4)
    sql5 = """create table Cook (Name varchar(100), phone number varchar(20),
             Dishes varchar(100), Salary integer, DOJ varchar(20))"""
    c.execute(sql5)
    sql6 = """create table Salary (Name varchar(100), phone number varchar(20),Bank
       varchar(20), Month varchar(20), Salary integer, Days integer, Net integer)"""
    c.execute(sql6)
    sql7 = """create table Expenditure (Type varchar(100), Cost integer,
                Date varchar(20))"""
    c.execute(sql7)
    con.commit()

def signin():
    print("\n")
    print("        ---------->>>>>>>>> Welcome <<<<<<<<<--------")
    print("\n")
    print("        ******************** KAFFYN *******************")
    print("                      Taste The Tradition            ")
    print("\n")
    p = input("System Password: ")
    if p == "kaffyn":
        main()
    else:
        signin()


def Dish():
    while True:
        print("1. Add dish")
        print("2. Remove dish")
        print("3. Display dish")
        print("4. Main menu")
        print("5. Exit")
        choice = input("enter number to modify dish: ")
        if choice == '1':
            dn = input("Dish Name : ")
            dc = input("Dish Cost : ")
            Cname()
            cb = input("Cooked By : ")
            did = str(DishID())                             
            data = (dn,dc,cb,did)
            sql = 'insert into Dish values(%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql,data)
            con.commit()
            print("Data Entered Successfully")
        elif choice == '2':
            did = input("Dish ID : ")
            data = (did,)
            sql = 'delete from Dish where DishID = %s'
            c = con.cursor()
            c.execute(sql,data)
            con.commit()
            print("Data Updated Successfully")
        elif choice == '3':
            print("\n")
            sql = "select * from Dish"
            c = con.cursor()
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i[0],"-",i[1],"-",i[2],"-",i[3])
            print("\n")
        elif choice=='4':
            options()
        else:
            print("thank you")


def DishID():
    sql = 'select count(*) , max(dishid) from dish' 
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        if i[0] == 0:
            return(1)
        else:
            return(int(i[1])+1)

def Cname():
    sql = "select Name , Dishes from Cook"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print("<----  Available Cooks ---->")
    for i in d:
        print(i[0],"---",i[1])
    return

 

def Cook():
    while True:
        choice = input("1. Add    2. Remove    3. Display   4. Main Menu  5.exit: ")
        if choice == '1':
            cn = input("Cook Name : ")
            p = int(input("enter phone number : "))
            d = input("Dishes : ")
            s = int(input("Salary : "))
            doj = input("Date of Joining : Y/M/D : ")
            data = (cn,p,d,s,doj)
            sql = 'insert into Cook values(%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql,data)
            con.commit()
            print("Data Entered Successfully")
        elif choice == '2':
            cn = input("Cook Name : ")
            ca = input("Aadhar : ")
            data = (cn,ca)
            sql = 'delete from Cook where Name = %s and Aadhar = %s'
            c = con.cursor()
            c.execute(sql,data)
            con.commit()
            print("Data Updated Successfully")
        elif choice == '3':
            sql = "select * from cook"
            c = con.cursor()
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i[0],"-",i[1],"-",i[2],"-",i[3],"-",i[4])
            print("\n")
        elif choice=='4':
            options()
        else:
            print("thank you")
            

         
 
def PaySalary():
    sql8 = "select * from cook"
    c = con.cursor()
    c.execute(sql8)
    d = c.fetchall()
    for i in d:
        print(i[0],"-",i[1],"-",i[2],"-",i[3],"-",i[4])
        print("---------------------------------------------------------------------")
    cn = input("Cook Name : ")
    ca = input("phone : ")
    ba = input("SBI Account : ")
    mn = input("DATE : Y/M/D : ")
    s = int(input("Salary : "))
    d = int(input("Working days : "))
    if mn[5:7] in ['01','03','05','07','08','10','12']:
        ns = (s/31)*d
    elif mn[5:7] in ['04','06','09','11']:
        ns = (s/30)*d
    else:
        ns = (s/28)*d
    data = (cn,ca,ba,mn,s,d,ns)
    sql = 'insert into Salary values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Net Salary Paid : ",ns,"Rs")
    print("-----------------------------------------------------------------")
    xy = input("1. Salary Menu       2. Main Menu    :  ")
    print("-----------------------------------------------------------------")
    if xy == '1':
        PaySalary()
    elif xy == '2':
        options()
    else:
        options()



def NewOrder():               
    sql = "select * from Dish"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    print("NAME ----- COST ----- COOK ----- DISH ID ")
    for i in d:
        print(i[0],"-",i[1],"-",i[2],"-",i[3])
    print("\n")
    dil = []                                       
    while True:
        di = input("Select Dish ID  { 0 When Done }  : ")    
        if di == '0':
            break
        else:
            dil.append(di)
    sql = "select DishID, Cost from Dish"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    dicl = {}                  
    for i in d:
        dicl[i[0]] = i[1]
    tc = 0
    for i in dil:
        dc = dicl[i]
        tc = tc + dc
    dt = input("Date : Y/M/D :  ")
    cn = input("Customer Name : ")
    ca = input("phone number : ")
    lis = input("Enter Dish IDs : ")                    
    data = (lis,tc,dt,cn,ca) 
    sql = 'insert into Orders values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("--------------kaffyn--------------")
    print("        taste the tradition    ")
    print("************customer bill************")
    print("name:-",cn)
    print("phone number:-",ca)
    print("Total Amount:-",tc,"Rs")
    print("Thank you")
    print("-----------------------------------------------------------------")
    xy = input("1. new order  2.exit  :  ")
    print("-----------------------------------------------------------------")
    if xy == '1':
        NewOrder()
    else:
        print("thank you")

  




def NetIncome():
    while True:
        c = con.cursor()
        t = input("1. All     2. Year    3. Month   4. Date   5. Main Menu  6. exit ")
        if t == '1':
            sql = 'select Cost from Orders'
            c.execute(sql)
            d = c.fetchall()
            oi = 0                                             
            for i in d:
                oi = oi + i[0]
            print("Total Income from Orders : ",oi,"Rs")
        elif t == '2':
            y = input("Enter Year : ")
            sql = 'select Cost , Date from Orders'
            c.execute(sql)
            d = c.fetchall()
            oi = 0
            for i in d:
                if y in i[1]:
                    oi = oi + i[0]
            print("Total Income from Orders : ",oi,"Rs")
        elif t == '3':
            my = input("Enter Year/Month : ")
            sql = 'select Cost , Date from Orders'
            c.execute(sql)
            d = c.fetchall()
            oi = 0
            for i in d:
                if my in i[1]:
                    oi = oi + i[0]
                print("Total Income from Orders : ",oi,"Rs")
        elif t == '4':
            y = input("Enter Y/M/D : ")
            sql = 'select Cost from Orders where Date like %s'
            data = (y,)
            c.execute(sql,data)
            d = c.fetchall()
            oi = 0                                              
            for i in d:
               oi = oi + i[0]
            print("Total Income from Orders : ",oi,"Rs")
        elif t=='5':
            options()
        else:
            break

              

def Expenditure():
    choice = input("1. BILL ENTRY       2. SHOW BILLS     3. Main Menu  4.Thank you : ")
    if choice == '1':
        sql = "select dish , cost from dish"
        c = con.cursor()
        c.execute(sql)
        d = c.fetchall()
        for i in d:
            print(i)
        t = input("dish name : ")
        c = int(input("Cost : "))
        d = input("Date : Y/M/D : ")
        data = (t,c,d)
        sql = 'insert into Expenditure values(%s,%s,%s)'
        c = con.cursor()
        c.execute(sql,data)
        con.commit()
        print("")
        options()
    elif choice == '2':
        c = con.cursor()
        t = input("1. All     2. Year    3. Month   4. Date  : ")
        if t == '1':
            sql = 'select * from Expenditure'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                print(i)
        elif t == '2':
            y = input("Enter Year : ")
            sql = 'select * from Expenditure'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
        elif t == '3':
            y = input("Enter : YEAR/MONTH : ")
            sql = 'select * from Expenditure'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
        elif t == '4':
            y = input("Enter Date : ")
            sql = 'select * from Expenditure'
            c.execute(sql)
            d = c.fetchall()
            for i in d:
                if y in i[2]:
                    print(i)
    elif t=='3':
        options()

    else:
        print("thank you")

def owner():
    print("""                                1.  modify DISHES 
                                2.  modify COOKS
                                3.  to show salary 
                        	4.  total earning
                        	5.  generate bills """)
    choice = input("Select Option : ")
    if (choice == '1'): 
        Dish()
    elif (choice=='2'):
        Cook()
    elif (choice=='3'): 
        PaySalary() 
    elif (choice=='4'): 
        NetIncome()
    elif (choice=='5'):
        Expenditure()
    else:
        print(" Wrong choice..........")

def main():
    print("1.login as admin ")
    print("2.login as customer ")
    ch=int(input("enter the way you want to login:  "))
    if ch==1:
        owner()
    elif ch==2:
        NewOrder()
    else:
        print("thank you")
        
signin()

#***************** THANK YOU ****************
