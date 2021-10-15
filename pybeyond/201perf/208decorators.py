# decorator to make things thread-safe
from threading import Lock

# function used to make a class thread-safe, using locks
def lock_class(methodnames, lockfactory):
    return lambda cls:make_thread_safe(cls, methodnames, lockfactory)

def lock_method(method): # this will return a locked version of the method passed in as argument
    if getattr(method, '__is_locked', False):
        raise TypeError('Method {} locked'.format(method))
    def locked_method(self, *args, **kwargs):
        with self._lock: # lock will be released at the end of 'with'
            return method(self, *args, **kwargs) # call the method
    lock_method.__name__ = 'locked method({})'.format(method.__name__)
    locked_method.__is_locked = True
    return locked_method

def make_thread_safe(cls, methodnames, lockfactory):
    init = cls.__init__ # take a copy of the exisiting __init__ of this cls
    def newinit(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.__lock  = lockfactory
    cls.__init__ = newinit # override the original __init__ with this new one

    # now iterate over all the class methods and make them thread-safe
    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        newmethod = lock_method(oldmethod)
        setattr(cls, methodname, newmethod)
    return cls # class with new init and new version of all methods which are now thread-safe

@lock_class(['add', 'remove'], Lock) # Lock is a lock factory
class DecoratorLockSet(set): # set type has add and remove methods
    # due to presence of decorator, add and remove methods of set are now thread-safe
    @lock_method
    def methodToLock(self):
        print('explicitly making this methos thread-safe')

if __name__ == '__main__':
    my_set = (4, 3, 2)
    my_inst = DecoratorLockSet(my_set)

    # check locking
    print(my_inst.add.__is_locked)
    print(my_inst.remove.__is_locked)
    print(my_inst.methodToLock.__is_locked)