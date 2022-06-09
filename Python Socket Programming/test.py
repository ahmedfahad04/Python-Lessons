# import time
# file = open("demo.txt", "r")
# data = file.read()
# print(data)
# print(len(data))
#
#
# print(time.ctime(time.time()))
t = "10     Hello world"
msg = bytes(t, "utf-8")
print(int(msg[:6]))