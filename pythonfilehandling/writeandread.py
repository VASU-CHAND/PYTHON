file=open("data.text", "w+")
file.write("Hello")
file.seek(0)
line=file.read()
print(line)
file.close()
#file may not exist 
# it'll be created 
#old data deleted 
# for read and write file must already exist
# it does not delete old content