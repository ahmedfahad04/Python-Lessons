# Basic String Operation

name = "Istiaq Ahmed Fahad"  # same delimiter must("" means double qutation)
ch = name.replace("h", "H")
print(ch)

start = name.startswith("Istiaq")  # starts name with specific word
print(start)

cut = name[:-3]  # skip last 3 words
print(cut)

print(name.find("Z"))  # find character at certain index

parts = name.split()  # split words
print(parts)

# files
print("Info of Files: ")
infile = open("input.txt", "r")

data = [lines for lines in infile]

print(data)
con = " ".join(data)  # concatenate words of strings
ex = ["book", "pen", "cutter"]
p = ", ".join(ex)           # toooooooo important
print(p)

print("Concatenated Data:\n", con)
lin = con.splitlines()  # split words basis of new line
print(lin)

print(name.upper())  # upper, lower, title

# useful built in function:
a = "123456"
print(a.isdigit())  # str of only digits
b = "IIT"
print(b.isalpha())  # str of only letter
c = "BSSE12"
print(c.isalnum())  # mixture of digits and letters
d = "ahmedfahad"
print(d.islower())  # if all letter are in lower form
e = "AHMED"
print(e.isupper())  # if all letter are in upper case form
f = "       "
print(f.isspace())  # if only spaces, tabs are contained
infile.close()

# print("New DATA: ")
# pairs = open("input.txt", "r")
# data = pairs.readlines()
#
# print(data)
# pair = list()
# for line in data:
#     d = line.split()
#     for p in d:
#         p = p[1:-1]
#         a, b = p.split(',')
#         pa = (float(a),float(b))
#         pair.append(pa)
#
# print(pair)

# with open("input.txt", "r") as infile:
#     lines = infile.readlines()
# # Analyze the contents of each line
#     pairs = [] # list of (n1, n2) pairs of numbers
#     for line in lines:
#         words = line.split()
#         for word in words:
#             word = word[1:-1] # strip off parenthesis
#             n1, n2 = word.split(",")
#             print(n1)
#             n1 = float(n1); n2 = float(n2)
#             pair = (n1, n2)
#             pairs.append(pair)
#     print(pairs)
#
#     infile.close()

# great example of slicing************
with open("input.txt", "r") as file:
    f = file.readlines()
    tp = []
    for line in f:
        x = line[2:line.find("y")]
        x = x.rstrip()

        y = line[line.find("y=")+2:line.find("z")]
        y = y.strip()

        z = line[line.find("z=")+2:]
        z = z.strip()

        tp.append((float(x),float(y),float(z)))

    file.close()
    print(tp)


import pprint
pprint.pprint(tp)
# --------------------------------------------------------------------------------------