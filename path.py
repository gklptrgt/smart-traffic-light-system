import copy

from ursina import *
from vehicle import Vehicle


class PathEditor(Entity):

    def __init__(self, county):
        super().__init__()

        self.path = []  # maybe change for performance.
        self.master_paths = []
        self.line = None
    
        self.vehicle = Vehicle(self.path, county, loop=True, boxes=True)

    def input(self, key):
        if key == 'left mouse down':
            self.add_path(mouse.world_point)

        if held_keys['x']:
            self.remove_path()

    def add_path(self, position):
        ent = Entity(model="sphere", color=color.blue, position=position, scale=2, collider="sphere")
        self.path.append(ent)
        self.draw_lines()


    def remove_path(self):
        if len(self.path) <= 0:
            pass
        else:
            destroy(self.path.pop())
            destroy(self.line)
            self.draw_lines()

    def draw_lines(self):
        self.vehicle.path = self.path

        if len(self.path) > 0:
            destroy(self.line)

        lines = []
        for item in self.path:
            lines.append(item.position)

        if len(lines) >= 2:
            self.line = Entity(model=Mesh(vertices=lines, mode='line', thickness=3), color=color.cyan)

    def get_path(self):
        return self.path

    def save_single(self):

        copy_path = self.path.copy()

        copy_path.pop()  # we remove the last one because when pressing button it 1 more to the list.
        paths_to_save = [item.position for item in copy_path]
        self.master_paths.append(paths_to_save)

        # remove all the objects.
        for item in self.path:
            destroy(item)
            # clears all the boxes
        destroy(self.line)

        self.path = []
        self.vehicle.path = self.path

    def get_master_path(self):
        # self.master_paths.pop()
        print(self.master_paths)
        return self.master_paths
