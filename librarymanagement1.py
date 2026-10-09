# this is our code for library management system

# make library class 
# make inctence variables like no_of_books and books 
# with a program to create a library class and show how you can print all books, add a book and get the number of books using method
# ask the user which books he wants to take by asking index no.

class library:
    no_of_books = 11
    books = ["rework","deep work","TSANGAF","everything is fucked","thinking,fast and slow","phycology of money","the alminack of naval ravikant","blue ocean strategy","zero to one","ikigai","meditations"]

b = library()
c = library.no_of_books
d = library.books
a = int(input("0 for no of books and 1 for all books: "))
if(a==0):
    print(c)
else:
    for index,book in enumerate(d):
        print(index, book)
print()
input()
f = input("enter index of books you want sapreted by coma: ")
try:
    h = [int(index.strip()) for index in f.split(',')]
except ValueError:
    print("invalid input: please enter coma separated numbers for input.")
    exit()
print("selected items: ")
for index in h:
    if 0 <= index < len(d):
        print(f"book for {index}: {d[index]}")
    else:
        print(f"index {index} is out of bounds for the list")
j = len(d)
i = len(f)
print(f"books remaining in library: ",j-i+1)