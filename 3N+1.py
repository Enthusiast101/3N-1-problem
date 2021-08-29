# 3N +1:
import matplotlib.pyplot as plt
value = int(input("Enter the value:- "))
initial = 0
ly= [value]
lx =[0]
while value> 1:
    initial= initial+ 1
    if value%2== 0:
        value = value / 2
        ly.append(value)
    else:
        value = 3 * value + 1
        ly.append(value)
    lx.append(initial)
print(ly)
print(lx)
plt.xlabel("No. of iterations")
plt.ylabel("Values")
plt.plot(lx, ly)
plt.show()
