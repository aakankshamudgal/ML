fd = "new.txt"
file2=open(fd,'w')
file2.write("hi")
file2.close()
file2 = open(fd, 'r')
text = file2.read()
print(text)
new=open()
