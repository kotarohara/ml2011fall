from numpy import *
from util import *
from pylab import *
import logging, pdb
import datasets
import kernel

logging.basicConfig( level=logging.DEBUG )

def pca(X, K):
	'''
	X is an N*D matrix of data (N points in D dimensions)
	K is the desired maximum target dimensionality (K <= min{N,D})

	should return a tuple (P, Z, evals)
	
	where P is the projected data (N*K) where
	the first dimension is the higest variance,
	the second dimension is the second higest variance, etc.

	Z is the projection matrix (D*K) that projects the data into
	the low dimensional space (i.e., P = X * Z).

	and evals, a K dimensional array of eigenvalues (sorted)
	'''
	
	N,D = X.shape

	# make sure we don't look for too many eigs!
	if K > N:
		K = N
	if K > D:
		K = D

	# first, we need to center the data
	### TODO: YOUR CODE HERE
	#util.raiseNotDefined()
	mu = 	average( X, axis=0 )
	
	Xnorm = X - multiply( mu, ones((N, D)) )
	Dcov =	dot( Xnorm.T, Xnorm ) / X.shape[0]

	# next, compute eigenvalues of the data variance
	#	hint 1: look at 'help(pylab.eig)'
	#	hint 2: you'll want to get rid of the imaginary portion of the eigenvalues; use: real(evals), real(evecs)
	#	hint 3: be sure to sort the eigen(vectors,values) by the eigenvalues: see 'argsort', and be sure to sort in the right direction!
	#			 
	### TODO: YOUR CODE HERE
	# util.raiseNotDefined()
	evals, evecs = eig( Dcov )
	evals = real( evals )
	evecs = real( evecs.T )
	
	eorder = argsort( evals )[::-1][:K] # reverse order and only K items
	#logging.debug( "Dcov:\n" + str( Dcov ) + "\n" )
	#logging.debug( "evecs:\n" + str( evecs ) + "\n" )
	#logging.debug( "evals:\n" + str( evals ) + "\n" )
	#logging.debug( "eorder:\n" + str( eorder ) + "\n" )
	U = evecs[ eorder ]
	P = dot( Xnorm, U.T )
	Z = U
	return (P, Z, evals[eorder])


def kpca(X, K, kernel):
	'''
	X is an N*D matrix of data (N points in D dimensions)
	K is the desired maximum target dimensionality (K <= min{N,D})
	kernel is a FUNCTION that computes K(x,z) for some desired kernel and vectors x,z

	should return a tuple (P, alpha, evals), where P and evals are
	just like in PCA, and alpha is the vector of alphas (mixing
	parameters) for the kernel PCA decomposition.
	'''

	### TODO: YOUR CODE HERE
	#util.raiseNotDefined()
	N, D  =	X.shape
	
	# Ker0: Kernel Matrix 0
	# KerC: Kernel Matrix Centered
	# KerM: Kernel Matrix
	Z = X.copy()
	Ker0 = zeros((N,N))
	for i, x in enumerate( X ):
		for j, z in enumerate( Z ):
			Ker0[i,j] = kernel(x,z)
	# Ker0 = kernel( X, X.T )
	H = 	ones((N,N)) / N
	KerC = 	Ker0 - dot(H, Ker0) - dot(Ker0, H) + dot( dot(H, Ker0), H )
	
	evals, evecs = eig( KerC )
	evals = real( evals ) / N

	evecs = real( evecs ) # / sqrt( evals )
	eorder = argsort( evals )[::-1][:K]
	
	evals = evals[ eorder ]
	alpha = evecs[ eorder ]
	
	a_norm = divide(alpha.T, sum(alpha, axis=1) ).T
	a_norm = divide( a_norm.T, sqrt( evals ) ).T
	P = dot( KerC, a_norm.T )
	return (P, alpha, evals )

def pcaTest():
	"""
	Si = sqrtm( array([[3,2], [2,4]]) )
	x = dot( randn(1000, 2), Si )
	
	(P,Z,evals) = pca( x, 2 )
	print "Z:", Z
	print "evals:", evals
	x0 = dot(dot(x, Z[0,:]).reshape(1000,1), Z[0,:].reshape(1,2))
	x1 = dot(dot(x, Z[1,:]).reshape(1000,1), Z[1,:].reshape(1,2))
	
	plot(x[:,0], x[:,1], 'b.', x0[:,0], x0[:,1], 'r.', x1[:,0], x1[:,1], 'g.')
	input()
	"""

	#(X, Y) = datasets.loadDigits()
	#(P,Z,evals) = pca( X, 784 )
	
	"""
	esum = sum( evals )
	print esum
	print "evals", evals[0:3]
	evals = evals / esum
	print "evals", evals[0:3]
	print "evals", evals
	plot( evals, zeros([evals.shape[0]]), 'b.')
	input()
	"""
	#print cumsum( evals )

	"""acum = 0
	for i in xrange( len( evals ) ):
		acum = sum( evals[:i] )
		print acum
		if acum >= 0.90:
			print "i:", i
			break
			"""
	
	# print Z
	#x0 = dot(dot(X, Z[0,:]).reshape(1000,1), Z[0,:].reshape(1,2))
	#plot(X[:,0], X[:,1], 'b.', x0[:,0], x0[:,1], 'r.')
	#input()
	
	#drawDigits(Z[1:50], arange(50))
	#input()
	
	(a,b) = datasets.makeKPCAdata()
	
	x = vstack((a,b))
	(P,Z,evals) = pca(x,2)
	
	Pa = P[0:a.shape[0],:]
	Pb = P[a.shape[0]:-1,:]
	
	plot(Pa[:,0], randn(Pa.shape[0]), 'b.', Pb[:,0], randn(Pb.shape[0]), 'r.')
	input()
	
	return

def kpcaTest():
	import numpy
	numpy.random.seed(2780)
	Si = sqrtm(array([[3,2],[2,4]]))
	x = dot(randn(1000, 2), Si)
	
	(P, alpha, evals) = kpca(x, 2, kernel.linear)

	print "evals", evals
	print "alpha", alpha
	
	return

if __name__=="__main__":
	pcaTest()
	#kpcaTest()
