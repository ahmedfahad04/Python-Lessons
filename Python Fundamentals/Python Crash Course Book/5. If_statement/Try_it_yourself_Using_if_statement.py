#5.8 hello admin

username = ['ahmedfahad','Mobin1234','MaxCurl','33Sakib33','khairul','admin']

for names in username:
    if names == 'admin':
        print("Hello Mr. Admin. Welcome to Codeforces")
    else:
        print("Hello "+names+" thank you for loggin in again")


print("--------------------------------------------------------------")
#5.9 no users

new_user = []
if len(new_user) == 0:
    print("We need to find some users!")
else:
    print("Hello everyone!")

print("--------------------------------------------------------------")
#5.10 checking username

current_users = ['ahmedfahad','Mobin1234','MaxCurl','33Sakib33','khairul','admin']

new_users = ['ahmedfahad','MaxCurl','saad','Sami123','Araf']

for names in new_users:
    if names in current_users:
        print("You have to enter new username.")
    else:
        print("This username is available")

print("--------------------------------------------------------------")
#5.11 ordinal numbers:

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in num:
    if i==1:
        print("1st")
    elif i==2:
        print("2nd")
    elif i==3:
        print("3rd")
    else:
        print(str(i)+"th")

print("--------------------------------------------------------------")