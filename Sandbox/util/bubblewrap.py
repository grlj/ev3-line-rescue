from util.robotutils import stop_motors


def bubblewrap(fun, final_fun=(lambda:1)):
    def bubblewrapped_fun():
        try:
            fun()
        except BaseException as e:
            print(str(e))
            stop_motors()
        finally:
        	final_fun()


    return bubblewrapped_fun
