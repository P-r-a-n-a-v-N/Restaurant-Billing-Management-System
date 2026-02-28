import mysql.connector as m # importing python - mysql connector module
import datetime # to get date and time
# connecting python to mysql
C=m.connect(host="localhost",user="root",passwd="1234")
c=C.cursor()
c.execute("drop database if exists project")
c.execute("create database if not exists project")
c.execute("Use project")

# password table
c.execute("create table if not exists password(mode varchar(6),pass_word varchar(12))")
c.execute("insert into password values('admin','admin@2023')")
c.execute("insert into password values('user','user@2023')")

# employee table
c.execute("create table if not exists Empl(Empid varchar(5) primary key, Ename char(20),gender char(1),desig varchar(20), salary varchar(20), email varchar(40), phno varchar(16))")
c.execute("create table Empl(Empid varchar(5) primary key, Ename char(20), username varchar(30), passwd varchar(29),up varchar(1),desig varchar(20), salary (in Rs) int, email varchar(20), phno char(16))")
c.execute("insert into Empl values('E1','Adarsh','adarsh','adarsh@2007','U','Assistant Manager',800000,'adharsh@gmail.com','+91 9200394867')")
c.execute("insert into Empl values('E2','Anish','anish','anish@2007','A','Co-Founder',30000000,'anish2007@gmail.com','+91 9500394867')")
c.execute("insert into Empl values('E3','Arul','arul','arul@2006','U','Manager',1000000,'arul@gmail.com','+91 9900394867')")
c.execute("insert into Empl values('E4','Pranav','pranav','pranav@2006','A','Co-Founder',5000000,'pranavneelu06@gmail.com','+91 9990394867')")
c.execute("insert into Empl values('E5','Kedharanathan','kedhar','kedhar@2006','Founder','A',5000000,'kedharanathancr@gmail.com,'+91 99443848333')")
c.execute("insert into Empl values('E6','Sanjay','sanjay','sanjay@2006','U','Sales Manager',100000,'sanjay@gmail.com','+91 9900394867')")
c.execute("insert into Empl values('E7','Ramkumar','ramkumar','ramkumar@2006','U','Marketing Manager',100000,'ramkumar@gmail.com','+91 9900392467')")
c.execute("insert into Empl values('E8','Sathish','sathish','sathish@2006','U','Marketing Manager',100000,'sathish@gmail.com','+91 9300392467')")

