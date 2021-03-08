### Microlibrary for Python, defines functions to create a neuron - Brendan Scott 2021 ###
class Neuron:
	def InitValues(WeightCount):
		Weights = [0] * WeightCount
		for WeightEnum in range(len(Weights)):
			Weights[WeightEnum - 1] = (random.random() * 2) - 1
		return Weights
	def Guess(Weights, Input):
		sum = 0
		for WeightEnum2 in range(len(Weights)):
			sum += Input[WeightEnum2 - 1] * Weights[WeightEnum2 - 1]
		return Neuron.activate(sum)
	def Train(Weights, Inputs, Target):
		Error = Target - Neuron.Guess(Inputs)
		for WeightEnum3 in range(len(Weights)):
			Weights[WeightEnum3 - 1] += Error * Inputs[WeightEnum3 - 1] * LearnRate
		return Weights
	def activate(num):
		if (num >= 0) : return 1 else : return -1
