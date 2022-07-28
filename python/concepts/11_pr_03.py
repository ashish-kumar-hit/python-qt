# Create a class with a class attribute a; Create an object from it and set a directly using
# object a = 0. Does this charge the class attribute
class Sample:
    a = "Ashish"
obj = Sample()
obj.a = "Aarush" # Sets Instance Attributes
Sample.a = "Aarush" # Change class Attribute
print(Sample.a)
print(obj.a)
print(Sample.a)