# menu table 
c.execute("Drop table if exists menu")
c.execute("create table if not exists menu(itemid varchar(4) primary key,itemname varchar(100),price varchar(10),variety char(15),v_nv char(3))")
c.execute("insert into menu values('V1','Rava Kesari','₹75.00','sweet','v')")
c.execute("insert into menu values('V2','Carrot Halwa','₹65.00','sweet','v')")
c.execute("insert into menu values('V3','Bread Halva','₹70.00','sweet','v')")
c.execute("insert into menu values('V4','Kashi Halva','₹70.00','sweet','v')")
c.execute("insert into menu values('V5','Mysore Pak (3pcs)','₹70.00','sweet','v')")
c.execute("insert into menu values('V6','Badhushah (3pcs)','₹65.00','sweet','v')")
c.execute("insert into menu values('V7','Fresh Cream Tomato Soup','₹120.00','soup','v')")
c.execute("insert into menu values('V8','Sweet Corn Soup','₹100.00','soup','v')")
c.execute("insert into menu values('V9','Mushroom Soup','₹85.00','soup','v')")
c.execute("insert into menu values('V10','Hot And Pepper','₹100.00','soup','v')")
c.execute("insert into menu values('N1','French Onion(Chicken)','₹125.00','soup','nv')")
c.execute("insert into menu values('N2','Garlic Chicken Soup','₹120.00','soup','nv')")
c.execute("insert into menu values('N3','Hot And Sour Loabster Soup','₹130.00','soup','nv')")
c.execute("insert into menu values('N4','Mutton Pepper Soup','₹110.00','soup','nv')")
c.execute("insert into menu values('N5','Crab Soup','₹150.00','soup','nv')")
c.execute("insert into menu values('V11','Gobi 65','₹120.00','starter','v')")
c.execute("insert into menu values('V12','Panner Tikka','₹125.00','starter','v')")
c.execute("insert into menu values('V13','Mushroom Tikka','₹130.00','starter','v')")
c.execute("insert into menu values('V14','Gobi Manchurian','₹125.00','starter','v')")
c.execute("insert into menu values('V15','Honey Potato','₹120.00','sweet','v')")
c.execute("insert into menu values('V16','Panner 65','₹120.00','starter','v')")
c.execute("insert into menu values('N6','Chicken 65','₹150.00','starter','nv')")
c.execute("insert into menu values('N7','chicken 88','₹190.00','starter','nv')")
c.execute("insert into menu values('N8','chicken 007','₹210.00','starter','nv')")
c.execute("insert into menu values('N9','Chicken Tikka','₹150.00','starter','nv')")
c.execute("insert into menu values('N10','Chicken Tandoori','₹150.00','starter','nv')")
c.execute("insert into menu values('N11','Honey Chicken','₹125.00','starter','nv')")
c.execute("insert into menu values('N12','Crab Lollipop','₹165.00','starter','nv')")
c.execute("insert into menu values('N13','Fish Fingers','₹170.00','starter','nv')")
c.execute("insert into menu values('N14','Golden Prawn','₹190.00','starter','nv')")
c.execute("insert into menu values('N15','Grilled Fish','₹150.00','starter','nv')")
c.execute("insert into menu values('N16','Fish 65','₹150.00','starter','nv')")
c.execute("insert into menu values('N17','Grill Chicken','₹250.00','starter','nv')")
c.execute("insert into menu values('V17','Dosa','₹40.00','maindish','v')")
c.execute("insert into menu values('V18','Idli(2 pcs)','₹25.00','maindish','v')")
c.execute("insert into menu values('V19','Ghee Roast','₹50.00','maindish','v')")
c.execute("insert into menu values('V20','Masal Dosa','₹65.00','maindish','v')")
c.execute("insert into menu values('V21','Podi Dosa','₹55.00','maindish','v')")
c.execute("insert into menu values('V22','Mushroom Dosa','₹65.00','maindish','v')")
c.execute("insert into menu values('V23','Panneer Dosa','₹65.00','maindish','v')")
c.execute("insert into menu values('V24','Onion Dosa','₹60.00','maindish','v')")
c.execute("insert into menu values('V25','Upma','₹40.00','maindish','v')")
c.execute("insert into menu values('V26','Idiyappam','₹50.00','maindish','v')")
c.execute("insert into menu values('V27','Pongal','₹55.00','maindish','v')")
c.execute("insert into menu values('N18','Chicken Dosa','₹70.00','maindish','nv')")
c.execute("insert into menu values('N19','Mutton Dosa','₹90.00','maindish','nv')")
c.execute("insert into menu values('N20','Prawn Dosa','₹120.00','maindish','nv')")
c.execute("insert into menu values('V28','Phulka','₹40.00','roti','v')")
c.execute("insert into menu values('V29','Chappati','₹25.00','roti','v')")
c.execute("insert into menu values('V30','Naan','₹40.00','roti','v')")
c.execute("insert into menu values('V31','Butter Naan','₹50.00','roti','v')")
c.execute("insert into menu values('V32','Paratha','₹20.00','roti','v')")
c.execute("insert into menu values('V33','Tandoori Roti','₹50.00','roti','v')")
c.execute("insert into menu values('V34','Panneer Butter Masala','₹165.00','gravy','v')")
c.execute("insert into menu values('V35','Mushroom Gravy','₹150.00','gravy','v')")
c.execute("insert into menu values('V36','Babycorn Gravy','₹170.00','gravy','v')")
c.execute("insert into menu values('V37','Malai Cofta (Red/White)','₹190.00','gravy','v')")
c.execute("insert into menu values('V38','Dal Makhini','₹150.00','gravy','v')")
c.execute("insert into menu values('V39','Panneer Lababdar','₹190.00','gravy','v')")
c.execute("insert into menu values('V40','Palak Panneer','₹175.00','gravy','v')")
c.execute("insert into menu values('V41','Mixed Veggie Gravy','₹150.00','gravy','v')")
c.execute("insert into menu values('V42','Mixed Fruits And Veggie Gravy','₹180.00','gravy','v')")
c.execute("insert into menu values('N21','Butter Chicken','₹180.00','gravy','nv')")
c.execute("insert into menu values('N22','Chettinad Chicken','₹190.00','gravy','nv')")
c.execute("insert into menu values('N23','Kadai Chicken','₹170.00','gravy','nv')")
c.execute("insert into menu values('V43','Curd Rice','₹45.00','rice','v')")
c.execute("insert into menu values('V44','Sambar Rice','₹55.00','rice','v')")
c.execute("insert into menu values('V45','Dal Rice','₹50.00','rice','v')")
c.execute("insert into menu values('V46','Rasam Rice','₹45.00','rice','v')")
c.execute("insert into menu values('V47','Podi Rice','₹50.00','rice','v')")
c.execute("insert into menu values('V48','Friedrice','₹120.00','rice','v')")
c.execute("insert into menu values('V49','Baby Corn Friedrice','₹135.00','rice','v')")
c.execute("insert into menu values('V50','Panneer Friedrice','₹170.00','rice','v')")
c.execute("insert into menu values('V51','Mushroom Friedrice','₹150.00','rice','v')")
c.execute("insert into menu values('N24','Chicken Gravy Rice','₹150.00','rice','nv')")
c.execute("insert into menu values('N25','Mutton Gravy Rice','₹165.00','rice','nv')")
c.execute("insert into menu values('N26','Prawn Thokku Rice','₹150.00','rice','nv')")
c.execute("insert into menu values('N27','Fish Gravy Rice','₹150.00','rice','nv')")
c.execute("insert into menu values('N28','Chicken Fried Rice','₹210.00','rice','nv')")
c.execute("insert into menu values('N29','Mutton Fried rice','₹230.00','rice','nv')")
c.execute("insert into menu values('N30','Prawn Fried rice','₹250.00','rice','nv')")
c.execute("insert into menu values('V52','Paneer Biriyani','₹190.00','biriyani','v')")
c.execute("insert into menu values('V53','Mushroom Biriyani','₹150.00','biriyani','v')")
c.execute("insert into menu values('V54','Plain Biriyani','₹135.00','biriyani','v')")
c.execute("insert into menu values('N31','Chicken Biriyani','₹170.00','biriyani','nv')")
c.execute("insert into menu values('N32','Mutton Biriyani','₹210.00','biriyani','nv')")
c.execute("insert into menu values('N33','Prawn Biriyani','₹210.00','biriyani','nv')")
c.execute("insert into menu values('N34','Egg Omlette','₹15.00','sidedish','nv')")
c.execute("insert into menu values('N35','Egg Kalaki','₹20.00','sidedish','nv')")
c.execute("insert into menu values('N36','Halfboil','₹20.00','sidedish','nv')")
c.execute("insert into menu values('V55','Gulab Jamoon','₹60.00','desert','v')")
c.execute("insert into menu values('V56','Panner Jamoon','₹65.00','desert','v')")
c.execute("insert into menu values('V57','Butter scotch (3 Scoops)','₹60.00','desert','v')")
c.execute("insert into menu values('V58','Chocolate (3 Scoops)','₹55.00','desert','v')")
c.execute("insert into menu values('V59','Vanilla (3 Scoops)','₹50.00','desert','v')")
c.execute("insert into menu values('V60','Strawberry (3 scoops)','₹55.00','desert','v')")
c.execute("insert into menu values('V61','Cranberry (3 scoops)','₹55.00','desert','v')")
c.execute("insert into menu values('V62','Blueberry (3 scoops)','₹55.00','desert','v')")
c.execute("insert into menu values('V63','Black Current (3 scoops)','₹55.00','desert','v')")
c.execute("insert into menu values('V64','Coffee Choco Crunch (3 scoops)','₹55.00','desert','v')")
c.execute("insert into menu values('V65','Chocolate Milkshake','₹110.00','desert','v')")
c.execute("insert into menu values('V66','Strawberry Milkshake','₹110.00','desert','v')")
c.execute("insert into menu values('V67','Coffee Milkshake','₹110.00','desert','v')")
c.execute("insert into menu values('V68','Butter Scotch Milkshake','₹130.00','desert','v')")
c.execute("insert into menu values('V69','Blueberry Milkshake','₹150.00','desert','v')")
c.execute("insert into menu values('V70','Vnilla Milkshake','₹110.00','desert','v')")
c.execute("insert into menu values('V71','Black Current Milkshake','₹120.00','desert','v')")
c.execute("insert into menu values('V72','Fruit Falooda','₹110.00','desert','v')")
c.execute("insert into menu values('V73','Degeree Coffee','₹45.00','hot beverages','v')")
c.execute("insert into menu values('V74','Caramel Coffee','₹65.00','hot beverages','v')")
c.execute("insert into menu values('V75','Butter Coffee','₹55.00','hot beverages','v')")
c.execute("insert into menu values('V76','Cappuccino','₹60.00','hot beverages','v')")
c.execute("insert into menu values('V77','Espresso','₹60.00','hot beverages','v')")
c.execute("insert into menu values('V78','Indian Chai','₹45.00','hot beverages','v')")
c.execute("insert into menu values('V79','Butter Chai','₹65.00','hot beverages','v')")
c.execute("insert into menu values('V80','Masala Chai','₹65.00','hot beverages','v')")
c.execute("insert into menu values('V81','Hot Chocholate','₹50.00','hot beverages','v')")

