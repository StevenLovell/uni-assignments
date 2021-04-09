class Message:  # encapsulation
    __hello = None  # Private Attribute or variable

    # constructor
    def __init__(self, value1):
        self.__hello = value1  # assigned with the given argument

    def __say_hello(self):
        print("Message:", self.__hello + " you are welcome")

    def getAttribute(self):  # Allows the use of a private function outside the class
        print("Attribute: " + self.__hello)

    def accessFunction(self):   # used to run the function
        self.__say_hello()

    def setAttribute(self, value2):     # Used to change the attribute
        self.__hello = value2
        print("New attribute: " + self.__hello)


run = Message("hello Fred")
run.getAttribute()  # Requesting the attribute
run.accessFunction()
run.setAttribute("Hello George")
run.accessFunction()
