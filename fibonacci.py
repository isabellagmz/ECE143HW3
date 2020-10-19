# Isabella Gomez A15305555

# Instructions:
# The Fibonacci numbers are defined by the following recursion:
# F[n] = F[n-1]+F[n-2] with initial values F[1]=F[0]=1. Write a
# generator to compute the first n Fibonacci numbers. For
# example, for n=10, the output for list(fibonacci(n)) should
# be [1,1,2,3,5,8,13,21,34,55].

def fibonacci(n):
    '''
    This generator will compute the first n fibonacci numbers

    :param n: the index of fibonacci numbers
    :return:
    '''

    # check that n is positive integer
    assert type(n) == int
    assert n > 0

    seed_0, seed_1 = 0, 1
    counter = 0
    while True:
        if (counter > n): return
        yield seed_0
        seed_0, seed_1 = seed_1, seed_0 + seed_1
        counter += 1
