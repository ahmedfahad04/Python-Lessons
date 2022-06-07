#8.1 message

def display_message():
    print("Its a great book. Its quit convenient for me to learn the basic of Python.")

display_message()
print("---------------------------------------------------")

#8.2 favorite Book

def favorite_book(Title):
    print("ONe of my facorite books is "+Title.title())

book = input("Enter book name: ")
favorite_book(book)

print("---------------------------------------------------")