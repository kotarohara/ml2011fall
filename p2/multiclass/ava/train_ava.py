"""
Trains the binary classifiers for the ava multiclass problem
"""

import os, sys
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    data_loc = '%s/multiclass/data/ava' % p2_home

    # train the graphics matchups
    os.system('%s/megam -lambda 8 -fvals binary %s/train-graphics-windows.megam > %s/model-graphics-windows.megam' % (megam_home, data_loc, data_loc))
    os.system('%s/megam -lambda 8 -fvals binary %s/train-graphics-hockey.megam > %s/model-graphics-hockey.megam' % (megam_home, data_loc, data_loc))
    os.system('%s/megam -lambda 8 -fvals binary %s/train-graphics-baseball.megam > %s/model-graphics-baseball.megam' % (megam_home, data_loc, data_loc))
    
    # train the windows matchups
    os.system('%s/megam -lambda 8 -fvals binary %s/train-windows-baseball.megam > %s/model-windows-baseball.megam' % (megam_home, data_loc, data_loc))
    os.system('%s/megam -lambda 8 -fvals binary %s/train-windows-hockey.megam > %s/model-windows-hockey.megam' % (megam_home, data_loc, data_loc))

    # train the hockey matchup
    os.system('%s/megam -lambda 8 -fvals binary %s/train-hockey-baseball.megam > %s/model-hockey-baseball.megam' % (megam_home, data_loc, data_loc))


if __name__=='__main__':
    main()
