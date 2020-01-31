## @package pyexample
#  Documentation for this module.
#
#  More details.

## Documentation for a function.
#
#  More details.
def func():
    pass


## Documentation for a class.
#
#  More details.
class PyClass:
    ## A class variable.
    classVar1 = 0
    ## A class variable.
    classVar2 = "123"
    ## A class variable.
    classVar3 = None
    classVar4 = False
    classVar5 = [1,2,3]
    classVar6 = {"A":1,"B":2}


    ## The constructor.
    def __init__(self):
        self._memVar = 0;

    ## Documentation for a method.
    #  @param self The object pointer.
    def PyMethod(self):
        pass

    ## Documentation for a method.
    #  @param self The object pointer.
    def _PyMethod(self):
        pass

    ## @var _memVar
    #  a member variable
