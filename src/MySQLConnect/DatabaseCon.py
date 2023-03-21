import mysql.connector

#Creating Connection
mycon = mysql.connector.connect(host="localhost",user="root",password="Ashiv@0511")

cur = mycon.cursor()

try:
    dbs1 = cur.execute("show databases")
    #dbs2 = cur.execute("Use weekend3pm")
    #dbs = cur.execute("Create table amz_deal(trade_deal int,region varchar(10),primary key(trade_deal))")
    #dbs3 = cur.execute("show tables")

except:
    mycon.rollback()

for x in cur:
    print(x)
    
cur.close()
    
    
