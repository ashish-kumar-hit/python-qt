class Employee():
    company = "Goggle"
    salary = 100

harry = Employee()
rajni = Employee()
# Creating instance attributes salary for both the objects
#harry.salary = 300
# rajni.salary = 400
print(harry.salary)
print(rajni.salary)

# Below line throughs an Attribute Error as assress in not avialable
#print(rajni.address)
