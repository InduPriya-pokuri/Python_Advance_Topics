file=open('data.txt')
data=file.read()
count=0
for line in data.split('\n'):
    for word in line:
        for ch in word:
            if ch!=' ':
                count+=1

print("no.of characters are ",count)
print(len(data))

