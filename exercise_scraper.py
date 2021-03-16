from datetime import datetime
import time
testing = open("testing.txt", "w+")
fruits = ["apple", "banana", "cherries"]

counter = 0
while counter < len(fruits):
    testing.write(fruits[counter] + " worked \n")
    print("Added index " + str(counter))
    counter += 1
#for i in (fruits):


testing.close()