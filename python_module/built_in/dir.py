"""
def dir(p_object=None): # real signature unknown; restored from __doc__
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.
    return []
"""


class SampleClass:

    def sample_method(self):
        pass


sample = [
    int, float, list, set, dict, tuple, str, SampleClass()
]

for s in sample:
    print(s, dir(s))