# customer table 
c.execute("create table if not exists customer(cname char(20),cph varchar(15) primary key,caddress varchar(45),cpoints int,cemail char(40))")
c.execute("insert into customer values('Adarsh','+91 7586942130','25,kamaraj nagar,chennai-600028',0,'adar2007@gmail.com')")
c.execute("insert into customer values('Arul','+91 9874562565','321,main street,vandalur-602324',0,'arulanandha@gmail.com')")
c.execute("insert into customer values('jagan','+91 8025654789','3B,nehru nagar,keelpakkam-601235',0,'jaganmani@gmail.com')")
c.execute("insert into customer values('Marwan','+91 9847542580','17,jaganmahan street,chennai=600025',0,'Maru@gmail.com')")

# sales report
c.execute("create table if not exists Sales_Report(bill_no varchar(30),date varchar(10),time varchar(10),id varchar(5), dish varchar(30),cost varchar(10),quantity int,price varchar(12))")


# header
print()
print()
print()
Header="""                              WELLCOME TO
                                          SREE PRANAVA BALAJI BHAVAN
                                                                     -By KPA Groups"""
print("-"*(len(Header)-87))
print("-"*(len(Header)-87))
print(Header)
print("-"*(len(Header)-87))
print("-"*(len(Header)-87))
print()
print()
print()
                            


