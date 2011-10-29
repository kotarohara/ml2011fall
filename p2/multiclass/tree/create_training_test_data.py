"""
Creates test and training data for the tree multiclass problem
"""

import os, sys
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    make_training_files()

def make_training_files():
    blah_loc = '%s/multiclass/data' % p2_home

    os.system("python %s/wordExtractor.py megam %s/data/train.comp.graphics.txt %s/data/train.comp.windows.x.txt > %s/train1.megam" % (p2_home, p2_home, p2_home, blah_loc))
    os.system("python %s/wordExtractor.py megam %s/data/train.rec.sport.hockey.txt %s/data/train.rec.sport.baseball.txt > %s/train2.megam" % (p2_home, p2_home, p2_home, blah_loc))

    data_loc = '%s/tree' % blah_loc
    # graphics-windows VERSUS hockey-baseball
    gw = open('%s/train-graphics-windows.megam' % data_loc, 'w')
    train1 = [line.strip().split(' ') for line in file('%s/train1.megam' % blah_loc).readlines()]
    train2 = [line.strip().split(' ') for line in file('%s/train2.megam' % blah_loc).readlines()]

    for vals in train1:
        vals[0] = '1'
        gw.write('%s\n' % ' '.join(vals))

    for vals in train2:
        vals[0] = '-1'
        gw.write('%s\n' % ' '.join(vals))

    gw.close()

    hb = open('%s/train-hockey-baseball.megam' % data_loc, 'w')
    train1 = [line.strip().split(' ') for line in file('%s/train1.megam' % blah_loc).readlines()]
    train2 = [line.strip().split(' ') for line in file('%s/train2.megam' % blah_loc).readlines()]

    for vals in train1:
        vals[0] = '-1'
        hb.write('%s\n' % ' '.join(vals))

    for vals in train2:
        vals[0] = '1'
        hb.write('%s\n' % ' '.join(vals))

    hb.close()

    # graphics VERSUS windows
    g = open('%s/train-graphics.megam' % data_loc, 'w')
    train1 = [line.strip().split(' ') for line in file('%s/train1.megam' % blah_loc).readlines()]
    for vals in train1:
        g.write('%s\n' % ' '.join(vals))
    g.close()

    w = open('%s/train-windows.megam' % data_loc, 'w')
    train1 = [line.strip().split(' ') for line in file('%s/train1.megam' % blah_loc).readlines()]
    for vals in train1:
        if vals[0] == '1':
            vals[0] = '-1'
        else:
            vals[0] = '1'
        w.write('%s\n' % ' '.join(vals))
    w.close() 

    # hockey VERSUS baseball
    h = open('%s/train-hockey.megam' % data_loc, 'w')
    train2 = [line.strip().split(' ') for line in file('%s/train2.megam' % blah_loc).readlines()]
    for vals in train2:
        h.write('%s\n' % ' '.join(vals))
    h.close()

    b = open('%s/train-baseball.megam' % data_loc, 'w')
    train2 = [line.strip().split(' ') for line in file('%s/train2.megam' % blah_loc).readlines()]
    for vals in train2:
        if vals[0] == '1':
            vals[0] = '-1'
        else:
            vals[0] = '1'
        b.write('%s\n' % ' '.join(vals))
    b.close()


if __name__=='__main__':
    main()
