"""
Make predictions on the test data
"""

import os, sys
from numpy import argmax
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    data_loc = '%s/multiclass/data/ava' % p2_home

    # classifier with the best record wins!!!!!!!!!
    # predict ALL the things!
    do_model_predictions(data_loc)
    compute_final_predictions(data_loc)


def do_model_predictions(data_loc):
    # graphics model predictions
    os.system('%s/megam -fvals -predict %s/model-graphics-windows.megam binary %s/test-multi.megam > %s/predictions-graphics-windows.megam' % (megam_home, data_loc, data_loc, data_loc))
    os.system('%s/megam -fvals -predict %s/model-graphics-hockey.megam binary %s/test-multi.megam > %s/predictions-graphics-hockey.megam' % (megam_home, data_loc, data_loc, data_loc))
    os.system('%s/megam -fvals -predict %s/model-graphics-baseball.megam binary %s/test-multi.megam > %s/predictions-graphics-baseball.megam' % (megam_home, data_loc, data_loc, data_loc))

    # windows model predictions
    os.system('%s/megam -fvals -predict %s/model-windows-baseball.megam binary %s/test-multi.megam > %s/predictions-windows-baseball.megam' % (megam_home, data_loc, data_loc, data_loc))
    os.system('%s/megam -fvals -predict %s/model-windows-hockey.megam binary %s/test-multi.megam > %s/predictions-windows-hockey.megam' % (megam_home, data_loc, data_loc, data_loc))

    # hockey model prediction
    os.system('%s/megam -fvals -predict %s/model-hockey-baseball.megam binary %s/test-multi.megam > %s/predictions-hockey-baseball.megam' % (megam_home, data_loc, data_loc, data_loc))

def compute_final_predictions(data_loc):
    # determine who will live, and who will dieee
        
    # read in all the predictions
    pred = []
    w = [line.strip().split('\t')[0] for line in file('%s/predictions-graphics-windows.megam' % data_loc).readlines()]
    for val in w:
        pred.append({'graphics-windows': val})

    w = [line.strip().split('\t')[0] for line in file('%s/predictions-graphics-hockey.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x]['graphics-hockey'] = w[x]

    w = [line.strip().split('\t')[0] for line in file('%s/predictions-graphics-baseball.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x]['graphics-baseball'] = w[x]

    w = [line.strip().split('\t')[0] for line in file('%s/predictions-windows-hockey.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x]['windows-hockey'] = w[x]

    w = [line.strip().split('\t')[0] for line in file('%s/predictions-windows-baseball.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x]['windows-baseball'] = w[x]

    w = [line.strip().split('\t')[0] for line in file('%s/predictions-hockey-baseball.megam' % data_loc).readlines()]
    for x in xrange(len(w)):
        pred[x]['hockey-baseball'] = w[x]

    out = open('%s/predictions-multi.megam' % data_loc, 'w')
    # now score each classifier
    for x in xrange(len(pred)):
        gfx_score = 0
        win_score = 0
        hoc_score = 0
        bas_score = 0
        cur = pred[x]

        if cur['graphics-windows'] == '1':
            gfx_score += 1
        else:
            win_score += 1

        if cur['graphics-hockey'] == '1':
            gfx_score +=1
        else:
            hoc_score +=1

        if cur['graphics-baseball'] == '1':
            gfx_score +=1
        else:
            bas_score +=1

        if cur['windows-hockey'] == '1':
            win_score +=1
        else:
            hoc_score +=1

        if cur['windows-baseball'] == '1':
            win_score +=1
        else:
            bas_score +=1

        if cur['hockey-baseball'] == '1':
            hoc_score +=1
        else:
            bas_score +=1

        scores = [gfx_score, win_score, hoc_score, bas_score]
        index = int(argmax(scores)) + 1
        out.write('%d\n' % index)
    out.close()

if __name__=='__main__':
    main()


