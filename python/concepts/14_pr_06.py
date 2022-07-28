# Can you change the self parameter inside a class to something else (say harry).
# Try Changing self to 'slf' or 'harry' and see the effects
class Sample:
    a = "Harry"
    def __init__(slf,name):
        slf.name = name

obj = Sample("Harry")
print(obj.name)
