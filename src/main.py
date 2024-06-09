import mysql.connector as scon
from welcome import welcome
from create import create

DBobj = scon.connect(host="localhost", user="root", passwd="090038", database="bank")
if DBobj.is_connected() == False:
    print("Database connection failed...")
else:
    a = welcome()
    if a == 1:
        create(DBobj)
DBobj.close()