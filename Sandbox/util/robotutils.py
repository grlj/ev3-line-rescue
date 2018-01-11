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


def set_led_color(color):
    if color == 'none':
        Leds().all_off()
    else:
        d = {
            'red': Leds.RED,
            'green': Leds.GREEN,
            'orange': Leds.ORANGE,
            'amber': Leds.AMBER,
            'yellow': Leds.YELLOW
        }
        Leds().set_color(Leds.LEFT, d[color])
        Leds().set_color(Leds.RIGHT, d[color])


def display_bool(v):
    if v:
        set_led_color('green')
    else:
        set_led_color('none')


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
