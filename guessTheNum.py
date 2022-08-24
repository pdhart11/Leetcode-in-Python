import numpy as np
random_number = np.random.randint(100)
value = input("Enter a number: ")
count = 0
while count < 4:
    if int(value) == random_number:
        print("You won!")
        break
    else:
        value = input("Please try again: ")
        count = count + 1
if count == 4:
    print("Sorry you did not win. The number was " + str(random_number))
