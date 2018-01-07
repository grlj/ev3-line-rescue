from ev3dev.ev3 import Screen, Button, LargeMotor, Leds
from ev3dev.fonts import load as load_font


def wait_until(fun):
    while not fun():
        pass

def wait_until_not(fun):
    while fun():
        pass

def message(*lines):
    print(*lines)
    screen = Screen()
    for i in range(len(lines)):
        screen.draw.text((10, 10 + i * 20), str(lines[i]),
                         font=load_font('luBS14'))
    screen.update()


def display_bool(v):
    if v:
        Leds().set_color(Leds.LEFT, Leds.GREEN)
        Leds().set_color(Leds.RIGHT, Leds.GREEN)
    else:
        Leds().all_off()


def stop_motors():
    ports = ['outA', 'outB', 'outC', 'outD']
    for port in ports:
        # noinspection PyBroadException
        try:
            LargeMotor(port).stop()
            print('stopped LargeMotor(\'' + port + '\')')
        except Exception:  # Device is not connected
            pass


def pause(*msg):
    message(*msg)
    wait_for_any_key()


def wait_for_any_key():
    while not Button().any():
        pass
    while Button().any():
        pass
