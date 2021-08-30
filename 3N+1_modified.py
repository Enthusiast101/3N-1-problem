# 3N+ 1
limit = int(input("Enter the limit of list:- "))
ly = []
for number in range(2, limit+1):
    ly.append(number)
    while number > 1:
        if number % 2 == 0:
            number = int(number / 2)
            ly.append(number)
        else:
            number = int(3 * number + 1)
            ly.append(number)
    print(ly)
    ly.clear()

