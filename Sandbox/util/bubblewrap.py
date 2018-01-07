from util.robotutils import stop_motors


def bubblewrap(fun):
    def bubblewrapped_fun():
        try:
            fun()
        except BaseException as e:
            print(str(e))
            stop_motors()

    return bubblewrapped_fun
