# -*- encode: utf-8 -*-
from __future__ import print_function

def rek(x,y,recurrent=False):
    """
        A recursive version of two numeric nested loops like this:
        a=1
        b=5
        L=[(i,j) for i in range(a,b) for j in range(a,b) if j<=i]
        print L

        You can see the evolution of this algorithm on Polish Python Coders Group forum
        http://pl.python.org/forum/index.php?topic=5163.0

        >>> print(rek(3,7))
        [(3, 3), (4, 3), (4, 4), (5, 3), (5, 4), (5, 5), (6, 3), (6, 4), (6, 5), (6, 6)]

        >>> print(rek(1,5))
        [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (4, 4)]
    """
    
    if x == y:
        return [(x,y)]
    elif x > y:
        return [(x,y)] + rek(x,y+1,True)
    else: # x < y
        if recurrent:
            return rek(x,y-1,True) + rek(y,x,True)
        else:
            return rek(x,y-1,True)



if __name__ == '__main__':
    
    import doctest
    import timeit
    EXE_NR = 1000
    X = 1
    Y = 100
    setup_str = 'x={0}; y={1};'.format(X,Y)
    
    doctest.testmod()
    print('Execution time of nested loop version:')
    print(timeit.timeit('[(i,j) for i in range(x,y) for j in range(x,y) if j<=i]',setup=setup_str,number=EXE_NR))
    print('Execution time of recursive version:')
    print(timeit.timeit('rek(x,y)',setup='from __main__ import rek;'+setup_str,number=EXE_NR))

    
