"""
Trains the binary classifiers for the tree multiclass problem
"""

import os, sys
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    data_loc = '%s/multiclass/data/tree-alt' % p2_home

    # train ALL the classifiers!
    os.system('%s/megam -lambda 8 -fvals binary %s/train-graphics-baseball.megam > %s/model-graphics-baseball.megam' % (megam_home, data_loc, data_loc))
    
    os.system('%s/megam -lambda 8 -fvals binary %s/train-windows-hockey.megam > %s/model-windows-hockey.megam' % (megam_home, data_loc, data_loc))

    os.system('%s/megam -lambda 8 -fvals binary %s/train-graphics.megam > %s/model-graphics.megam' % (megam_home, data_loc, data_loc))

    os.system('%s/megam -lambda 8 -fvals binary %s/train-windows.megam > %s/model-windows.megam' % (megam_home, data_loc, data_loc))

    os.system('%s/megam -lambda 8 -fvals binary %s/train-hockey.megam > %s/model-hockey.megam' % (megam_home, data_loc, data_loc))
    
    os.system('%s/megam -lambda 8 -fvals binary %s/train-baseball.megam > %s/model-baseball.megam' % (megam_home, data_loc, data_loc))


if __name__=='__main__':
    main()
