"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if (x <= 1):
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return (ra + rb)
    pass

def longest_run(mylist, key):
    ### TODO
    counter = 0
    maxRun = 0
    for i in range(len(mylist)):
        if (mylist[i] == key):
            counter+= 1
        else:
            if (counter > maxRun):
                maxRun = counter
            counter = 0
    return maxRun
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key

    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))


def longest_run_recursive(mylist, key):
    ### TODO

    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([2,12,12,8,12,12,12,12,12,12,12,0,12,12,12,1], 12) == 7
    assert longest_run([2,12,1,12], 12) == 1
    assert longest_run([2,1], 12) == 0
