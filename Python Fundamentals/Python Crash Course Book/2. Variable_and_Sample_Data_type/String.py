data = "istiaq ahMED fahad"

print("Using Title Method: " + data.title())

print("Using Upperclass Method: "+ data.upper())

print("Using Lowerclass Methon: "+ data.lower())

verb = "is at"

clg = "University of Dhaka"

sen = data.title() + " "+ verb + " " +clg
print("Using Concatenation: "+ sen)

garbage = "     Hello Mango People  "
print("With white space: "+garbage+data.title())
garbage = garbage.strip()
print("Without whitespace: "+garbage+data.title())
garbage = "     Hello Mango People  "
garbage = garbage.rstrip()
print("Without whitespace: "+garbage+data.title())
garbage = "     Hello Mango People  "
garbage = garbage.lstrip()
print("Without whitespace: "+garbage+data.title())

