"""
Trains the binary classifiers for the ova multiclass problem
"""

import os, sys
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())

    os.system('%s/megam -fvals binary %s/multiclass/data/train-graphics-multi.megam > %s/multiclass/data/model-graphics.megam' % (megam_home, p2_home, p2_home))

    os.system('%s/megam -fvals binary %s/multiclass/data/train-windows-multi.megam > %s/multiclass/data/model-windows.megam' % (megam_home, p2_home, p2_home))

    os.system('%s/megam -fvals binary %s/multiclass/data/train-hockey-multi.megam > %s/multiclass/data/model-hockey.megam' % (megam_home, p2_home, p2_home))

    os.system('%s/megam -fvals binary %s/multiclass/data/train-baseball-multi.megam > %s/multiclass/data/model-baseball.megam' % (megam_home, p2_home, p2_home))

if __name__=='__main__':
	main()
