import math

#The class Vector represents the vector of a physicsbody
class Vector:
    
    """
    The constructor for Vector.
    Defaults as a vector with net magnitude of 0. Can take three keyword args.
    
    Kwargs:
        x (float): The x-component of vector.
        y (float): The y-component of vector.
        z (float): The z-component of vector.
    """
    def __init__(self, **kwargs):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        if "x" in kwargs and "y" in kwargs and "z" in kwargs and len(kwargs) == 3:
            for i, n in kwargs.items():
               self.x = n if i == "x" else self.x
               self.y = n if i == "y" else self.y
               self.z = n if i == "z" else self.z
        elif len(kwargs) == 0:
            pass
        else:
            print("Vector initialized with invalid keyword args or invalid combination of keyword args.")
            
    #Override for addition.
    #Allows two vectors to be added together.
    #Returns the new vector.
    def __add__(self, vect):
        self.x += vect.x
        self.y += vect.y
        self.z += vect.z
        return Vector(x=self.x, y=self.y, z=self.z)
    
    #Override for subtraction.
    #Allows one vector to be subtracted from another.
    #Returns the new vector.
    def __sub__(self, vect):
        self.x -= vect.x
        self.y -= vect.y
        self.z -= vect.z
        return Vector(x=self.x, y=self.y, z=self.z)

    def zero(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    #Returns the magnitude of the current vector.
    def get_magnitude(self):       
        return (math.sqrt(self.x**2 + self.y**2 + self.z**2))
