class TestClass:
    def method(self):
        """through the self parameter, instance methods
        can freely access attributes and methods of the
        same object.

        instance methods come in handy when modifying an
        object's state, as well as the class state via
        the self.__class__ attribute
        """
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        """flagged with the @classmethod decorator

        this cannot change a singular instance of a class.

        it is used to change something for EVERY instance
        of a class
        """
        return 'class method called', cls

    @staticmethod
    def static_method():
        """this cannot modify an object's state nor class state.

        these functions are restricted in what they can access.
        they're primarily used to namespace your methods.
        """
        return 'static method called'
x