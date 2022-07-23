import re

with open('grav.txt') as f:
    data=f.readlines()
idx=[]
n=len(data)
for i in range(n):
    if mathches := re.search("Line*",data[i]):
        idx.append(i)
j=idx[0]+2
i=1



file = open("data.csv","w")

while j<n:
    if i<len(idx) and j<idx[i]:
        if data[j].isspace()==False:
            file.write(data[j])
        j+=1
    elif i==len(idx):
        if data[j].isspace()==False:
            file.write(data[j])
        j+=1
    else:
        j=idx[i]+2
        i+=1
file.close()


