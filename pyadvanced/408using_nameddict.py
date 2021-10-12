# we can declare a function to use as a default when making dictionaries
# useful to set defaults where data maybe missing especially in big data scenarios

from collections import defaultdict

def not_appl():
    return 'None found'

if __name__ == '__main__':
    museum = defaultdict(not_appl)
    museum['a'] = 'Aurochs'
    museum['b'] = 'Baiji'
    museum['c'] = 'Cape Lion'
    museum['d'] = 'Dodo'
    museum['e']
    museum['f'] = 'Fossa'
    museum['g'] = 'Godzilla'
    museum['h'] = 'Hornbill'
    museum['i'] = 'Indri'
    museum['j']
    museum['k'] = 'Killer Whale'
    museum['l'] = 'Lungfish'
    museum['m'] = 'Mammoth'
    museum['n'] = 'Neanderthal'
    museum['o'] = 'Oryx'
    museum['p'] = 'Pangolin'
    museum['q'] = 'Quagga'
    museum['r'] = 'Pid Tamarin'
    museum['s'] = 'Sea Cow'
    museum['t'] = 'Tasmanian Tiger'
    museum['u'] = 'Unicorn'
    museum['v']
    museum['w'] = 'Wombat'
    museum['x']
    museum['y']
    museum['z']
    print(museum)
