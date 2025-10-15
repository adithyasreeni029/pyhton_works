'''
A grocery store wants to calculate the final bill for a customer.
The store has 3 products: rice, sugar, and oil. Each product has a fixed price per kilogram:
Rice: ?45 per kg
Sugar: ?40 per kg
Oil: ?130 per kg
Assume a customer bought:
3 kg of rice
2.5 kg of sugar
1.8 kg of oil
Your task:
Use variables to store the prices and quantities.
Use appropriate data types.
Calculate and print the total price for each item and the final total bill.
Show the total bill as an integer and also as a string.
Convert the float values where needed using explicit conversion.
Use random number generation to add a random ?5–?10 delivery charge.
Show the final bill amount including delivery charge.
'''
import random
#price of the product per kg
rice_p,sugar_p,oil_p = 45,40,130
#quantity of the product which bought by customer
rice_qu,sugar_qu,oil_qu = 3,2.5,1.8

#Calculate and print the total price for each item and the final total bill.
rice_t = rice_p*rice_qu
sugar_t = sugar_p*sugar_qu
oil_t = oil_p*oil_qu
final_bill = rice_t+sugar_t+oil_t
print("total price for rice :",rice_t)
print("total price for sugar :",sugar_t)
print("total price for oil :",oil_t)
print("final total bill :",final_bill)

#Show the total bill as an integer and also as a string.
final_bill = int(final_bill)
print("totla bill as integer :",final_bill)
print("datatype of final bill after type conversion :",type(final_bill))

final_bill_s = str(final_bill)
print("final bill as string :",final_bill_s)
print("datatype of final bill after type conversion:",type(final_bill_s))

#Use random number generation to add a random ?5–?10 delivery charge.
#Show the final bill amount including delivery charge.
delivary_charge = random.randrange(5,10)
print("delivary charge:",delivary_charge)
print("total bill including delivary charge :",final_bill+delivary_charge)