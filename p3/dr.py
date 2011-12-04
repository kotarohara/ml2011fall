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
	N  =	X.shape[0]
	logging.debug( X.shape )
	
	pdb.set_trace()
	
	KerM = 	kernel(X.T, X)
	H = 	ones([N,N]) / N
	KerC = 	KerM - dot(KerM, H) - dot(H,KerM) + dot( dot(H, KerM), H )
	
	#logging.debug( KerC.shape[0] )
	#logging.debug( KerC )
	
	evals, evecs = eig( KerC / KerC.shape[0] )
	evals = real( evals )
	evecs = real( evecs ) / evals
	eorder = argsort( evals )[::-1][:K]
	
	evals = evals[ eorder ][:K]
	alpha = evecs[ eorder ][:K]
	P = dot( KerC, alpha.T )

	return (P, alpha, evals)

def pcaTest():
	"""
	X = array( [
				[1, 2, 3, 8], 
				[4, 5, 6, 9]
				] )
	K = 2
	logging.debug( "(X, K):\n" + str( (X, K) ) )
	logging.debug( "pca:\n" + str( pca( X, K ) ) )
	"""
	"""
	Si = sqrtm( array([[3,2], [2,4]]) )
	x = dot( randn(1000, 2), Si )
	
	(P,Z,evals) = pca( x, 2 )
	logging.debug( "Z: \n" + str( Z ) )
	logging.debug( "evals: \n" + str( evals ))
	x0 = dot(dot(x, Z[0,:]).reshape(1000,1), Z[0,:].reshape(1,2))
	x1 = dot(dot(x, Z[1,:]).reshape(1000,1), Z[1,:].reshape(1,2))
	
	plot(x[:,0], x[:,1], 'b.', x0[:,0], x0[:,1], 'r.', x1[:,0], x1[:,1], 'g.')
	input()
	"""
	(X, Y) = datasets.loadDigits()
	(P,Z,evals) = pca( X, 784 )
	#logging.debug( evals )
	drawDigits(Z[1:50,:], arange(50))
	input()
	return

def kpcaTest():
	Si = sqrtm(array([[3,2],[2,4]]))
	X = dot( randn(1000,2), Si)
	
	#logging.debug( "Si:\n" + str(Si) + "\n" )
	#logging.debug( "X:\n" + str(X)) + "\n" )
	
	#(P, alpha, evals) = kpca(X, 2, kernel.linear)
	
	(a, b) = datasets.makeKPCAdata()
	# plot( a[:,0], a[:,1], 'b.', b[:,0], b[:,1], 'r.' )
	x = vstack((a,b))
	# (P,Z,evals) = pca(x,2)
	
	# Pa = P[0:a.shape[0],:]
	# Pb = P[a.shape[0]:-1,:]
	# plot(Pa[:,0], randn(Pa.shape[0]), 'b.', Pb[:,0], randn(Pb.shape[0]), 'r.')
	(P, alpha, evals) = kpca(x,2,kernel.rbf1)
	logging.debug( evals )
	Pa = P[0:a.shape[0],:]
	Pb = P[a.shape[0]:-1,:]
	plot(Pa[:,0], Pa[:,1], 'b.', Pb[:,0], Pb[:,1], 'r.')
	
	logging.debug( "Z:\n" + str( Z ) + "\n" )
	logging.debug( "evals:\n" + str( evals ) + "\n" )
	input()
	logging.debug( "evals:\n" + str(evals) + "\n" )
	logging.debug( "alpha:\n" + str(alpha) + "\n" )
	
	return

if __name__=="__main__":
	kpcaTest()