while True:

    # choosing profile
    P=input("Enter 'C' if you are customer and 'E' if you are employee : ")
    print()
    print()

    if P=='E' or P=='C':
        
# employee profile 
        if P=="E":
            c.execute("select * from password")
            pt=c.fetchall()
            uA=pt[0][0]
            pA=pt[0][1]
            u=pt[1][0]
            p=pt[1][1]
# checking mode of employee
            while True:
                u1=input("Enter User id : ")
                print()
                p1=input("Enter user password : ")
                print()
                print()
# admin mode
                if (u1==uA or u1==u) and (p1==pA or p1==p) :
                    if u1==uA and p1==pA:
                        while True:
# choosing admin options 
                            print("""Admin options:
                                                    V: View All The Emplyees
                                                    A: Add Employee
                                                    E: Edit Employee
                                                    D: Delete Employee
                                                    S: View Sales Report""")
                            print()
                            print()
                            o=input("Enter the options : ")
                            print()
                            print()

# view of all employees
                            if o=="V":
                                print("Employees : ")
                                print()
                                c.execute("Select * from empl")
                                r=c.fetchall()
                                e_column_names = ["ID","Name","Gender","Designation","Salary","Email","Phone no"]
                                e_col="| {:5} | {:13} | {:6} | {:25} | {:8} | {:25} | {:14} |".format(*e_column_names)
                                print("+"+"-"*(len(e_col)-2)+"+")
                                print(e_col)
                                print("+"+"-"*(len(e_col)-2)+"+")
                                for row in r:
                                    print("| {:5} | {:13} | {:6} | {:25} | {:8} | {:25} | {:14} |".format(*row))
                                print("+"+"-"*(len(e_col)-2)+"+")
                                print()
                                print()

# adding new employees
                            elif o=="A":
                                while True:
                                    e_id=input("Enter employee id : ")
                                    print()
                                    n=input("Enter the name : ").lstrip().rstrip()
                                    print()
                                    g=input("Enter the gender : ").lstrip().rstrip()
                                    print()
                                    d=input("Enter the designation : ").lstrip().rstrip()
                                    print()
                                    s=int(input("Enter the salary : "))
                                    s='₹'+str(s)
                                    print()
                                    em=input("Enter email : ")
                                    print()
                                    print("Enter mobile number (with country code : ")
                                    cc=input("Enter country code : ").lstrip().rstrip()
                                    mn=input("Enter mobile number : ").lstrip().rtsrip()
                                    ph=cc+mn
                                    print()
                                    c.execute("insert into empl values('{}','{}','{}','{}',{},'{}','{}')".format(e_id,n,g,d,s,em,ph))
                                    print("! The entered new record is added successfully !")
                                    print()
                                    print()
                                    ch=input('Do you wish to continue in adding records of new employees ? (y/n) : ')
                                    if ch=='n':
                                        print()
                                        print()
                                        break
                                    elif ch=='y':
                                        print()
                                        print()
                                        continue

