#read input
f = open('adultdata.txt')
r = f.read().splitlines()
f.close()

#Preprocessing
data=[]
check=['?']
de=[]

del r[-1]
l=len(r)
print(l)
for i in range(0,l):
    data.append(i)
    data[i]=r[i].split(', ')  
    if set(check).issubset(set(data[i])):
        de.append(i)
    del data[i][-2]
    #I think that 'education_num', 'fnlwgt', 'capital-gain', 'capital-loss' can be neglected.
    del data[i][2]
    del data[i][3]
    del data[i][8]
    del data[i][8]
# print(len(de))
data = [data[i] for i in range(len(data)) if (i not in de)]


f = open('attribute.txt')
attr = f.read().splitlines()
f.close()
# count
attr_li = [a.split(', ') for a in attr]
# print(attr_li)
dict_less = []
dict_more = []
for i in range(len(attr_li)):
	dict_less.append(dict.fromkeys(attr_li[i],0))
	dict_more.append(dict.fromkeys(attr_li[i],0))

def age_judge(n):
	if n in range(0,20):
		n = '20'
	elif n in range(20,31):
		n = '30'
	elif n in range(30,41):
		n = '40'
	elif n in range(40,51):
		n = '50'
	elif n in range(50,61):
		n = '60'
	elif n in range(60,71):
		n = '70'
	elif n >= 71:
		n = '71'
	else:
		print(n)
	return n

def hour_judge(n):
	if n in range(0,11):
		n = '9'
	elif n in range(10,21):
		n = '19'
	elif n in range(20,31):
		n = '29'
	elif n in range(30,41):
		n = '39'
	elif n in range(40,51):
		n = '49'
	elif n in range(50,61):
		n = '59'
	elif n >= 61:
		n = '61'
	else:
		print(n)
	return n

yes = '<=50K'
no = '>50K'

for i in range(len(data)):
	# print(i)
	for j in range(len(data[i])):
		# print(j)
		if data[i][9] == yes:	
			if j == 0:
				age = age_judge(int(data[i][j]))
				dict_less[0][age] = dict_less[0][age] + 1
			elif j == 8:
				work_hour = hour_judge(int(data[i][j]))
				dict_less[8][work_hour] = dict_less[8][work_hour] + 1
			else:
				dict_less[j][data[i][j]] = dict_less[j][data[i][j]] + 1
		else:
			if j == 0:
				age = age_judge(int(data[i][j]))
				dict_more[0][age] = dict_more[0][age] + 1
			elif j == 8:
				work_hour = hour_judge(int(data[i][j]))
				dict_more[8][work_hour] = dict_more[8][work_hour] + 1
			else:
				dict_more[j][data[i][j]] = dict_more[j][data[i][j]] + 1

print('----')
print(dict_less)
print('----')
print(dict_more)

# calculate prob
L = len(data)
less = dict_less[9][yes]
more = dict_more[9][no]
less_p = less / L
more_p = more / L

def pro(attr, less_more):
	if less_more == yes:
		for a in dict_less:
			if attr in a:
				p_attr = a.get(attr) / less
	else:
		for a in dict_more:
			if attr in a:
				p_attr = a.get(attr) / more
	return p_attr

p_less = dict_less.copy()
p_more = dict_more.copy()
for i in p_less:
	for a in i.keys():
		i[a] = pro(a, yes)
		if i.get(a) < 0.000001:
			i[a] = 0.000001
for i in p_more:
	for a in i.keys():
		i[a] = pro(a, no)
		if i.get(a) < 0.000001:
			i[a] = 0.000001

def yesorno(data):
	def get_pro(attr, p_dict):
		p_attr = 1
		for i in p_dict:
			if attr in i :
				p_attr = i.get(attr)
		return p_attr
	p_yes = 1
	p_no = 1
	for a in data:
		p_yes = p_yes * get_pro(a, p_less)
		p_no = p_no * get_pro(a, p_more)
	p_yes = p_yes * less_p	
	p_no = p_no * more_p
	if p_yes >= p_no:
		data_label = yes
	else:
		data_label = no
	return data_label


