"""
    CLASS:
        POI

    ATTRIBUTES:
        Tuple Coordinate : (X,Y) position of the POI.
        String Type : Type of POI (mission, viewpoint, collection site, etc.)
        String Name : Name of the POI.
        String Note : Description of POI.

    METHODS:
        __init__ : Constructor for the class.
        Getters : Returns the value of the attribute.
        Setters : Changes the value of the attribute.
        __str__ : Returns a string of the object.
"""
class POI:
    """
    Name: __init__ (CONSTRUCTOR)
    
    INPUT: 
        coordinate: coordinate location on the grid of the POI. Coordinates will be 
                    verified before the POI is created.
        type : type of POI (mission, viewpoint, collection site, etc.).
        String Name : Name of the POI.
        String Note : Description of POI.
    
    RETURN: 
        N/A
    
    DESCRIPTION:
        This Method will instantiate a POI object.
    """
    def __init__(self, coordinates, type, name, note):
        self.coordinates = coordinates # tuple
        self.type = type # string
        self.name = name # string
        self.note = note # string

    # getters and setters:
    def getCoordinates(self):
        return self.coordinates
    
    def setCoordinates(self, coordinates):
        self.coordinates = coordinates

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getNote(self):
        return self.note
    
    def setNote(self, note):
        self.note = note
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
        return f"Coordinates: {self.coordinates}, Type: {self.type}, Name: {self.name}, Notes: {self.note}"
