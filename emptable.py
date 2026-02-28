import mysql.connector as m
C=m.connect(host='localhost', user='root',passwd='1234', database='Proj')
c=C.cursor()
c.execute("create database if not exist Project")
c.execute("use databases Empl")
c.execute("create table Empl(Empid varchar(5) primary key, Ename char(20), username varchar(30), passwd varchar(29),up varchar(1),desig varchar(20), salary (in Rs) int, email varchar(20), phno char(16))")
# Core employees
c.execute("INSERT INTO Empl VALUES('E1','Adarsh','adarsh','adarsh@2007','U','Assistant Manager',800000,'adharsh@gmail.com','+91 9200394867')")
c.execute("INSERT INTO Empl VALUES('E2','Anish','anish','anish@2007','A','Co-Founder',30000000,'anish2007@gmail.com','+91 9500394867')")
c.execute("INSERT INTO Empl VALUES('E3','Arul','arul','arul@2006','U','Manager',1000000,'arul@gmail.com','+91 9900394867')")
c.execute("INSERT INTO Empl VALUES('E4','Pranav','pranav','pranav@2006','A','Co-Founder',5000000,'pranavneelu06@gmail.com','+91 9990394867')")
c.execute("INSERT INTO Empl VALUES('E5','Kedharanathan','kedhar','kedhar@2006','A','Founder',5000000,'kedharanathancr@gmail.com','+91 9944384833')")
c.execute("INSERT INTO Empl VALUES('E6','Sanjay','sanjay','sanjay@2006','U','Sales Manager',100000,'sanjay@gmail.com','+91 9900394868')")
c.execute("INSERT INTO Empl VALUES('E7','Ramkumar','ramkumar','ramkumar@2006','U','Marketing Manager',100000,'ramkumar@gmail.com','+91 9900392467')")
c.execute("INSERT INTO Empl VALUES('E8','Sathish','sathish','sathish@2006','U','Marketing Manager',100000,'sathish@gmail.com','+91 9300392467')")


# Assistant Managers E9–E20
c.execute("INSERT INTO Empl VALUES('E9','Emp9','emp9','emp9@2025','A','Assistant Manager',800000,'emp9@example.com','+91 9000000009')")
c.execute("INSERT INTO Empl VALUES('E10','Emp10','emp10','emp10@2025','A','Assistant Manager',800000,'emp10@example.com','+91 9000000010')")
c.execute("INSERT INTO Empl VALUES('E11','Emp11','emp11','emp11@2025','A','Assistant Manager',800000,'emp11@example.com','+91 9000000011')")
c.execute("INSERT INTO Empl VALUES('E12','Emp12','emp12','emp12@2025','A','Assistant Manager',800000,'emp12@example.com','+91 9000000012')")
c.execute("INSERT INTO Empl VALUES('E13','Emp13','emp13','emp13@2025','A','Assistant Manager',800000,'emp13@example.com','+91 9000000013')")
c.execute("INSERT INTO Empl VALUES('E14','Emp14','emp14','emp14@2025','A','Assistant Manager',800000,'emp14@example.com','+91 9000000014')")
c.execute("INSERT INTO Empl VALUES('E15','Emp15','emp15','emp15@2025','A','Assistant Manager',800000,'emp15@example.com','+91 9000000015')")
c.execute("INSERT INTO Empl VALUES('E16','Emp16','emp16','emp16@2025','A','Assistant Manager',800000,'emp16@example.com','+91 9000000016')")
c.execute("INSERT INTO Empl VALUES('E17','Emp17','emp17','emp17@2025','A','Assistant Manager',800000,'emp17@example.com','+91 9000000017')")
c.execute("INSERT INTO Empl VALUES('E18','Emp18','emp18','emp18@2025','A','Assistant Manager',800000,'emp18@example.com','+91 9000000018')")
c.execute("INSERT INTO Empl VALUES('E19','Emp19','emp19','emp19@2025','A','Assistant Manager',800000,'emp19@example.com','+91 9000000019')")
c.execute("INSERT INTO Empl VALUES('E20','Emp20','emp20','emp20@2025','A','Assistant Manager',800000,'emp20@example.com','+91 9000000020')")


