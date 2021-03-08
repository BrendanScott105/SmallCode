class Neuron:
	def Init(Weights):
		b = [0] * Weights
		for C in range(len(b)):
			b[C - 1] = (random.random() * 2) - 1
		return b
	def Guess(ArrIn, Guess):
		J = 0
		for D in range(len(ArrIn)):
			J += Guess[D - 1] * ArrIn[D - 1]
		return Neuron.M(J)
	def Train(ArrIn, Data, Val):
		for E in range(len(ArrIn)):
			ArrIn[E - 1] += Val - Neuron.Guess(ArrIn, Data) * Data[E - 1]
		return ArrIn
	def M(L):
		if (L >= 0) : return 1 
		else : return -1
