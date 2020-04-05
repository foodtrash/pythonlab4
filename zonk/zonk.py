def score(selection):
	rule=[1,2,3,4,5,6]
	total=0
	number=0
	count6dif=0
	count3pair=0
	for x in rule:
		match =0
		for y in selection:
			if y==x:
				match=match+1
				number=y
		if match==1:
			count6dif+=1
			if count6dif==6:
				total=1500
			elif number==5 or number==1:
				if number==5:
					total+=50
				elif number==1:
					total+=100
		elif match==2:		
			count3pair+=1
			if count3pair==3:
				total=750
				continue
			elif number==5 or number==1:
				if number==5:
					total+=100
				if number==1:
					total+=200
		elif match>=4:
			if number==1:
				total+=1000*(match-2)
			else:
				total+=number*100*(match-2)
		elif match==3:
			if number==1:
				total+=1000
			else:
				total+=number*100
	return total


passed=0
if score([2,2,2,1,1,1])==1200:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([2,3,2,2,3,3])==500:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([5,5,3,2,3,3])==400:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([6,5,4,3,2,1])==1500:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([3,4,1,6,2,5])==1500:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([2,2,3,3,5,5])==750:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([1,1,1,1,1,1])==4000:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([2,2,2,2,2,2])==800:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([3,3,3,3,3,3])==1200:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([4,4,4,4,4,4])==1600:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([5,5,5,5,5,5])==2000:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([6,6,6,6,6,6])==2400:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([1,3,3,3,1,1])==1300:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([5,1,1,1,1,5])==2100:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([5,3,3,3,3,3])==950:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([4,4,4,4,4,5])==1250:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([1,1,2,2,3,3])==750:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([6,6,6,1,6,6])==1900:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([6,6,1,1,6,6])==1400:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([2,2,2,2,1,2])==700:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
if score([3,3,3,1,5,5])==500:
	passed+=1
	print(":passed:")
else:
    print(":denied:")
print(passed)

