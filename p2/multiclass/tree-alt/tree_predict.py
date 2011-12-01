"""
Make predictions on the test data
"""

import os, sys
from numpy import argmax
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    data_loc = '%s/multiclass/data/tree-alt' % p2_home

    # do the various binary model predictions
    do_model_predictions(data_loc)

    # determine which path of the tree we take first
    pred = []
    w = [line.strip().split('\t')[1] for line in file('%s/predictions-graphics-baseball.megam' % data_loc).readlines()]
    for val in w:
        pred.append([val])

    w = [line.strip().split('\t')[1] for line in file('%s/predictions-windows-hockey.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x].append(w[x])

    branches = [] # 1 => graphics-baseball, 2 => windows-hockey
    for y in pred:        
        index = int(argmax(y)) + 1 # index of highest scoring classifier
        branches.append(index)

    
    out = open('%s/predictions-multi.megam' % data_loc, 'w')
    graphics = [line.strip().split('\t')[1] for line in file('%s/predictions-graphics.megam' % data_loc).readlines()]
    windows = [line.strip().split('\t')[1] for line in file('%s/predictions-windows.megam' % data_loc).readlines()]
    hockey = [line.strip().split('\t')[1] for line in file('%s/predictions-hockey.megam' % data_loc).readlines()]
    baseball = [line.strip().split('\t')[1] for line in file('%s/predictions-baseball.megam' % data_loc).readlines()]

    for i in xrange(len(branches)):
        winner = branches[i]
        if winner == 1:
            # classify between windows and graphics
            pred = [graphics[i], baseball[i]]
            index = int(argmax(pred))
            if index == 0:
                index = 1
            else:
                index = 4
            out.write('%d\n' % index)
        else:
            # classify between hockey and baseball
            pred = [windows[i], hockey[i]]
            index = int(argmax(pred))
            if index == 0:
                index = 2
            else:
                index = 3
            out.write('%d\n' % index)

    out.close()



def do_model_predictions(data_loc):
    # graphics-window prediction
    os.system('%s/megam -fvals -predict %s/model-graphics-baseball.megam binary %s/test-multi.megam > %s/predictions-graphics-baseball.megam' % (megam_home, data_loc, data_loc, data_loc))

    # hockey-baseball prediction
    os.system('%s/megam -fvals -predict %s/model-windows-hockey.megam binary %s/test-multi.megam > %s/predictions-windows-hockey.megam' % (megam_home, data_loc, data_loc, data_loc))

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
