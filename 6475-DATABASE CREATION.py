def Create_Database_Railway():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='Gagan@2005')    
    cursor=mycon.cursor()
    mycon.autocommit=True
    s1="create database railway"
    cursor.execute(s1)
    print('Database Created')
Create_Database_Railway()
