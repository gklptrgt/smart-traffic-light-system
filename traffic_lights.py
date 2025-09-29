from ursina import *


class TrafficLight(Entity):

    def __init__(self):
        super().__init__()

        self.red_off = color.hex("#930004")
        self.red_on = color.hex("#ff1319")

        self.yellow_off = color.hex("#7a8a00")
        self.yellow_on = color.hex("#e1ff00")

        self.green_off = color.hex("#00560b")
        self.green_on = color.hex("#00ff18")

        self.road_block_e_1 = Entity(model="cube", color=color.clear, scale=2, collider="box",
                                     position=(17, 0, -9),
                                     scale_z=10)

        self.road_block_e_2 = Entity(model="cube", color=color.clear, scale=2, collider="box",
                                     position=(17, 0, -1.5),
                                     scale_z=4)

        self.road_block_w_1 = Entity(model="cube", color=color.clear, scale=2, collider="box",
                                     position=(-17, 0, 9),
                                     scale_z=10)

        self.road_block_w_2 = Entity(model="cube", color=color.clear, scale=2, collider="box",
                                     position=(-17, 0, 1.5),
                                     scale_z=4)

        self.road_block_n_1 = Entity(model="cube", color=color.clear, scale=2, collider="box",
                                     position=(3.5, 0, 16),
                                     scale_x=4)

        self.road_block_n_2 = Entity(model="cube", color=color.clear, scale=2, collider="box",
                                     position=(10, 0, 16),
                                     scale_x=4)

        self.road_block_s = Entity(model="cube", color=color.clear, scale=2, collider="box",
                                   position=(-5, 0, -16),
                                   scale_x=4)

        self.red_light_e_1 = Entity(model="sphere", color=self.red_off, position=(16.7, 8.5, -8.6), scale=0.7)
        self.yellow_light_e_1 = Entity(model="sphere", color=self.yellow_off, position=(16.7, 7.6, -8.6), scale=0.7)
        self.green_light_e_1 = Entity(model="sphere", color=self.green_off, position=(16.7, 6.7, -8.6), scale=0.7)

        self.red_light_e_2 = Entity(model="sphere", color=self.red_off, position=(16.6, 5.05, 1.7), scale=0.7)
        self.yellow_light_e_2 = Entity(model="sphere", color=self.yellow_off, position=(16.6, 4.15, 1.7), scale=0.7)
        self.green_light_e_2 = Entity(model="sphere", color=self.green_off, position=(16.6, 3.25, 1.7), scale=0.7)

        self.red_light_w_1 = Entity(model="sphere", color=self.red_off, position=(-17.5, 8.5, 8.3), scale=0.7)
        self.yellow_light_w_1 = Entity(model="sphere", color=self.yellow_off, position=(-17.5, 7.6, 8.3), scale=0.7)
        self.green_light_w_1 = Entity(model="sphere", color=self.green_off, position=(-17.5, 6.7, 8.3), scale=0.7)

        self.red_light_w_2 = Entity(model="sphere", color=self.red_off, position=(-17.5, 5.05, -1.95), scale=0.7)
        self.yellow_light_w_2 = Entity(model="sphere", color=self.yellow_off, position=(-17.5, 4.15, -1.95), scale=0.7)
        self.green_light_w_2 = Entity(model="sphere", color=self.green_off, position=(-17.5, 3.25, -1.95), scale=0.7)

        self.red_light_n_1 = Entity(model="sphere", color=self.red_off, position=(0.3, 3.6, 16.3), scale=0.7)
        self.yellow_light_n_1 = Entity(model="sphere", color=self.yellow_off, position=(0.3, 2.8, 16.3), scale=0.7)
        self.green_light_n_1 = Entity(model="sphere", color=self.green_off, position=(0.3, 2, 16.3), scale=0.7)

        self.red_light_n_2 = Entity(model="sphere", color=self.red_off, position=(13.6, 3.5, 16.3), scale=0.7)
        self.yellow_light_n_2 = Entity(model="sphere", color=self.yellow_off, position=(13.6, 2.7, 16.3), scale=0.7)
        self.green_light_n_2 = Entity(model="sphere", color=self.green_off, position=(13.6, 1.9, 16.3), scale=0.7)

        self.red_light_s = Entity(model="sphere", color=self.red_off, position=(-0.7, 3.6, -15.2), scale=0.7)
        self.yellow_light_s = Entity(model="sphere", color=self.yellow_off, position=(-0.7, 2.8, -15.2), scale=0.7)
        self.green_light_s = Entity(model="sphere", color=self.green_off, position=(-0.7, 2, -15.2), scale=0.7)

    # Green
    def turn_green_on_e_1(self):
        self.green_light_e_1.color = self.green_on
        self.road_block_e_1.disable()

    def turn_green_on_w_1(self):
        self.green_light_w_1.color = self.green_on
        self.road_block_w_1.disable()

    def turn_green_on_n_1(self):
        self.green_light_n_1.color = self.green_on
        self.road_block_n_1.disable()

    def turn_green_on_s(self):
        self.green_light_s.color = self.green_on
        self.road_block_s.disable()

    def turn_green_off_e_1(self):
        self.green_light_e_1.color = self.green_off
        self.road_block_e_1.enable()

    def turn_green_off_w_1(self):
        self.green_light_w_1.color = self.green_off
        self.road_block_w_1.enable()

    def turn_green_off_n_1(self):
        self.green_light_n_1.color = self.green_off
        self.road_block_n_1.enable()

    def turn_green_off_s(self):
        self.green_light_s.color = self.green_off
        self.road_block_s.enable()

    def turn_green_on_e_2(self):
        self.green_light_e_2.color = self.green_on
        self.road_block_e_2.disable()

    def turn_green_on_w_2(self):
        self.green_light_w_2.color = self.green_on
        self.road_block_w_2.disable()

    def turn_green_on_n_2(self):
        self.green_light_n_2.color = self.green_on
        self.road_block_n_2.disable()

    def turn_green_off_e_2(self):
        self.green_light_e_2.color = self.green_off
        self.road_block_e_2.enable()

    def turn_green_off_w_2(self):
        self.green_light_w_2.color = self.green_off
        self.road_block_w_2.enable()

    def turn_green_off_n_2(self):
        self.green_light_n_2.color = self.green_off
        self.road_block_n_2.enable()


    # Yellow
    def turn_yellow_on_e_1(self):
        self.yellow_light_e_1.color = self.yellow_on

    def turn_yellow_on_w_1(self):
        self.yellow_light_w_1.color = self.yellow_on

    def turn_yellow_on_n_1(self):
        self.yellow_light_n_1.color = self.yellow_on

    def turn_yellow_on_s(self):
        self.yellow_light_s.color = self.yellow_on

    def turn_yellow_off_e_1(self):
        self.yellow_light_e_1.color = self.yellow_off

    def turn_yellow_off_w_1(self):
        self.yellow_light_w_1.color = self.yellow_off

    def turn_yellow_off_n_1(self):
        self.yellow_light_n_1.color = self.yellow_off

    def turn_yellow_off_s(self):
        self.yellow_light_s.color = self.yellow_off

    def turn_yellow_on_e_2(self):
        self.yellow_light_e_2.color = self.yellow_on

    def turn_yellow_on_w_2(self):
        self.yellow_light_w_2.color = self.yellow_on

    def turn_yellow_on_n_2(self):
        self.yellow_light_n_2.color = self.yellow_on

    def turn_yellow_off_e_2(self):
        self.yellow_light_e_2.color = self.yellow_off

    def turn_yellow_off_w_2(self):
        self.yellow_light_w_2.color = self.yellow_off

    def turn_yellow_off_n_2(self):
        self.yellow_light_n_2.color = self.yellow_off

    # Red
    def turn_red_on_e_1(self):
        self.red_light_e_1.color = self.red_on

    def turn_red_on_w_1(self):
        self.red_light_w_1.color = self.red_on

    def turn_red_on_n_1(self):
        self.red_light_n_1.color = self.red_on

    def turn_red_on_s(self):
        self.red_light_s.color = self.red_on

    def turn_red_off_e_1(self):
        self.red_light_e_1.color = self.red_off

    def turn_red_off_w_1(self):
        self.red_light_w_1.color = self.red_off

    def turn_red_off_n_1(self):
        self.red_light_n_1.color = self.red_off

    def turn_red_off_s(self):
        self.red_light_s.color = self.red_off

    def turn_red_on_e_2(self):
        self.red_light_e_2.color = self.red_on

    def turn_red_on_w_2(self):
        self.red_light_w_2.color = self.red_on

    def turn_red_on_n_2(self):
        self.red_light_n_2.color = self.red_on

    def turn_red_off_e_2(self):
        self.red_light_e_2.color = self.red_off

    def turn_red_off_w_2(self):
        self.red_light_w_2.color = self.red_off

    def turn_red_off_n_2(self):
        self.red_light_n_2.color = self.red_off
