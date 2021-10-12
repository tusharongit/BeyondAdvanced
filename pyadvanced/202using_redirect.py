# sys controls inputs and outputs
import sys

class Redirect: # brackets are optional
    '''
    Provide an easy way to redirect std output
    which is print to screen/ console
    to a file instead
    '''
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout

    # override default enter lifecycle method
    def __enter__(self):
        '''implement a redirect for output'''
        # save current std output
        self.orig_stdout = sys.stdout
        # set a new std output
        sys.stdout = self.new_stdout

    # override default exit lifecycle method
    def __exit__(self, exc_type, exc_val, exc_traceback):
        '''restore the original output'''
        sys.stdout = self.orig_stdout

if __name__ == '__main__':
    print('Current stdout is {}'.format(sys.stdout))
    # use the redirection class
    with open('mylog.txt', 'a') as fobj: # using 'with' to define a file access object automatically takes care of file.close
        with Redirect(fobj): 
            print('this is redirected to the log file')
    print('back to console')