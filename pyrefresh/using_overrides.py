# we can override any of the puthon built-ins 9they start with __)

# override the equality operator so it equates two strings ignoring case
class Word():
    '''
    The class overrides the equality operator __eq__
    so it equates two strings ignoring their case
    '''
    def __init__(self, text):
        self.text = text

    def __eq__(self, otherword):
        return self.text.lower() == otherword.text.lower()

if __name__ == '__main__':
    lower = 'hello'
    upper = 'HELLO'

    w_lower = Word(lower)
    w_upper = Word(upper)

    print(w_lower == w_upper)
    print(w_lower.__doc__)  # docstring
