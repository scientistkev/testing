''' Unit tests are tests that check a small component of the
application. The following is a unit test for the method sum()'''

assert sum([1,2,3]) == 6 'should be 6, won\'t print if correct'
print ('Assertion is correction')

assert sum([1,1,1]) == 6  'should be 6, will return AssertionError'

''' A function of the assert sum() function, using name/main
scripting ''' 

def test_sum():
    """ A function to test the sum method, in function form! """
    assert sum([1,2,3]) == 6, 'should be 6, won\'t print if correct'

if __name__ == "__main__": 'command line entry point'
    test_sum() 'This is also called a test assertion'
    print('Everything passed')