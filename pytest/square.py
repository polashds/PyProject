class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('length must be a number')
        self.length = length

    def area(self):
        return self.length * self.length
    
