import physics.vector as vect

#The class Physicsbody represents a body who has three major components:
#A Physics body has a vector for acceleration.
#A physics body has a vector for velocity.
#A physics body has a vector for position.
#All physics bodies must have the method "physics_process" called in a loop to be updated.
class Physicsbody():
    bodies = []
    
    #init the position
    def __init__(self, x, y, z):
        self.accel_vector = vect.Vector()
        self.vel_vector = vect.Vector()
        self.pos_vector = vect.Vector()
        self.pos_vector.x = x
        self.pos_vector.y = y
        self.pos_vector.z = z
        self.bodies.append(self)

    def get_pos(self):
        return self.pos_vector.x, self.pos_vector.y, self.pos_vector.z
    
    #Returns the velocity of the physics body.
    def get_velocity(self):
        return self.vel_vector.get_magnitude()
    
    #Returns the magnitude of net force experienced by the physics body.
    def get_netforce(self):
        return (self.mass * self.accel_vector.get_magnitude())
        
    #Updates turtle position and velocity.
    #dt (float): The timestep.
    def physics_process(self, dt):
        #First, the velocity vector changes based on the acceleration vector and change in time.
        #The velocity vector in the x or y direction cannot exceed the terminal velocity.
        self.vel_vector.x = (self.vel_vector.x + ((self.accel_vector.x) * dt))
        self.vel_vector.y = (self.vel_vector.y + ((self.accel_vector.y) * dt))
        self.vel_vector.z = (self.vel_vector.z + ((self.accel_vector.z) * dt))

        #Lastly, the x and y coordinates are updated based on the current velocity and change in time.        
        self.pos_vector.x += (self.vel_vector.x * dt)
        self.pos_vector.y += (self.vel_vector.y * dt) 
        self.pos_vector.z += (self.vel_vector.z * dt)