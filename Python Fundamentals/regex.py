import re
ro = re.compile(r'\d{2}-\d{3}')

mo = ro.search("here is the num 22-333, 23-345")

#print(type( mo.group()))
#import pprint as p
#p.pprint(dir(re))


#ro1 = re.compile(r'\{\}')
#mo1 = ro1.search("{25{{2}{")
#mo2 = ro1.search("{}{{{}{}}}}{}")
#print("Ans: " + mo2.group())


#ro2 = re.compile(r'Wo((ha){3,})')
#mo3 = ro2.search(" happy boy..Wohahahahaha")
#print("Ans: " + mo3.group())


#ro2 = re.compile(r'\+880(\d{10})')
#strr = "+8801766610087,  +998010101, +8801815047916, +8806373737"
#mo3 = ro2.findall(strr)
#num = list(map(lambda x: '0'+str(x), mo3))
#print(mo3)
#print(num)


#ro4 = re.compile(r'\w+-?\d+')
#strrr = 'Hello people this radio-89 whats up2. Hope6'
#res = ro4.findall(strrr)
#print(res)


#email = re.compile(r'\w+@gmail.com|\w+@iit.du.ac.bd')
#str2 = "ahmedfahad3596@gmail.com fahad's mail and buzzsky786@gmail.com buzz's mail also bsse12@iit.du.ac.bd is another type of mail"
#track_mail = email.findall(str2)
#print(track_mail)


#nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
#names = "First Name: Istiaq Ahmed Last Name: Fahad Ali"
#print(nameRegex.findall(names))


#hello = re.compile(r'(wa)(ha)(hi)?')
#str4 = 'waha wa wahahi hi wahi wahahii'
#print(hello.findall(str4))


#namesRegex = re.compile(r'Agent \w+')
 
#x = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
#print(x)

agentNamesRegex = re.compile(r'Agent (\w)\w*')

y = agentNamesRegex.sub(r'\1*****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(y)

