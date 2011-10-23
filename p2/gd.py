"""
Generic implementation of gradient descent.
"""

from numpy import *
import util
from numpy import *
from pylab import *
#import pdb; pdb.set_trace()

def gd(func, grad, x0, numIter, stepSize):
	"""
	Perform gradient descent on some function func, where grad(x)
	computes its gradient at position x.  Begin at position x0 and run
	for exactly numIter iterations.  Use stepSize/sqrt(t+1) as a
	step-size, where t is the iteration number.

	We return the final solution as well as the trajectory of function
	values.
	"""

	# initialize current location
	x = x0
	
	a = array([0])
	if type( a ) != type( x ):
		x = array( [x] )
	
	# set up storage for trajectory of function values
	#trajectory = zeros(numIter + 1)
	trajectory = zeros( (numIter + 1, len( x ) ) )
	#trajectory[0] = func(x)
	trajectory[0] = func(x)

	# begin iterations
	for iter in range(numIter):
		# compute the gradient at the current location
		#g = util.raiseNotDefined()	### TODO: YOUR CODE HERE
		g = array( grad( x ) )
		print x
		print g
		# compute the step size
		#eta = util.raiseNotDefined()	### TODO: YOUR CODE HERE
		eta = stepSize / sqrt( iter + 1 )

		# step in the direction of the gradient
		#x = util.raiseNotDefined()	### TODO: YOUR CODE HERE
		x = x - eta * g

		# record the trajectory
		trajectory[iter+1] = func(x)

	# return the solution
	return (x, trajectory)

if __name__=='__main__':
	# for debugging	
	import logging
	logging.basicConfig( level=logging.DEBUG )
	
	#logging.debug( gd(lambda x: x**2, lambda x: 2*x, 10, 10, 0.2 ) )
	#x, trajectory = gd(lambda x: x**2, lambda x: 2*x, array([10,5]), 100, 6.7 )
	x, trajectory = gd(lambda x: x**2, lambda x: 2*x, array([10, 5]), 100, 0.2 )
	logging.debug( x )
	plot( trajectory )
	input("Hit enter")