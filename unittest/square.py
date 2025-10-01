class Square:
    def __init__(self, lenth) -> None:
        # To pass the test, you need to raise an exception
        #  if the type of the length property is not int or float in the Square constructor:
        if type(lenth) not in [int, float]:
            raise TypeError('lenth must be in int or float')
        
        # To make the test pass, you add another check to the Square() constructor:
        if lenth < 0:
            raise ValueError('Length must not be negative')
        
        self.length = lenth

    def area(self):
        return self.length * self.length
    