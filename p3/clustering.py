from numpy import *
from util import *
from pylab import *

def kmeans(X, mu0):
    '''
    X is an N*D matrix of N data points in D dimensions.

    mu is a K*D matrix of initial cluster centers, K is
    the desired number of clusters.

    this function should return a tuple (mu, z, obj) where mu is the
    final cluster centers, z is the assignment of data points to
    clusters, and obj[i] is the kmeans objective function:
      (1/N) sum_n || x_n - mu_{z_n} ||^2
    at iteration [i].

    mu[k,:] is the mean of cluster k
    z[n] is the assignment (number in 0...K-1) of data point n

    you should run at *most* 100 iterations, but may run fewer
    if the algorithm has converged
    '''

    mu = mu0.copy()    # for safety

    N,D = X.shape
    K   = mu.shape[0]

    # initialize assignments and objective list
    z   = zeros((N,), dtype=int)
    obj = []

    # run at most 100 iterations
    for it in range(100):
        # store the old value of z so we can check convergence
        z_old = z.copy()
        
        # recompute the assignment of points to centers
        for n in range(N):
            bestK    = -1
            bestDist = 0
            for k in range(K):
                d = linalg.norm(X[n,:] - mu[k,:])
                if d < bestDist or bestK == -1:
                    bestK = k
                    bestDist = d
            z[n] = bestK

        # recompute means
        for k in range(K):
            mu[k,:] = mean(X[z==k, :], axis=0)

        # compute the objective
        currentObjective = 0
        for n in range(N):
            currentObjective = currentObjective + linalg.norm(X[n,:] - mu[z[n],:]) ** 2 / float(N)
        obj.append(currentObjective)

        # check to see if we've converged
        if all(z == z_old):
            break

    # return the required values
    return (mu, z, array(obj))

def initialize_clusters(X, K, method):
    '''
    X is N*D matrix of data
    K is desired number of clusters (>=1)
    method is one of:
      determ: initialize deterministically (for comparitive reasons)
      random: just initialize randomly
      ldh   : use largest-distance heuristic

    returns a matrix K*D of initial means.

    you may assume K <= N
    '''

    N,D = X.shape
    mu = zeros((K,D))

    if method == 'determ':
        # just use the first K points as centers
        mu = X[0:K,:].copy()     # be sure to copy otherwise bad things happen!!!

    elif method == 'random':
        # pick K random centers
        dataPoints = range(N)
        permute(dataPoints)
        mu = X[dataPoints[0:K], :].copy()   # ditto above

    elif method == 'ldh':
        # pick the first center randomly and each subsequent
        # subsequent center according to the largest-distance
        # heuristic

        # pick the first center totally randomly
        mu[0,:] = X[int(rand() * N), :].copy()    # be sure to copy!
        #mu[0,:] = X[1,:].copy()

        # pick each subsequent center by ldh
        for k in range(1, K):
            # find m such that data point n is the best next mean, set
            # this to mu[k,:]
            
            bestN = -1
            bestDist = 0
            for n in range(N):
                dist = 100000000
                for k0 in range(k):
                    d = linalg.norm(X[n,:] - mu[k0,:])
                    if d < dist:
                        dist = d
                if bestN == -1 or dist > bestDist:
                    bestN = n
                    bestDist = dist
                
            # set the mean
            mu[k,:] = X[bestN,:].copy()
            #print "mu(%d) = X(%d), distance = %g" % (k, bestN, bestDist)

    else:
        print "Initialization method not implemented"
        sys.exit(1)

    return mu


def gmm(X, mu0):
    '''
    just like kmeans.  X is an N*D matrix of data, mu is a K*D matrix of initial cluster centers.

    the function should return the tuple:
      (mu, Si, pk, ll)

    Si is a K*D*D matrix of covariance matrices.  i.e., Si[0,:,:] is a D*D matrix for the covariance
    of the first cluster.  pk is a K-vector of cluster prior probabilities (this is called "pi" in
    most sources, but we call it pk so it does not overload "pi = 3.1415...".)

    ll is an array of log likelihoods.

    we will always run exactly 100 iterations of EM
    '''

    mu = mu0.copy()    # for safety

    N,D = X.shape
    K   = mu.shape[0]

    # initialize pk uniformly
    pk = ones(K) / real(K)
    
    # initalize Si to identity matrices
    Si = zeros((K,D,D))
    for k in range(K):
        Si[k,:,:] = eye(D)

    # initialize ll
    ll = zeros((100,))

    doPlot = (D==2)

    for it in range(100):
        # E-step: compute probability that each point belongs to some cluster
        # hint: see util.normalLikelihood
        gamma = zeros((N,K))

        ### TODO: YOUR CODE HERE
        util.raiseNotDefined()

        if it == 0 and doPlot:
            plotDatasetEM(X, mu, Si, gamma)
            x = raw_input("Press enter to continue...")
            if x == "q":
                doPlot = False

        # M-step: update each variable in turn:

        # compute Nk
        Nk = sum(gamma, axis=0)

        # update mu:
        ### TODO: YOUR CODE HERE
        util.raiseNotDefined()
            
        # update Si: (hint: see help(outer))
        ### TODO: YOUR CODE HERE
        util.raiseNotDefined()
            
        # update pk:
        ### TODO: YOUR CODE HERE
        util.raiseNotDefined()


        # compute log likelihood.  hint: see util.normalLikelihood(x, mu, Si)
        currentLL = 0
        ### TODO: YOUR CODE HERE
        util.raiseNotDefined()
        ll[it] = currentLL

        print "Iteration %d... ll %g" % (it, currentLL)

        if doPlot:
            plotDatasetEM(X, mu, Si, gamma)
            x = raw_input("Press enter to continue...")
            if x == "q":
                doPlot = False

    if D==2:
        plotDatasetEM(X, mu, Si, gamma)

    return (mu, Si, pk, ll)

