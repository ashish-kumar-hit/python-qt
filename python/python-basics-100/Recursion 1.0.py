# Find the sum element inside the list using Recursion
l=[1,2,3,4]
def find_sum(l):
    # Base Case:
    if len(l) == 0:
        return 0
# Recursive Case
# s[0] + find_sum(<Sequence without first element>)
    else:
        return l[0] + find_sum(l[1:])
print(find_sum(l))
