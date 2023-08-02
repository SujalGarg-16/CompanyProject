import tabulate as t
import mysql.connector as m

a=m.connect(host="localhost",user="root",password="",database="employee")
b=a.cursor()

def insert_record():
    print("\n\t\t********ENTER EMPLOYEE DETAILS********\n")
    x=int(input("ENTER EMPLOYEE ID NUMBER:"))
    y=input("ENTER EMPLOYEE NAME:")
    z=int(input("ENTER EMPLOYEE SALARY:"))
    t=input("ENTER DATE OF JOINING:")
    a1=int(input("ENTER EMPLOYEE PHONE NUMBER:"))
    q="insert into company values('{}','{}','{}','{}','{}')".format(x,y,z,t,a1)
    b.execute(q)
    a.commit()
    print("\n\t\t********DATA INSERTED SUCCESSFULLY********\n")

def search_record():
    print("\n\t\t*********SEARCH MENU***********\t")
    print("1.SEARCH BY EMPLOYEE ID NO:\n2. SEARCH BY EMPLOYEE NAME:\n3. EXIT\n****ENTER*****")
    choice=int(input())
    if choice==1:
        ad=int(input("ENTER EMPLOYEE ID NUMBER:"))
        q="select * from company where Eid='{}'".format(ad)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t****NO DATA FOUND*****\n")
        else:
            print(t.tabulate(res,headers=['employee id','employee name','employee salary','employee date of joining','employee phone number'
                                          ],tablefmt='pretty'))
    elif choice==2:
        cd=input("\n\t\t----ENTER EMPLOYEE NAME:------\n")
        q="select * from company where ename='{}'".format(cd)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t******NO DATA FOUND********\n")
        else:
            print(t.tabulate(res,headers=['employee id','employee name','employee salary','employee date of joining','employee phone number'
                                          ],tablefmt='pretty'))
def delete_record():
    print("\n\t\t*********ENTER WHAT YOU WANT TO DELETE*************\n")
    print("1.DELETE BY EMPLOYEE ID NO:\n2. DELETE BY EMPLOYEE DATE OF JOINING:\n3. EXIT\n*******ENTER******")
    choice=int(input())
    if choice==1:
        ad=int(input("ENTER EMPLOYEE ID NUMBER:"))
        q="select * from company where Eid='{}'".format(ad)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("\n\t\t*****NO DATA FOUND*******\n")
        else:
            print(t.tabulate(res,headers=['employee id','employee name','employee salary','employee date of joining','employee phone number'
                                          ],tablefmt='pretty'))
            q="delete from company where Eid='{}'".format(ad)
            b.execute(q)
            a.commit()
            print("\n\t\t------DATA DELETED SUCCESSFULLY--------\n")
    elif choice==2:
        cd=input("\n\t\t-------ENTER EMPLOYEE DATE OF JOINING:--------\n")
        q="select * from company where edoj='{}'".format(cd)
        
        b.execute(q)
        
        res=b.fetchall()
        
        if len(res)==0:
            print("\n\t\t****NO DATA FOUND******\n")
        else:
            print(t.tabulate(res,headers=['employee id','employee name','employee salary','employee date of joining','employee phone number'
                                          ],tablefmt='pretty'))
            q="delete from company where edoj='{}'".format(cd)
            b.execute(q)
            a.commit()
            print("\n\t\t-------DATA DELETED SUCCESSFULLY--------\n")
def update_record():
    print("\n\t\t***********UPDATE MENU*****************\n")
    print("1.UPDATE BY EMPLOYEE NAME:\n2. UPDATE BY EMPLOYEE ID NO:\n***********ENTER**********")
    choice=int(input())
    if choice==1:
        ad=input("****ENTER EMPLOYEE NAME******")
        q="select * from company where ename='{}'".format(ad)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("******NO DATA FOUND*******")
        else:
            print(t.tabulate(res,headers=['employee id','employee name','employee salary','employee date of joining','employee phone number'],tablefmt='pretty'))
            print("PRESS 1 TO UPDATE EMPLOYEE NAME:\n")
            print("PRESS 2 TO UPDATE EMPLOYEE ID NO:\n")
            print("PRESS 3 TO UPDATE EMPLOYEE SALARY:\n")
            print("PRESS 4 TO UPDATE EMPLOYEE DATE OF JOINING:\n")
            print("PRESS 5 TO UPDATE EMPLOYEE PHONE NUMBER:\n")
            choice=int(input())
            if choice==1:
                ad1=input("ENTER NEW EMPLOYEE NAME:")
                q="update company set ename='{}' where ename='{}'".format(ad1,ad)
                b.execute(q)
                a.commit()
                print("\n\t\t---------DATA UPDATED SUCCESSFULLY---------\n")
            if choice==2:
                ad2=int(input("ENTER NEW EMPLOYEE ID NO:"))
                q="update company set eid='{}' where ename='{}'".format(ad2,ad)
                b.execute(q)
                a.commit()
                print("\n\t\t---------DATA UPDATED SUCCESSFULLY---------\n")
            if choice==3:
                ad3=int(input("ENTER NEW EMPLOYEE SALARY:"))
                q="update company set esalary='{}' where ename='{}'".format(ad3,ad)
                b.execute(q)
                a.commit()
                print("\n\t\t---------DATA UPDATED SUCCESSFULLY---------\n")
            if choice==4:
                ad4=input("ENTER NEW EMPLOYEE DATE OF JOINING:")
                q="update company set edoj='{}' where ename='{}'".format(ad4,ad)
                b.execute(q)
                a.commit()
                print("\n\t\t---------DATA UPDATED SUCCESSFULLY---------\n")
            if choice==5:
                ad5=int(input("ENTER NEW EMPLOYEE PHONE NO:"))
                q="update company set epno='{}' where ename='{}'".format(ad5,ad)
                b.execute(q)
                a.commit()
                print("\n\t\t---------DATA UPDATED SUCCESSFULLY---------\n")
                
    if choice==2:
        cd=input("******ENTER EMPLOYEE ID NO:********")
        q="select * from company where eid='{}'".format(cd)
        b.execute(q)
        res=b.fetchall()
        if len(res)==0:
            print("*********NO DATA FOUND***********")
        else:
            print(t.tabulate(res,headers=['employee id','employee name','employee salary','employee date of joining','employee phone number'
                                      ],tablefmt='pretty'))
            choice=input("-----DO YOU WANT TO UPDATE------PRESS 'Y' FOR YES ")
            if choice in 'yY':
                
                ad=input("*****ENTER NEW EMPLOYEE ID NO:*******")
                q="update company set eid='{}' where eid='{}'".format(ad,cd)
                b.execute(q)
                a.commit()
                print("********* UPDATE SUCCESSFULLY********")
    
        
def export_data():
    '''
    com="select * from company order by eid desc"
    b.execute(com)
    f=open("records.csv","w",newline="")
    import csv
    import os
    x=csv.writer(f)
    l=[]
    for i in b:
        l.append(i)
    x.writerows(l)
    f.close()
    print("\n\n\t\t-----Data Saved to file----")
    print("location of file created= ",os.getcwd())
    '''
    cd=input("*******ENTER FILE NAME*********")
    cd=cd+".csv"
    try:
        
        f=open(cd,"r")
        print("\n---File already Present---")
        f.close()
    except:
        q="select * from company "
        b.execute(q)
        f1=open(cd,"w",newline="")
        import csv
        import os
        x=csv.writer(f1)
        l=[]
        for i in b:
            l.append(i)
        x.writerows(l)
        f1.close()
        print("\n\t\t-------Data Saved to file-------")
        print("location of file created=",os.getcwd())

