"""
Implementation of OVA multiclass classification
"""
import sys, os

cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

megam_home = "/home/mawhidby/Desktop/megam_0.92"
p2_home = "/home/mawhidby/Dropbox/UMD/Fall2011/726/Projects/ml2011fall2/p2"

def main():
    # prepare training data for each classifier
    # we are assuming that we have 4 classes:
    # graphics, windows, baseball, and hockey
    
    # create the train1.megam and train2.megam files
    # train1.megam -> graphics: +1, windows: -1
    # train2.megam -> hockey: +1, baseball: -1
    os.system("python %s/wordExtractor.py megam %s/data/train.comp.graphics.txt %s/data/train.comp.windows.x.txt > %s/multiclass/data/train1.megam" % (p2_home, p2_home, p2_home, p2_home))
    os.system("python %s/wordExtractor.py megam %s/data/train.rec.sport.hockey.txt %s/data/train.rec.sport.baseball.txt > %s/multiclass/data/train2.megam" % (p2_home, p2_home, p2_home, p2_home))
    
    # make ALL the things!
    make_training_files()

    os.system('python %s/wordExtractor.py megam %s/data.test.comp.graphics.txt %s/data/test.comp.windows.x.txt > %s/multiclass/data/test1.megam' % (p2_home, p2_home, p2_home, p2_home))
    os.system("python %s/wordExtractor.py megam %s/data/test.rec.sport.hockey.txt %s/data/test.rec.sport.baseball.txt > %s/multiclass/data/test2.megam" % (p2_home, p2_home, p2_home, p2_home))
    make_test_data()

    # now, train the different classifiers
    os.system('%s/megam -fvals binary %s/multiclass/data/train-graphics-multi.megam > %s/multiclass/data/model-graphics.megam' % (megam_home, p2_home, p2_home))
    os.system('%s/megam -fvals binary %s/multiclass/data/train-windows-multi.megam > %s/multiclass/data/model-windows.megam' % (megam_home, p2_home, p2_home))
    os.system('%s/megam -fvals binary %s/multiclass/data/train-hockey-multi.megam > %s/multiclass/data/model-hockey.megam' % (megam_home, p2_home, p2_home))
    os.system('%s/megam -fvals binary %s/multiclass/data/train-baseball-multi.megam > %s/multiclass/data/model-baseball.megam' % (megam_home, p2_home, p2_home))

    # then, predict on the test data
    
def make_training_files():
    train1 = [line.strip().split(' ') for line in file('%s/multiclass/data/train1.megam' % p2_home).readlines()]
    train2 = [line.strip().split(' ') for line in file('%s/multiclass/data/train2.megam' % p2_home).readlines()]

    # create the training data for graphics
    train_gfx = open('%s/multiclass/data/train-graphics-multi.megam' % p2_home, 'w')
    for values in train1:
        train_gfx.write('%s\n' % ' '.join(values))

    for values in train2:
        values[0] = '-1'
        train_gfx.write('%s\n' % ' '.join(values))
    train_gfx.close()

    # create the training data for windows
    train_windows = open('%s/multiclass/data/train-windows-multi.megam' % p2_home, 'w')
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
    train_hockey = open('%s/multiclass/data/train-hockey-multi.megam' % p2_home, 'w')
    for values in train1:
        values[0] = '-1'
        train_hockey.write('%s\n' % ' '.join(values))

    for values in train2:
        train_hockey.write('%s\n' % ' '.join(values))
    train_hockey.close()

    # create the training data for baseball
    train_base = open('%s/multiclass/data/train-baseball-multi.megam' % p2_home, 'w')
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
    #test-multi.megam -> graphics: 1, windows: 2, hockey: 3, baseball: 4
    out = open('%s/multiclass/data/test-multi.megam' % p2_home, 'w')

    test1 = [line.strip().split(' ') for line in file('%s/multiclass/data/test1.megam' % p2_home).readlines()]
    for values in test1:
        if values[0] == '-1':
            values[0] = '2'
        out.write('%s\n' % ' '.join(values))

    test2 = [line.strip().split(' ') for line in file('%s/multiclass/data/test2.megam' % p2_home).readlines()]
    for values in test2:
        if values[0] == '1':
            values[0] = '3'
        else:
            values[0] = '4'
        out.write('%s\n' % ' '.join(values))
    out.close()

if __name__=='__main__':
	main()
