from numpy import *

X = array([[  1,  0,  0,     1,  0,  0,    1,    0   ],
           [  1,  0,  0,     1,  0,  0,    1,    1   ],
           [  0,  1,  0,     1,  0,  0,    1,    0   ],
           [  0,  0,  1,     0,  1,  0,    1,    0   ],
           [  0,  0,  1,     0,  0,  1,    0,    0   ],
           [  0,  0,  1,     0,  0,  1,    0,    1   ],
           [  0,  1,  0,     0,  0,  1,    0,    1   ],
           [  1,  0,  0,     0,  1,  0,    1,    0   ],
           [  1,  0,  0,     0,  0,  1,    0,    0   ],
           [  0,  0,  1,     0,  1,  0,    0,    0   ],
           [  1,  0,  0,     0,  1,  0,    0,    1   ],
           [  0,  1,  0,     0,  1,  0,    1,    1   ],
           [  0,  1,  0,     1,  0,  0,    0,    0   ],
           [  0,  0,  1,     0,  1,  0,    1,    1   ]
           ], dtype=float)
Y = array([ -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1 ], dtype=float)

d = 1
left_vx = X[X[:,d]<=0]
left_vy = Y[X[:,d]<=0]
right_vx = X[X[:,d]>0]
right_vy = Y[X[:,d]>0]

leftY  = 1
rightY = 1

error = len( left_vy[ left_vy!=leftY ] ) + len( right_vy[ right_vy!=rightY ] )
print left_vy
print right_vy
print error