# Supervisors E21–E25
c.execute("INSERT INTO Empl VALUES('E21','Emp21','emp21','emp21@2025','U','Supervisor',450000,'emp21@example.com','+91 9000000021')")
c.execute("INSERT INTO Empl VALUES('E22','Emp22','emp22','emp22@2025','U','Supervisor',450000,'emp22@example.com','+91 9000000022')")
c.execute("INSERT INTO Empl VALUES('E23','Emp23','emp23','emp23@2025','U','Supervisor',450000,'emp23@example.com','+91 9000000023')")
c.execute("INSERT INTO Empl VALUES('E24','Emp24','emp24','emp24@2025','U','Supervisor',450000,'emp24@example.com','+91 9000000024')")
c.execute("INSERT INTO Empl VALUES('E25','Emp25','emp25','emp25@2025','U','Supervisor',450000,'emp25@example.com','+91 9000000025')")


# Chefs E26–E30
c.execute("INSERT INTO Empl VALUES('E26','Emp26','emp26','emp26@2025','U','Head Chef',700000,'emp26@example.com','+91 9000000026')")
c.execute("INSERT INTO Empl VALUES('E27','Emp27','emp27','emp27@2025','U','Sous Chef',550000,'emp27@example.com','+91 9000000027')")
c.execute("INSERT INTO Empl VALUES('E28','Emp28','emp28','emp28@2025','U','Sous Chef',550000,'emp28@example.com','+91 9000000028')")
c.execute("INSERT INTO Empl VALUES('E29','Emp29','emp29','emp29@2025','U','Pastry Chef',500000,'emp29@example.com','+91 9000000029')")
c.execute("INSERT INTO Empl VALUES('E30','Emp30','emp30','emp30@2025','U','Line Cook',300000,'emp30@example.com','+91 9000000030')")


# Service staff (Waiters) E31–E40
c.execute("INSERT INTO Empl VALUES('E31','Emp31','emp31','emp31@2025','U','Waiter',250000,'emp31@example.com','+91 9000000031')")
c.execute("INSERT INTO Empl VALUES('E32','Emp32','emp32','emp32@2025','U','Waiter',250000,'emp32@example.com','+91 9000000032')")
c.execute("INSERT INTO Empl VALUES('E33','Emp33','emp33','emp33@2025','U','Waiter',250000,'emp33@example.com','+91 9000000033')")
c.execute("INSERT INTO Empl VALUES('E34','Emp34','emp34','emp34@2025','U','Waiter',250000,'emp34@example.com','+91 9000000034')")
c.execute("INSERT INTO Empl VALUES('E35','Emp35','emp35','emp35@2025','U','Waiter',250000,'emp35@example.com','+91 9000000035')")
c.execute("INSERT INTO Empl VALUES('E36','Emp36','emp36','emp36@2025','U','Waiter',250000,'emp36@example.com','+91 9000000036')")
c.execute("INSERT INTO Empl VALUES('E37','Emp37','emp37','emp37@2025','U','Waiter',250000,'emp37@example.com','+91 9000000037')")
c.execute("INSERT INTO Empl VALUES('E38','Emp38','emp38','emp38@2025','U','Waiter',250000,'emp38@example.com','+91 9000000038')")
c.execute("INSERT INTO Empl VALUES('E39','Emp39','emp39','emp39@2025','U','Waiter',250000,'emp39@example.com','+91 9000000039')")
c.execute("INSERT INTO Empl VALUES('E40','Emp40','emp40','emp40@2025','U','Waiter',250000,'emp40@example.com','+91 9000000040')")


# Cashiers E41–E45
c.execute("INSERT INTO Empl VALUES('E41','Emp41','emp41','emp41@2025','U','Cashier',280000,'emp41@example.com','+91 9000000041')")
c.execute("INSERT INTO Empl VALUES('E42','Emp42','emp42','emp42@2025','U','Cashier',280000,'emp42@example.com','+91 9000000042')")
c.execute("INSERT INTO Empl VALUES('E43','Emp43','emp43','emp43@2025','U','Cashier',280000,'emp43@example.com','+91 9000000043')")
c.execute("INSERT INTO Empl VALUES('E44','Emp44','emp44','emp44@2025','U','Cashier',280000,'emp44@example.com','+91 9000000044')")
c.execute("INSERT INTO Empl VALUES('E45','Emp45','emp45','emp45@2025','U','Cashier',280000,'emp45@example.com','+91 9000000045')")


# Cleaning staff E46–E50
c.execute("INSERT INTO Empl VALUES('E46','Emp46','emp46','emp46@2025','U','Cleaner',200000,'emp46@example.com','+91 9000000046')")
c.execute("INSERT INTO Empl VALUES('E47','Emp47','emp47','emp47@2025','U','Cleaner',200000,'emp47@example.com','+91 9000000047')")
c.execute("INSERT INTO Empl VALUES('E48','Emp48','emp48','emp48@2025','U','Cleaner',200000,'emp48@example.com','+91 9000000048')")
c.execute("INSERT INTO Empl VALUES('E49','Emp49','emp49','emp49@2025','U','Cleaner',200000,'emp49@example.com','+91 9000000049')")
c.execute("INSERT INTO Empl VALUES('E50','Emp50','emp50','emp50@2025','U','Cleaner',200000,'emp50@example.com','+91 9000000050')")


