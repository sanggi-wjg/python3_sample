import chardet

file = open('ADBanner.xml', mode = 'rb')
result = chardet.detect(file.read())
print(result)

for f in file.readlines():
    print(f)

file.close()
