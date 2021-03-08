class Neuron:
	def InitValues(a):
		b = [0] * a
		for C in range(len(b)):
			b[C - 1] = (random.random() * 2) - 1
		return b
	def Guess(b, K):
		J = 0
		for D in range(len(b)):
			J += K[D - 1] * b[D - 1]
		return Neuron.activate(J)
	def Train(b, G, I):
		F = I - Neuron.Guess(G)
		for E in range(len(b)):
			b[E - 1] += F * G[E - 1]
		return b
	def activate(L):
		if (L >= 0) : return 1 
		else : return -1
