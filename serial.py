"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=None):
        self.start = start
        self.serial = start - 1

    def generate(self):
        """ Increment the serial number 1 when generate is called on the instance"""
        self.serial += 1
        return self.serial

    def reset(self):
        """Reset the serial to one less then the start so when generate is called it
        displays the start and counts up from there"""
        self.serial = self.start - 1

