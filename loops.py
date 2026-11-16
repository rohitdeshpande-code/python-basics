
#if else

greeting = "Good Morning"
a = 4
#if greeting == "Good Morning" :
if a > 2:
    print("Condition Matches")
else:
    print("Condition do not matches")
print("If else condition code is completed")

print('--------------------------------------------------')

#for loop

obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i*2) #4,6,10,14,18

print('--------------------------------------------------')

# Sum of first 5 natural numbers 1+2+3+4+5 = 15
#range(i,j) => i, j-1

summation = 0

for j in range(1, 6):  #for(i=0; i<5; i++)
    summation = summation + j
    print(summation) #1,3,6,10,15
print('--------------------------------------------------')
print(summation) #15

print('--------------------------------------------------')

for k in range(1, 10, 2):
    print(k) #1,3,5,7,9

print('-------------SKIPPING FIRST INDEX----------')

for l in range(10):
    print(l) #0,1,2,3,4,5,6,7,8,9

print('--------------------------------------------------')

num = [1, 2, 3, 4, 5]
for i in num:
    print(i*2)
print('--------------------------------------------------')
for j in range(1, 5):
    print(j)