"""
Implementation of *regularized* linear classification/regression by
plug-and-play loss functions
"""

from numpy import *
from pylab import *

from binary import *


class KNN(BinaryClassifier):
	"""
	This class defines a nearest neighbor classifier, that support
	_both_ K-nearest neighbors _and_ epsilon ball neighbors.
	"""

	def __init__(self, opts):
		"""
		Initialize the classifier.  There's actually basically nothing
		to do here since nearest neighbors do not really train.
		"""

		# remember the options
		self.opts = opts

		# just call reset
		self.reset()

	def reset(self):
		self.trX = zeros((0,0))    # where we will store the training examples
		self.trY = zeros((0))      # where we will store the training labels

	def online(self):
		"""
		We're not online
		"""
		return False

	def __repr__(self):
		"""
		Return a string representation of the tree
		"""
		return    "w=" + repr(self.weights)

	def predict(self, X):
		"""
		X is a vector that we're supposed to make a prediction about.
		Our return value should be the 'vote' in favor of a positive
		or negative label.  In particular, if, in our neighbor set,
		there are 5 positive training examples and 2 negative
		examples, we return 5-2=3.

		Everything should be in terms of _Euclidean distance_, NOT
		squared Euclidean distance or anything more exotic.
		"""

		isKNN = self.opts['isKNN']     # true for KNN, false for epsilon balls
		N     = self.trX.shape[0]      # number of training examples

		if self.trY.size == 0:
			return 0                   # if we haven't trained yet, return 0
		else:
			S = self.prepare_data(X, N)

			if isKNN:
				K = self.opts['K']
				return self.predict_knn(S, K)
			else:
				eps = self.opts['eps']
				return self.predict_eps(S, eps)		

	def predict_knn(self, S, K):
		prediction = 0

		for k in xrange(K):
			if len(S) < 1:
				break
			cur = S.pop(0)
			prediction = prediction + cur[-1] # add the y value for this training example to prediction

		if prediction >= 0:
			return 1 # we'll just return positive in case of ties, too
		else: 
			return -1

	def predict_eps(self, S, e_size):
		prediction = 0
		
		for dist, y in S:
			if dist <= e_size:
				prediction = prediction + y
			else:
				break #break since they are sorted, no need to keep checking

		if prediction >= 0:
			return 1
		else:
			return -1

	def prepare_data(self, X, N):
		S = []
		for n in xrange(N):
			cur = self.trX[n]
			y = self.trY[n]

			S.append((self.euclidean_distance(X, cur), y))

		S = sorted(S, key=lambda value: value[0])
		return S

	def euclidean_distance(self, X, X0):
		total = 0
		for n in xrange(len(X)):
			x = X[n]
			x0 = X0[n]
			total = total + (x - x0)**2

		return total**.5

	def getRepresentation(self):
		"""
		Return the weights
		"""
		return (self.trX, self.trY)

	def train(self, X, Y):
		"""
		Just store the data.
		"""
		self.trX = X
		self.trY = Y

