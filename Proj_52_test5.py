import pandas as pd
import numpy as np
import time
import math
import matplotlib.pyplot as plt 

Location_T = [380, 510]
Location_A = [439, 165]
Location_B = [660, 432]
Location_C = [138, 409]
Location_D = [447, 750]
Location_E = [223, 724]

x = [Location_T[0], Location_A[0], Location_B[0]
, Location_C[0], Location_D[0], Location_E[0]] 

y = [Location_T[1], Location_A[1], Location_B[1]
, Location_C[1], Location_D[1], Location_E[1]] 

xs = [Location_T[0], Location_A[0],Location_T[0], Location_B[0]
,Location_T[0], Location_C[0],Location_T[0], Location_D[0],Location_T[0], Location_E[0],Location_T[0]]

ys = [Location_T[1], Location_A[1],Location_T[1], Location_B[1]
,Location_T[1], Location_C[1],Location_T[1], Location_D[1],Location_T[1], Location_E[1],Location_T[1]] 

#Distance From T
dist_A = math.hypot(Location_A[0] - Location_T[0], Location_A[1] - Location_T[1])
dist_B = math.hypot(Location_B[0] - Location_T[0], Location_B[1] - Location_T[1])
dist_C = math.hypot(Location_C[0] - Location_T[0], Location_C[1] - Location_T[1])
dist_D = math.hypot(Location_D[0] - Location_T[0], Location_D[1] - Location_T[1])
dist_E = math.hypot(Location_E[0] - Location_T[0], Location_E[1] - Location_T[1])

All_Dist = []
All_Dist.append(dist_A)
All_Dist.append(dist_B)
All_Dist.append(dist_C)
All_Dist.append(dist_D)
All_Dist.append(dist_E)



plt.scatter(x,y)
plt.plot(xs, ys, 'r-o')

for x,y in zip(x,y):

    label = f"({x},{y})"

    plt.annotate(label, 
                 (x,y), 
                 textcoords="offset points",
                 xytext=(0,10), 
                 ha='center') 

plt.show()

#Current(Amper)
Current_A = 24
Current_B = 12
Current_C = 21
Current_D = 17
Current_E = 8

#Cable Diameter
Diameter = [0.010, 0.012, 0.014, 0.016, 0.018, 0.020, 0.024, 0.036]
Cable_Price = [9.60, 15.75, 15.83, 23.39, 28.77, 31.51, 44.93, 57.96]

left = [1, 2, 3, 4, 5, 6, 7, 8]

plt.bar(left, Cable_Price, tick_label = Diameter,
		width = 0.3, color = ['blue'])

plt.xlabel('Diameter')
plt.ylabel('Price')
plt.title('Cable Price Based On Diameter')
plt.show()

#cable price and distance between points to T
print('Distance Between A Point To T Points(m): ',dist_A)
for i in Cable_Price:
    print('Cable Price Of A Based On Diameters: ',i*dist_A)
print('\n')
print('Distance Between B Point To T Points(m): ',dist_B)
for i in Cable_Price:
    print('Cable Price Of B Based On Diameters: ',i*dist_B)
print('\n')
print('Distance Between C Point To T Points(m): ',dist_C)
for i in Cable_Price:
    print('Cable Price Of C Based On Diameters: ',i*dist_C)
print('\n')
print('Distance Between D Point To T Points(m): ',dist_D)
for i in Cable_Price:
    print('Cable Price Of D Based On Diameters: ',i*dist_D)
print('\n')
print('Cable Price Of E Based On Diameters: ',dist_E)
for i in Cable_Price:
    print('Cable Price Of E Based On Diameters: ',i*dist_E)

print('\n')
print('---------------------------')


#energy losses through the cable calculations
Part_1=[]
for i in All_Dist:
    Part_1.append((1.7) * (10**-5) * (i)) 
    
Part_2=[]
for i in Diameter:
    Part_2.append((3.14) * (i**2)/4)

R=[]
for i in Part_1:
    R.append(i/Part_2[0])
    R.append(i/Part_2[1])
    R.append(i/Part_2[2])
    R.append(i/Part_2[3])
    R.append(i/Part_2[4])
    R.append(i/Part_2[5])
    R.append(i/Part_2[6])
    R.append(i/Part_2[7])

print('-----------------------------------------------')

for i in R[0:8]:
    print('energy losses through the cable from T to A: ',Current_A*Current_A*i)

print('\n')
print('-----------------------------------------------')

for i in R[8:16]:
    print('energy losses through the cable from T to B: ',Current_B*Current_B*i)

print('\n')
print('-----------------------------------------------')

for i in R[16:24]:
    print('energy losses through the cable from T to C: ',Current_C*Current_C*i)

print('\n')
print('-----------------------------------------------')

for i in R[24:32]:
    print('energy losses through the cable from T to D: ',Current_D*Current_D*i)

print('\n')
print('-----------------------------------------------')

for i in R[32:40]:
    print('energy losses through the cable from T to E in : ',Current_E*Current_E*i)


Choose=input('Do You Want Optimize Outputs: (Y/N) ')
print(Choose)
if Choose=='Y':
    time.sleep(4)
    exit()
else:
    exit()

