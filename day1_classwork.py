'''
A juice shop sells three types of drinks: apple, orange, and grape. You are asked to calculate the total volume of juice sold in one day.
The shop sold:
15.5 liters of apple juice
20 liters of orange juice
10.25 liters of grape juice
Your task:
Store the volume of each juice in separate variables.
Calculate the total volume sold.
Print the total volume.
Convert the total volume to an integer and print it.
Convert the total volume to a string and print it with a message.
Add a random number between 5 and 10 (representing additional bonus liters) and print the final total
'''

#Store the volume of each juice in separate variables.
apple = 15.5
orange = 20
grape = 10.25

#Calculate the total volume sold.
total = apple+orange+grape

#Print the total volume.
print (total)
print(type(total))

#Convert the total volume to an integer and print it.
total = int(total)
print (total)
print (type(total))

#Convert the total volume to a string and print it with a message.
total = str(total)
print("the total volum as string :",total)
print("the data type of totla after conversion:",type(total))