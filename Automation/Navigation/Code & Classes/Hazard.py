"""
    CLASS:
        Hazard

    ATTRIBUTES:
        Tuple Coordinate : (X,Y) position of the hazard. Coordinates will be
                            verified before the hazard is created.
        Float Size : Total area of the hazard.
        String Type : Type of hazard (rock, crater, cliff, etc.)
        String Name : Name of the hazard.

    METHODS:
        __init__ : Constructor for the class.
        Getters : Returns the value of the attribute.
        Setters : Changes the value of the attribute.
        __str__ : Returns a string of the object.
"""
class Hazard:
    """
    Name: __init__ (CONSTRUCTOR)
    
    INPUT: 
       coordinate: coordinate location on the grid of the hazard.
       size : total size (area) of the hazard.
       type : type of hazard (rock, crater, cliff, etc.).
       name : name of hazard.
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will instantiate a hazard object.
    """
    def __init__(self, coordinate, size, type, name):
        self.coordinate = coordinate # tuple
        self.size = size # float
        self.type = type # string
        self.name = name # string

    # getters and setters:
    def getCoordinates(self):
        return self.coordinate
    
    def setCoordinates(self, coordinate):
        self.coordinate = coordinate

    def getSize(self):
        return self.size
    
    def setSize(self, size):
        self.size = size

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    """
    Name: __str__
    
    INPUT: 
       N/A
    
    RETURN: 
        String
    
    DESCRIPTION:
        This Method will begin convert the object to a string and return.
    """
    def __str__(self):
        return f"Coordinate: {self.coordinate}, Size: {self.size}, Type: {self.type}, Name: {self.name}"


