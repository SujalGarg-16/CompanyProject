import function1

while True:
    print("\n\t\t***********EMPLOYEE MANAGEMENT SYSTEM****************\n")
    print("1.Employee Data insert\n2.Employee Data Search\n3.Employee Data Delete")
    print("4.Employee Data Update\n5.Export Employee All data to File with Location\n6.EXIT")
    choice=int(input("\n\tENTER YOUR CHOICE=  "))
    if choice==1:
        try:
            function1.insert_record()
        except:
            print("-------ERROR COMES-----DATA NOT SAVED")

    if choice==2:
        try:
            function1.search_record()
        except:
            print("--------ERROR COMES-----DATA NOT SAVED")

    if choice==3:
        try:
            function1.delete_record()
        except:
            print("---------ERROR COMES-----DATA NOT SAVED")
    if choice==4:
        try:
            function1.update_record()
        except:
            print("----------ERROR COMES-----DATA NOT SAVED")
    if choice==5:
        function1.export_data()
    if choice==6:
        break
print("\n*********THANKYOU FOR USING OUR SOFTWARE************")        
