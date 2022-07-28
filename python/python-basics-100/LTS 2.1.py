# Distance Between Two 3-D Points
# Option-1
l1 = [-3,4,-5]
l2 = [2,0,-5]
difference = ((l2[0]-l1[0])**2 +(l2[1]-l1[1])**2 +(l2[2]-l1[2])**2)**0.5
print(difference)

# Option-2
import math
addition = (l2[0]-l1[0])**2 +(l2[1]-l1[1])**2 +(l2[2]-l1[2])**2
distance = math.sqrt(addition)
print(distance)