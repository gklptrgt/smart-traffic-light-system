from ursina import *


def normal(lights):
    n_red_time = 97
    n_green_time = 15

    w_red_time = 80
    w_green_time = 32

    s_red_time = 100
    s_green_time = 10

    e_red_time = 80
    e_green_time = 32


    invoke(lights.turn_red_on_w_1, delay=0)
    invoke(lights.turn_red_on_w_2, delay=0)
    invoke(lights.turn_red_on_s, delay=0)
    invoke(lights.turn_red_on_n_1, delay=0)
    invoke(lights.turn_red_on_n_2, delay=0)

    starter = 0
    for x in range(1, 11):
        # starting from e

        e_1_yellow_on = starter
        e_1_yellow_off = starter + 3
        invoke(lights.turn_yellow_on_e_1, delay=e_1_yellow_on)
        invoke(lights.turn_yellow_off_e_1, delay=e_1_yellow_off)
        invoke(lights.turn_yellow_on_e_2, delay=e_1_yellow_on)
        invoke(lights.turn_yellow_off_e_2, delay=e_1_yellow_off)
        e_1_green_on = e_1_yellow_off
        e_1_green_off = e_1_green_on + e_green_time
        e_1_yellow_on = e_1_green_off - 2
        e_1_yellow_off = e_1_green_off + 2
        e_1_red_on = e_1_green_off + 2

        s_1_yellow_on = e_1_yellow_off
        s_1_yellow_off = s_1_yellow_on + 3
        invoke(lights.turn_yellow_on_s, delay=s_1_yellow_on)
        invoke(lights.turn_yellow_off_s, delay=s_1_yellow_off)
        s_1_green_on = s_1_yellow_off
        s_1_green_off = s_1_green_on + s_green_time
        s_1_yellow_on = s_1_green_off - 2
        s_1_yellow_off = s_1_green_off + 2
        s_1_red_on = s_1_green_off + 2

        w_1_yellow_on = s_1_green_off
        w_1_yellow_off = w_1_yellow_on + 3
        invoke(lights.turn_yellow_on_w_1, delay=w_1_yellow_on)
        invoke(lights.turn_yellow_off_w_1, delay=w_1_yellow_off)
        invoke(lights.turn_yellow_on_w_2, delay=w_1_yellow_on)
        invoke(lights.turn_yellow_off_w_2, delay=w_1_yellow_off)
        w_1_green_on = w_1_yellow_off
        w_1_green_off = w_1_green_on + w_green_time
        w_1_yellow_on = w_1_green_off - 2
        w_1_yellow_off = w_1_green_off + 2
        w_1_red_on = w_1_green_off + 2

        n_1_yellow_on = w_1_green_off
        n_1_yellow_off = w_1_yellow_on + 3
        invoke(lights.turn_yellow_on_n_1, delay=n_1_yellow_on)
        invoke(lights.turn_yellow_off_n_1, delay=n_1_yellow_off)
        invoke(lights.turn_yellow_on_n_2, delay=n_1_yellow_on)
        invoke(lights.turn_yellow_off_n_2, delay=n_1_yellow_off)
        n_1_green_on = n_1_yellow_off
        n_1_green_off = n_1_green_on + n_green_time
        n_1_yellow_on = n_1_green_off - 2
        n_1_yellow_off = n_1_green_off + 2
        n_1_red_on = n_1_green_off + 2

        # Red OFF
        e_1_red_off = n_1_yellow_off
        s_1_red_off = e_1_yellow_off
        w_1_red_off = s_1_yellow_off
        n_1_red_off = w_1_yellow_off

        starter = n_1_green_off

        # E 1
        invoke(lights.turn_red_on_e_1, delay=e_1_red_on)
        invoke(lights.turn_red_off_e_1, delay=e_1_red_off)

        invoke(lights.turn_yellow_on_e_1, delay=e_1_yellow_on)
        invoke(lights.turn_yellow_off_e_1, delay=e_1_yellow_off)

        invoke(lights.turn_green_on_e_1, delay=e_1_green_on)
        invoke(lights.turn_green_off_e_1, delay=e_1_green_off)

        # E 2
        invoke(lights.turn_red_on_e_2, delay=e_1_red_on)
        invoke(lights.turn_red_off_e_2, delay=e_1_red_off)

        invoke(lights.turn_yellow_on_e_2, delay=e_1_yellow_on)
        invoke(lights.turn_yellow_off_e_2, delay=e_1_yellow_off)

        invoke(lights.turn_green_on_e_2, delay=e_1_green_on)
        invoke(lights.turn_green_off_e_2, delay=e_1_green_off)

        # S
        invoke(lights.turn_red_on_s, delay=s_1_red_on)
        invoke(lights.turn_red_off_s, delay=s_1_red_off)

        invoke(lights.turn_yellow_on_s, delay=s_1_yellow_on)
        invoke(lights.turn_yellow_off_s, delay=s_1_yellow_off)

        invoke(lights.turn_green_on_s, delay=s_1_green_on)
        invoke(lights.turn_green_off_s, delay=s_1_green_off)

        # W 1
        invoke(lights.turn_red_on_w_1, delay=w_1_red_on)
        invoke(lights.turn_red_off_w_1, delay=w_1_red_off)

        invoke(lights.turn_yellow_on_w_1, delay=w_1_yellow_on)
        invoke(lights.turn_yellow_off_w_1, delay=w_1_yellow_off)

        invoke(lights.turn_green_on_w_1, delay=w_1_green_on)
        invoke(lights.turn_green_off_w_1, delay=w_1_green_off)
        # W 2
        invoke(lights.turn_red_on_w_2, delay=w_1_red_on)
        invoke(lights.turn_red_off_w_2, delay=w_1_red_off)

        invoke(lights.turn_yellow_on_w_2, delay=w_1_yellow_on)
        invoke(lights.turn_yellow_off_w_2, delay=w_1_yellow_off)

        invoke(lights.turn_green_on_w_2, delay=w_1_green_on)
        invoke(lights.turn_green_off_w_2, delay=w_1_green_off)

        # N 1
        invoke(lights.turn_red_on_n_1, delay=n_1_red_on)
        invoke(lights.turn_red_off_n_1, delay=n_1_red_off)

        invoke(lights.turn_yellow_on_n_1, delay=n_1_yellow_on)
        invoke(lights.turn_yellow_off_n_1, delay=n_1_yellow_off)

        invoke(lights.turn_green_on_n_1, delay=n_1_green_on)
        invoke(lights.turn_green_off_n_1, delay=n_1_green_off)
        # N 2
        invoke(lights.turn_red_on_n_2, delay=n_1_red_on)
        invoke(lights.turn_red_off_n_2, delay=n_1_red_off)

        invoke(lights.turn_yellow_on_n_2, delay=n_1_yellow_on)
        invoke(lights.turn_yellow_off_n_2, delay=n_1_yellow_off)

        invoke(lights.turn_green_on_n_2, delay=n_1_green_on)
        invoke(lights.turn_green_off_n_2, delay=n_1_green_off)