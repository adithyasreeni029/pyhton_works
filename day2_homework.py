'''Write a Python program that does the following:
Store a short paragraph about a Python course using a multiline string.
Display the length of the paragraph (number of characters).
Display the first and last characters in the paragraph.
Slice and print a short preview: the first 50 characters.
Replace all occurrences of the word "Python" with "PYTHON" (in all caps).
Convert the entire paragraph to lowercase.
Remove any extra whitespaces from the start or end.
Split the paragraph into individual words and print the list.
Check if the word "course" exists in the paragraph. Print a message if found.
Display the final message:
"The course description is {} characters long and has {} words." using the format() method.'''

#code
para = '''     A Python course introduces coding through simple, readable syntax.
It covers basics like variables, loops, and functions.
Students build small projects and automate tasks.
This Python course Perfect for beginners aiming at web, data, or AI fields'''
print("about Python course \n", para)
print("\nthe length of the paragraph :",len(para))
print("\nthe first and last charecters are",para[0],para[-1],"respectively")
print("\nthe first 50 characters :",para[:50])
print("\nreplacing python with PYTHON :\n",para.replace("Python","PYTHON"))
print("\nEntire paragraph in to lowercase :\n",para.lower())
print("\nRemoving extra whitespaces from the start or end if any :")
print(para.strip())
print("\nSpliting the paragraph into individual words:\n",para.split(","))
a="course" in para
print("\nChecking the word course in the paragraph it shows, ",a)
length=len(para)
word_count=len(para.strip())
message="\nThe course description is {} characters long and has {} words."
print(message.format(length,word_count))