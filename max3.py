list1=[]
print "Enter 3 numbers : "

for x in range(0,3):
	list1.append(int(raw_input()))
k=0
for i in range(1,3):
	if(list1[i]>list1[k]):
		k=i
print "largest of 3 is : ",list1[k]
