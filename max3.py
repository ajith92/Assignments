import sys
list1=[]
if len(sys.argv)==4:
	k=1
	for i in range(2,4):
		if(int(sys.argv[i])>int(sys.argv[k])):
			k=i
	print "largest of 3 is : ",sys.argv[k]
else:	
	print "Enter 3 numbers : "
	for x in range(0,3):
		list1.append(int(raw_input()))
	k=0
	for i in range(1,3):
		if(list1[i]>list1[k]):
			k=i
	print "largest of 3 is : ",list1[k]
