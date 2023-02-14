# Project Name: STUDENT REPORT CARD MANAGEMENT
# Made by: S. BALAVIGNESH REDDY
#School: HILLWOODS SCHOOL
# Class : 12 A
# Session: 2021-22
# Roll No:11607201

import mysql.connector as a


school_name='Hillwoods School'
school_address='GIDC Electronic Estate, Sector 25, Gandhinagar, Gujarat'
school_email='hillwoods2001@yahoo.com'
school_phone='07923287174'

conn = a.connect(host='localhost', database='report_card', user='root', password='Balavignesh@1')
cur=conn.cursor()



    
l1=[]
sql="select * from marks1"
cur.execute(sql)
read=cur.fetchall()
for i in read:
    l1.append(i[0])

l2=[]
sql1="select * from student1"
cur.execute(sql1)
read1=cur.fetchall()
for j in read1:
    l2.append(j[0])

def database_creation():
    conn = a.connect(host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur=conn.cursor()
    sql='create database report_card'
    cur.execute(sql)
    conn.close()
#database_creation()



def table_creation():
    conn = a.connect(host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur=conn.cursor()
    sql='''create table student1(admno int NOT NULL auto_increment,
				     fname varchar(30) DEFAULT NULL,
                     lname varchar(30) DEFAULT NULL,
                     class varchar(15) DEFAULT NULL,
                     section varchar(10) DEFAULT NULL,
                     primary key(admno));


            create table marks1(admno int DEFAULT NULL,
                                       term varchar(20) DEFAULT NULL,
                   session varchar(20) DEFAULT NULL,
                   phy int DEFAULT NULL,
                   chem int DEFAULT NULL,
                   math int DEFAULT NULL,
                   eng int DEFAULT NULL,
                   comp int DEFAULT NULL)'''
    cur.execute(sql)
#table_creation()

def insert_values():
    sql='''insert into student1(admno, fname, lname, class, section)
values(101,'Balavignesh','Reddy','12','A'),
	  (102,'Tavish','Gupta','12','A');

	  insert into marks1 values(101,'UT-1','2021-22',67,89,90,67,90),
		    (102,'UT-1','2021-22',67,78,56,34,45);'''
#insert_values()
    
def clear():
    for i in range(50):
        print()


def pswd():
    pass1=input("Enter the password here:")
    if pass1=="**":
        clear()
        print("--------Logging u in....--------")
        print()
        print("Successfully logged in ...")
        print("\U0001F600")
        print('\n\n')
        main_menu()
    else:
        print("-------WRONG PASSWORD-------")
        print("\U0001F602")
        pswd()
        
#pswd()
    
def add_student():
    print('-'*100)
    print(' Add New Student Record Screen ')
    print('-'*100)
    admno=int(input("Enter the admission number of the student........"))
    if admno not in l1:
        fname=input(' Enter student name........: ')
        lname=input(" Enter student's last name.......: ")
        clas=int(input(' Enter student Class........: '))
        section=input(' Enter student Section.......: ')
        query="insert into student1 values(%s,%s,%s,%s,%s)"
        data=(admno,fname,lname,clas,section)
        cur.execute(query,data)
        conn.commit()
        print("\n\n\nNew Student Added Successfully \U0001F600\U0001F600...")
        add_marks()
    else:
        print("\n\n\nThe entered admission number is already existing \U0001F605\U0001F605.......\n\n")
    wait=input("\n\n\nPress any key to continue...")
    print()
    main_menu()

#add_student()

def delete_student():
    conn = a.connect(
        host='localhost',database='report_card',user='root',password='Balavignesh@1')
    cur=conn.cursor()
    
    print('-'*100)
    print(' Delete the Student Record Screen ')
    print('-'*100)
    admno=int(input("Enter the admno of the student whose record is to be deleted......:"))
    if admno in l2:
        
        query="Delete from student1 where admno=%s"
        data=(admno,)
        cur.execute(query,data)
        conn.commit()
        print("\n\n\nDeleted the Student Record Successfully \U0001F600\U0001F600...")
        delete_marks()
    else:
        print("\n\n\nThe entered admission number is not present \U0001F605\U0001F605.......\n\n")
    wait=input("\n\n\nPress any key to continue...")
    print()
    main_menu()
    
#delete_student()

def modify_student():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cursor = conn.cursor()
    clear()
    print('-'*100)
    print('Modify Student Information - Screen')
    print('-'*100)
    admno = input('Enter admission number in which it is to be modified......:')
    if admno not in l2:
        print('\n1.   First Name  ')
        print('\n2.   Last Name  ')
        print('\n3.   Class  ')
        print('\n4.   Section  ')
        print('\n\n')
        ch=int(input("Enter your choice.......:"))
        if ch==1:
            fname=input("Enter the new first name.....:")
            sql="update student1 set fname=%s where admno=%s"
            data=(fname,admno)
            cursor.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Record Updated \U0001F600\U0001F600.....')
        if ch==2:
            lname=input("Enter the new last name.....:")
            sql="update student1 set lname=%s where admno=%s"
            data=(lname,admno)
            cursor.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Record Updated \U0001F600\U0001F600.....')
        if ch==3:
            Class=input("Enter the new class.....:")
            sql="update student1 set Class=%s where admno=%s"
            data=(Class,admno)
            cursor.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Record Updated \U0001F600\U0001F600.....')
        if ch==4:
            Sec=input("Enter the new section.....:")
            sql="update student1 set Section=%s where admno=%s"
            data=(Sec,admno)
            cursor.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Record Updated \U0001F600\U0001F600.....')
    else:
        print("The admission number you have entered is not existing \U0001F605\U0001F605.......")
        
    wait = input('\n\n\nPress any key to continue......')
    print()
    main_menu()
    
    
def modify_student1():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cursor = conn.cursor()
    clear()
    print('-'*100)
    print('Modify Student Information - Screen')
    print('-'*100)
    admno = input('Enter admission number in which it is to be modified......:')
    print('\n1.   First Name  ')
    print('\n2.   Last Name  ')
    print('\n3.   Class  ')
    print('\n4.   Section  ')
    print('\n\n')
    choice = int(input('Enter your choice......:'))
    field=''
    if choice ==1:
       field ='fname' 
    if choice == 2:
       field = 'lname'
    if choice == 3:
       field = 'class'
    if choice == 4:
       field = 'section'
    value =input('Enter new value........:')   
    sql ='update student1 set '+field+' ="'+value +'" where admno ='+admno+';'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\n\n Student Record Updated.....')
    wait = input('\n\n\nPress any key to continue......')
    print()

    
#modify_student()


def add_marks():
    conn=a.connect(
        host='localhost',database='report_card', user='root',password='Balavignesh@1')
    cur=conn.cursor()

    print('-'*100)
    print("Add New Marks Screen")
    print('-'*100)
    admno=int(input("Enter the admission number......:"))


    if admno not in l1:
        
        term=input("Enter the term......:")
        session=input("Enter session......:")
        phy=int(input("Enter the marks in Physics......:"))
        chem=int(input("Enter the mark in Chemistry....:"))
        math=int(input("Enter the marks in Maths.....:"))
        eng=int(input("Enter the marks in English......:"))
        comp=int(input("Enter the marks in Computer Science......"))
        query="insert into marks1 values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(admno,term,session,phy,chem,math,eng,comp)
        cur.execute(query,data)
        conn.commit()
        conn.close()
        print("\n\n\nNew Marks Added Successfully in the Record \U0001F600\U0001F600...........")
    else:
        print("\n\n\nThe entered admission number is already there \U0001F605\U0001F605.....")
    wait=input("\n\n\nPress any key to continue.....")
    print()
    main_menu()
    
#add_marks()


def delete_marks():
    conn=a.connect(
        host='localhost',database='report_card', user='root',password='Balavignesh@1')
    cur=conn.cursor()

    print('-'*100)
    print("Delete the Marks Record of Student Screen")
    print('-'*100)
    admno=int(input("Enter the admission number whose record you have deleted now......:"))

    if admno in l1:
        query="delete from marks1 where admno=%s"
        data=(admno,)
        cur.execute(query,data)
        conn.commit()
        conn.close()
        print("\n\n\nDeleted the marks Record Successfully \U0001F600\U0001F600........")
    else:
        print("\n\n\nThe admission number you have entered is not present \U0001F605\U0001F605.....")
    wait=input("\n\n\nPress any key to continue.....")
    print()
    main_menu()


#delete_marks()

def modify_marks():
    print('-'*100)
    print("Modify the Student Report Screen")
    print('-'*100)
    admno=input("Enter admission of student whose marks is to be modified.....:")
    if admno not in l1:
        print("\n1. Physics")
        print("\n2. Chemistry")
        print("\n3. Mathematics")
        print("\n4. English")
        print("\n5. Computer")
        print()
        ch=int(input("Enter your choice.......:"))
        if ch==1:
            mrks=input("Enter the new Physics marks.....:")
            sql="update marks1 set phy=%s where admno=%s"
            data=(mrks,admno)
            cur.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Marks Updated \U0001F600\U0001F600.....')
        if ch==2:
            mrks=input("Enter the new Chemistry marks.....:")
            sql="update marks1 set chem=%s where admno=%s"
            data=(mrks,admno)
            cur.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Marks Updated \U0001F600\U0001F600.....')
        if ch==3:
            mrks=input("Enter the new Mathematics marks.....:")
            sql="update marks1 set math=%s where admno=%s"
            data=(mrks,admno)
            cur.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Marks Updated \U0001F600\U0001F600.....')
        if ch==4:
            mrks=input("Enter the new English marks.....:")
            sql="update marks1 set eng=%s where admno=%s"
            data=(mrks,admno)
            cur.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Marks Updated \U0001F600\U0001F600.....')
        if ch==5:
            mrks=input("Enter the new Computer Science marks.....:")
            sql="update marks1 set comp=%s where admno=%s"
            data=(mrks,admno)
            cur.execute(sql,data)
            conn.commit()
            print('\n\n\n Student Marks Updated \U0001F600\U0001F600.....')
    else:
        print("The admission number you have entered is not existing \U0001F605\U0001F605.........")
    wait=input("\n\n\nPress any key to continue......")
    print()
    main_menu()
            

def modify_marks1():
    conn=a.connect(
        host='localhost',database='report_card', user='root',password='Balavignesh@1')
    cur=conn.cursor()

    print('-'*100)
    print("Modify the Student Report Screen")
    print('-'*100)
    admno=input("Enter admission of student whose marks is to be modified.....:")

    print("\n1. Physics")
    print("\n2. Chemistry")
    print("\n3. Mathematics")
    print("\n4. English")
    print("\n5. Computer")
    print()
    ch=int(input("Enter your choice.......:"))
    field=''
    if ch==1:
        field='phy'
    if ch==2:
        field='chem'
    if ch==3:
        field='math'
    if ch==4:
        field='eng'
    if ch==5:
        field='comp'
    value=input("Enter the new marks......")
    sql ='update marks1 set '+field+' ="'+value +'" where admno ='+admno+';'
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("\n\n\nStudents Report Modified Successfully......")
    wait=input("\n\n\nPress any key to continue......")
    print()

#modify_marks()




def search_student():
  print('-'*100)
  print("Search Menu Screen")
  print('-'*100)
  admno=input("Enter the admission number whose record you want to see.......")
  if admno not in l1:
      sql ='select * from student1 where admno=%s'
      data=(admno,)
      cur.execute(sql,data)
      records = cur.fetchall()
      for i in records:
          print('-'*100)
          print("Admno:",i[0])
          print("First Name:",i[1])
          print("Last Name:",i[2])
          print("Class:",i[3])
          print("Section:",i[4])
          print('-'*100)
          wait = input('\n\n\n Press any key to continue.....')
          print()
          search_menu()
  else:
      print("The Entered roll number is invalid \U0001F605\U0001F605.......")
      search_menu()
  wait = input('\n\n\n Press any key to continue.....')
  print()
  main_menu()


  
def search_student1():
  conn = a.connect(
      host='localhost', database='report_card', user='root', password='Balavignesh@1')
  cur = conn.cursor()
  print('-'*100)
  print("Search Menu Screen")
  print('-'*100)
  admno=input("Enter the admission number whose record you want to see.......")
  if admno not in l1:
      sql ='select * from student1 where admno=%s'
      data=(admno,)
      cur.execute(sql,data)
      records = cur.fetchall()
      for i in records:
          print('-'*100)
          print("Admno:",i[0])
          print("First Name:",i[1])
          print("Last Name:",i[2])
          print("Class:",i[3])
          print("Section:",i[4])
          print('-'*100)
  else:
      print("The Entered roll number is invalid \U0001F605\U0001F605.......")
  wait = input('\n\n\n Press any key to continue.....')
  print()
  user_menu()

def search_marks():
    print('-'*100)
    print("Search Menu Screen")
    print('-'*100)
    admno=input("Enter the admission number whose record you want to see.......")
    sql1="select * from student1 where admno=%s"
    data1=(admno,)
    cur.execute(sql1,data1)
    record=cur.fetchall()
    for j in record:
        print('-'*100)
        print("Name:",j[1],j[2])
        print("Class:",j[3])
        print("Section:",j[4])
        print('-'*100)
    if admno not in l1:
        sql ='select * from marks1 where admno=%s'
        data=(admno,)
        cur.execute(sql,data)
        records = cur.fetchall()
        for i in records:
            print("Admno:",i[0])
            print("Term:",i[1])
            print("Session:",i[2])
            print("Physics Marks:",i[3])
            print("Chemistry Marks:",i[4])
            print("Maths Marks:",i[5])
            print("English Marks:",i[6])
            print("Computer Marks:",i[7])
            print('-'*100)
    else:
        print("The admission number entered is not present \U0001F605\U0001F605......")
        wait=input("\n\n\nPress any key to continue........:")
        print()
        search_menu()
    wait=input("\n\n\nPress any key to continue........:")
    print()
    main_menu()
      
    


def search_marks1():
    
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    print('-'*100)
    print("Search Menu Screen")
    print('-'*100)
    admno=input("Enter the admission number whose record you want to see.......")
    sql1="select * from student1 where admno=%s"
    data1=(admno,)
    cur.execute(sql1,data1)
    record=cur.fetchall()
    for j in record:
        print('-'*100)
        print("Name:",j[1],j[2])
        print("Class:",j[3])
        print("Section:",j[4])
        print('-'*100)
    if admno not in l1:
        sql ='select * from marks1 where admno=%s'
        data=(admno,)
        cur.execute(sql,data)
        records = cur.fetchall()
        for i in records:
            print("Admno:",i[0])
            print("Term:",i[1])
            print("Session:",i[2])
            print("Physics Marks:",i[3])
            print("Chemistry Marks:",i[4])
            print("Maths Marks:",i[5])
            print("English Marks:",i[6])
            print("Computer Marks:",i[7])
            print('-'*100)
            
            
    else:
        print("The admission number entered is not present \U0001F605\U0001F605......")
    wait=input("\n\n\nPress any key to continue........:")
    print()
    user_menu()    
    


def search_menu():
    while True:
      clear()
      print('-'*100)
      print(' S E A R C H    M E N U')
      print('-'*100)
      print("\n1.  Search Student")
      print('\n2.  Student Term Marks')
      print('\n3.  Back to main')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        search_student()
      if choice == 2:
        search_marks()
      if choice == 3:
        clear()
        main_menu()

#search_menu()
def search_menu1():
    while True:
      clear()
      print('-'*100)
      print(' S E A R C H    M E N U')
      print('-'*100)
      print("\n1.  Search Student")
      print('\n2.  Student Term Marks')
      print('\n3.  Back to main')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        search_student1()
      if choice == 2:
        search_marks1()
      if choice == 3:
        clear()
        user_menu()

def single_term():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    admno=input("Enter the admission number.......:")
    if admno not in l1:
        session=input("Enter the session......:")
        term=input("Enter the term......:")
        sql='select s.admno,fname,lname,phy,math,chem,eng,comp from student1 s, \
        marks1 m where s.admno=m.admno and s.admno=%s and m.session=%s;'
        data=(admno,session)
        cur.execute(sql,data)
        record=cur.fetchone()
        clear()
        print('-'*100)
        print("School Name:",school_name)
        print("School Address:",school_address)
        print("Phone:",school_phone,'\nEmail',school_email)
        print('-'*100)
        print("Admno:",record[0],"\nFirst Name:",record[1],"\nLast Name:",record[2])
        print("Session:",session,"\nTerm:",term)
        print('-'*100)
        print("Subject","\t\tMax_Marks",'\tMin_Marks','\tMarks obtained')
        print("Physics",'\t\t100','\t\t33','\t\t',record[3])
        print("Chemistry",'\t\t100','\t\t33','\t\t',record[5])
        print("Mathematics",'\t\t100','\t\t33','\t\t',record[4])
        print("English",'\t\t100','\t\t33','\t\t',record[6])
        print("Computer Science",'\t100','\t\t33','\t\t',record[7])
        print('-'*100)
        total=record[3]+record[4]+record[5]+record[6]+record[7]
        per=(total/500)*100
        print("Total Marks:",total,'\nMarks in %:',per)
        conn.close()
    else:
        print("The admission number entered is not present \U0001F605\U0001F605........")
    wait=input("\n\n\nPress any key to continue........")
    print()




def single_term1():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    admno=input("Enter the admission number.......:")
    if admno not in l1:
        session=input("Enter the session......:")
        term=input("Enter the term......:")
        sql='select s.admno,fname,lname,phy,math,chem,eng,comp from student1 s, marks1 m where s.admno=m.admno and s.admno=%s and m.session=%s;'
        data=(admno,session)
        cur.execute(sql,data)
        record=cur.fetchone()
        clear()
        print('-'*100)
        print("School Name:",school_name)
        print("School Address:",school_address)
        print("Phone:",school_phone,'\nEmail',school_email)
        print('-'*100)
        print("Admno:",record[0],"\nFirst Name:",record[1],"\nLast Name:",record[2])
        print("Session:",session,"\nTerm:",term)
        print('-'*100)
        print("Subject","\t\tMax_Marks",'\tMin_Marks','\tMarks obtained')
        print("Physics",'\t\t100','\t\t33','\t\t',record[3])
        print("Chemistry",'\t\t100','\t\t33','\t\t',record[5])
        print("Mathematics",'\t\t100','\t\t33','\t\t',record[4])
        print("English",'\t\t100','\t\t33','\t\t',record[6])
        print("Computer Science",'\t100','\t\t33','\t\t',record[7])
        print('-'*100)
        total=record[3]+record[4]+record[5]+record[6]+record[7]
        per=(total/500)*100
        print("Total Marks:",total,'\nMarks in %:',per)
        conn.close()
    else:
        print("The admission number entered is not present \U0001F605\U0001F605........")
    wait=input("\n\n\nPress any key to continue........")
    print()
    user_menu()



    

from prettytable import PrettyTable    
def whole_class():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    clas=input("Enter Class.......:")
    section=input("Enter section........:")
    session=input("Enter Session.......:")
    sql='select s.admno,fname,lname,phy,math,chem,eng,comp from student1 s, \
         marks1 m where s.admno=m.admno and s.class=%s and s.section=%s'
    data=(clas,section)
    cur.execute(sql,data)
    records=cur.fetchall()
    clear()
    print('-'*100)
    print("School Name:",school_name)
    print("School Address:",school_address)
    print("Phone:",school_phone,'\nEmail',school_email)
    print('-'*100)
    print('Class Wise Report Card:')
    print("Class:",clas,'-',section,'Session:',session)
    print('-'*100)
    p1=PrettyTable()
    p1.field_names=['admno','fname','lname','phy_marks','chem_marks','math_marks','eng_marks','comp_marks']
    for i in records:
        p1.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    print(p1)
    conn.close()
    wait=input("\n\n\nPress any key to continue.........")
    print()


from prettytable import PrettyTable    
def whole_class1():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    clas=input("Enter Class.......:")
    section=input("Enter section........:")
    session=input("Enter Session.......:")
    sql='select s.admno,fname,lname,phy,math,chem,eng,comp from student1 s, marks1 m where s.admno=m.admno and s.class=%s and s.section=%s'
    data=(clas,section)
    cur.execute(sql,data)
    records=cur.fetchall()
    clear()
    print('-'*100)
    print("School Name:",school_name)
    print("School Address:",school_address)
    print("Phone:",school_phone,'\nEmail',school_email)
    print('-'*100)
    print('Class Wise Report Card:')
    print("Class:",clas,'-',section,'Session:',session)
    print('-'*100)
    p1=PrettyTable()
    p1.field_names=['admno','fname','lname','phy_marks','chem_marks','math_marks','eng_marks','comp_marks']
    for i in records:
        p1.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
    print(p1)
    conn.close()
    wait=input("\n\n\nPress any key to continue.........")
    print()
    user_menu()



def whole_session():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    session=input("Enter Session......:")
    sql='select s.admno,fname,lname,phy,math,chem,eng,comp from student1 s, marks1 m where s.admno=m.admno and m.session="'+session+'"order by class,section,term;'
    cur.execute(sql)
    records=cur.fetchall()
    clear()
    print("School Name:",school_name)
    print("School Address:",school_address)
    print("Phone:",school_phone,'\nEmail',school_email)
    print('WHole Session Report Card:')
    print('Session:',session)
    print('-'*100)
    for i in records:
        print(i)
    wait=input("\n\n\nPress any key to continue.......")
    print()



#whole_session()


def class_toppers():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    clas=input("Enter Class.......:")
    section=input("Enter section........:")
    session=input("Enter Session.......:")
    sql='select s.admno,fname,lname,phy,math,chem,eng,comp, phy+chem+math+eng+comp \
   "Total" from student1 s, marks1 m where s.admno=m.admno and \
   s.class=%s and s.section=%s;'
    data=(clas,section)
    cur.execute(sql,data)
    record=cur.fetchall()
    clear()
    print('-'*100)
    print("School Name:",school_name)
    print("School Address:",school_address)
    print("Phone:",school_phone,'\nEmail',school_email)
    print('-'*100)
    print()
    print('T O P P E R S     L I S T')
    print()
    print('-'*100)
    l1=[]
    d1={}
    for i in record:
        total=i[3]+i[4]+i[5]+i[6]+i[7]
        per=(total/500)*100
        l1.append(per)
        d1[per]=i[0]
    m1=max(l1)
    a1=d1[m1]
    
    sql1='select * from student1 where admno=%s and section=%s'
    data=(a1,section)
    cur.execute(sql1,data)
    records=cur.fetchall()
    p1=PrettyTable()
    p1.field_names=['Admno','First Name','Last name','Class','Section','Session','Percentage']
    for j in records:
        p1.add_row([j[0],j[1],j[2],j[3],j[4],session,round(m1,2)])
    print(p1)
    conn.close()
    print('-'*100)
    wait=input("\n\n\nPress any key to continue........")
    print()



def class_toppers1():
    conn = a.connect(
        host='localhost', database='report_card', user='root', password='Balavignesh@1')
    cur = conn.cursor()
    clas=input("Enter Class.......:")
    section=input("Enter section........:")
    session=input("Enter Session.......:")
    sql='select s.admno,fname,lname,phy,math,chem,eng,comp, phy+chem+math+eng+comp "Total" from student1 s, marks1 m where s.admno=m.admno and \
s.class=%s and s.section=%s;'
    data=(clas,section)
    cur.execute(sql,data)
    record=cur.fetchall()
    clear()
    print('-'*100)
    print("School Name:",school_name)
    print("School Address:",school_address)
    print("Phone:",school_phone,'\nEmail',school_email)
    print('-'*100)
    print()
    print('T O P P E R S     L I S T')
    print()
    print('-'*100)

    l1=[]
    d1={}
    for i in record:
        total=i[3]+i[4]+i[5]+i[6]+i[7]
        per=(total/500)*100
        l1.append(per)
        d1[per]=i[0]
    m1=max(l1)
    a1=d1[m1]
    sql1='select * from student1 where admno=%s and section=%s'
    data=(a1,section)
    cur.execute(sql1,data)
    records=cur.fetchall()
    p1=PrettyTable()
    p1.field_names=['Admno','First Name','Last name','Class','Section','Session','Percentage']
    for j in records:
        p1.add_row([j[0],j[1],j[2],j[3],j[4],session,m1])
    print(p1)

    
    #print('-'*100)
  #  print("Admno:",i[0])
  #  print("First Name:",i[1])
  #  print("Last Name:",i[2])
  #  print("Class:",clas)
  #  print("Section:",section)
   # print("Session:",session)
    conn.close()
    print('-'*100)
    wait=input("\n\n\nPress any key to continue........")
    print()
    user_menu()


    
def report_menu():
    while True:
        clear()
        print('-'*100)
        print(" R E P O R T   M E N U")
        print("\n1. Single Term Report Card")
        print("\n2. Whole Class report Card")
        print("\n3. Class Wise Topppers")
        print("\n4. Back to main menu")
        print('\n\n')
        ch= int(input("Enter your choice.......:"))
        if ch==1:
            single_term()
        if ch==2:
            whole_class()
        if ch==3:
            class_toppers()
        if ch==4:
            clear()
            main_menu()



def report_menu1():
    while True:
        clear()
        print('-'*100)
        print(" R E P O R T   M E N U")
        print("\n1. Single Term Report Card")
        print("\n2. Whole Class report Card")
        print("\n3. Class Wise Topppers")
        print("\n4. Back to main menu")
        print('\n\n')
        ch= int(input("Enter your choice.......:"))
        if ch==1:
            single_term1()
        if ch==2:
            whole_class1()
        if ch==3:
            class_toppers1()
        if ch==4:
            clear()
            user_menu()




            
#report_menu()
from prettytable import PrettyTable
def table_view():
    while True:
        print('-'*100)
        print('TABLE VIEW MENU')
        print('-'*100)
        print('\n1.   Table of Student Data  ')
        print('\n2.   Table of Marks Data  ')
        print('\n3.   Back to main part  ')
        print('\n\n') 
        ch=int(input("Enter your choice...:"))
        print()
        if ch==1:
            sql='select * from student1'
            cur.execute(sql)
            record=cur.fetchall()
            p1=PrettyTable()
            p1.field_names=['admno','fname','lname','class','section']
            for i in record:
                p1.add_row([i[0],i[1],i[2],i[3],i[4]])
            print(p1)
            print()
            
        if ch==2:
            sql='select * from marks1 order by admno'
            cur.execute(sql)
            
            r=cur.fetchall()
            p1=PrettyTable()
            p1.field_names=['admno','term','session','phy','chem','math','eng','comp']
            for i in r:
                p1.add_row([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]])
            print(p1)
            print()
        if ch==3:
            main_menu()


def admin():
    pass1=input("Enter the password here:")
    if pass1=="12":
        clear()
        print("--------Logging u in....--------")
        print()
        print("Successfully logged in ...")
        print("\U0001F600")
        print('\n\n')
        main_menu()
    else:
        print("-------WRONG PASSWORD-------")
        print("\U0001F602")
        pswd()


def user_menu():
    print("^"*100)
    print(' M A I N      M E N U        F O R       U S E R')
    print("^"*100)
    print("\n1. Search Menu")
    print("\n2. Report Menu")
    print("\n3. Display Menu")
    print("\n4. Close application")
    print("\n\n")
    choice=int(input("Enter your choice......:"))
    if choice==1:
        search_menu1()
    if choice==2:
        report_menu1()
    if choice==3:
        table_view()
    if choice==4:
        print("\n\n\nT H A N K\t Y O U")
        print(exit())
        


def admin_user():
    print('\n\n')
    print('*'*18,'W E L C O M E','*'*18)
    print('\n\n')
    a=input("You are admin or user.....:")
    
    if a in ['user','User','USER']:
        user_menu()
    elif a  in ['admin','Admin','ADMIN']:
        pswd()
        main_menu()
    else:
        print("Your entry is invalid")


        
def main_menu():
    print("^"*100)
    print(' R E P O R T       C A R D         M E N U ')
    print("^"*100)
    print("\n1.  Add Student")
    print("\n2. Delete the Student Record")
    print("\n3. Modify Student Record")
    print("\n4. Add Marks to New Student")
    print("\n5. Delete the Marks Record of Student")
    print("\n6. Modify Student's Report")
    print("\n7. Search Menu")
    print("\n8. Report Menu")
    print("\n9. Display Menu")
    print("\n10. Close application")
    print('\n\n')
    choice=int(input("Enter your choice......:"))
    if choice == 1:
        add_student()
    if choice==2:
        delete_student()
    if choice == 3:
        modify_student()
    if choice == 4:
        add_marks()
    if choice==5:
        delete_marks()
    if choice == 6:
        modify_marks()
    if choice == 7:
        search_menu()
    if choice == 8:
        report_menu()
    if choice==9:
        table_view()
    if choice == 10:
        print("\n\n\nT H A N K\t Y O U")
        print(exit())
admin_user()
































