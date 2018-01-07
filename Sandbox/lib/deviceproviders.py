import evdev

SENSOR_PORTS = ('in1', 'in2', 'in3', 'in4')
MOTOR_PORTS = ('outA', 'outB', 'outC', 'outD')
DEVICE_PORTS = SENSOR_PORTS + MOTOR_PORTS


def provide_ev3_devices(device_constructor,
                        count, ports=DEVICE_PORTS, user=''):
    devices = []
    for port in ports:
        device = device_constructor(port)
        if device.connected:
            devices.append(device)
            print((user + ' is ', '')[user == ''] +
                  'using ' + device_constructor.__name__ +
                  ' (\'' + port + '\')')
            if len(devices) == count:
                return devices

    input(
        (user if len(user) else 'Program') + ' requires at least ' +
        str(count) + ' ' + device_constructor.__name__ +
        ('s' if count > 1 else '') +
        #  '. Searched ports: ' + ', '.join(ports) +
        '\nPress enter to try again ...'
    )
    return provide_ev3_devices(device_constructor, count, ports, user)


def provide_ev3_device(device_constructor, ports=DEVICE_PORTS, user=''):
    return provide_ev3_devices(device_constructor, 1, ports, user)[0]


def provide_character_device(capabilities, user=''):
    for fn in evdev.list_devices():
        dev = evdev.InputDevice(fn)
        device_capabilities = list(
            zip(*dev.capabilities(verbose=True).keys())
        )[0]
        if set(device_capabilities) >= set(capabilities):
            print((user + ' is ', '')[user == ''] +
                  'using ' + dev.name + ' (' + fn + ')')
            return dev

    input(
        (user if len(user) else 'Program') +
        ' requires a character device with capabilities: ' +
        ', '.join(capabilities) +
        '\nPress enter to try again ...'
    )
    return provide_character_device(capabilities, user)
