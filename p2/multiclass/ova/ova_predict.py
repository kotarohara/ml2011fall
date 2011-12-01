"""
Make predictions on the test data
"""

import os, sys
from numpy import argmax
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    data_loc = '%s/multiclass/data' % p2_home

    # do the various binary model predictions
    do_model_predictions(data_loc)
    
    # read these predictions into an array
    pred = []
    w = [line.strip().split('\t')[1] for line in file('%s/predictions-graphics.megam' % data_loc).readlines()]
    for val in w:
        pred.append([val])

    w = [line.strip().split('\t')[1] for line in file('%s/predictions-windows.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x].append(w[x])

    w = [line.strip().split('\t')[1] for line in file('%s/predictions-hockey.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x].append(w[x])

    w = [line.strip().split('\t')[1] for line in file('%s/predictions-baseball.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x].append(w[x])
    

    out = open('%s/predictions-multi.megam' % data_loc, 'w')

    # iterate through the array
    # for each arr of predictions
    # see which indices have '1' outputs
    # select random 1 for 
    for y in pred:        
        index = int(argmax(y)) + 1 # index of highest scoring classifier
        out.write('%d\n' % index)
        
    out.close()    

def do_model_predictions(data_loc):
    # graphics model prediction
    os.system('%s/megam -fvals -predict %s/model-graphics.megam binary %s/test-multi.megam > %s/predictions-graphics.megam' % (megam_home, data_loc, data_loc, data_loc))

    # windows model prediction
    os.system('%s/megam -fvals -predict %s/model-windows.megam binary %s/test-multi.megam > %s/predictions-windows.megam' % (megam_home, data_loc, data_loc, data_loc))

    # hockey model prediction
    os.system('%s/megam -fvals -predict %s/model-hockey.megam binary %s/test-multi.megam > %s/predictions-hockey.megam' % (megam_home, data_loc, data_loc, data_loc))

    # baseball model prediction
    os.system('%s/megam -fvals -predict %s/model-baseball.megam binary %s/test-multi.megam > %s/predictions-baseball.megam' % (megam_home, data_loc, data_loc, data_loc))

if __name__=='__main__':
    main()
