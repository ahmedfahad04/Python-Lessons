data = "istiaq ahmed fahad"

encript = ""

for i in range(len(data)):
    x = (ord(data[i]) - 97 + 1) % 26
    x = chr(x+97)
    encript += x

print("Actual Text: ", data)
print("Encripted Text: ", encript)

decript = ""

for i in range(len(encript)):
    x = (ord(encript[i])+97-1) % 26
    x = chr(x+97)
    decript += x

print("Decripted Text: ", decript)
