class Neuron:
	def Init(a):
		b = [0] * a
		for C in range(len(b)):
			b[C - 1] = (random.random() * 2) - 1
		return b
	def Guess(b, K):
		J = 0
		for D in range(len(b)):
			J += K[D - 1] * b[D - 1]
		return Neuron.M(J)
	def Train(b, G, I):
		for E in range(len(b)):
			b[E - 1] += I - Neuron.Guess(G) * G[E - 1]
		return b
	def M(L):
		if (L >= 0) : return 1 
		else : return -1
