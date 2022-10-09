# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


x = []
number = ''
with open("input_10.txt") as file:
    int_number = file.readlines()
    for e in range(1,len(int_number)) :
        number = number +int_number[e]
        x.append(int(number))
        number = ''
print (x)
x1 = []


for i in x:
 if i not in x1:
  x1.append(i)
print(x1)
chast = []
sumchast = []
suma = 0
for y in x1:
 h = 0
 for k in x:
  if(y==k):
   h += 1
 chast.append(h)
 suma += h
 sumchast.append(suma)
print(chast)
for y in range(len(x1)):
  print("Chislo = ",x1[y]," Chastota = ",chast[y]," SukupChast = ", sumchast[y])
mode = 0
b=0
med = 0
if len(x) % 2 == 0:
 med = (x[int(len(x)/2)]+x[int(len(x)/2-1)])/2
else:
 med = x[int((len(x)-1)/2)]

print("Mediana = ", med)
for i in range(len(x)):
 c=0
 for j in range(len(x)):
  if(x[i]==x[j]):
   c += 1
 if(c>b):
  b=c
  mode = x[i]

print("Moda = ", mode)

avg = sum(x) / len(x)
disp = sum((y-avg)**2 for y in x) / len(x)
print("disp = ", disp)
inqRan = math.sqrt(disp)
print("Ser kv vidhyl = ", inqRan)
import matplotlib
import matplotlib.pyplot as plt
plt.hist(x,bins = len(x)*5, color ="yellowgreen")
plt.xlabel('Chislo')
plt.ylabel('Chastota')
plt.show()
my_file = open("ResultInput_"+str(len(x))+".txt", "w+")
my_file.write("Data from input_"+str(len(x))+".txt")
for y in range(len(x1)):
    my_file.write("\nChislo = "+ str(x1[y])+" Chastota = "+str(chast[y])+" SukupChast = "+str(sumchast[y]))
my_file.write("\nMediana = "+ str(med)+ "\nModa = "+str(mode)+"\nSer kv vidhyl = " +str(inqRan)+ "\nDisp = "+ str(disp))
my_file.close()