import csv
import math
from random import randrange
print 'input parameter k'
k=raw_input()

f = open('ecoli.csv', 'rU') # opens the csv file
try:
	reader = csv.reader(f)  
	flag=1
	lines=-1
	tuples=[]				#data structure to hold attributes of examples
	classs=[]				#data structure to hold class of examples
	for row in reader:   # iterates the rows of csv files
		if flag==0:			# gets the examples and the seventh field class and store it
			tuples.append(row)
			classs.append(row[7])
		if flag==1:			# gets the first row of our file and stor the attributes
			attributes=row	#data structure to store names of the attributes
			flag=0
		
		lines=lines+1

finally:		# to close our csv file
	f.close()	

	
#------------------normalization starts------------------#	
for z in range (0,7):#loop for all 7 attributes
	min=float(tuples[0][z])
	max=float(tuples[0][z])
	for data in tuples:#calculating min and max for each attributes
		if float(data[z])<min:
			min=float(data[z])
		if float(data[z])>max:
			max=float(data[z])
	for i in range(0,len(tuples)):
		temp=float((float(tuples[i][z])-min)/float(max-min))# normalized value of attribute for that example data
		tuples[i][z]=float(temp)
#------------------normalization ends------------------#
	
	
training_set=[]			#will hold training examples
testing_set=[]			#will hold testing examples
indices_used=[]			#will store which examples(indices) of our total 336 examples have already been taken in testing examples.

iterations=math.ceil(float(lines)/float(k)) #total no. of examples there will be in our testing_set

def getrandom_index():#self explanatory
	global random_index
	random_index = randrange(0,len(tuples))
	for i in indices_used:#to check the random index we recieved has already been used or not
		if i==random_index:
			getrandom_index()

for i in range(0,int(iterations)):#will populate testing examples set
	global random_index
	getrandom_index()
	indices_used.append(random_index)	
	testing_set.append(tuples[random_index])

for i in range(0,lines):#will populate remaining k-1/k tuples into training set
	flag=1
	for j in indices_used:#checking whether this particular example has been used in testing set or not.
		if i==j:
			flag=0
	if flag==1:#if not used in testing set,insert it into training set
		training_set.append(tuples[i])

#printing the results
print 'There are ' +str(len(testing_set))+ ' testing sets and these are they,'
for data in testing_set:
	print data
print '------------------------------------------------------------------'

print 'There are ' +str(len(training_set))+ ' training sets and these are they,'
for data in training_set:
	print data
	








	
  
	

