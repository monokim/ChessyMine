import time

class Timer():
    instance = None
    def __init__(self):
        if Timer.instance != None:
            raise Exception("This class is a singletone!")
        else:
            Timer.instance = self
        self.times = []
        self.cnt = 0

    def get_instance(self):
        if Timer.instance == None:
            Timer()
        return Timer.instance

    def set_timer(name="timer"):
        flag = False
        for i, t in enumerate(self.times):
            if t[1] == name:
                flag = True
                t[0] = time.time()
                break

        if flag == False:
            self.times.append([time.time(), name])

    def print_time(name="timer"):
        flag = False
        for i, t in enumerate(self.times):
            if t[1] == name:
                flag = True
                print(name + " is %d" % (time.time() - t[0]))
                break

        if flag == False:
            raise Exception("There is no timer")

    def delete_timer(name = None):
        for i, t in enumerate(self.times):
            if t[1] == name:
                self.times.pop(i)
                break
