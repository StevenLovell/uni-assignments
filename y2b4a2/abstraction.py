from abc import ABC, abstractmethod  # ABC = Abstract Base Classes. Recommended for using abstract classes in python.


class AbstractClass(ABC):
    def test(self, value):
        print("Passed value: ", value)

    @abstractmethod  # abc marks a method of a parent class using the decorator @abstractmethod
    def task(self):
        print("We are inside Abstract Class task")


class test_class(AbstractClass):
    def task(self):
        print("We are inside test_class task")


# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.test(100)

# Testing the object to see if it is an instance of AbstractClass.
print(isinstance(test_obj, AbstractClass))
