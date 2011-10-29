"""
Test the tree multiclass classifier
"""

import os

cmd_folder = os.path.dirname(os.path.abspath('%s/..' % __file__))

def main():
    execfile('%s/config.cfg' % cmd_folder, globals())
    get_accuracy()
    
    # used for debugging purposes
    #get_answer_stats()
    #get_stats()

def get_accuracy():
    data_loc = '%s/multiclass/data/tree-alt' % p2_home
    preds = [line.strip() for line in file('%s/predictions-multi.megam' % data_loc).readlines()]
    actual = [line.strip().split(' ')[0] for line in file('%s/test-multi.megam' % data_loc).readlines()]

    total = len(preds)
    correct = 0
    for x in xrange(total):
        if preds[x] == actual[x]:
            correct += 1
    
    accuracy = float(correct)/total
    print 'Final Stats:'
    print '\t', correct, '/', total, ':', accuracy

def get_answer_stats():
    # just to see how many of every example there are in the 
    # test data -> was getting some errors earlier
    data_loc = '%s/multiclass/data/tree-alt' % p2_home

    # gather some stats on the test data that was created...
    f = open('%s/predictions-multi.megam' % data_loc, 'r')

    ones = 0
    twos = 0
    threes = 0
    fours = 0

    for line in f:
        vals = line.strip().split(' ')
        if vals[0] == '1':
            ones += 1
        elif vals[0] == '2':
            twos += 1
        elif vals[0] == '3':
            threes += 1
        elif vals[0] == '4':
            fours += 1
    print 'answer stats'
    print '\tones:', ones
    print '\ttwos:', twos
    print '\tthrees:', threes
    print '\tfours:', fours


def get_stats():
    # just to see how many of every example there are in the 
    # test data -> was getting some errors earlier
    data_loc = '%s/multiclass/data' % p2_home

    # gather some stats on the test data that was created...
    f = open('%s/test-multi.megam' % data_loc, 'r')

    ones = 0
    twos = 0
    threes = 0
    fours = 0

    for line in f:
        vals = line.strip().split(' ')
        if vals[0] == '1':
            ones += 1
        elif vals[0] == '2':
            twos += 1
        elif vals[0] == '3':
            threes += 1
        elif vals[0] == '4':
            fours += 1

    print 'ones:', ones
    print 'twos:', twos
    print 'threes:', threes
    print 'fours:', fours
        

if __name__=='__main__':
    main()
