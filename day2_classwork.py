'''
You work for a bookstore that generates receipts for customers. 
Your task is to prepare a simple receipt using string techniques.
Here’s what you need to do:
Create a multiline string to store the receipt header.
The customer bought 2 items:
Book Title: "Python Basics" – ₹450
Book Title: "Data Science Intro" – ₹600
For each line showing the book and price, use a single string with basic 
{} placeholders and call format() once to fill in the values.
Calculate the total price and add it similarly.
Concatenate a thank-you message at the end.
Make sure the output uses newline (\n) and tab (\t) for readability.
Display the entire receipt in uppercase.
'''
#Create a multiline string to store the receipt header.
bookstore = '''Bookstore,
Palarivattom, Kochi
Date:2025-10-13'''
print(bookstore.upper())
#For each line showing the book and price, use a single string with basic 
#{} placeholders and call format() once to fill in the values.
book1 = "Python Basics"
price1=450
book2= "Data Science Intro"
price2=600
details = "\nBook\t\t\tPrice\n{0}\t\t\u20B9{1}\n{2}\t\u20B9{3}\n"
print(details.format(book1,price1,book2,price2).upper())
print("Total :\u20B9",price1+price2)
str1="\nThank"
str2="You :)"
print(str1.upper()+" "+str2.upper())
