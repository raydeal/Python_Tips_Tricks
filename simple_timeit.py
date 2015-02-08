import time                                                
 
def simple_timeit(method):
    """
    Helper function to measure execution time of procedures/methods.
    Use it as decorator.

    Examples:

    from time import sleep
    
    @simple_timeit
    def test_one():
        sleep(5)

    class A:

        @simple_timeit
        def test_two(self):
            sleep(10)

    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
 
        print '%r %2.2f sec' % (method.__name__, te-ts)
        return result
 
    return timed

if __name__ == "__main__":
    
    from time import sleep
    
    @simple_timeit
    def test_one():
        sleep(5)

    class A:

        @simple_timeit
        def test_two(self):
            sleep(10)

    test_one()
    a = A()
    a.test_two()