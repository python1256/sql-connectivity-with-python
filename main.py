import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="")
print("connection established")
mydb=db.cursor()
mydb.execute("USE pa")
mydb.execute("SHOW DATABASES")
for x in mydb:
    print(x)

while(1):
    insert_stmt=("INSERT INTO REGISTER(first_name,last_name,Email,mobile_no)"
                 "VALUES(%s,%s,%s,%s)")
    first_name=input("enter name")
    last_name=input("last name")
    Email=input("enter email")
    mobile_no=input("enter mobile number")
    data=(first_name,last_name,Email,mobile_no)
    try:
        
        mydb.execute("SELECT Email FROM REGISTER")
        MY_EMAIL=mydb.fetchall()
        for x in my_email:
            if(MY_EMAIL!=Email):
                mydb.execute(insert_stmt,data)
                db.commit()
                print("data inserted")                
                
            
    except:
        db.rollback()
        print("email aready in use")
    
    print("want to enter more recods[y/n]")
    ans=input()
    if(ans=="n" or ans=="N"):
        n=0
        break






    


