import random
import numpy

def logistic(inval):
	return 1/(1+numpy.exp(-inval+3))

def weightChange(a,trueResult,finalResult,currentInput,currentWeight):
	return a*(trueResult-finalResult)*logistic(currentInput*currentWeight)*(1+logistic(currentInput*currentWeight))*currentInput

def test(inArray,inNeuronArray,inTrainLen):
	result = 0
	for x in range(0,inTrainLen):
		result += inNeuronArray[x] * inArray[x]
	result = logistic(result)
	return result

def train(inTraining,inResult,inNeuron,inTrainLen):
	result = test(inTraining,inNeuron,inTrainLen)
	for y in range(0,inTrainLen):
		inNeuron[y] += weightChange(0.01,inResult,result,inTraining[y],inNeuron[y])

def massTrain(rep, recet = False):
	trainIn = [[0,1,0,1],[0,0,1,0],[0,1,1,1],[1,1,0,0],[1,0,1,1],[1,1,0,0]]
	trainLen = len(trainIn[0])
	trainRes = [0,0,0,1,1,1]

	seed = 7
	random.seed(seed)

	neuronWeight = []

	if recet:
		for x in range(0,trainLen):
			neuronWeight.append(random.random())
	else:
		neuronWeightFile = open('neuronWeightFile.txt')

		with neuronWeightFile as f:
			for line in f:
				neuronWeight.append(float(line))

	print(neuronWeight)

	for x in range(0,rep):
		for x in range(0,len(trainIn)):
			train(trainIn[x],trainRes[x],neuronWeight,trainLen)

	print(neuronWeight)

	neuronWeightFile = open('neuronWeightFile.txt', 'w')
	for item in neuronWeight:
		neuronWeightFile.write("%s\n" % item)

	finalTest = [0,0,0,0]
	print(test(finalTest,neuronWeight,trainLen))

def run(testList,answer = False, realRes = 0):
	neuronWeight = []

	neuronWeightFile = open('neuronWeightFile.txt')

	with neuronWeightFile as f:
	    for line in f:
	       neuronWeight.append(float(line))

	trainLen = len(neuronWeight)

	print(test(testList,neuronWeight,trainLen))

	if answer:
		train(testList,realRes,neuronWeight,trainLen)
		neuronWeightFile = open('neuronWeightFile.txt', 'w')
		for item in neuronWeight:
			neuronWeightFile.write("%s\n" % item)

repeat = True
while repeat:
	action = input('Select Action: ')
	if action == 'train':
		mainIn = input('What list do you want to test: ')
		mainIn = mainIn.split(',')
		for x in range(0,len(mainIn)):
			mainIn[x] = int(mainIn[x]);
		res =  int(input('What is the real result: '))
		run(mainIn, True, res)
	elif action == 'test':
		mainIn = input('What list do you want to test: ')
		mainIn = mainIn.split(',')
		for x in range(0,len(mainIn)):
			mainIn[x] = int(mainIn[x]);
		run(mainIn)
	elif action == 'mass train':
		repeats = int(input('How many iterations do you want: '))
		massTrain(repeats)
	elif action == 'end':
		break
	elif action == 'reset':
		repeats = int(input('How many iterations do you want: '))
		massTrain(repeats, True)
	elif action == 'display':
		neuronWeight = []
		neuronWeightFile = open('neuronWeightFile.txt')
		with neuronWeightFile as f:
			for line in f:
				neuronWeight.append(float(line))
		print(neuronWeight)
	else:
		print('That is invalid')



