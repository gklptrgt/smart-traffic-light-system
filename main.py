from ursina import *
from path import PathEditor
import pickle
# from spawner import Spawner
from vehicle import Vehicle
from traffic_lights import TrafficLight
from road_algos import normal

class Statistic:

    def __init__(self):
        self.count = 0

        self.total = 0
        self.run = 0
        self.avg = 0

    def add(self):
        self.count += 1
    
    def show(self):
        return self.count

    def reset(self):
        self.run += 1
        self.total += self.count
        self.avg = self.total // self.run
        self.count = 0

        return self.run, self.avg


app = Ursina()
map = Entity(model='tezgahv2', texture="tezgahv2_text.png", position=(0, -2, 0))

stat_text = Text("calculating vehicles/min", origin=(0, 18))
avg_text = Text("Run: 0, Avg ? vehicles/min", origin=(0, 16))
sim_text = Text("Simulation: Real Life",  origin=(0, -18))

county = Statistic()
# Active road algo
lights = TrafficLight()
normal(lights)

# load paths
with open("car_paths.pickle", "rb") as f:
    loaded_path = pickle.load(f)

# Car Spawn
def spawn():
    path = random.choice(loaded_path)
    Vehicle(path, county)



def update_per_minute():
    val = county.show()
    run, avg = county.reset()

    avg_text.text = f"Run: {run}, Avg {avg} vehicles/min"
    stat_text.text = f"{str(val)} vehicles/min"


for x in range(1, 1000):
    invoke(spawn, delay=x)
    invoke(update_per_minute, delay=x*60)

# path_editor = PathEditor(county)

# def single_path_save():
#     path_editor.save_single()

# def save_all_path():
#     paths = path_editor.get_master_path()
#     print(paths)
#     # save the list to a file
#     # with open("car_paths.pickle", "wb") as f:
#     #     pickle.dump(paths, f)



# save_single_path = Button(text='Save Path',
#                           color=color.black,
#                           highlight_color=color.gray,
#                           scale=(.15, .03),
#                           position=(-0.81, 0.48))

# save_single_path.on_click = single_path_save

# save_path = Button(text='Save All Path',
#                    color=color.black,
#                    highlight_color=color.gray,
#                    scale=(.15, .03),
#                    position=(-0.81, 0.445))

# save_path.on_click = save_all_path






EditorCamera()
app.run()








