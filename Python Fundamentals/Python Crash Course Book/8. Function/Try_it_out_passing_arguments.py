#8.3 t-shirt

def make_shirt(size,message):
    print("Size: "+size.upper()+ ", " +message)

make_shirt('xxl','its perfect for me') # positional arguments
make_shirt(size='xxl',message='Roar') # keyword arguments


print("-----------------------------------------------")
#8.4 large shirts

def make_shirt_2(size='large',msg='I love Python'):
    print("\nSize: "+size.upper()+ ", " +msg)


def make_shirt_3(size='medium',msg='I love Python'):
    print("\nSize: "+size.upper()+ ", " +msg)


def make_shirt_4(size='small',msg='I love Doraemon'):
    print("\nSize: "+size.upper()+ ", " +msg)


make_shirt_2()
make_shirt_3()
make_shirt_4()

print("--------------------------------------------------")
#8.5 cities

def describe_city(name,country="Bangladesh"):
    print(name.title()+" is in "+country.title())

describe_city("Dhaka","Bangladesh")
describe_city("Chattogram")
describe_city("Moscow","Russia")

print("-----------------------------------------------")