# Kitchen helpers E51–E55
c.execute("INSERT INTO Empl VALUES('E51','Emp51','emp51','emp51@2025','U','Kitchen Helper',210000,'emp51@example.com','+91 9000000051')")
c.execute("INSERT INTO Empl VALUES('E52','Emp52','emp52','emp52@2025','U','Kitchen Helper',210000,'emp52@example.com','+91 9000000052')")
c.execute("INSERT INTO Empl VALUES('E53','Emp53','emp53','emp53@2025','U','Kitchen Helper',210000,'emp53@example.com','+91 9000000053')")
c.execute("INSERT INTO Empl VALUES('E54','Emp54','emp54','emp54@2025','U','Kitchen Helper',210000,'emp54@example.com','+91 9000000054')")
c.execute("INSERT INTO Empl VALUES('E55','Emp55','emp55','emp55@2025','U','Kitchen Helper',210000,'emp55@example.com','+91 9000000055')")


# Security E56–E60
c.execute("INSERT INTO Empl VALUES('E56','Emp56','emp56','emp56@2025','U','Security',230000,'emp56@example.com','+91 9000000056')")
c.execute("INSERT INTO Empl VALUES('E57','Emp57','emp57','emp57@2025','U','Security',230000,'emp57@example.com','+91 9000000057')")
c.execute("INSERT INTO Empl VALUES('E58','Emp58','emp58','emp58@2025','U','Security',230000,'emp58@example.com','+91 9000000058')")
c.execute("INSERT INTO Empl VALUES('E59','Emp59','emp59','emp59@2025','U','Security',230000,'emp59@example.com','+91 9000000059')")
c.execute("INSERT INTO Empl VALUES('E60','Emp60','emp60','emp60@2025','U','Security',230000,'emp60@example.com','+91 9000000060')")


# Hosts / receptionists E61–E65
c.execute("INSERT INTO Empl VALUES('E61','Emp61','emp61','emp61@2025','U','Host',320000,'emp61@example.com','+91 9000000061')")
c.execute("INSERT INTO Empl VALUES('E62','Emp62','emp62','emp62@2025','U','Host',320000,'emp62@example.com','+91 9000000062')")
c.execute("INSERT INTO Empl VALUES('E63','Emp63','emp63','emp63@2025','U','Host',320000,'emp63@example.com','+91 9000000063')")
c.execute("INSERT INTO Empl VALUES('E64','Emp64','emp64','emp64@2025','U','Host',320000,'emp64@example.com','+91 9000000064')")
c.execute("INSERT INTO Empl VALUES('E65','Emp65','emp65','emp65@2025','U','Host',320000,'emp65@example.com','+91 9000000065')")


# Delivery staff E66–E70
c.execute("INSERT INTO Empl VALUES('E66','Emp66','emp66','emp66@2025','U','Delivery',260000,'emp66@example.com','+91 9000000066')")
c.execute("INSERT INTO Empl VALUES('E67','Emp67','emp67','emp67@2025','U','Delivery',260000,'emp67@example.com','+91 9000000067')")
c.execute("INSERT INTO Empl VALUES('E68','Emp68','emp68','emp68@2025','U','Delivery',260000,'emp68@example.com','+91 9000000068')")
c.execute("INSERT INTO Empl VALUES('E69','Emp69','emp69','emp69@2025','U','Delivery',260000,'emp69@example.com','+91 9000000069')")
c.execute("INSERT INTO Empl VALUES('E70','Emp70','emp70','emp70@2025','U','Delivery',260000,'emp70@example.com','+91 9000000070')")


# Admin / back office E71–E75
c.execute("INSERT INTO Empl VALUES('E71','Emp71','emp71','emp71@2025','A','Accountant',600000,'emp71@example.com','+91 9000000071')")
c.execute("INSERT INTO Empl VALUES('E72','Emp72','emp72','emp72@2025','A','HR',550000,'emp72@example.com','+91 9000000072')")
c.execute("INSERT INTO Empl VALUES('E73','Emp73','emp73','emp73@2025','A','Admin',500000,'emp73@example.com','+91 9000000073')")
c.execute("INSERT INTO Empl VALUES('E74','Emp74','emp74','emp74@2025','A','IT Support',500000,'emp74@example.com','+91 9000000074')")
c.execute("INSERT INTO Empl VALUES('E75','Emp75','emp75','emp75@2025','A','Procurement',520000,'emp75@example.com','+91 9000000075')")


