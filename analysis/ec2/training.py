'''File for data preprocessing script 
Convert raw ms files into training data set 
'''
import numpy as np
import csv

# input files
files = [
# trial 1
'mass-scan-pos-neg-4-13-18-4600-20180622-142124.csv', # halo
'mass-scan-pos-neg-4-13-18-4607-20180622-150245.csv', # juul
'mass-scan-pos-neg-4-13-18-4608-20180622-151114.csv', # blu
'mass-scan-pos-neg-4-13-18-5923-20180726-131606.csv', # v2
# trial 2
'mass-scan-pos-neg-4-13-18-4619-20180622-184858.csv', # halo
'mass-scan-pos-neg-4-13-18-4615-20180622-182527.csv', # juul
'mass-scan-pos-neg-4-13-18-4623-20180622-190449.csv', # blu
'mass-scan-pos-neg-4-13-18-5930-20180726-140538.csv', # v2
# trial 3
'mass-scan-pos-neg-4-13-18-4663-20180625-174200.csv', # halo
'mass-scan-pos-neg-4-13-18-4659-20180625-172435.csv', # juul
'mass-scan-pos-neg-4-13-18-4667-20180625-180620.csv', # blu
'mass-scan-pos-neg-4-13-18-5938-20180726-145530.csv', # v2
# trial 4
'mass-scan-pos-neg-4-13-18-4697-20180626-160732.csv',# halo
'mass-scan-pos-neg-4-13-18-4690-20180626-153051.csv', #juul
'mass-scan-pos-neg-4-13-18-4701-20180626-162915.csv', # blu
'mass-scan-pos-neg-4-13-18-5955-20180726-173918.csv', # v2
# trial 5
'mass-scan-pos-neg-4-13-18-4840-20180628-172915.csv', # halo
'mass-scan-pos-neg-4-13-18-4836-20180628-171152.csv', # juul
'mass-scan-pos-neg-4-13-18-4841-20180628-173842.csv', # blu
'mass-scan-pos-neg-4-13-18-5970-20180727-124102.csv', # v2
# trial 6
'mass-scan-pos-neg-4-13-18-4897-20180702-165302.csv', # halo
'mass-scan-pos-neg-4-13-18-4893-20180702-162712.csv', # juul
'mass-scan-pos-neg-4-13-18-5115-20180710-124320.csv', # blu
'mass-scan-pos-neg-4-13-18-5976-20180727-133614.csv', # v2
# trial 7
'mass-scan-pos-neg-4-13-18-5110-20180710-122638.csv', # halo
'mass-scan-pos-neg-4-13-18-5098-20180709-191303.csv', # juul
'mass-scan-pos-neg-4-13-18-5122-20180710-131215.csv', # blu
'mass-scan-pos-neg-4-13-18-5982-20180727-143114.csv', # v2
#trial 8
'mass-scan-pos-neg-4-13-18-5166-20180711-143331.csv', # halo
'mass-scan-pos-neg-4-13-18-5160-20180711-141428.csv', # juul 
'mass-scan-pos-neg-4-13-18-5171-20180711-145222.csv', # blu
'mass-scan-pos-neg-4-13-18-5989-20180727-171215.csv', # v2
# trial 9
'mass-scan-pos-neg-4-13-18-5187-20180711-181539.csv', # halo
'mass-scan-pos-neg-4-13-18-5198-20180711-185413.csv', #juul
'mass-scan-pos-neg-4-13-18-5204-20180711-191256.csv', #blu
'mass-scan-pos-neg-4-13-18-5994-20180727-174923.csv', #v2

# trial 10
'mass-scan-pos-neg-4-13-18-5235-20180712-134449.csv', #halo
'mass-scan-pos-neg-4-13-18-5229-20180712-132412.csv', #juul
'mass-scan-pos-neg-4-13-18-5250-20180712-150005.csv', #blu
'mass-scan-pos-neg-4-13-18-6013-20180730-165438.csv', #v2
# trial 11
'mass-scan-pos-neg-4-13-18-5265-20180712-172235.csv', #halo
'mass-scan-pos-neg-4-13-18-5274-20180712-174609.csv', #juul
'mass-scan-pos-neg-4-13-18-5288-20180712-191958.csv', #blu
'mass-scan-pos-neg-4-13-18-6017-20180730-171128.csv', #v2
# trial 12
'mass-scan-pos-neg-4-13-18-5305-20180712-200505.csv', #halo
'mass-scan-pos-neg-4-13-18-5297-20180712-194355.csv', #juul
'mass-scan-pos-neg-4-13-18-5313-20180712-202745.csv', #blu
'mass-scan-pos-neg-4-13-18-6022-20180730-174656.csv' #v2
]

# Consts
IONS = ['19', '30', '32', '17', '16', '46', '62']
# precursor ion list 
H3O = 19 #index 0
NO = 30 #index 1
O2 = 32 #index 2 pos, 3 neg
OH = 17 #index 4
O = 16 #index 5
NO2 = 46 #index 6
NO3 = 62 #index 7
MZSTART = 15
MZEND = 400
NUMBER_OF_CIG = 4
NUMBER_OF_IONS = 8
BEGINNING = 0 # first element 
INFOCOLS = 2 # precursor ion + m/z
MZEND = 400 # mz range max limit
# identifier 
HALO = 1
JUUL = 2
BLU = 3
V2 = 4

# write csv file
out_file = open('training.csv', 'w')
writer = csv.writer(out_file)

# helper function for data import 
def getInput(filename, totalIndiv, index, label):
	with open(file, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		data = []
		data += [label]

		for line in csv_reader:
			if line[0] in IONS and int(line[1]) < (MZEND + 1):
				data.append(float(line[index + INFOCOLS]))
		return data 


# import csv files as trainingset 
trainingSet = []
i = 0
for file in files:
	with open('ms/p_e_' + file, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		data = [str(i%NUMBER_OF_CIG + 1)]

		for line in csv_reader: 
			if line[0] in IONS and int(line[1]) < (MZEND + 1):
				data.append(float(line[INFOCOLS]))
		trainingSet.append(data)
	i += 1


# file export
# total length 3088 (1 label + 386 m/z * 8 ions)
for a in trainingSet:
	print(len(a))
	writer.writerow(a)
out_file.close()

	

