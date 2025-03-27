"""
This file contains the Grid class.
The Grid class is used as part of the Map class in order to determine
where certain coordinated are located on the map. The map class shall
have one Grid object as an attribute
"""
class Grid:

    '''
    Paramaterized constructor for the Grid class.
    May be default later, but left paramaterized for now for testing
    GridRowCol is the number of rows and columns in the grid
    GridSize squares GridRowCol to make the size of the grid
    XYMax and XYMin are the maximum and minimum values for the x and y coordinates
    squareSize is the range of possible values per section (renamed from cubeRange)
    '''
    def __init__(self, GridRowCol, XYMax, XYMin):

        self.GridRowCol = GridRowCol
        self.GridSize = GridRowCol * GridRowCol
        self.XYMax = XYMax
        self.XYMin = XYMin
        self.squareSize = (XYMax - XYMin) / GridRowCol 

    """
    Name: verifyCoords
    Purpose: To verify that the coordinates are within the range of the grid
    Parameters: self, x, y
    Returns: Bool (True if the coordinates are within the range, False otherwise
    """
    def verifyCoords(self, x, y):

        if x < self.XYMin or x > self.XYMax:
            return False
        if y < self.XYMin or y > self.XYMax:
            return False
        return True
    
    """
    Name: searchGrid
    Purpose: To determine which section of the grid the a coordinate is in
    Parameters: self, coord
    Returns: int (the section of the grid the coordinate is in)
    """  
    def searchGrid(self, coord):
        #commenting out verify step rn as we wanted to reuse this during psuedocode phase
        #but we'd be missing a parameter? Is this something Python allows?
        """
        while self.verifyCoords(coord) == False:
                print("Invalid coordinates. Please enter coordinates within the range or enter q to quit.")
                coord = input("Enter coordinates in the form of (x, y): ")
                if coord == "q":
                        return None
        """                
        #creating the boundaries for binary search
        #high is -1 because our size count starts at 0
        low = 0
        high = self.GridRowCol - 1
        while low <= high:
                #make the midpoint the avg of low and high values
                mid = (low + high) // 2
                #determine the start and end of the midpoint section
                #so, if our XYmin is -50, the squareSize is 20, and the mid is 2
                #we'd get a start value of -10 for the section
                #and an end value of 10 for the section
                start = self.XYMin + mid * self.squareSize
                end = start + self.squareSize
    
                #return the section if coordinate is within its range
                if start <= coord < end:
                    return mid, (start, end) 
                #if the coordinate is less than the start, move the high boundary
                elif coord < start:
                    high = mid - 1
                #if the coordinate is greater than the end, move the low boundary
                else:
                    low = mid + 1
    
    """
    Name: convertCoords
    Purpose: convert a coordinates tuple to ints to figure out which section it's in
    Parameters: self, coordPair
    Returns: Tuple (with the section of the grid the coordinate is in)
    """  
    def convertCoords(self, coordPair):
        #get the tuple values by themselves
        x = int(coordPair[0])
        y = int(coordPair[1])
        
        #call searchGrid for each value
        x = self.searchGrid(x)
        y = self.searchGrid(y)

        #make a new tuple for the grid section
        GridSection=(x, y)
        return GridSection