# Generic staff E76–E100
c.execute("INSERT INTO Empl VALUES('E76','Emp76','emp76','emp76@2025','U','Staff',240000,'emp76@example.com','+91 9000000076')")
c.execute("INSERT INTO Empl VALUES('E77','Emp77','emp77','emp77@2025','U','Staff',240000,'emp77@example.com','+91 9000000077')")
c.execute("INSERT INTO Empl VALUES('E78','Emp78','emp78','emp78@2025','U','Staff',240000,'emp78@example.com','+91 9000000078')")
c.execute("INSERT INTO Empl VALUES('E79','Emp79','emp79','emp79@2025','U','Staff',240000,'emp79@example.com','+91 9000000079')")
c.execute("INSERT INTO Empl VALUES('E80','Emp80','emp80','emp80@2025','U','Staff',240000,'emp80@example.com','+91 9000000080')")
c.execute("INSERT INTO Empl VALUES('E81','Emp81','emp81','emp81@2025','U','Staff',240000,'emp81@example.com','+91 9000000081')")
c.execute("INSERT INTO Empl VALUES('E82','Emp82','emp82','emp82@2025','U','Staff',240000,'emp82@example.com','+91 9000000082')")
c.execute("INSERT INTO Empl VALUES('E83','Emp83','emp83','emp83@2025','U','Staff',240000,'emp83@example.com','+91 9000000083')")
c.execute("INSERT INTO Empl VALUES('E84','Emp84','emp84','emp84@2025','U','Staff',240000,'emp84@example.com','+91 9000000084')")
c.execute("INSERT INTO Empl VALUES('E85','Emp85','emp85','emp85@2025','U','Staff',240000,'emp85@example.com','+91 9000000085')")
c.execute("INSERT INTO Empl VALUES('E86','Emp86','emp86','emp86@2025','U','Staff',240000,'emp86@example.com','+91 9000000086')")
c.execute("INSERT INTO Empl VALUES('E87','Emp87','emp87','emp87@2025','U','Staff',240000,'emp87@example.com','+91 9000000087')")
c.execute("INSERT INTO Empl VALUES('E88','Emp88','emp88','emp88@2025','U','Staff',240000,'emp88@example.com','+91 9000000088')")
c.execute("INSERT INTO Empl VALUES('E89','Emp89','emp89','emp89@2025','U','Staff',240000,'emp89@example.com','+91 9000000089')")
c.execute("INSERT INTO Empl VALUES('E90','Emp90','emp90','emp90@2025','U','Staff',240000,'emp90@example.com','+91 9000000090')")
c.execute("INSERT INTO Empl VALUES('E91','Emp91','emp91','emp91@2025','U','Staff',240000,'emp91@example.com','+91 9000000091')")
c.execute("INSERT INTO Empl VALUES('E92','Emp92','emp92','emp92@2025','U','Staff',240000,'emp92@example.com','+91 9000000092')")
c.execute("INSERT INTO Empl VALUES('E93','Emp93','emp93','emp93@2025','U','Staff',240000,'emp93@example.com','+91 9000000093')")
c.execute("INSERT INTO Empl VALUES('E94','Emp94','emp94','emp94@2025','U','Staff',240000,'emp94@example.com','+91 9000000094')")
c.execute("INSERT INTO Empl VALUES('E95','Emp95','emp95','emp95@2025','U','Staff',240000,'emp95@example.com','+91 9000000095')")
c.execute("INSERT INTO Empl VALUES('E96','Emp96','emp96','emp96@2025','U','Staff',240000,'emp96@example.com','+91 9000000096')")
c.execute("INSERT INTO Empl VALUES('E97','Emp97','emp97','emp97@2025','U','Staff',240000,'emp97@example.com','+91 9000000097')")
c.execute("INSERT INTO Empl VALUES('E98','Emp98','emp98','emp98@2025','U','Staff',240000,'emp98@example.com','+91 9000000098')")
c.execute("INSERT INTO Empl VALUES('E99','Emp99','emp99','emp99@2025','U','Staff',240000,'emp99@example.com','+91 9000000099')")
c.execute("INSERT INTO Empl VALUES('E100','Emp100','emp100','emp100@2025','U','Staff',240000,'emp100@example.com','+91 9000000100')")


# Commit all changes
C.commit()

