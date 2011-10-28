"""
Creates test and training data for the ova multiclass problem
"""

import os, sys
cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    make_training_files()
    make_test_data()


def make_training_files():
    # prepare training data for each classifier
    # we are assuming that we have 4 classes:
    # graphics, windows, baseball, and hockey
    
    # create the train1.megam and train2.megam files
    # train1.megam -> graphics: +1, windows: -1
    # train2.megam -> hockey: +1, baseball: -1

    data_loc = '%s/multiclass/data' % p2_home

    os.system("python %s/wordExtractor.py megam %s/data/train.comp.graphics.txt %s/data/train.comp.windows.x.txt > %s/train1.megam" % (p2_home, p2_home, p2_home, data_loc))
    os.system("python %s/wordExtractor.py megam %s/data/train.rec.sport.hockey.txt %s/data/train.rec.sport.baseball.txt > %s/train2.megam" % (p2_home, p2_home, p2_home, data_loc))

    train1 = [line.strip().split(' ') for line in file('%s/train1.megam' % data_loc).readlines()]
    train2 = [line.strip().split(' ') for line in file('%s/train2.megam' % data_loc).readlines()]

    # create the training data for graphics
    train_gfx = open('%s/train-graphics-multi.megam' % data_loc, 'w')
    for values in train1:
        train_gfx.write('%s\n' % ' '.join(values))

    for values in train2:
        values[0] = '-1'
        train_gfx.write('%s\n' % ' '.join(values))
    train_gfx.close()

    # create the training data for windows
    train_windows = open('%s/train-windows-multi.megam' % data_loc, 'w')
    for values in train1:
        # reverse the signs of the training data in train1.megam
        if values[0] == '1':
            values[0] = '-1'
        else:
            values[0] = '1'
        train_windows.write('%s\n' % ' '.join(values))

    for values in train2:
        values[0] = '-1'
        train_windows.write('%s\n' % ' '.join(values))
    train_windows.close()

    # create the training data for hockey
    train_hockey = open('%s/train-hockey-multi.megam' % data_loc, 'w')
    for values in train1:
        values[0] = '-1'
        train_hockey.write('%s\n' % ' '.join(values))

    for values in train2:
        train_hockey.write('%s\n' % ' '.join(values))
    train_hockey.close()

    # create the training data for baseball
    train_base = open('%s/train-baseball-multi.megam' % data_loc, 'w')
    for values in train1:
        values[0] = '-1'
        train_base.write('%s\n' % ' '.join(values))

    for values in train2:
        # reverse the signs of the training data in train2.megam
        if values[0] == '1':
            values[0] = '-1'
        else:
            values[0] = '1'
        train_base.write('%s\n' % ' '.join(values))
    train_base.close()

def make_test_data():
    data_loc = '%s/multiclass/data' % p2_home
    #test-multi.megam -> graphics: 1, windows: 2, hockey: 3, baseball: 4
    os.system('python %s/wordExtractor.py megam %s/data/test.comp.graphics.txt %s/data/test.comp.windows.x.txt > %s/test1.megam' % (p2_home, p2_home, p2_home, data_loc))
    os.system("python %s/wordExtractor.py megam %s/data/test.rec.sport.hockey.txt %s/data/test.rec.sport.baseball.txt > %s/test2.megam" % (p2_home, p2_home, p2_home, data_loc))
    out = open('%s/test-multi.megam' % data_loc, 'w')

    test1 = [line.strip().split(' ') for line in file('%s/test1.megam' % data_loc).readlines()]
    for values in test1:
        if values[0] == '-1':
            values[0] = '2'
        #print values[0]        
        out.write('%s\n' % ' '.join(values))

    test2 = [line.strip().split(' ') for line in file('%s/test2.megam' % data_loc).readlines()]
    for values in test2:
        if values[0] == '1':
            values[0] = '3'
        else:
            values[0] = '4'
        out.write('%s\n' % ' '.join(values))
    out.close()

if __name__=='__main__':
	main()
