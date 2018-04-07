from evdev import InputDevice, ecodes


class Mouse:
    def __init__(self, mouse: InputDevice):
        self.mouse = mouse

        self.move = lambda dx, dy: 0
        self.left_state_change = lambda is_btn_down: 0
        self.left_press = lambda: 0
        self.left_release = lambda: 0
        self.right_state_change = lambda is_btn_down: 0
        self.right_press = lambda: 0
        self.right_release = lambda: 0
        self.scroll = lambda direction: 0
        self.extra_state_change = lambda is_btn_down: 0
        self.extra_press = lambda: 0
        self.extra_release = lambda: 0
        self.extra2_state_change = lambda is_btn_down: 0
        self.extra2_press = lambda: 0
        self.extra2_release = lambda: 0
        self.extra3_state_change = lambda is_btn_down: 0
        self.extra3_press = lambda: 0
        self.extra3_release = lambda: 0


    def update(self):

        dx = 0
        dy = 0
        try:
            for event in self.mouse.read():
                if event.type == ecodes.EV_REL:
                    if event.code == ecodes.REL_X:
                        dx -= event.value
                    elif event.code == ecodes.REL_Y:
                        dy += event.value
                    elif event.code == ecodes.REL_WHEEL:
                        self.scroll(event.value)

                if event.type == ecodes.EV_KEY:
                    # print(event.code, event.value)
                    if event.code == ecodes.BTN_LEFT:
                        self.left_state_change(event.value)
                        if event.value:
                            self.left_press()
                        else:
                            self.left_release()
                    elif event.code == ecodes.BTN_RIGHT:
                        self.right_state_change(event.value)
                        if event.value:
                            self.right_press()
                        else:
                            self.right_release()
                    elif event.code == ecodes.BTN_EXTRA:
                        self.extra_state_change(event.value)
                        if event.value:
                            self.extra_press()
                        else:
                            self.extra_release()
                    elif event.code == ecodes.BTN_EXTRA-1:
                        self.extra2_state_change(event.value)
                        if event.value:
                            self.extra2_press()
                        else:
                            self.extra2_release()
                    elif event.code == 280:
                        self.extra3_state_change(event.value)
                        if event.value:
                            self.extra3_press()
                        else:
                            self.extra3_release()
        except BlockingIOError:
            pass

        if dx or dy:
            self.move(dx, dy)

    def update_loop(self):
        try:
            while 1:
                self.update()
        except KeyboardInterrupt:
            pass


def provide_character_device(capabilities, user=''):
    import evdev

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


mouse = Mouse(provide_character_device(capabilities=['EV_REL']))
