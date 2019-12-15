import Bayes_Classifier

f = open('adulttest.txt')
r = f.read().splitlines()
f.close()

#Preprocessing
data=[]
check=['?']
de=[]
del r[0], r[-1]
l=len(r)
print(l)
for i in range(0,l):
    data.append(i)
    data[i] = r[i].split(', ')
    data[i][-1] = data[i][-1].strip('.')  
    if set(check).issubset(set(data[i])):
        de.append(i)
    del data[i][-2]
    del data[i][2]
    del data[i][3]
    del data[i][8]
    del data[i][8]    
print(len(de))
data = [data[i] for i in range(len(data)) if (i not in de)]
print(len(data))

# test
right_num = 0
wrong_num = 0

for li in data:
    data_li = li[0:-1]
    if Bayes_Classifier.yesorno(data_li) == li[-1]:
        right_num += 1
    else:
        wrong_num += 1

print(right_num)
print(wrong_num)



