
f = open("demo.txt", "w")
f.write("ABCDEFGHIJ")
f.close()

f = open("demo.txt", "r")

print("Position:", f.tell())

print("Data:", f.read(3))
print("Position:", f.tell())

f.seek(5)
print("After seek:", f.tell())

print("Remaining Data:", f.read())

f.close()
