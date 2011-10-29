"""
Create the training and test data sets for the AVA multiclass classifier
"""

import os

cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())

    # AVA -> pair up each binary classifier, 
    # pit them against each other in a fight to the death
    # the one left alive is the winner
    # good luck, have fun!! ^___^
    make_training_files()

def make_training_files():
    make_graphics_files()
    make_windows_files()
    make_hockey_files()
        
def make_graphics_files():
    # make the various training files
    # for graphic's matchups
    # graphics fighting!
    data_loc = '%s/multiclass/data' % p2_home
    ava_data = '%s/ava' % data_loc

    os.system("python %s/wordExtractor.py megam %s/train.comp.graphics.txt %s/train.comp.windows.x.txt > %s/train-graphics-windows.megam" % (p2_home, data_loc, data_loc, ava_data))
    os.system("python %s/wordExtractor.py megam %s/train.comp.graphics.txt %s/train.rec.sport.hockey.txt > %s/train-graphics-hockey.megam" % (p2_home,data_loc, data_loc, ava_data))
    os.system("python %s/wordExtractor.py megam %s/train.comp.graphics.txt %s/train.rec.sport.baseball.txt > %s/train-graphics-baseball.megam" % (p2_home, data_loc, data_loc, ava_data))

def make_windows_files():
    # make the various training files
    # for windows's matchups
    # windows fighting!
    data_loc = '%s/multiclass/data' % p2_home
    ava_data = '%s/ava' % data_loc

    os.system("python %s/wordExtractor.py megam %s/train.comp.windows.x.txt %s/train.rec.sport.hockey.txt > %s/train-windows-hockey.megam" % (p2_home, data_loc, data_loc, ava_data))
    os.system("python %s/wordExtractor.py megam %s/train.comp.windows.x.txt %s/train.rec.sport.baseball.txt > %s/train-windows-baseball.megam" % (p2_home, data_loc, data_loc, ava_data))

def make_hockey_files():
    # really we only need to make one file for hockey
    # since the other thingamabops cover the other matchups
    # hockey fighting!
    data_loc = '%s/multiclass/data' % p2_home
    ava_data = '%s/ava' % data_loc

    os.system("python %s/wordExtractor.py megam %s/train.rec.sport.hockey.txt %s/train.rec.sport.baseball.txt > %s/train-hockey-baseball.megam" % (p2_home, data_loc, data_loc, ava_data))

if __name__=='__main__':
    main()
