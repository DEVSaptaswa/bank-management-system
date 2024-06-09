def create(obj) :
    curobj = obj.cursor()
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    email = str(input("Enter your email address: "))

    query = f"insert into users (first_name, last_name, email) values ('{fname}', '{lname}', '{email}')"
    curobj.execute(query)
    obj.commit()

    query = "select id from users"
    curobj.execute(query)
    data = curobj.fetchall()
    print(f"Account created successfully.\nYour account number is: {data[-1][0]}")
