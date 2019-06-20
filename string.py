def conn():
    a=input("servername: ")
    b=input("dbname: ")
    c=input("username:")
    d=input("password: ")
    return a,b,c,d
a,b,c,d=conn()
print("servername= %s;dbname= %s;username= %s;password= %s" %(a,b,c,d))