# edditing current employees' details
                            elif o=="E":
                                while True:
                                    e_id=input("Enter employee id : ")
                                    print()
                                    while True:
                                        print("""Constraints :
                                                                n: Name
                                                                d: Designation
                                                                s: Salary
                                                                em: Email
                                                                ph: Phone number""")
                                        print()
                                        co=input("Enter the desired constraints to be changed : ")
                                        print()
                                        if co=="n":
                                            n=input("Enter the new name : ")
                                            print()
                                            c.execute("Update empl set ename='{}' where empid='{}'".format(n,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="d":
                                            d=input("Enter the new designation : ")
                                            print()
                                            c.execute("Update empl set desig='{}' where empid='{}'".format(d,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="s":
                                            s=input(int("Enter the new salary : "))
                                            s='₹'+str(s)
                                            print()
                                            c.execute("Update empl set salary='{}' where empid='{}'".format(s,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="em":
                                            em=input("Enter the new email : ")
                                            print()
                                            c.execute("Update empl set email='{}' where empid='{}'".format(em,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="ph":
                                            ph=input("Enter the new phone number : ")
                                            print()
                                            c.execute("Update empl set phno='{}' where empid='{}'".format(ph,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                        ch=input('Do you wish to continue editting this employee record ? (y/n) : ')
                                        if ch=='n':
                                            print()
                                            print()
                                            break
                                        elif ch=='y':
                                            print()
                                            print()
                                            continue
                                    ch=input('Do you wish to continue in editting records of employees ? (y/n) : ')
                                    if ch=='n':
                                        print()
                                        print()
                                        break
                                    elif ch=='y':
                                        print()
                                        print()
                                        continue

# deleting employees
                            elif o.upper()=="D":
                                while True:
                                    e_id=input("Enter employee id : ")
                                    print()
                                    c.execute("delete empl where empid='{}'".format(e_id))
                                    print("! The record is deleted successfully !")
                                    print()
                                    print()
                                    ch=input('Do you wish to continue in deleting records of employees ? (y/n) : ')
                                    if ch=='n':
                                        print()
                                        print()
                                        break
                                    elif ch=='y':
                                        print()
                                        print()
                                        continue

# sales report
                            elif o=="S":
                                while True:
                                    O=input("Enter 'V' to view all sales report and 'S' to view with specifications : ")
                                    print()
                                    print()
                                    if O=='V':
                                        c.execute('Select * from sales_Report')
                                        r=c.fetchall()
                                        column_names = ["Bill Number","Date","Time","ID","Dishes","Cost","Quantity","Price"]
                                        col="| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:6} | {:7} |".format(*column_names)
                                        print("+"+"-"*(len(col)-2)+"+")
                                        print(col)
                                        print("+"+"-"*(len(col)-2)+"+")
                                        for row in r:
                                            print("| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:8} | {:7} |".format(*row))
                                            print("+"+"-"*(len(col)-2)+"+")
                                        print()
                                        print()
                                    elif O=='S':
                                        while True:
                                            date=input("Enter date (in proper format or it causes error !) to view sales details : ")
                                            print()
                                            print()
                                            r=c.fetchall()
                                            if r:
                                                c.execute('Select * from sales_Report')
                                                r=c.fetchall()
                                                column_names = ["Bill Number","Date","Time","ID","Dishes","Cost","Quantity","Price"]
                                                col="| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:6} | {:10} |".format(*column_names)
                                                print("+"+"-"*(len(col)-2)+"+")
                                                print(col)
                                                print("+"+"-"*(len(col)-2)+"+")
                                                for row in r:
                                                    print("| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:6} | {:10} |".format(*row))
                                                    print("+"+"-"*(len(e_col)-2)+"+")
                                                print()
                                                print()
                                            else:
                                                print("SORRY, WRONG INPUT !!!")
                                                print("ENTER CORRECT VALUES !!!")
                                                print()
                                                print()
                                                continue
                                    else:
                                        print("SORRY, WRONG INPUT !!!")
                                        print("ENTER CORRECT VALUES !!!")
                                        print()
                                        print()
                                        continue
                                    ch=input('Do you wish to continue viewing Sales Report ? (y/n) : ')
                                    if ch=='n':
                                        print()
                                        print()
                                        break
                                    elif ch=='y':
                                        print()
                                        print()
                                        continue
                                                                                        
                            ch=input('Do you wish to continue to be in admin account ? (y/n) : ')
                            if ch=='n':
                                print()
                                print()
                                break
                            elif ch=='y':
                                print()
                                print()
                                continue


# normal user mode
                    elif u1==u and p1==p:
# user options 
                        while True:
                            print("""User options:
                                                    V: View All The Emplyees
                                                    A: Add Employee
                                                    E: Edit Employee
                                                    S: View Sales Report""")
                            print()
                            print()
                            o=input("Enter the options : ")
                            print()
                            print()

# view of all employees
                            if o=="V":
                                print("Employees : ")
                                print()
                                c.execute("Select * from empl")
                                r=c.fetchall()
                                e_column_names = ["ID","Name","Gender","Designation","Salary","Email","Phone no"]
                                e_col="| {:5} | {:13} | {:6} | {:25} | {:8} | {:25} | {:14} |".format(*e_column_names)
                                print("+"+"-"*(len(e_col)-2)+"+")
                                print(e_col)
                                print("+"+"-"*(len(e_col)-2)+"+")
                                for row in r:
                                    print("| {:5} | {:13} | {:6} | {:25} | {:8} | {:25} | {:14} |".format(*row))
                                print("+"+"-"*(len(e_col)-2)+"+")
                                print()
                                print()

# adding new employees
                            elif o=="A":
                                while True:
                                    e_id=input("Enter employee id : ")
                                    print()
                                    n=input("Enter the name : ").lstrip().rstrip()
                                    print()
                                    g=input("Enter the gender : ").lstrip().rstrip()
                                    print()
                                    d=input("Enter the designation : ").lstrip().rstrip()
                                    print()
                                    s=int(input("Enter the salary : "))
                                    s='₹'+str(s)
                                    print()
                                    em=input("Enter email : ")
                                    print()
                                    print("Enter mobile number (with country code : ")
                                    cc=input("Enter country code : ").lstrip().rstrip()
                                    mn=input("Enter mobile number : ").lstrip().rtsrip()
                                    ph=cc+mn
                                    print()
                                    c.execute("insert into empl values('{}','{}','{}','{}',{},'{}','{}')".format(e_id,n,g,d,s,em,ph))
                                    print("! The entered new record is added successfully !")
                                    print()
                                    print()
                                    ch=input('Do you wish to continue in adding records of new employees ? (y/n) : ')
                                    if ch=='n':
                                        print()
                                        print()
                                        break
                                    elif ch=='y':
                                        print()
                                        print()
                                        continue

# edditing current employees' details
                            elif o=="E":
                                while True:
                                    e_id=input("Enter employee id : ")
                                    print()
                                    while True:
                                        print("""Constraints :
                                                                n: Name
                                                                d: Designation
                                                                s: Salary
                                                                em: Email
                                                                ph: Phone number""")
                                        print()
                                        co=input("Enter the desired constraints to be changed : ")
                                        print()
                                        if co=="n":
                                            n=input("Enter the new name : ")
                                            print()
                                            c.execute("Update empl set ename='{}' where empid='{}'".format(n,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="d":
                                            d=input("Enter the new designation : ")
                                            print()
                                            c.execute("Update empl set desig='{}' where empid='{}'".format(d,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="s":
                                            s=input(int("Enter the new salary : "))
                                            s='₹'+str(s)
                                            print()
                                            c.execute("Update empl set salary='{}' where empid='{}'".format(s,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="em":
                                            em=input("Enter the new email : ")
                                            print()
                                            c.execute("Update empl set email='{}' where empid='{}'".format(em,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                            print()
                                        elif co=="ph":
                                            ph=input("Enter the new phone number : ")
                                            print()
                                            c.execute("Update empl set phno='{}' where empid='{}'".format(ph,e_id))
                                            print("! The edited new record is added successfully !")
                                            print()
                                        ch=input('Do you wish to continue editting this employee record ? (y/n) : ')
                                        if ch=='n':
                                            print()
                                            print()
                                            break
                                        elif ch=='y':
                                            print()
                                            print()
                                            continue
                                    ch=input('Do you wish to continue in editting records of employees ? (y/n) : ')
                                    if ch=='n':
                                        print()
                                        print()
                                        break
                                    elif ch=='y':
                                        print()
                                        print()
                                        continue

# sales report
                            elif o=="S":
                                while True:
                                    O=input("Enter 'V' to view all sales report and 'S' to view with specifications : ")
                                    print()
                                    print()
                                    if O=='V':
                                        c.execute('Select * from sales_Report')
                                        r=c.fetchall()
                                        column_names = ["Bill Number","Date","Time","ID","Dishes","Cost","Quantity","Price"]
                                        col="| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:6} | {:7} |".format(*column_names)
                                        print("+"+"-"*(len(col)-2)+"+")
                                        print(col)
                                        print("+"+"-"*(len(col)-2)+"+")
                                        for row in r:
                                            print("| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:6} | {:7} |".format(*row))
                                            print("+"+"-"*(len(col)-2)+"+")
                                        print()
                                        print()
                                    elif O=='S':
                                        while True:
                                            date=input("Enter date (in proper format or it causes error !) to view sales details : ")
                                            print()
                                            print()
                                            r=c.fetchall()
                                            if r:
                                                c.execute('Select * from sales_Report')
                                                r=c.fetchall()
                                                column_names = ["Bill Number","Date","Time","ID","Dishes","Cost","Quantity","Price"]
                                                col="| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:6} | {:10} |".format(*column_names)
                                                print("+"+"-"*(len(col)-2)+"+")
                                                print(col)
                                                print("+"+"-"*(len(col)-2)+"+")
                                                for row in r:
                                                    print("| {:30} | {:10} | {:5} | {:5} | {:30} | {:7} | {:8} | {:10} |".format(*row))
                                                    print("+"+"-"*(len(col)-2)+"+")
                                                print()
                                                print()
                                            else:
                                                print("SORRY, RECORD NOT FOUND !!!")
                                                print("ENTER CORRECT VALUES !!!")
                                                print()
                                                print()
                                                continue
                                    else:
                                        print("SORRY, WRONG INPUT !!!")
                                        print("ENTER CORRECT VALUES !!!")
                                        print()
                                        print()
                                        continue
                                    ch=input('Do you wish to continue viewing Sales Report ? (y/n) : ')
                                    if ch=='n':
                                        print()
                                        print()
                                        break
                                    elif ch=='y':
                                        print()
                                        print()
                                        continue


                            ch=input('Do you wish to continue to be in user account ? (y/n) : ')
                            if ch=='n':
                                print()
                                print()
                                break
                            elif ch=='y':
                                continue
                else:
                    print("!!! SORRY PLEASE ENTER CORRECT USER ID AND PASSWORD !!!")
                    print()
                    print()
                    continue
                ch=input('Do you wish to continue to be in employee profile ? (y/n) : ')
                if ch=='n':
                    print()
                    print()
                    break
                elif ch=='y':
                    print()
                    print()
                    continue

# Customer profile
        elif P=="C":
# printing menu
            print("    Vegitarian : ")
            print()
            print("       Starters - Sweets : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'sweet' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()        
            print("       Starters - Soups : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'soup' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()        
            print("       Starters - Main : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'starter' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - South Indian: ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'maindish' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Indian Breads : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'roti' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Rice Specials : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'rice' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Gravy : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'gravy' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Biryani : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'biriyani' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Desserts : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'desert' and v_nv = 'v'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print()
            print("    Non - Vegitarian (Including Vegetarian) : ")
            print()
            print("       Starters - Sweets : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'sweet'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print() 
            print("       Starters - Soups : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'soup'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print() 
            print("       Starters - Main : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'starter'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - South Indian: ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'maindish'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Indian Breads : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'roti'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Rice Specials : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'rice'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Gravy : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'gravy'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Biryani : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'biriyani'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print("       Mains - Desserts : ")
            print()
            c.execute("Select itemid,itemname,price as 'ID','Dishes','Price' from menu where variety = 'desert'")
            menu=c.fetchall()
            m_column_names = ['ID','Dishes','Price']
            m_col="| {:5} | {:30} | {:7} |".format(*m_column_names)
            print("+"+"-"*(len(m_col)-2)+"+")
            print(m_col)
            print("+"+"-"*(len(m_col)-2)+"+")
            for row in menu:
                print("| {:5} | {:30} | {:7} |".format(*row))
            print("+"+"-"*(len(m_col)-2)+"+")
            print()
            print()


#billing

            now = datetime.datetime.now()    # for generating unique bill no
            now_=str(now)
            date=now_[:10]
            time=now_[11:16]
            l=now_.split()
            char='bill'+l[0][0:4]+'_'+l[0][5:7]+'_'+l[0][8:]+'__'+l[1][:2]+'_'+l[1][3:5]+'_'+l[1][6:8]
            total=0
            TOTAL=[]
            while True:                
                code=input("Enter the code to order the food : ")
                print()
                c.execute("Select itemname, price from menu where itemid = '{}'".format(code))
                list1=c.fetchall()
                if list1:
                    price=float(list1[0][1][1:])
                    dish=list1[0][0]
                    cp="₹"+str(price)+"0"
                    q=int(input("Enter the quantity : "))
                    print()
                    print()
                    ch=input("Are you sure of the quantity ? If you wish to change the quantity enter y or else enter n : ")
                    if ch=='n':
                        pass
                    elif ch=='y':
                        q=int(input("Enter the new quantity : ")) 
                    total+=price*q
                    sp='₹'+str(price*q)+'0'
                    c.execute("insert into Sales_report values('{}','{}','{}','{}','{}','{}',{},'{}')".format(char,date,time,code,dish,cp,q,sp))
                    print()
                    print()
                    ch=input('Do you wish to continue ordering ? (y/n) : ')
                    print()
                    if ch=='n':
                        print()
                        print()
                        break
                    elif ch=='y':
                        print()
                        print()
                        continue
                else:
                    print()
                    print()
                    print("Sorry wrong input !!! Please enter correct code !!!")
                    print()
                    print()
                    continue
            Tot_str="₹"+str(total)+"0"
            TOTAL.append(Tot_str)

# for customer points
            print("Enter your mobile number with country code without leading and trailing spaces : ")
            print()
            print()
            code_=input("Enter country code with '+' leading : ")
            print()
            mn_=input("Enter your number : ")
            print()
            print()
            ph_no=code_+mn_
            c.execute("Select cname, cpoints from customer where cph = '{}' ".format(ph_no))
            list2=c.fetchall()
            if list2 :
                cpoints=int(list2[0][1])
                if total>=10000:
                    cpoints+=100
                    c.execute("update customer set cpoints = {} where cph = '{}' ".format(cpoints,ph_no))
                elif total>=1000 and total<10000:
                    cpoints+=50
                    c.execute("update customer set cpoints = {} where cph = '{}' ".format(cpoints,ph_no))
                elif total>=500 and total<1000:
                    cpoints+=10
                    c.execute("update customer set cpoints = {} where cph = '{}' ".format(cpoints,ph_no))
                elif total<500:
                    cpoints+=1
                    c.execute("update customer set cpoints = {} where cph = '{}' ".format(cpoints,ph_no))
# for printing bill
                print()
                print()
                b=input("Would you like to print the bill ? (y/n) : ")
                print()
                print()
                if b=="y":
                    print("    Bill : ")
                    print()
                    title=['     SREE PRANAVA BALAJI BHAVAN  (a Kedharanahan Groups of company) ']
                    c.execute("Select id,dish,cost,quantity,price from sales_report")
                    Bill=c.fetchall()
                    b_column_names = ['ID','Dishes','Cost','Quantity','Price']
                    b_col="| {:5} | {:30} | {:7} | {:6} | {:10} |".format(*b_column_names)
                    print("+"+"-"*(len(b_col)-2)+"+")
                    print("| {:72} |".format(*title))
                    print("+"+"-"*(len(b_col)-2)+"+")
                    print("| {:72} |".format(char))
                    print("+"+"-"*(len(b_col)-2)+"+")
                    print(b_col)
                    print("+"+"-"*(len(b_col)-2)+"+")
                    for row in Bill:
                        print("| {:5} | {:30} | {:7} | {:8} | {:10} |".format(*row))
                        print("+"+"-"*(len(b_col)-2)+"+")
                    print("|                                                  |  TOTAL : | {:10} |".format(*TOTAL))
                    print("+"+"-"*(len(b_col)-2)+"+")
                    print()
                    print()
                    if cpoints>=1000:
                        print("Congrats!!! You are rewarded with a gift voucher of ₹500 with which you can claim in any of our branch !!!")
                        print()
                        print()
                    elif cpoint>=500 and cpoints<1000:
                        print("Congrats!!! You are rewarded with a gift voucher of ₹100 with which you can claim in any of our branch !!!")
                        print()
                        print()
                    elif cpoint>=100 and cpoints<500:
                        print("Congrats!!! You are rewarded with a gift voucher of ₹50 with which you can claim in any of our branch !!!")
                        print()
                        print()
            else:
                print("It seems you are a new customer...")
                ch=input("Do you wish to join our premium customer membership with which you will be rewarded gift vouchers according to your points every time you visit ? (y/n) : ")
                print()
                if ch=='y':
                    n=input("Enter your name : ")
                    a=input("Enter your address : ")
                    m=input("Enter your email address : ")
                    list3=[n,ph_no,a,0,m]
                    c.execute("insert into customer values('{}','{}','{}',{},'{}')".format(*list3))
                    print()
                    print("!!! Thank you for joining our membership !!!")
                    print()
# for printing bill
                    print()
                    print()
                    b=input("Would you like to print the bill ? (y/n) : ")
                    print()
                    print()
                    if b=="y":
                        print("    Bill : ")
                        print()
                        title=['     SREE PRANAVA BALAJI BHAVAN  (a Kedharanahan Groups of company) ']
                        c.execute("Select id,dish,cost,quantity,price from sales_report")
                        Bill=c.fetchall()
                        b_column_names = ['ID','Dishes','Cost','Quantity','Price']
                        b_col="| {:5} | {:30} | {:7} | {:6} | {:10} |".format(*b_column_names)
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print("| {:72} |".format(*title))
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print("| {:72} |".format(char))
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print(b_col)
                        print("+"+"-"*(len(b_col)-2)+"+")
                        for row in Bill:
                            print("| {:5} | {:30} | {:7} | {:8} | {:10} |".format(*row))
                            print("+"+"-"*(len(b_col)-2)+"+")
                        print("|                                                  |  TOTAL : | {:10} |".format(*TOTAL))
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print()
                        print()
                else:

# for printing bill
                    print()
                    print()
                    b=input("Would you like to print the bill ? (y/n) : ")
                    print()
                    print()
                    if b=="y":
                        print("    Bill : ")
                        print()
                        title=['     SREE PRANAVA BALAJI BHAVAN  (a Kedharanahan Groups of company) ']
                        c.execute("Select id,dish,cost,quantity,price from sales_report")
                        Bill=c.fetchall()
                        b_column_names = ['ID','Dishes','Cost','Quantity','Price']
                        b_col="| {:5} | {:30} | {:7} | {:6} | {:10} |".format(*b_column_names)
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print("| {:72} |".format(*title))
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print("| {:72} |".format(char))
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print(b_col)
                        print("+"+"-"*(len(b_col)-2)+"+")
                        for row in Bill:
                            print("| {:5} | {:30} | {:7} | {:8} | {:10} |".format(*row))
                            print("+"+"-"*(len(b_col)-2)+"+")
                        print("|                                                  |  TOTAL : | {:10} |".format(*TOTAL))
                        print("+"+"-"*(len(b_col)-2)+"+")
                        print()
                        print()
            
            
        ch=input("Do you wish to continue changing profile ? (y/n) : ")
        if ch=="y":
            print()
            print()
            continue
        else:
            
# footer
            print()
            print()
            print()
            Footer="""                                             THANK YOU
                                                         VISIT AGAIN"""
            print("-"*(len(Header)-87))
            print("-"*(len(Header)-87))
            print(Footer)
            print("-"*(len(Header)-87))
            print("-"*(len(Header)-87))
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            break
    else:
        print("!!! SORRY, ENTER CORRECT OPTION !!!")
        print()
        print()
        continue

