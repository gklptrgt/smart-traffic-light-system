from ursina import *
import math


class Vehicle(Entity):

    def __init__(self, path, counter, loop=False, boxes=False):
        # add timer that calculates how many seconds does it take to travel from a point to a point.

        try:
            position = path[0]
        except IndexError:
            position = (0, 1, 0)

        # should add the start posiition as the first item of the path
        self.vehicle = Entity(
            model='car',
            color=color.random_color(),
            position=position,
            collider="box")
        super().__init__()

        self.speed = 20.0
        self.path = path
        self.curr_index = 0
        self.loop = loop
        self.boxes = boxes
        self.path_cube = None
        
        
        self.max_speed = 20  # Maximum speed in units per second
        self.acceleration = 5.0  # Acceleration in units per second squared
        self.velocity = Vec3(0, 0, 0)
        self.car_removed = False
        self.counter = counter

    def update(self):
        
        if self.car_removed:
            return

        elif len(self.path) == 0:
            return

        elif self.curr_index >= len(self.path) and self.loop:
            self.curr_index = 0

        elif self.curr_index >= len(self.path):
            self.counter.add()
            self.car_removed = True
            destroy(self.vehicle)
            return

        else:
            
            
            self.speed += self.acceleration * time.dt
            
            if self.speed > self.max_speed:
                self.speed = self.max_speed
                
            if self.speed < 0.0:
                self.speed = 0.0

            target = self.path[self.curr_index]
            
            # full stop
            hit_info_right = raycast(self.vehicle.position, self.vehicle.right, distance=5, ignore=(self.vehicle,))
            if hit_info_right.hit:
                self.speed = 0
                return

            self.path_cube = Entity(model="cube", position=target, color=color.pink, collider="box", scale=5)
            self.path_cube.visible = self.boxes

            if self.vehicle.intersects(self.path_cube):
                self.curr_index += 1
                destroy(self.path_cube)

            destroy(self.path_cube)
            
            
            angle = math.atan2(target.z - self.vehicle.z, target.x - self.vehicle.x)
            dx = int(math.cos(angle) * self.speed)
            dy = int(math.sin(angle) * self.speed)
            
            self.vehicle.x += dx * time.dt
            self.vehicle.z += dy * time.dt

            self.vehicle.rotation_y = - math.degrees(angle)

