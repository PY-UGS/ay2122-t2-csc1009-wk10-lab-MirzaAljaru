def average(x, y):
    avg = (x + y) / 2
    return avg


x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
avg = average(x, y)
print("The average of " + str(x) + " and " + str(y) + " is : " + str(avg))
