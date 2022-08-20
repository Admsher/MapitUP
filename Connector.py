import mysql.connector

mydb =mysql.connector.connect(host="localhost",user="root",passwd="")

print(mydb)

mycursor=mydb.cursor()




if(mydb):
    print("Connected")
else:
    print("Cannot Connect")
mycursor.execute("show databases")
for db in mycursor:
    print(db)